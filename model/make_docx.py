# -*- coding: utf-8 -*-
"""Rebuild the DOCX files with one consistent type specification:
Times New Roman throughout, 12 pt body, bold 12 pt sub-headings, 14 pt title,
double spacing, tables at 10 pt single-spaced, A4, line numbers."""
import os, re, shutil, subprocess, zipfile

PANDOC = "/opt/homebrew/bin/pandoc"
REF_RAW = "/tmp/ref_raw.docx"
REF = "/tmp/ref_tt.docx"

# ---------------------------------------------------------------- styles ----
def style_block(sid, size, bold=False, italic=False, before=0, after=0,
                keep=False):
    b = "<w:b />" if bold else ""
    i = "<w:i />" if italic else ""
    k = "<w:keepNext />" if keep else ""
    return (
        f'<w:style w:type="paragraph" w:styleId="{sid}">'
        f'<w:name w:val="{sid}" /><w:basedOn w:val="Normal" /><w:next w:val="BodyText" />'
        f'<w:qFormat />'
        f'<w:pPr>{k}<w:spacing w:before="{before}" w:after="{after}" '
        f'w:line="480" w:lineRule="auto" /><w:jc w:val="left" /></w:pPr>'
        f'<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" '
        f'w:eastAsia="Times New Roman" w:cs="Times New Roman" />{b}{i}'
        f'<w:color w:val="000000" /><w:sz w:val="{size}" /><w:szCs w:val="{size}" /></w:rPr>'
        f'</w:style>')

def build_reference():
    subprocess.run([PANDOC, "--print-default-data-file", "reference.docx"],
                   stdout=open(REF_RAW, "wb"), check=True)
    zin = zipfile.ZipFile(REF_RAW)
    zout = zipfile.ZipFile(REF, "w", zipfile.ZIP_DEFLATED)
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == "word/styles.xml":
            s = data.decode("utf-8")
            # global default: Times New Roman 12, double spaced, no space after
            s = re.sub(r'<w:rFonts w:asciiTheme="minorHAnsi"[^/]*/>',
                       '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" '
                       'w:eastAsia="Times New Roman" w:cs="Times New Roman" />', s)
            s = s.replace('<w:spacing w:after="200" />',
                          '<w:spacing w:before="0" w:after="0" w:line="480" w:lineRule="auto" />')
            s = re.sub(r'<w:sz w:val="22" />', '<w:sz w:val="24" />', s)
            s = re.sub(r'<w:szCs w:val="22" />', '<w:szCs w:val="24" />', s)
            # drop the existing heading/compact definitions, then append ours
            for sid in ("Heading1", "Heading2", "Heading3", "Heading4", "Compact",
                        "Title", "Subtitle", "SourceCode"):
                s = re.sub(r'<w:style [^>]*w:styleId="%s".*?</w:style>' % sid,
                           "", s, flags=re.S)
            new = (
                style_block("Heading1", 28, bold=True, before=240, after=120, keep=True) +
                style_block("Heading2", 24, bold=True, before=240, after=60, keep=True) +
                style_block("Heading3", 24, bold=True, italic=True, before=180, after=60, keep=True) +
                style_block("Heading4", 24, bold=True, italic=True, before=120, after=0, keep=True) +
                style_block("Title", 28, bold=True, before=0, after=120, keep=True) +
                style_block("Subtitle", 24, italic=True, before=0, after=120) +
                style_block("Compact", 24) +
                style_block("SourceCode", 18) +
                '<w:style w:type="paragraph" w:styleId="TableText">'
                '<w:name w:val="Table Text" /><w:basedOn w:val="Normal" />'
                '<w:pPr><w:spacing w:before="0" w:after="0" w:line="240" '
                'w:lineRule="auto" /></w:pPr>'
                '<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" '
                'w:cs="Times New Roman" /><w:sz w:val="20" /><w:szCs w:val="20" />'
                '</w:rPr></w:style>')
            s = s.replace("</w:styles>", new + "</w:styles>")
            data = s.encode("utf-8")
        zout.writestr(item, data)
    zout.close()

# ------------------------------------------------------------ postprocess ----
PGSZ = '<w:pgSz w:w="11906" w:h="16838" />'
PGMAR = ('<w:pgMar w:top="1417" w:right="1417" w:bottom="1417" w:left="1417" '
         'w:header="709" w:footer="709" w:gutter="0" />')

def single_space_tables(xml):
    """Every paragraph inside a table uses the TableText style (10 pt, single)."""
    def fix_table(m):
        t = m.group(0)
        t = re.sub(r'<w:pStyle w:val="[^"]+"\s*/>',
                   '<w:pStyle w:val="TableText" />', t)
        # paragraphs with no pStyle inside tables
        t = re.sub(r'<w:p>(?!<w:pPr><w:pStyle)',
                   '<w:p><w:pPr><w:pStyle w:val="TableText" /></w:pPr>', t)
        return t
    return re.sub(r"<w:tbl>.*?</w:tbl>", fix_table, xml, flags=re.S)

def postprocess(path):
    tmp = path + ".tmp"
    zin = zipfile.ZipFile(path)
    zout = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == "word/document.xml":
            s = data.decode("utf-8")
            if "<w:pgSz" not in s:
                s = s.replace("<w:sectPr>", "<w:sectPr>" + PGSZ + PGMAR, 1)
            else:
                s = re.sub(r"<w:pgSz[^/]*/>", PGSZ, s)
                s = re.sub(r"<w:pgMar[^/]*/>", PGMAR, s)
            if "<w:lnNumType" not in s:
                s = s.replace("</w:sectPr>",
                              '<w:lnNumType w:countBy="1" w:restart="continuous" /></w:sectPr>')
            s = single_space_tables(s)
            data = s.encode("utf-8")
        zout.writestr(item, data)
    zout.close()
    shutil.move(tmp, path)

jobs = [
    ("Ban_thao/Manuscript_EN.md", "Ban_thao/Manuscript_EN.docx"),
    ("Ban_thao/Manuscript_VI.md", "Ban_thao/Manuscript_VI.docx"),
    ("Ban_thao/Appendices_EN.md", "Ban_thao/Appendices_EN.docx"),
    ("Ban_thao/Appendices_VI.md", "Ban_thao/Appendices_VI.docx"),
    ("Ban_thao/Cover_letter.md",   "Ban_thao/Cover_letter.docx"),
]

build_reference()
for src, dst in jobs:
    subprocess.run([PANDOC, src, "-f", "markdown", "-t", "docx",
                    "--reference-doc", REF, "-o", dst], check=True)
    postprocess(dst)
    print(f"{dst:36s} {os.path.getsize(dst)/1024:7.1f} KB")

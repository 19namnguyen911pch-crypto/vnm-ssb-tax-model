# -*- coding: utf-8 -*-
"""Convert the submission files to DOCX with journal-friendly formatting:
A4, 2.5 cm margins, Times New Roman 12 pt, double spacing, continuous line
numbers."""
import os, re, shutil, subprocess, zipfile

PANDOC = "/opt/homebrew/bin/pandoc"
REF = "/tmp/ref_tt.docx"

def build_reference():
    subprocess.run([PANDOC, "--print-default-data-file", "reference.docx"],
                   stdout=open("/tmp/ref_raw.docx", "wb"), check=True)
    zin = zipfile.ZipFile("/tmp/ref_raw.docx")
    zout = zipfile.ZipFile(REF, "w", zipfile.ZIP_DEFLATED)
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == "word/styles.xml":
            s = data.decode("utf-8")
            # explicit Times New Roman, 12 pt, double spacing
            s = re.sub(r'<w:rFonts w:asciiTheme="minorHAnsi"[^/]*/>',
                       '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" '
                       'w:eastAsia="Times New Roman" w:cs="Times New Roman" />', s)
            s = s.replace('<w:spacing w:after="200" />',
                          '<w:spacing w:after="0" w:line="480" w:lineRule="auto" />')
            data = s.encode("utf-8")
        zout.writestr(item, data)
    zout.close()

def blacken_headings():
    zin = zipfile.ZipFile(REF)
    zout = zipfile.ZipFile("/tmp/ref_tt2.docx", "w", zipfile.ZIP_DEFLATED)
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == "word/styles.xml":
            t = data.decode("utf-8")
            t = re.sub(r'(<w:style [^>]*w:styleId="Heading\d"[^>]*>.*?</w:style>)',
                       lambda m: re.sub(r'<w:color w:val="[0-9A-Fa-f]{6}"[^/]*/>',
                                        '<w:color w:val="000000" />', m.group(1), flags=re.S),
                       t, flags=re.S)
            data = t.encode("utf-8")
        zout.writestr(item, data)
    zout.close()
    shutil.move("/tmp/ref_tt2.docx", REF)

SECT = ('<w:pgSz w:w="11906" w:h="16838" />'
        '<w:pgMar w:top="1417" w:right="1417" w:bottom="1417" w:left="1417" '
        'w:header="709" w:footer="709" w:gutter="0" />')

def postprocess(path):
    tmp = path + ".tmp"
    zin = zipfile.ZipFile(path)
    zout = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == "word/document.xml":
            s = data.decode("utf-8")
            # replace the section geometry and add line numbering
            s = re.sub(r"<w:pgSz[^/]*/>", '<w:pgSz w:w="11906" w:h="16838" />', s)
            s = re.sub(r"<w:pgMar[^/]*/>",
                       '<w:pgMar w:top="1417" w:right="1417" w:bottom="1417" '
                       'w:left="1417" w:header="709" w:footer="709" w:gutter="0" />', s)
            if "<w:pgSz" not in s:
                s = s.replace("<w:sectPr>",
                              "<w:sectPr><w:pgSz w:w=\"11906\" w:h=\"16838\" />"
                              "<w:pgMar w:top=\"1417\" w:right=\"1417\" "
                              "w:bottom=\"1417\" w:left=\"1417\" "
                              "w:header=\"709\" w:footer=\"709\" w:gutter=\"0\" />", 1)
            if "<w:lnNumType" not in s:
                s = s.replace("</w:sectPr>",
                              '<w:lnNumType w:countBy="1" w:restart="continuous" />'
                              "</w:sectPr>")
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
blacken_headings()
for src, dst in jobs:
    subprocess.run([PANDOC, src, "-f", "markdown", "-t", "docx",
                    "--reference-doc", REF, "-o", dst], check=True)
    postprocess(dst)
    print(f"{dst:36s} {os.path.getsize(dst)/1024:8.1f} KB")

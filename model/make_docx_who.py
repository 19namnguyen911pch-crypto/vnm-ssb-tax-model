# -*- coding: utf-8 -*-
"""Build the Bulletin WHO submission files with the same type specification as
the main manuscripts."""
import os
import re
import subprocess

import make_docx as md

PANDOC = "/opt/homebrew/bin/pandoc"
REF = "/tmp/ref_tt.docx"

if not os.path.exists(REF):
    md.build_reference()

jobs = [
    ("Banthao_Who/Manuscript_WHO.md", "Banthao_Who/Manuscript_WHO.docx"),
    ("Banthao_Who/Cover_letter_WHO.md", "Banthao_Who/Cover_letter_WHO.docx"),
    ("Banthao_Who/Supplement_WHO.md", "Banthao_Who/Supplement_WHO.docx"),
]

for src, dst in jobs:
    subprocess.run([PANDOC, src, "-f", "markdown", "-t", "docx",
                    "--reference-doc", REF, "-o", dst], check=True)
    md.postprocess(dst)
    print(f"{dst:44s} {os.path.getsize(dst)/1024:7.1f} KB")

from builtins import input
import zipfile
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PyPDF2 import PdfFileMerger, PdfFileReader


# Enter file name
fname = input('Notebook file: ')
# Opens file
f = zipfile.ZipFile(fname)
# Get pages with extension .svg
svgpages = [name for name in f.namelist() if name.endswith('.svg')]
# Extract .svg pages
[f.extract(svgpage) for svgpage in svgpages]
# Creates list with pdf names (same as svg page names)
pdfpages = [svgpage.split(".")[0]+".pdf" for svgpage in svgpages]
# Creates pdf pages
for svgpage, pdfpage in zip(svgpages, pdfpages):
    svgpage = svg2rlg(svgpage)
    renderPDF.drawToFile(svgpage, pdfpage)
# Merges pdf pages in document.pdf
merger = PdfFileMerger()
[merger.append(PdfFileReader(file(pdfpage, 'rb'))) for pdfpage in pdfpages]
# Writes pdf file with all pages with same name as notebook file
merger.write(fname.split(".")[0]+".pdf")
# Delete intermediary files
[os.remove(svgfile) for svgfile in svgpages]
[os.remove(pdffile) for pdffile in pdfpages]

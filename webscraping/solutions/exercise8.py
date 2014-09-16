from pyPdf import PdfFileReader
import glob

pdfs = glob.glob("*.pdf")

for pdf in pdfs:
    with open(pdf,"rb") as f:
        reader = PdfFileReader(f)
        contents = reader.getPage(0).extractText().split("\n")
        print contents

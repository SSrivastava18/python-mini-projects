from PyPDF3 import PdfFileMerger

pdfs = ['s1.pdf','s2.pdf','s3.pdf']
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")

merger.close()

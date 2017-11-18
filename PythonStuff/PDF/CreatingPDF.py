import PyPDF2
# copying, cutting or reordering pdf pages
p = open('files/meetingminutes.pdf', 'rb')
q = open('files/meetingminutes2.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(p)
pdf2 = PyPDF2.PdfFileReader(q)

pdfWaterMark = PyPDF2.PdfFileReader(open('files/watermark.pdf', 'rb'))
pdfWriter = PyPDF2.PdfFileWriter()

for page in range(pdf.numPages):
    pageObj = pdf.getPage(page)

    # merge page
    # just to add overlay - water mark for every other page
    if page % 2 != 0:
        pageObj.mergePage(pdfWaterMark.getPage(0))

    pdfWriter.addPage(pageObj)

for page in range(pdf2.numPages):
    pageObj = pdf2.getPage(page)

    # rotating
    pageObj.rotateClockwise(90)
    pdfWriter.addPage(pageObj)

newPdf = open('files/combination.pdf', 'wb')
pdfWriter.write(newPdf)

encryptedPdf = open('files/myEpdf.pdf', 'wb')
pdfWriter.encrypt('myPass')
pdfWriter.write(encryptedPdf)

encryptedPdf.close()
newPdf.close()
p.close()
q.close()



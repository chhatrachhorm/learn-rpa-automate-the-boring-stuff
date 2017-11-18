import PyPDF2
# pip install PyPDF2

pdf = open('files/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)

print(pdfReader.numPages)
page = pdfReader.getPage(0)
print(page.extractText())

# to decrypt the encrypted pdf
epdf = PyPDF2.PdfFileReader(open('files/encrypted.pdf', 'rb'))
if epdf.isEncrypted:
    print('File is encrypted')
    epdf.decrypt('rosebud')
    print(epdf.getPage(0).extractText())
else:
    print('File is not encrypted')

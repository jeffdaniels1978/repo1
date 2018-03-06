import PyPDF2

file = open(r'', 'rb')
reader = PyPDF2.PdfFileReader(file)
pageCount = reader.numPages
for pageNumber in range(pageCount):
    page = reader.getPage(pageNumber)
    #print(page)
    #print(page.getContents())
    print(page.extractText())
    
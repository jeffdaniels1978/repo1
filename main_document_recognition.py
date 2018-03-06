from libFile     import getFileExtension, getFileType
from libDocument import getDocumentTypeByExtension, getDocumentTypeBySignature
from libContent  import getContentType
import sys

fileNames=[
    r'C:\Python27\python.exe', 
    r'C:\slimerjs\macys.png', 
    r'C:\slimerjs\application.ini', 
    r'C:\python_apps\test_text_input_1.txt', 
    r'C:\python_apps\test_excel_input_1.xlsx', 
    r'C:\python_apps\test_word_input_1.docx', 
]

for fileName in fileNames:
    file=open(fileName,  'r')
    fileExtension=getFileExtension(fileName)
    fileType=getFileType(file)
    documentType1=getDocumentTypeByExtension(file=file,  extension=fileExtension)
    documentType2=getDocumentTypeBySignature(fileName)
    print('%s, %s, %s, %s' %(fileName,  fileType,  documentType1,  documentType2) )


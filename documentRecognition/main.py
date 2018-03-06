'''
Created on Dec 9, 2017

@author: carter
'''
from libFile     import getFileExtension, getFileType
from libDocument import getDocumentTypeByExtension, getDocumentTypeBySignature
from libContent  import getContentType
import sys

'''
A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. 
Such a docstring becomes the __doc__ special attribute of that object.

All modules should have docstrings
All functions and classes exported by a module should have docstrings
Public methods (including the __init__ constructor) should have docstrings
A package may be documented in the module docstring of the __init__.py file in the package directory
'''

fileNames=[
#      r'C:\Python27\python.exe', 
#      r'C:\slimerjs\macys.png', 
#      r'C:\slimerjs\application.ini', 
#      r'C:\python_apps\test_text_input_1.txt', 
#      r'C:\python_apps\test_excel_input_1.xlsx', 
#      r'C:\python_apps\test_word_input_1.docx',
#      r'C:\python_apps\wale_bad.mp4',
#      r'C:\Users\carter\Videos\ghettogaggerssample3.mpg',
     r'C:\Users\carter\Desktop\my electronics docs\MTX Monitor12 Speaker.pdf'
]

printFormat = '%-61s %11s %26s %26s %12s'
print(printFormat % ('file name',  'file type', 'type from ext', 'type from sig', 'match') )
print(printFormat % ('-'*60, '-'*10, '-'*25, '-'*25, '-'*11,) )

for fileName in fileNames:
    file=open(fileName,  'r')
    fileExtension=getFileExtension(fileName)
    fileType=getFileType(file)
    documentTypeFromExt = getDocumentTypeByExtension(file=file,  extension=fileExtension)
    documentTypeFromSig, match = getDocumentTypeBySignature(fileName)
    fileName = fileName[-60:]
    print(printFormat % (fileName,  fileType,  documentTypeFromExt,  documentTypeFromSig, match) )
import string

def getFileExtension(fileName=None):
    '''
    Get extension (string after the final '.') and return it
    parameters:
        fileName: string
    returns:
        string
    '''
    return fileName[ fileName.rfind('.') + 1 :  ]
    
def getFileType(file=None):
    '''
    Determine file type (text or binary) and return it
    parameters:
        file: a file object (an object returned by open())
    returns:
        string
    '''    
    try:
        chars = file.read(1000)
        if all(char.isprintable  for char in chars):
            return 'text'
        else:
            return 'binary'
    except UnicodeDecodeError:
        return 'binary'

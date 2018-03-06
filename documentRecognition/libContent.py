def getContentType(file, documentType):
    '''
    Return a weighted guess of the content type (e.g. purchase order, invoice, resume) for a given file and document type 
    parameters:
        file: a file (an object returned by open())
        documentType: a string of the name of the application that created the file (e.g. excel, word)
    returns:
        content type (string)
    '''
    
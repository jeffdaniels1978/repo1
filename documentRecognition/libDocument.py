#import magic
import binascii
import PyPDF2 # https://pythonhosted.org/PyPDF2/index.html

def getDocumentTypeByExtension(file, extension=None):
    extensions={
        'csv':'text',
        'txt':'text',
        'yaml':'text',
        'xlsx':'excel', 
        'docx':'word', 
    }
    return extensions.get(extension)

def getDocumentTypeBySignature(fileName):
    signatures={
        b'504b0304':'ms office document', 
        b'89504e47':'png image',
        b'25504446':'pdf', 
        b'fffb':    'mp3',
        b'494433':  'mp3',
        b'000001ba':'mpeg',
        b'000001b3':'mpeg',
    }
    file=open(fileName, 'rb')
    
    sigMax = binascii.hexlify(file.read(8))
    sig8 = sigMax[:8]
    sig6 = sigMax[:6]
    sig4 = sigMax[:4]
    sig2 = sigMax[:2]
    for sig in (sig8, sig6, sig4, sig2):
        documentType = signatures.get(sig)
        if documentType:
            return documentType, sig
    return None, sig

def reader():
    pass

def wordReader():
    pass

def pdfReader(file):
    pass
    
    
    
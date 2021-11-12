from PyPDF2 import PdfFileMerger, PdfFileReader
import os
from os.path import isfile

dirs = os.listdir()
dirs.sort()
err = []
err2 = []
i = 1 
for dir in dirs:
    print("actual dir " + dir)
    print(str(i) + "/" + str(len(dirs)))
    i += 1
    if not isfile(dir):
        os.chdir(dir)
        files = list(filter(lambda x: isfile(x) and '.pdf' in x, os.listdir()))
        try:
            merger = PdfFileMerger()
            files.sort()
            for file in files:
                print(file)
                with open(file, 'rb') as pdf:
                    merger.append(PdfFileReader(pdf))
            
            merger.write(dir + '_merged.pdf')
            merger.close
            del merger
            for file in files:
                os.remove(file)
        except Exception as e:
            err2.append(e) 
            print("erro na pasta " + dir)
            err.append(dir)
    os.chdir('..')

print("Erros: ")
print(err)
print(err2)
print("done")
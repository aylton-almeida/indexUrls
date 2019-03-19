import os

class Arquivo:
    nomeArquivo = str()

    def __init__ (self, nomeArquivo):
        self.setNomeArquivo(nomeArquivo)

    def setNomeArquivo(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo

    def addRegistro(self, r):
        if (os.path.isfile('./%s' % (self.nomeArquivo))):
            file = open(self.nomeArquivo, 'r+')
        else:
            file = open(self.nomeArquivo, 'w')
        file.seek(0, 2)
        file.write(r + "\n")
        file.close()

    def getRegistro(self, id):
        file = open(self.nomeArquivo, 'r')
        list = file.readlines()
        for item in list:
            if (id in item):
                return item

    def getAllRegistros(self):
        file = open(self.nomeArquivo, 'r')
        myList = file.readlines()
        file.close()
        return myList

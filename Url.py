import urllib.request
import re


class Url:
    paginaString: str()

    def __init__(self, url):
        self.setPaginaString(url)

    # Acessa o site e pega o html em uma unica string
    def setPaginaString(self, url):
        site = urllib.request.urlopen(url)
        html = site.read()
        htmlDecoded = html.decode('utf8')
        site.close()
        self.paginaString = htmlDecoded

    # Retorna a pagina html em uma string
    def getPaginaString(self):
        return self.paginaString

    # Retorna a pagina html em uma lista
    def getPaginaList(self):
        return self.paginaString.split('\n')

    # Filtra as linhas importantes e remove as tags e artigos/preposições
    def getWords(self):
        list = self.getPaginaList()
        palavras = []
        for line in list:
            if("<h" in line or "<p" in line or "<a" in line):
                # Remover tags
                line = re.sub("<.*?>", "", line)
                # Remover tabs
                line = re.sub("\t", "", line)
                # Remover numeros
                #line = re.sub("\d", "", line)
                palavras.append(line)

        palavrasDefinitivas = []
        for line in palavras:
            quickList = line.split(" ")
            for item in quickList:
                if (len(item) > 1):
                    palavrasDefinitivas.append(item)
        return palavrasDefinitivas

    # Indexar cada palavra dentro das frases
    def indexaPalavra(self, str):
        pagina = self.getPaginaList()
        strIndexada = str + "<";
        for i in range(len(pagina)):
            if str in pagina[i]:
                # Definir index da palavra na linha
                index = pagina[i].find(str)
                strIndexada += '%s, %d>' % (i, index)
        return strIndexada

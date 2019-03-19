from Arquivo import Arquivo
from Url import Url

url = Url('https://docs.python.org/3/')
file = Arquivo('teste')

list = url.getWords()

for word in list:
    file.addRegistro(url.indexaPalavra(word))

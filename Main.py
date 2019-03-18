from Arquivo import Arquivo
import urllib.request

url = urllib.request.urlopen("http://www.aylton.dev")
html = url.read()

str = html.decode("utf8")
url.close()

print(str)

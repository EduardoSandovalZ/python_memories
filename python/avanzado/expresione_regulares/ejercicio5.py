import re 

text = 'Este es un ejemplo de una pagina web: https://www.youtube-hola.com'
# el ? indica que el caracter antes de ? puede o no coincidir
pattern = r'https?://www\.+[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
result = re.findall(pattern,text)


print(result)
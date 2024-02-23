import re
# esta es la cadena original
text = 'La fecha es 23/06/2021 y el telefono es +1-555-5555'
print(text)
pattern = r'\d{2}/\d{2}/\d{4}|\+\d{1}-\d{3}-\d{4}'
# pattern = r'\+\d{1}-\d{3}-\d{4}'

repl = 'Informacion privada'
new_text = re.sub(pattern,repl,text)
print(new_text)


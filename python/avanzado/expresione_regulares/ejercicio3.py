import re
text = 'remmplazando todas las vocales por asteriscos'
vocales = '[aeiou]'
new_text = re.sub(vocales,'*',text)
print(new_text)
# Contar el numero de vocales de un texto
def count_vowels(text):
    vocals = ['a','e','i','o','u']
    vocal_count = 0
    for letter in text:
        if letter in vocals:
            vocal_count += 1
    
    return vocal_count



text = input('Proporcione un texto: ').lower()
print(count_vowels(text))

# Contar el numero de vocales de un texto
# def count_vowels(text):
#     vocals = ['a','e','i','o','u']
#     vocal_count = 0
#     for letter in text:
#         if letter in vocals:
#             vocal_count += 1
    
#     return vocal_count



# text = input('Proporcione un texto: ').lower()
# print(count_vowels(text))


# Otro ejemplo

def random_pass(num):
    chars = 'abcdefghij'
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = num - 2
    print(c1)
    c2 = num
    c3 = num - 5
    print(c3)
    password = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return password
    
    
password = random_pass(9)
print(f'Tu password es: {password}')
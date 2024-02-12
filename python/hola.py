

name = input('Name:').capitalize()
last_name = input('Last Name:').capitalize()
age = int(input('Age:'))
gender = input('Gender (M/F):').upper()

person = {
    'Name': name,
    'Last_name': last_name,
    'Age': age,
    'Gender': gender
}

print(len(person['Last_name']))

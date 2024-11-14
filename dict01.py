man = {
    'age': 19,
    'name': 'John',
    'birthday': '2005-01-01',
    'addres': {
        'street': 'Mira',
        'number': '22',

    }

}



print(
    man['age']
)


def add(a):
    a['age'] = 10

add(man)

print(man)


man['eye_color'] = 'blue' #add new key

print(man)

del man ['age'] #delete element

print (man)


# Let us see how to create a dictionary

phonebook = {}
phonebook["Asun"] = 651996148
phonebook["Andrea"] = 648507865
phonebook["Mummy"] = 616925243
phonebook["Daddy"] = 676834126

print(phonebook)

# Alternatively a dictionary can be built as follows:

second_phonebook = {"Marina": 666819090,
                    "Asun": 651996148,
                    "Ana Happy": 645401239}
print(second_phonebook)

# To iterate in the dictionaries we have to use both the key and the value as follows:

print("The phone numbers of my family and I are:")
for name, number in phonebook.items():
    print("If you want to call %s, just type %d" % (name, number))

# To delete a value of the dictionary use the del function

del second_phonebook["Asun"]
print(second_phonebook)

# Alternatively

second_phonebook.pop("Ana Happy")
print(second_phonebook)

# EXERCISE: Create a nested dictionary. The keys of the outer one should be the letters in alphabetical order, and the
# keys of the inner one should be the name of a person, age, color of eyes, and color of hair:

fantastic_group = {'a': {'name': 'Ana Happy',
                         'age': 28,
                         'eyes_color': 'blue',
                         'hair_color': 'brown'},
                   'b': {'name': 'Asun',
                         'age': 27,
                         'eyes_color': 'brown',
                         'hair_color': 'brown'},
                   'c': {'name': 'Bea',
                         'age': 28,
                         'eyes_color': 'blue',
                         'hair_color': 'brown'},
                   'd': {'name': 'Cristina',
                         'age': 27,
                         'eyes_color': 'brown',
                         'hair_color': 'brown'}
                   }
for letter, dictionary in fantastic_group.items():
    print("The age of %s is %d" % (dictionary['name'], dictionary['age']))

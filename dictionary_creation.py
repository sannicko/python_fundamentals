
# Each item in the dictionary is known as a "key-value pair"

acronyms = {'LOL': 'laugh out loud',
            'IDK': 'I don\'t know', # back slash to scape ' inside the word
            'TBH': 'to be honest'}

print(acronyms['LOL']) # to look up a value in a dictionary, send in a key and the value is return.

# to delete a value use del and send the key:

del acronyms['LOL']
print(acronyms)

definition = acronyms.get('CML')
if definition:
  print(definition)
else:
  print("key doesn't exist")
print(definition) # None absence of the value


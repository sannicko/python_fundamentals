acronyms = {'ASAP': 'as soon as possible',
            'LMK': 'let me know',
            'EOD': 'end of day',
            'BAH': 'basic allowance for housing'}
try:
  definition = acronyms['BTW']
  print('Definition of ', 'BTW', ' is ', definition)
except:
  print('The key ', 'BTW', 'does not exist')
finally:
  print('The acronyms defined are:')
  for acronym in acronyms:
    print(acronym)
print('The program keeps going...')

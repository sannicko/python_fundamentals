# # String Iteration
# An iterable in Python refers to any object that can provide its elements or members one by one. Examples of iterables include lists, strings, and other collection objects. This means that strings can be looped over and processed character by character. In each iteration of the loop, a single character of the string is accessed.


# for-each Loop
txt =  "Moon"
for char in txt:
    print(char)

# range() Loop
txt =  "Moon"
for i in range(len(txt)):
	print(txt[i])

# enumerate() Loop

txt =  "Moon"
for i, char in enumerate(txt):
    print(i, char)

txt2 = "Hello Moon"
for index, character in enumerate(txt2):
  print(index, character)


    

s = 'presidency college bengaluru'

char = list(s)
print(char)

names = s.split()
print(names)

str2 = ''.join(char)      #no space is provided as real list has space
print(str2)

str3 = ' '.join(names)        #space is provided (joins the elements of the list names into a string with given delimiter space)
print(str3)


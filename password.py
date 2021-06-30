import random 
pasword_len = int(input("enter the lengh password : "))
characters = 'abcdefghijklnmopqrstuvwxz0123456789{}()_-+=:;.?></@#%^&*'
a = ''.join (random.sample(characters, pasword_len))
print(a)
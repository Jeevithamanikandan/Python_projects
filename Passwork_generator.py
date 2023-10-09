# import 'Random' lib module
import random
print('Welcome to HEWLETT password generator')

characters= ('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz')
number_of_passwords= int(input('Enter number of passwords you want:'))
password_length= int(input('Enter number of password length:'))
print('Here are your passwords:')
for x in range (number_of_passwords):
    password= ''
    for i in range(password_length):
        password=password+random.choice(characters)
    print(password)



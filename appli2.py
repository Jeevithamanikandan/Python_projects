import random
def Generate_OTP():
    return random.randint(100000, 999999)
print('Welcome to Craftofia Creations')
a={}
phone_number=[]
option1=input('l/r')
if option1=='r':
    option2 = input('Are you above 15 [yes/no]')
    while True:
        if option2=='no':
                print('Your are not able to register',end='')
                break
        else:
            name=input('Enter your first name')
            phone_number=input('Enter your phone number')
            user_name=input('Enter your user_name')
            password=input('Enter your password')
            print(f'your account was registered successfully+ {name}')
            a[user_name]=password
            option1=input('l/q')
            if option1=='q':
                print('Thankyou for using our application')
            break
if option1=='l':
    user_name=input('Enter your user_name')
    password=input('Enter your password')
    if user_name in a and a[user_name]==password:
        print('login successfully')
    else:
        print('Incorrect username and password')

option3 = input('Enter (g) for main menu\n')
if option3 == 'g':
    print('Main menu')
print('~~~~~~Items available in our shops~~~~~~')

product = {
    'Onion': 10,
    'Tomato': 15,
    'Mushroom': 20,
    'Shop': 15,
    'Shampoo': 90,
    'face wash': 85,
    'Laundry shop': 10,
    'Egg': 6,
    'Milk': 15,
    'Butter': 18,
    'Cookies': 35,
    'Chips': 10,
    'Candy': 5,
    'Popcorn': 12,
    'Garbage bags': 25,
    'Washing powder': 15
}

cart = []
total = 0

for key, value in product.items():
    print(f'{key:15}: ${value:.2f}')

while True:
    option4 = input('Do you wish to continue shopping [yes/no]: ')
    if option4 == 'no':
        break
    elif option4 == 'yes':
        option5 = input('Add items: ')
        option5 = option5.capitalize()  # Capitalize the item name
        if option5 in product:
            option6 = int(input('Add quantity: '))
            cart.append((option5, option6))
        else:
            print('Invalid item. Please choose from the available items.')
    else:
        print('Invalid options, please click yes/no')

print('~~~~~~YOUR ORDER~~~~~~')

for item, quantity in cart:
    price = product.get(item, 0)
    item_total = price * quantity
    total += item_total
    print(f'{item:15}: ${price:.2f} x {quantity} = ${item_total:.2f}')


print(f'Total: ${total:.2f}')

OTP=Generate_OTP()
option7=input('To confirm order click [yes/no]')
if option7=='yes':
    print(f'OTP sent to you{phone_number}:{OTP}')
    entered_OTP= int(input('Enter the OTP sent to your phone'))
    if entered_OTP==OTP:
        print('Order confirmed. Thank you!')
    else:
        print('Incorrect OTP. Order confirmation failed')


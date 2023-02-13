cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("hold the anchovies")

answer = 17

if answer != 42:
    print("that is not the correct answer. Please try again!")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

deck = "black"
print("is deck == 'black'? i predict true.")
print( deck == 'black')

print("\nIs deck == 'red'? i predict false.")
print(deck == 'red')

alien_color = ('black')

if alien_color is ('red'):
    print("you earned five pts")
elif 'yellow' 'black':
    print("you lose")

age = 33

if age < 2:
    years = "ur a baby"
if age > 2 < 4:
    years = ("ur a toddler")
if age >= 4 < 13:
    years = ("ur a kid")
if age >= 13 < 20:
    years = ("ur a teenager")
if age >= 20 <65:
    years = ("ur an adult")
if age> 65:
    years = ("ur an elder")
else:
    ("ur immortal")
print("years is " + str(years) + ".")

favorite_fruits = ["banana", "cherry", "apple", "dragon", "avocado"]

if "dragon" in favorite_fruits:
    print("i love dragon")
if "banana" in favorite_fruits:
    print("i love banana")
if "orange" in favorite_fruits:
    print("i win")
if "avocado" in favorite_fruits:
    print("i love avos")
if "apple" in favorite_fruits:
    print("i love apple pie")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry, we are out of green peppers.")
    else:
        print("adding " + requested_topping + '.')

    print("\nFinished making your pizza!")

usernames = ['ed', 'jake', 'yin', 'chino', 'admin']

for username in usernames:
    if username == 'admin':
        print("hello admin would you like a status report")
    else:
        print("whats good")

current_user = ['ed', 'jake', 'yin', 'chino', 'admin']

new_user = ['john', 'larry', 'ed', 'yin', 'mort']

if user in new_user == current_user:
    print("username is already in use")
else:
    print("go ahead boss use that name")



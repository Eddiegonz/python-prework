magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    
    print("Thank you, everyone. That was a great magic show!")
pizzas = ['pep', 'cheese', 'shroom']
for pizza in pizzas:
    print(pizza)
    print("I like pep pizza")

print("I really like pizza we should have pizza once a week")

animals = ['bat', 'cat', 'bear']
for animal in animals:
    print(animal)
    print("All these animals are good pets, " + animal.title() + ".\n")

print("all these animals are in isekai's," + " any of these animals would make great pets")

for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

numbers = list(range(0,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1,20,2))
print(odd_numbers)

cubes = []
for value in range(1,11):
    cubes.append(value**2)

print(cubes)

cubes = [value**2 for value in range(1,11)]
print(cubes)

players = ['ed', 'john', 'ace', 'pete', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy favorites foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream', 'eggs']
print(my_foods)
print("the first three items in my list are")
print(my_foods[:3])
print("the three items from the middle of my list are")
print(my_foods[1:4])
print("the last three items in the list are")
print(my_foods[-3:])

my_pizzas = ['pep', 'cheese', 'shroom', 'sausage', 'chicken']
friend_pizzas =(my_pizzas[:])
my_pizzas.append('brocoli')
friend_pizzas.append('snakes')

print("my fav is")
print(my_pizzas)
print("\nfriends fav is")
print(friend_pizzas)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

foods = ('apple', 'grape', 'oj', 'jam', 'candy')
print("original foods:")
for food in foods:
    print(food)

foods = ('apple', 'grape', 'oj', 'beef', 'bacon')
print("\nfoods:")
for food in foods:
    print(food)

foods = ['pizza', 'tacos', 'dim sum', 'sushi']

print(foods[1])
for food in foods:
    print(f"i like {food} because its yummy")

    if food == "pizza":
        break
    print(food)
    
print(list(enumerate(foods)))

deck = ["pikachu", "mew", "mewtwo", "charizard"]
print(deck[1])

deck = ["pikachu", "mew", "mewtwo", "charizard"]
my_card=deck[-1]
print (my_card)

deck = ["pikachu", "mew", "mewtwo", "charizard"]
del deck[1]
print(deck)

deck = ["pikachu", "mew", "mewtwo", "charizard"]
deck[3] = "charmander"
deck.reverse()
print(deck)

deck = ["pikachu", "mew", "mewtwo", "charizard"]
del deck[1]
print(len(deck))

deck = ["pikachu", "mew", "mewtwo", "charizard"]
deck.sort(reverse=True)
print(deck)

deck = ["pikachu", "mew", "mewtwo", "charizard"]
sorted(deck)
print(deck)

deck = ["pikachu", "mew", "mewtwo", "charizard"]
deck.append(2)
print(deck)

deck = ["pikachu", "mew", "mewtwo", "charizard"]
deck.insert(1,"charmander")
print(deck)

deck = ["pikachu", "mew", "mewtwo", "charizard"]
deck = deck.pop()
print(deck)

my_list = ["chicken wing", "chicken wing" "hot dog", "bologna", "chicken", "macoroni"]
for index in my list:
    print(index, end=' ')

my_list = ["chicken wing", "chicken wing" "hot dog", "bologna", "chicken", "macoroni"]
my_string = ""
for index, object in enumerate(my_list):
    my_string += object + " "
    if index == 3 or index == 4:
        my_string += "and "
print(my_string)

my_list = ["chicken wing", "chicken wing" "hot dog", "bologna", "chicken", "macoroni"]
for index in range(3):
    print(my_list[index], end=" ")
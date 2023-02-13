alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# move the alien to the right.
# determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien.
    x_increment = 3
# the new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

print("\nNEW")
friend_info = {'first name':'ace','last name':'roger','lives at':'white beards ship'}
print(friend_info['first name'])
print(friend_info['last name'])
print(friend_info['lives at'])

fav_numbers = {
    'ace': '11',
    'roger': '1',
    'luffy': '8',
    'nami': '10',
    'eddie': '7'
    }
print("eddie' favorite number is " + fav_numbers['eddie'].title() + ".")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
print("\nNEW")


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")
        
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for language in favorite_languages.values():
    print(language.title())

fav_decks = {
    'luffy': 'red',
    'law': 'redgreen',
    'kid': 'green',
    'kaido': 'purple',
    }

print("fav deck color for leader")
for name, deck in fav_decks.items():
    print(name.title() + "'s fav decks is," + deck.title() + ".")

print("\nNEW")
for name in fav_decks.keys():
    print(name.title())
print("\nNEW")

for name in sorted(fav_decks.keys()):
    print(name.title() + ", thank you for chooseing EA sports.")
print("\nNEW")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\nNEW")

aliens = []

for alien_numbers in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:5]:
    print(alien)
print("...")

print("total number of aliens: " + str(len(aliens)))

print("\tNEW")
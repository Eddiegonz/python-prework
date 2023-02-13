bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
dead = ['ace', 'fire', 'roger']
message = "I need a friend like " + dead[0]
print(message)
dead.append('poison')
print(dead)
dead.remove('fire')
print(dead)
dead.insert(0, 'whitebeard')
print(dead)
dead.insert(2, 'big mom')
print(dead)
message = "i can only invite two people to dinner " + dead[0]
print(message)
del dead[4]
print(dead)
popped_dead = dead.pop
print(dead)
print(popped_dead)
dead = ['whitebeard', 'ace', 'big mom', 'roger']
popped_dead = dead.pop()
print(dead)
print(popped_dead)
print(dead)
print(popped_dead)
dead.pop(-1)
print(dead)
print(popped_dead)
del dead [1]
print(dead)
del dead[0]
print(dead)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
places = ['moon', 'mars', 'isekai', 'tokyo', 'japan']
print(places)
print("here is the original list")
print(places)
print("\nhere is the sorted list")
print(sorted(places))
print(places)
places = ['moon', 'mars', 'isekai', 'tokyo', 'japan']
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort
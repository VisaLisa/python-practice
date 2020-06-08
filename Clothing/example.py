from shirt import Shirt
from pant import Pant

shirt_one = Shirt('red', 'M', 'long_sleeve', 45)
shirt_two = Shirt('orange', 'S', 'short_sleeve', 30)

pant_one = Pant('pink',4,32,400.99)
pant_two = Pant('blue',12,34,49.99)

print(shirt_one.price)
print(shirt_two.price)
print(shirt_two.color)

shirt_two.change_price(45)
print(shirt_two.price)

shirt_one.color = 'yellow'
shirt_one.size = 'L'
shirt_one.price = 39

print(pant_one.price)


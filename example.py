from shirt import Shirt

shirt_one = Shirt('red', 'M', 'long_sleeve', 45)
shirt_two = Shirt('orange', 'S', 'short_sleeve', 30)

print(shirt_one.price)
print(shirt_two.color)

shirt_two.change_price(45)
print(shirt_two.price)
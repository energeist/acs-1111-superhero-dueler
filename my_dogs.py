import dog

my_dog = dog.Dog("Rex", "SuperDog")

my_other_dog = dog.Dog("Annie", "SuperDog")

my_other_other_dog = dog.Dog("Buster", "SuperDuperDog")

print(my_dog.name)
print(my_dog.breed)
my_dog.bark()
print(my_other_dog.name)
print(my_other_dog.breed)
my_other_dog.sit()
print(my_other_other_dog.name)
print(my_other_other_dog.breed)
my_other_other_dog.roll_over()
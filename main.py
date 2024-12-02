age = 12
name = "John"
favourite_number = "7"
city = "London"
print("\n Before typecasting: ")
i_std = True
print("Age type = ", type(age))
print("Name type = ", type(name))
print("Fav number type = ", type(favourite_number))
print("City type = ", type(city))
print("Is student datetype= ", type(i_std))
print("\n After typecasting: ")
age = str(age)
name= str(name)
favourite_number = int(favourite_number)
city = str(city)
i_std = str(i_std)
print("Age type = ", type(age))
print("Name type = ", type(name))
print("Fav number type = ", type(favourite_number))
print("City type = ", type(city))
print("Is student datetype= ", type(i_std))

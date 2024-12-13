Pet_Food = "dog"
age = 1
#Pet_Food = "Cat"


if Pet_Food == "dog":
    if age < 2:
        print( Pet_Food, "is Puppy food")
    else:
         print(Pet_Food, "is Adult food")
elif Pet_Food == "Cat":
    if age < 1:
        print(Pet_Food, "is Kitten food")
    elif age > 5:
        print(Pet_Food, "is Senior food")
    else:
        print("Adult cat food")
else:
    print("Invalid Pet_Food")
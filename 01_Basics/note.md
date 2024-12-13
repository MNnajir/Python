## List in Python

>>> chai = "Leomon"
>>> print(chai)
Leomon
>>> chai_type = "Masala"
>>> quantity = 3
>>> order = "I ordered {} cups of {} chai "
>>> order
'I ordered {} cups of {} chai '
>>> print(order.format(quantity, chai_type))
I ordered 3 cups of Masala chai 
>>> chai
'Lemon , Ginger, Masala, Mint'
>>> chai = "Masala Chai"
>>> chai
'Masala Chai'
>>> for letter in chai
  File "<python-input-31>", line 1
    for letter in chai
                      ^
>>> chai = "He said, "\Masala chai is awesome\" "
  File "<python-input-33>", line 1
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> for tea in tea_varities:
...     print(tea)
...     
Black 
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> if "Oolong" in tea_varities:
...     print(tea)
...     
>>> tea_varities.append("Oolong")
>>> tea_varities
['Black', 'green', 'Masala', 'White', 'Oolong']
>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
...     
I have Oolong tea
>>>  tea_varities.remove("green")
>>> tea_varities
['Black', 'Masala', 'White', 'Oolong']
>>> tea_varities.insert(1, "green")
>>> tea_varities
['Black', 'green', 'Masala', 'White', 'Oolong']
>>> tea_varities_copy = tea_varities.copy()
>>> tea_varities_copy
['Black', 'green', 'Masala', 'White', 'Oolong']
>>> tea_varities
['Black', 'green', 'Masala', 'White', 'Oolong']
>>> tea_varities_copy.append("Lemon")
>>> tea_varities_copy
['Black', 'green', 'Masala', 'White', 'Oolong', 'Lemon']
>>> squared_nums = [x**2 for x in range(10)]
>>> range(10)
range(0, 10)
>>> print(range)
<class 'range'>
>>> print(range(10))
range(0, 10)
>>> y = range(10)
>>> y
range(0, 10)
>>> squared_nums = [x**2 for x in range(10)]
>>> squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_num = [y**3 for y in range(5)]
>>> cube_num
[0, 1, 8, 27, 64]
>>> 


## Dictionary in Python 

>>> chai_types = {"Lemon": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
>>> chai_types
{'Lemon': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Lemon"]
'Spicy'
>>> chai_types.get("Ginger")
'Zesty'
>>> chai_types.get("Gingery")
>>> chai_types["Massala"]
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    chai_types["Massala"]
    ~~~~~~~~~~^^^^^^^^^^^
KeyError: 'Massala'
>>> chai_types
{'Lemon': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Green"] = "testy"
>>> chai_types
{'Lemon': 'Spicy', 'Ginger': 'Zesty', 'Green': 'testy'}
>>> for chai in chai_types:
...     print(chai)
...
Lemon
Ginger
Green
>>> for chai in chai_types:
...     print(chai, chai_types[chai])
...
Lemon Spicy
Ginger Zesty
Green testy
>>> for key, value in chai_types.items():
...     print(key, value)
...     
Lemon Spicy 
Ginger Zesty
Green testy 
>>> if "Lemon" in chai_types:
...     print("I have Lemon chai")
...     
I have Lemon chai
>>> print(len(chai_types))
3   
>>> chai_types
{'Lemon': 'Spicy', 'Ginger': 'Zesty', 'Green': 'testy'}
>>> chai_types["Earl Grey"] = "Citrus"
>>> chai_types
{'Lemon': 'Spicy', 'Ginger': 'Zesty', 'Green': 'testy', 'Earl Grey': 'Citrus'}
>>> chai_types.pop("Ginger")
'Zesty'
>>> chai_types
{'Lemon': 'Spicy', 'Green': 'testy', 'Earl Grey': 'Citrus'}
>>> chai_types.popitem()
('Earl Grey', 'Citrus')
>>> chai_types
{'Lemon': 'Spicy', 'Green': 'testy'}
>>> del chai_types["Green"]
>>> chai_types
{'Lemon': 'Spicy'}
>>> tea_shop = {
... "chai": {"Masala" : "Spicy", "Ginger": "Zesty"},
... "Tea" : {"Green": "Mild" , "Black":"Strong"}
... }
>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> print(tea_shop)
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"]
'Zesty'
>>> squared_num = {x:x**2 for x in range(6)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear()
>>> squared_num
{}  
>>> keys = ["Masala", "Ginger", "Lemon"]
>>> keys
['Masala', 'Ginger', 'Lemon']
>>> default_value = "Delicious"
>>> new_dict = dict.fromkeys(keys, default_value)
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> new_dict = dict.fromkeys(keys,keys)
>>> new_dict
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}

## Tuples in Python
>>> tea_types = ("Black" , "Green", "Lemon")
>>> tea_types
('Black', 'Green', 'Lemon')
>>> tea_types[0]
'Black'
>>> tea_types[-1]
'Lemon'
>>> tea_types[1:]
('Green', 'Lemon')
>>> tea_types[0] = "Masala"
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    tea_types[0] = "Masala"
    ~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
>>> more_tea = ("Herbal", "Early Grey")
>>> all_tea = more_tea + tea_types
>>> all_tea
('Herbal', 'Early Grey', 'Black', 'Green', 'Lemon')
>>> if "Green" in all_tea:
...     print("I have green tae")
...     
I have green tae
>>> more_tea = ("Herbal", "Early Grey","Herbal")
>>> more_tea.count("Herbal")
2   
>>> tea_types
('Black', 'Green', 'Lemon')
>>> (black, green, oolong) = tea_types
>>> black
'Black'
>>> green 
'Green'
>>> oolong
'Lemon'
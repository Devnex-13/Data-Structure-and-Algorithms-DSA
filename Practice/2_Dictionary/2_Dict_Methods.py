name = {
  "Fname":"Dev",
  "Lname":"Pote",
  "Age":21
}

print(name)

# To get all keys from the dictionary, we can use the keys() method.
print(name.keys())

# To get all values from the dictionary, we can use the values() method.
print(name.values())

# To get all key-value pairs from the dictionary, we can use the items() method.
print(name.items())

# To check if a key exists in the dictionary, we can use the in keyword.
if "Fname" in name:
  print("Key 'Fname' exists in the dictionary.")

# To check if a value exists in the dictionary, we can use the values() method along with the in keyword.
if 21 in name.values():
  print("Value '21' exists in the dictionary.")

# to remove a key-value pair from the dictionary, we can use the pop() method.
name.pop("Age")

# To remove the last inserted key-value pair from the dictionary, we can use the popitem() method.
name.popitem()

# To update the value of a key in the dictionary, we can use the update() method.
name.update({"Fname": "John"})

# To clear all key-value pairs from the dictionary, we can use the clear() method.
name.clear()
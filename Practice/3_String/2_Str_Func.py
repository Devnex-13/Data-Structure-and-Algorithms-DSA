name = "devanshu pote"
email = "devanshu.p.pote@gmail.com"

print(name.upper()) # Output: DEVANSHU POTE (converts all characters to uppercase)

print(name.lower()) # Output: devanshu pote (converts all characters to lowercase)

print(name.capitalize()) # Output: Devanshu Pote (converts the first character to uppercase and the rest to lowercase)

print(name.title()) # Output: Devanshu Pote (converts the first character of each word to uppercase)

print(name.strip()) # Output: devanshu pote (removes leading and trailing whitespace)

print(email.split("@")) # Output: ['devanshu.p.pote', 'gmail.com'] (splits the string at the '@' character)

print(email.replace("gmail.com", "yahoo.com")) # Output: devanshu.p.pote@yahoo.com

print(name.find("pote")) # Output: 8 (returns the index of the first occurrence of the substring "pote")

print(name.count("e")) # Output: 2 (counts the number of occurrences of the character "e" in the string)

print(name.swapcase()) # Output: DEVANSHU POTE (converts uppercase to lowercase and vice versa)

print(name.startswith("devan")) # Output: True (checks if the string starts with "devan")

print(email.endswith("gmail.com")) # Output: True (checks if the string ends with "gmail.com")

print(name.isalpha()) # Output: False (checks if all characters in the string are alphabetic; returns False due to space)

print(name.isalnum()) # Output: False (checks if all characters in the string are alphanumeric; returns False due to space)

print(name.isdigit()) # Output: False (checks if all characters in the string are digits; returns False)

name = "devanshupote"
email = "devanshu.p.pote@gmail.com"

print(name[0:5])  # Output: devan
print(name[:6]) # Output: devans
print(name[6:]) # Output: hupote 
print(name[::2]) # Output: dvnupte (every second character from the string)
print(name[0:5:2]) # Output: dvan (every second character from the first 5 characters)

print(name[-6:]) # Output: hupot
print(name[-4:]) # Output: pote
print(name[:8]) # Output: devanshu (first 8 characters from the string)

print(name[-4:]+name[:-4]) # Output: potedevanshu (last 4 characters + first 8 characters)

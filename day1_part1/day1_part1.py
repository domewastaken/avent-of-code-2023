
f = open('input.txt','r')
somma = 0
for line in f:
    first_d = 0
    for char in line:
        if char.isdigit():
            first_d = char
            break

    for char in line[::-1]:
        if char.isdigit():
            last_d = char
            break
    
    somma += int(first_d+last_d)
print(somma)
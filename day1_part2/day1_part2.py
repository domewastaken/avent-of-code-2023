
arr =['','one', 'two', 'three', 'four', 'five','six', 'seven', 'eight', 'nine']

f = open('input.txt','r')
somma = 0

for line in f:
    first_d = ''
    list1 = ''
    for char in line:
        if char.isdigit():
            first_d = char
            break
        else:
            list1+=char

            for i in range(1,10):

                if list1.find(arr[i]) != -1:
                    first_d = str(i)
                    break
            if first_d != '':
                break

    list1=''
    last_d=''
    for char in line[::-1]:
        if char.isdigit():
            last_d = char
            break
        else:
            list1 = char+list1
            print(list1)
            for i in range(1,10):
                if list1.find(arr[i])!=-1:
                    last_d = str(i)
                    break
            if last_d != '':
                break
    somma += int(first_d+last_d)
print(somma)
string = input("Enter a new string:")


def length():
    count = 0
    for i in string:
        count += 1
    print("Length of string is:",count)

length()

def repitition():
    rep = 0
    char=input("Enter a character:")

    for i in string:
         if i==char:
             rep +=1



    print("The letter occurs",rep,"times")

repitition()

def palindrome():
        if string==string[::-1]:
            print("Given word is a palindrome")
        else:
            print("Given word is not a palindrome")
palindrome()

def indexofsubstring():
    substr=input("Enter a substring:")
    index = 0
    for i in string:
        for j in substr:
            if i == substr:
                index += 1

    print("Index of first appearance of substring:", index)

indexofsubstring()
print("-----------start basic calculator-----")
while True:
        
    function= int(input('''
    press 1 for addition
    press 2 for subtraction
    press 3 for multiplication
    press 4 for division
    to quit press 0
    '''))
    if function > 4:
        print("Try again")
        continue
    if function < 1 :
        break
    num1=int(input("Enter a number"))
    num2=int(input("Another number"))

    if function==1:
        print(num1+num2)
    elif function==2:
        print(num1-num2)
    elif function==3:
        print(num1*num2)
    elif function==4:
        print(num1/num2)
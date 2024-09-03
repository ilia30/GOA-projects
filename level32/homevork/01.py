def positive_negative():
    num=int(input("enter your number:"))

    if num > 0:
     
        print(-num)         
    elif num < 0:
        print(abs(num))

    else:
        print("you entered 0")
    
result=positive_negative()
print(result)
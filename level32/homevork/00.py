def even_odd():
    num=int(input("enter your number:"))
    
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    return num
result = even_odd()
print(result)
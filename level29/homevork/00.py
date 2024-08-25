weight = float(input("enter your weight in kg "))
height = float(input("enter your height in m"))
result = weight // (height ** 2)
print(result)

if result < 18:
    print("you are underweight")
elif result < 25: 
    print("you are normalweight")
elif result <30:
    print("you are overwight")
else:
    print("you are obese")
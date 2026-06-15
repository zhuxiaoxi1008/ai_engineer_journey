height = input("Enter your height in meters (1.75): ")
height = float(height)

weight = input("Enter your weight in kg (80.5): ")
weight = float(weight)

# bmi = (weight / (height * height)) * 703
bmi = weight / (height * height)

if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 28:
    print("过重")
elif 28 <= bmi < 32:
    print("肥胖")
else:
    print("非常肥胖")


print(f"你的BMI指数是: {bmi:.2f}")
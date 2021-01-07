# print(3+5)
# print(10 - 3)
# print(3 * 30)
# print(8 / 5)
# print(3 ** 5)


# print(3 * (3 + 3) / 3 - 3)


# bmi calculation

height = input("enter your height in meters: ")
weight = input("enter your weight in kilos: ")

bmi =  int(weight) / float(height) ** 2
bmi_int = int(bmi)
print(f"your bmi is {bmi_int}")

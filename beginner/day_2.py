# two_digit_num = input("Enter two digit number: ")
# print(
#     f"{two_digit_num[0]} + {two_digit_num[1]} = {int(two_digit_num[0])+int(two_digit_num[1])}")

# # BMI - Calculator
# height = float(input("Enter your Height (in meters): "))
# weight = int(input("Enter your weight (in kgs): "))

# bmi = int(weight/(height) ** 2)

# print(bmi)
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
total_percentage = int(
    input("What percentage tip would you like to give? 5, 7 or 10? "))
total_member = int(input("How Many people to split the bill? "))
result = (total_bill*(1+(total_percentage/100)))/total_member
print(f"Each Person Should pay: {result:.2f}")

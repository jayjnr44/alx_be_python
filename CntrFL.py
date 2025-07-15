# age=0
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not Eligible"

#     message = "eligible" if age <= 18 else "Not Eligible"
#     print(message)


high_income = True
good_credit = False
Student = True

# if not Student:
#     print("Eligible")
# else:
#     print("Not Eligible")

if (high_income or good_credit) and not Student:
    print("Eligible")
else:
    print("Not Eligible")
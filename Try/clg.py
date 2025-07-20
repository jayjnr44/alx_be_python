def has_id(user):
    # Dummy implementation, replace with actual ID check logic
    return user.get("has_id", False)


user = {"has_id": True}  # Example user dictionary

age = int(input("Enter your age: "))

match age:
    case 18 | 19:
        if age >= 18 and has_id(user):
            print("You are eligible to vote.")
        else:
            print("You need a valid ID to vote.")
    case _:
        print("You are not eligible to vote.")

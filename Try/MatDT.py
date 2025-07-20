value = input("Enter a value (number or string): ")

match value:
    case int():
        print("you entered an integer:", value)
    case str():
        print("You entered a string:", value)
    case _:
        print("You entered an invalid data type")
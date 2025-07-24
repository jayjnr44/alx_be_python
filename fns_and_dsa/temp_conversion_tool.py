FAHRENHEIT_TO_CELSIUS_FACTOR=None
CELSIUS_TO_FAHRENHEIT_FACTOR=None

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR 
    FAHRENHEIT_TO_CELSIUS_FACTOR= 5/9
    """Convert Fahrenheit to Celsius using global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR 
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
    """Convert Celsius to Fahrenheit using global factor."""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


temperature= int(input("Enter the temperature to convert: "))
convert_type = str(input("Is this temperature in Celsius or Fahrenheit? (C/F) ")).upper()

if convert_type == 'C':
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp:.2f}°F")
elif convert_type == 'F':
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp:.2f}°C")
elif temperature is not type(int):
    print("Invalid temperature. Please enter a numeric value")
else:
    print("Invalid conversion type. Please enter 'C' for Celsius or 'F' for Fahrenheit.")  














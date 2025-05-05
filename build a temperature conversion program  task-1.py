def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    unit = unit.lower()
    if unit == "celsius" or unit == "c":
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        print(f"{value}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K")
    elif unit == "fahrenheit" or unit == "f":
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        print(f"{value}°F is {celsius:.2f}°C and {kelvin:.2f}K")
    elif unit == "kelvin" or unit == "k":
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        print(f"{value}K is {celsius:.2f}°C and {fahrenheit:.2f}°F")
    else:
        print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")

# Main program
try:
    temp_value = float(input("Enter the temperature value: "))
    temp_unit = input("Enter the unit (Celsius/Fahrenheit/Kelvin): ")
    convert_temperature(temp_value, temp_unit)
except ValueError:
    print("Please enter a valid numeric temperature.")

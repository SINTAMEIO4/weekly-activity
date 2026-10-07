def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = convert_temperature(celsius)
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")

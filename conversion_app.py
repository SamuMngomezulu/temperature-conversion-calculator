# Ask user for their name and carry out greetings

name = input("Hello there, what is your name? ")
print(f"Nice to meet you {name}, I hope you are doing well. Welcome to our temperature conversion calculator!\n")

# Receive Celsius value from user

celsius = float(input("Please enter a value in degrees Celsius: "))

# perform the Celsius temperature to Fahrenheit conversion
fahrenheit = (celsius * 1.8) + 32

# Display the result
print(f"\n{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit. We hope that was helpful!")

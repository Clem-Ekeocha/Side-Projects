'''
The program below is developed to take a text input from a kid user
supposed to be the feet and inches, convert to meters and then go ahead to
check if the value in meters is eligible for the kid to use
'''

feet_inches = input("Enter Feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}

def convert(feet, inches):
    meters = round(((feet * 0.3048) + (inches * 0.0254)), 2)
    return meters

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}m")


if result  < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide")


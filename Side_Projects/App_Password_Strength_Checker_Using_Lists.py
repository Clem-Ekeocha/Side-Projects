''' App is Built to check if a password can be classified as strong or weak
based on the conditions listed below:
    1. The length must be greater or equal to 8.
    2. The password must contain at least 1 digit.
    3. One of the characters must be uppercase. '''

password = input("Enter new password: ")
result = []

''' Check for Condition 1'''
if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

''' Check for Condition 2'''
digit = False
for char in password:
    if char.isdigit():
        digit = True
result.append(digit)

''' Check for Condition 3'''
uppercase = False
for character in password:
    if character.isupper():
        uppercase = True
result.append(uppercase)

# Print(result) -- This gives an output of 3 boleans depending on the inputted passsword

''' Check if all 3 conditions are true '''
if all(result) == True:
    print('Strong Password')
else:
    print('Weak Password')




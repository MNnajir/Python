password = "Secure3P@ss"

# password_length = len(password)
# print(f"Password length: {password_length}")
# if password_length < 6:
#         strength = "Weak"
# elif password_length <= 10:
#      strength = "Medium"
# else:
#      strength = "Strong"
# print(f"Password strength: {strength}")

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"
print("Password strength is:", strength)
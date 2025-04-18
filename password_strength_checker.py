import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
    common_patterns = ['123', 'password', 'qwerty', 'abc', 'letmein'] # can be extended to other patterns as well
    pattern_error = any(pattern in password.lower() for pattern in common_patterns)

    score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error]) - pattern_error

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\nPassword Strength:", strength)
    if length_error:
        print("- Too short (minimum 8 characters).")
    if digit_error:
        print("- Should include at least one number.")
    if uppercase_error:
        print("- Should include at least one uppercase letter.")
    if lowercase_error:
        print("- Should include at least one lowercase letter.")
    if symbol_error:
        print("- Should include at least one special character.")
    if pattern_error:
        print("- Contains a common pattern (e.g., '123', 'password').")

# --- Try it ---
password = input("Enter a password to check: ")
check_password_strength(password)

import re
import string

def check_length(password):
    length = len(password)
    if length < 8:
        return 0, "Too short (minimum 8 characters recommended)"
    elif length < 12:
        return 1, "Moderate length"
    else:
        return 2, "Strong length"


def count_special_characters(password):
    special_chars = [c for c in password if c in string.punctuation]
    if len(special_chars) == 0:
        return 0, "No special characters"
    elif len(special_chars) < 2:
        return 1, "At least 1 special character"
    else:
        return 2, "Good use of special characters"


def check_case_ratio(password):
    upper = sum(1 for c in password if c.isupper())
    lower = sum(1 for c in password if c.islower())

    if upper == 0 or lower == 0:
        return 0, "Use both uppercase and lowercase letters"

    ratio = upper / lower if lower != 0 else 0

    if 0.5 <= ratio <= 2:
        return 2, "Good balance of uppercase and lowercase"
    else:
        return 1, "Could improve letter balance"


def contains_identifying_info(password, personal_info):
    password_lower = password.lower()
    for info in personal_info:
        if info and info.lower() in password_lower:
            return True
    return False


def evaluate_password(password, personal_info):
    score = 0

    length_score, length_msg = check_length(password)
    special_score, special_msg = count_special_characters(password)
    case_score, case_msg = check_case_ratio(password)

    score += length_score + special_score + case_score

    print("\nPassword Evaluation:")
    print("----------------------")
    print(f"Length Check: {length_msg}")
    print(f"Special Characters: {special_msg}")
    print(f"Case Balance: {case_msg}")

    if contains_identifying_info(password, personal_info):
        print("Warning: Password contains identifying information!")
        score -= 2

    print("----------------------")

    if score <= 2:
        print("Overall Strength: Weak")
    elif score <= 4:
        print("Overall Strength: Moderate")
    else:
        print("Overall Strength: Strong")


def main():
    print("CS3090 Block 2 Project - Password Strength Checker")
    print("DISCLAIMER: This program does NOT store any information entered.\n")

    password = input("Enter a password to evaluate: ")
    name = input("Enter your name (for identification check): ")
    phone = input("Enter your phone number (for identification check): ")
    birth_year = input("Enter your birth year (for identification check): ")

    personal_info = [name, phone, birth_year, "password"]

    evaluate_password(password, personal_info)

    # Explicitly clear sensitive data
    password = None
    name = None
    phone = None
    personal_info = None
    birth_year = None


if __name__ == "__main__":
    main()
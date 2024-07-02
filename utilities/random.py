import random
import string


def generate_random_email():
    # Create a list of characters to choose from
    characters = string.ascii_lowercase + string.digits
    random_text = ''.join(random.choice(characters) for _ in range(3))
    return f"{random_text}@gmail.com"


def generate_random_phone_number():
    # Ensure the first digit is 6, 7, 8, or 9
    first_digit = random.choice('6789')
    # Generate the remaining 9 digits
    remaining_digits = ''.join(random.choice(string.digits) for _ in range(9))
    return first_digit + remaining_digits

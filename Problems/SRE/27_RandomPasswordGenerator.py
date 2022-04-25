# Implement a password generator (generate random strings given a charset).
# Be able to toggle charsets on/off for the password generation function.
import random
import string


def random_password_generator(size, restricted_chars):
    total_chars = string.ascii_letters + string.digits + string.punctuation
    allowed_chars = list(set(total_chars) - set(restricted_chars))
    return ''.join(random.choice(allowed_chars) for _ in range(size))


# Invoke function call
restricted_chars = 'abc123'
size = random.randint(10, 15)
print(random_password_generator(size, restricted_chars))

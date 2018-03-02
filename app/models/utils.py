import random, string

def make_test_string(size):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))

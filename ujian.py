import timeit
#original function
def valid_username1(username):
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._"
    for char in username:
        if char not in valid_chars:
            return False
    return True
# Using a set
def valid_username2(username):
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._")
    for char in username:
        if char not in valid_chars:
            return False
    return True
# Using all
def valid_username3(username):
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._")
    return all(char in valid_chars for char in username)
# Using regex
import re
def valid_username4(username):
    return re.match("^[a-zA-Z0-9._]+$", username) is not None
# Test with a valid username
username = "zany_123"
print('using for loop:', timeit.timeit(lambda: valid_username1(username))) # 0.785
print(timeit.timeit(lambda: valid_username2(username))) # 0.417
print(timeit.timeit(lambda: valid_username3(username))) # 0.374
print('using regex:', timeit.timeit(lambda: valid_username4(username))) # 0.216
# Test with an invalid username
username = "zany!123"
print('using for loop:', timeit.timeit(lambda: valid_username1(username))) # 0.116
print(timeit.timeit(lambda: valid_username2(username))) # 0.063
print(timeit.timeit(lambda: valid_username3(username))) # 0.057
print('using regex:', timeit.timeit(lambda: valid_username4(username))) # 0.216

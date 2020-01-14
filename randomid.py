import sys
import random
import string


def randomString(stringLength):
    numbers = "123456789"
    letters = string.ascii_lowercase
    return "".join(random.choice(letters + numbers) for i in range(stringLength))

#change format
chars1 = randomString(0)
chars2 = randomString(4)
print(chars1 + "-" + chars2)

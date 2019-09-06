import random
import math
from prettytable import PrettyTable


def is_prime(number):
    s = 0
    d = number - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    for i in range(5):
        a = random.randint(2, (number - 2))
        b = pow(a, d, number)
        if b == 1 or b == number - 1:
            continue
        for j in range(s - 1):
            b = pow(b, 2, number)
            if b == 1:
                return False
            if b == number - 1:
                break
        if b != number - 1:
            return False
    return True


if __name__ == "__main__":
    # 2
    n = [0] * 10
    p = [0] * 10
    for k in range(10):
        num = random.randint(2 ** 127, 2 ** 128)
        n[k] += 1
        while not is_prime(num):
            n[k] += 1
            num = random.randint(2 ** 127, 2 ** 128)
        p[k] = num
        n[k] += 1
    table = PrettyTable()
    table.field_names = ["Name", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    new_p = ["p"] + p
    new_n = ["n"] + n
    table.add_row(new_p)
    table.add_row(new_n)
    table.align["Name"] = "l"
    print(table)
    # 3
    pi = (2 ** 128 / math.log(2 ** 128) - 2 ** 127 / math.log(2 ** 127)) / 2 ** 127
    print((1 / pi))

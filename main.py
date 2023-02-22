import random

lenght = int(input("> Input your password lenght: "))
nums = "0123456789"
lett = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symb = "!$%&/()=?¿^*_:;"
char = {0 : nums, 1 : lett, 2 : symb}

def rand_pass():
    output = ""
    n = 0
    for x in range(3):
        if n > 2:
            n = 2
        for y in range(lenght//3):
            i = str(random.choice(char[n]))
            output += i
        n += 1
    output = list(output)
    random.shuffle(output)
    output = ''.join(output)
    print(output)

rand_pass()
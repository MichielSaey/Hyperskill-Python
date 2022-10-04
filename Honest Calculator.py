# write your code here
import re

# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

complete = False
pattern = re.compile("[-+/*]")
result = 0.0
memory = 0.0


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6

    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7

    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8

    if not msg == "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    return False


def save_in_memory(v):
    global memory
    memory_loop = True
    msg_index = 10
    answer = ""

    while memory_loop:
        if is_one_digit(v):

            input_loop = True

            while input_loop:
                print_msg(msg_index)
                answer = input()

                if answer == "y":
                    if msg_index < 12:
                        msg_index += 1
                        continue
                    else:
                        input_loop = False
                        memory_loop = False
                        memory = v
                elif answer == "n":
                    input_loop = False
                    memory_loop = False
        else:
            memory_loop = False
            memory = v


def print_msg(index):
    match index:
        case 10:
            print(msg_10)
        case 11:
            print(msg_11)
        case 12:
            print(msg_12)


while not complete:
    print(msg_0)
    x, oper, y = input().split()

    if x == "M":
        x = memory
    if y == "M":
        y = memory

    try:
        number_1 = float(x)
        number_2 = float(y)
    except ValueError:
        print(msg_1)
        continue

    if not pattern.fullmatch(oper):
        print(msg_2)
        continue

    check(number_1, number_2, oper)

    if oper == "+":
        result = number_1 + number_2
    elif oper == "-":
        result = number_1 - number_2
    elif oper == "*":
        result = number_1 * number_2
    elif oper == "/" and number_2 != 0:
        result = number_1 / number_2
    else:
        print(msg_3)
        complete = False
        continue

    print(result)

    read_from_memory = "n"

    loop = True
    while loop:
        print(msg_4)
        read_from_memory = input()
        if read_from_memory == 'y':
            loop = False
            save_in_memory(result)
        elif read_from_memory == "n":
            loop = False

    loop = True
    while loop:
        print(msg_5)
        read_from_memory = input()
        if read_from_memory == 'y':
            loop = False
            complete = False
        elif read_from_memory == "n":
            loop = False
            complete = True

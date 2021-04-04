OPERATORS_LIST = ["+", "-", "x", "*", "/", "="]


def main():
    user_math_express = input("Input your mathematical expression (e.g 1 + 2): ")
    stripped_express = user_math_express.strip()
    express_list = stripped_express.split()
    string_list = []

    for each in express_list:
        if each.isdigit():
            string_list.append(number2string(each))
        elif each in OPERATORS_LIST:
            string_list.append(operators2string(each))

    print(" ".join(string_list))


def number2string(string):
    int_string = int(string)
    if int_string == 1:
        return "one"
    elif int_string == 2:
        return "two"
    elif int_string == 3:
        return "three"
    elif int_string == 4:
        return "four"
    elif int_string == 5:
        return "five"
    elif int_string == 6:
        return "six"
    elif int_string == 7:
        return "seven"
    elif int_string == 8:
        return "eight"
    elif int_string == 9:
        return "nine"


def operators2string(string):
    if string == "+":
        return "plus"
    elif string == "-":
        return "minus"
    elif string == "x" or string == "*":
        return "times"
    elif string == "/":
        return "divided by"
    elif string == "=":
        return "equals to"


if __name__ == "__main__":
    main()


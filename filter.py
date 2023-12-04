import random

def upper_filter(text):
    return text.upper()


def lower_filter(text):
    return text.lower()


def random_filter(text):
    text_result = ""
    for i in text:
        r = random.randint(0, 1)
        if r == 0:
            text_result += text[i].upper()
        elif r == 1:
            text_result += text[i].lower()

    return text_result


def user_choice_input(min, max):
    filter = input("Введите номер желаемого фильтра : ")
    while True:
        if not filter.isdigit() or not min <= int(filter) <= max:
            print("Номер фильтра введен неверно, повторите попытку")
            filter = input("Введите номер желаемого фильтра : ")
        else:
            break
    return int(filter)




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
            text_result += i.upper()
        elif r == 1:
            text_result += i.lower()

    return text_result


def user_choice_input(prompt, error_message,  min, max):
    filter = input(prompt)
    while True:
        if not filter.isdigit() or not min <= int(filter) <= max:
            print(f"{error_message} Число должно быть от {min} до {max}")
            filter = input(prompt)
        else:
            break
    return int(filter)




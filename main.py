import filter

filter_dict = {1: {
                            "description": "ДЕЛАЕТ ВСЕ БУКВЫ ПРЕДЛОЖЕНИЯ ЗАГЛАВНЫМИ",
                            "name": "upper_filter",
                            "func": filter.upper_filter},
                   2: {
                            "description": "делает все буквы предложения строчными",
                            "name": "lower_filter",
                            "func": filter.lower_filter},
                   3: {
                            "description": "Меняет регистр слова в рандомном порядке",
                            "name": "random_filter",
                            "func": filter.random_filter}
                        }

next_move = 0

while next_move != 1:

    print("Введите предложение и номер фильтра, чтобы отредактировать текст")

    sentence = input("Введите предложение : ")

    for i, f in filter_dict.items():
        print(f"{i} - {f["description"]}")


    filter_num = filter.user_choice_input("Введите номер желаемого фильтра : ",
                                          "Номер фильтра введен неверно, повторите попытку", 1, len(filter_dict))

    text = filter_dict[filter_num]["func"](sentence)

    print(f"Отфильтрованное предложение - {text}")

    print("Что будем делать дальше?")
    next_move = filter.user_choice_input("Введите 1, если хотите выйти или 0, если хотите начать заново : ",
                                         "Число введено неверно, повторите попытку", 0, 1)

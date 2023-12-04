import filter

print("Введите предложение и номер фильтра, чтобы отредактировать текст")
sentence = input("Введите предложение : ")
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


for i, f in filter_dict.items():
    print(f"{i} - {f["description"]}")


filter = filter.user_choice_input(1, 3)


text = filter_dict[filter]["func"](sentence)

print(text)








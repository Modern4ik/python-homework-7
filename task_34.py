# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

def get_poem_from_user(message: str) -> str:
    flag = True
    
    while flag:
        user_poem = input(message)

        if len(user_poem.split()) == 0:
            print('Нельзя вводить пустую строку!')
            continue
        else:
            flag = False
    
    return user_poem

def check_poem_by_rhytm(user_poem: str, vow_lst: set) -> bool:
    vow_count = list()
    count = 0

    for word in user_poem.split():
        count = 0
        for char in word:
            if char in vow_lst:
                count += 1
        vow_count.append(count)

    if all(value == vow_count[0] for value in vow_count) and len(vow_count) > 1:
        return True
    else:
        return False
    
def print_report(res: bool) -> None:
    if res:
        print('Парам пам-пам')
    else:
        print('Пам парам')

#####################################################################

poem = get_poem_from_user('Введите стих: ')
vowels = {'а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы'}

result = check_poem_by_rhytm(poem, vowels)

print()
print_report(result)
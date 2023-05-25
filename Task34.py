# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да    
# Вывод: Парам пам-пам

def song(phrase):
    words = phrase.split()
    count_list = []
    for i in words:
        count_list.append(len(list(filter(lambda x: x in 'аоэеиыуёюя', i))))
    if len(set(count_list)) == 1:
        return 'Парам пам-пам'
    return 'Пам парам'

user_phrase = input("Введите фразу: ")
print(song(user_phrase))

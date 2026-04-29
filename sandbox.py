word_sets = [
    (1, 'ввести', 'класс', 'стихи', 'оглянуться', 'резкий'),
    (2, 'ценный', 'желание', 'спор', 'резкий', 'проверить'),
    (3, 'резкий', 'ждать', 'казенный', 'стихи', 'неделя')
]


queries = ['стихи', 'резкий']
fullmatch = []
singlematch = []


for word_set in word_sets:
    # Теперь у флага три состояния:
    # 0 - совпадения нет
    # 1 - в наборе найдено только одно слово
    # 2 - в наборе найдены оба слова
    flag = 0
    # Запускаем уже известный алгоритм, только теперь в каждом
    # наборе ищем по очереди каждое слово из queries
    for query in queries:
        for i in range(1, len(word_set)):
            if query.lower() in word_set[i].lower():
                flag += 1
                break


    if flag == 1:
        singlematch.append(word_set)
    elif flag > 1:
        fullmatch.append(word_set)


print('1', singlematch)
print('2', fullmatch)
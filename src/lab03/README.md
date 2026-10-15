Отчет по лабораторной работе №3 — Тексты и частоты слов

Задание A — Библиотечный модуль src/lib/text.py

Реализован переиспользуемый модуль src/lib/text.py, содержащий функции для нормализации текста, токенизации, подсчета частоты слов и формирования топа слов.

Функция normalize
Преобразует строку: приведение к нижнему регистру (casefold), замена ё/Ё на е/Е и удаление управляющих символов и лишних пробелов.


<img width="812" height="584" alt="img01" src="https://github.com/user-attachments/assets/207ba202-fd53-498b-a56a-4c85b4ac30e6" />


<img width="790" height="143" alt="img02" src="https://github.com/user-attachments/assets/35da79a7-8cce-4979-b6c4-dfe7619c2fd0" />


Рис. 1. Результат работы и тестов функции normalize

Функция tokenize
Разбивает текст на слова (буквы, цифры, знак подчеркивания) по разделителям, сохраняя дефисы внутри слов.


<img width="446" height="60" alt="img03" src="https://github.com/user-attachments/assets/3e62ea5b-7a61-415d-99e0-17b626dde304" />


<img width="639" height="180" alt="img04" src="https://github.com/user-attachments/assets/0534665e-920e-497d-9a64-1a9e393081ac" />


Рис. 2. Результат работы и тестов функции tokenize


Функции count_freq и top_n
count_freq подсчитывает частоту встречаемости токенов. top_n возвращает первые N частых слов с алфавитной сортировкой при равенстве частот.


<img width="957" height="563" alt="img05" src="https://github.com/user-attachments/assets/86c5ea09-bd50-4a89-9823-ae4c6c188d96" />


<img width="739" height="159" alt="img06" src="https://github.com/user-attachments/assets/bbd208c1-7f34-4997-93bb-ef510df049c8" />


Рис. 3. Результат работы и тестов функций count_freq и top_n


Задание B — Скрипт статистики src/lab03/text_stats.py

Скрипт читает вход из stdin, вызывает функции из src/lib/text.py и печатает базовую статистику текста.

Исходный код src/lab03/text_stats.py


```import sys

from lib.text import normalize, tokenize, count_freq, top_n

TABLE_MODE = True


def table(top: list[tuple[str, int]]) -> None:
    '''Печатает топ слов в виде выровненной таблицы

    Args:
        top: Список пар (слово, количество повторений), 
            например результат функции top_n

    Returns:
        None: Функция ничего не возвращает, только печатает таблицу.
            Ширина первого столбца равна длине самого длинного слова,
            но не меньше длины заголовка "слово".
    '''
    width = len("слово")
    for word, count in top:
        width = max(width, len(word))
    print("слово".ljust(width) + " | частота")
    print("-" * (width + 3 + len("частота")))
    for word, count in top:
        print(word.ljust(width) + " | " + str(count))


def main() -> None:
    '''Читает текст из stdin и печатает статистику по словам

    Весь ввод читается до EOF. Текст нормализуется, разбивается на слова,
    после чего печатаются общее число слов, число уникальных слов и топ-5.
    Формат топа зависит от константы TABLE_MODE: таблица (True)
    или строки вида "слово:кол-во" (False).

    Returns:
        None: Функция ничего не возвращает, только печатает результат.
    '''
    text = sys.stdin.read()
    new = normalize(text)
    words = tokenize(new)
    counter = count_freq(words)
    top = top_n(counter, 5)

    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(counter)}")
    print("Топ-5:")

    if TABLE_MODE:
        table(top)
    else:
        for word, count in top:
            print(f"{word}:{count}")


if __name__ == "__main__":
    main()
```

Примеры работы: Обычный режим вывода


<img width="758" height="111" alt="img07" src="https://github.com/user-attachments/assets/0016d020-5426-4df2-b128-130053b38745" />


Табличный режим вывода:


<img width="817" height="182" alt="img08" src="https://github.com/user-attachments/assets/1adc8def-f163-4c8a-8b95-ee112b27e4f4" />






























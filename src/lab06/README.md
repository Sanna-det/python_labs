Oтчет по лабораторной работе №6


Задание A — текстовые CLI-утилиты


Модуль cli_text.py содержит подкоманды cat и stats.


Подкоманда cat


Подкоманда выводит содержимое текстового файла построчно.

```
python -m src.lab06.cli_text cat --input data\lab04\input.txt
```


Для нумерации строк используется флаг -n:


```
python -m src.lab06.cli_text cat --input data\lab04\input.txt -n
```


Параметры:


--input — обязательный путь к входному файлу;


-n — необязательный флаг нумерации строк.



<img width="729" height="179" alt="img01" src="https://github.com/user-attachments/assets/9b9222ea-0371-4707-9964-b84432c356a2" />


Рис. 1. Работа подкоманды cat с флагом -n.



Подкоманда stats


Подкоманда подсчитывает частоты слов в текстовом файле. Для обработки используются функции из src/lib/text.py:


 1.normalize() — нормализация текста;

 
 2.tokenize() — выделение слов;

 
 3.count_freq() — подсчёт частот;

 
 4.top_n() — сортировка и выбор наиболее частых слов.


 
 Запуск с количеством слов по умолчанию:

```
python -m src.lab06.cli_text stats --input data\lab04\input.txt
```

Запуск с собственным размером топа:


```
python -m src.lab06.cli_text stats --input data\lab04\input.txt --top 5
```


Параметры:


--input — обязательный путь к текстовому файлу;


--top — количество слов в результате, по умолчанию 5.




<img width="796" height="225" alt="img02" src="https://github.com/user-attachments/assets/53222762-5893-49c7-bdf8-febf5c1b6ed3" />




Рис. 2. Работа подкоманды stats.



Задание B — CLI-конвертеры


Модуль cli_convert.py предоставляет три подкоманды. Внутри используются функции из лабораторной работы №5:



json_to_csv() из src.lab05.json_csv;


csv_to_json() из src.lab05.json_csv;


csv_to_xlsx() из src.lab05.csv_xlsx.



Для всех конвертеров обязательны параметры:

--in — путь к входному файлу;


--out — путь к выходному файлу.


Подкоманда json2csv


Преобразует JSON со списком словарей в CSV:


```
python -m src.lab06.cli_convert json2csv `
  --in data\lab05\samples\people.json `
  --out data\lab05\out\people_from_json.csv
```



<img width="824" height="183" alt="img03" src="https://github.com/user-attachments/assets/2525af71-61a8-45a7-9a4e-05320701e24d" />



Рис. 3. Справка по подкоманде json2csv.




<img width="429" height="157" alt="img04" src="https://github.com/user-attachments/assets/c3925f2a-1114-4655-be8c-8618ce0d1aa6" />



Рис. 4. Результат запуска json2csv.




Подкоманда csv2json


Преобразует CSV с заголовком в JSON-список словарей:


```
python -m src.lab06.cli_convert csv2json `
  --in data\lab05\samples\people.csv `
  --out data\lab05\out\people_from_csv.json
```



<img width="348" height="650" alt="img05" src="https://github.com/user-attachments/assets/8ec7d41f-f5b7-4381-a933-8861a606845b" />



Рис. 5. Результат запуска csv2json.



Подкоманда csv2xlsx


Преобразует CSV в таблицу XLSX:


```
python -m src.lab06.cli_convert csv2xlsx `
  --in data\lab05\samples\people.csv `
  --out data\lab05\out\people.xlsx
```



<img width="281" height="185" alt="img06" src="https://github.com/user-attachments/assets/6d0a5879-5a55-4cc9-bb29-84962180da2c" />




Рис. 6. Результат запуска csv2xlsx.

Справка --help


Справка всего CLI:



```
python -m src.lab06.cli_text --help
python -m src.lab06.cli_convert --help
```




Справка отдельных подкоманд:



```
python -m src.lab06.cli_text cat --help
python -m src.lab06.cli_text stats --help
python -m src.lab06.cli_convert json2csv --help
python -m src.lab06.cli_convert csv2json --help
python -m src.lab06.cli_convert csv2xlsx --help
```




<img width="626" height="297" alt="img07" src="https://github.com/user-attachments/assets/a4348507-5717-470b-8509-971995e14c7a" />




Рис. 7. Справка текстовых подкоманд




<img width="824" height="325" alt="img08" src="https://github.com/user-attachments/assets/df17e0fe-d782-49ed-9fe7-14dbb1f3a891" />




Рис. 8. Справка конвертеров.





Oбработка ошибок


При отсутствии входного файла программы вызывают FileNotFoundError с понятным сообщением о пути к файлу.



Ошибки формата входных файлов и пустых файлов обрабатываются функциями из лабораторных работ №4 и №5. Ошибки обязательных аргументов и неизвестных параметров обрабатываются самим argparse, который выводит сообщение об ошибке и справку по использованию команды.




Проверка работы


Для проверки были выполнены следующие сценарии:


 1.cat --input data\lab04\input.txt -n — вывод файла с номерами строк;

 
 2.stats --input data\lab04\input.txt --top 5 — вывод пяти наиболее частых слов;

 
 3.json2csv — конвертация JSON в CSV;

 
 4.csv2json — конвертация CSV в JSON;

 
 5.csv2xlsx — конвертация CSV в XLSX;

 
 6.--help для общего CLI и каждой подкоманды.


 
Результаты конвертаций сохраняются в data\lab05\out\, а скриншоты запусков находятся в images\lab06\.

Зависимости


Сам CLI использует стандартный модуль argparse, а также pathlib и функции из предыдущих лабораторных работ. Для команды csv2xlsx транзитивно требуется openpyxl, потому что она вызывает реализацию CSV → XLSX из ЛР5.


Установка зависимостей из корня репозитория:


```
python -m pip install -r requirements.txt
```

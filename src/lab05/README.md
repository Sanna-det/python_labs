Отчет по лабораторной работе №5 — JSON, CSV и XLSX

Структура лабораторной работы
  src/lab05/json_csv.py — преобразование JSON в CSV и CSV в JSON;
  src/lab05/csv_xlsx.py — преобразование CSV в XLSX.
Входные примеры находятся в каталоге data/lab05/samples/, а результаты конвертаций — в каталоге data/lab05/out/.

  Задание A — JSON ↔ CSV
Модуль json_csv.py содержит две функции.

Функция json_to_csv

```
def json_to_csv(json_path: str, csv_path: str) -> None:
    jp = Path(json_path)
    cp = Path(csv_path)

    if not jp.exists():
        raise FileNotFoundError("Указанный JSON файл не найден")

    if jp.suffix.lower() != '.json':
        raise ValueError("Указанный файл не формата JSON")

    with jp.open('r', encoding='utf-8') as p:
        try:
            data = json.load(p)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError('Файл JSON пустой или имеет неправильный формат')
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы списка JSON должны быть словарями")

    ensure_parent_dir(cp)
    fieldnames = {}
    for element in data:
        for key in element.keys():
            fieldnames[key] = None
```
    with cp.open('w', newline="", encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames.keys()))
        w.writeheader()
        w.writerows(data)

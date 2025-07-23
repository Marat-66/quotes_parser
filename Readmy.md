Quotes Parser
Цель проекта
Создание парсера цитат на основе открытого сайта https://quotes.toscrape.com. Цель — получить цитаты, авторов и теги, а также реализовать поиск по авторам и тегам с возможностью экспорта результатов.

Постановка задачи
Спарсить первую страницу цитат с сайта, сохранить их в структуре:
text (text of quote)
author (name)
tags (list)

После этого реализовать:
поиск цитат по автору
поиск цитат по тегу
поиск цитат по нескольким тегам
сохранение в JSON
сохранение в Excel

Структура проекта
quotes_project/
quotes_parser.py
quotes.json
quotes.xlsx
README.md
Зависимости
pip install requests beautifulsoup4 pandas openpyxl
Запуск
python quotes_parser.py

Пример выходных данных
Цитаты Айнштейна:
- "The world as we have created it..." (Albert Einstein)

Цитаты с тегом 'life':
- "Life isn’t about getting and having..." (Kevin Kruse)

Цитаты с тегами 'life' и 'inspirational':
- "Good friends, good books..." (Mark Twain)

quotes.json
quotes.xlsx

Автор: Марат Шайхлисламов



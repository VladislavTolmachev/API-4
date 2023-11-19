# Обрезка ссылок с помощью Битли

Данный проект создан для создания Битлинков из стандартных ссылок, а также получения количества кликов по ним.

## Как установить
Скачайте необходиные файлы, затем используйте `рір` (или `рір3`, если есть конфликт с Python2) для установки зависимостей и установить зависимости. Зависимости можно установить командой, представленно
Установите зависимости командой:
```pip install -r requirements.txt```

## Пример запуска скрипта
Для запуска скрипта у вас уже должен быть установлен Python3.
Для получения сокращенной ссылки, необходимо написать команду в таком формате:

```python
python main.py --ur1 https://translate.google.ru/
```
После аргумента " --ur] необходимо указать ссылку для работы кода, документацию можно найти на сайте [Сократить ссылку_Bitlx](https://gist.github.com/dvmn-tasks/58f5fdf7b8eb61ea4ed1b528b74d1ab5)
Для получения количества кликов, необходимо написать команду в таком формате:

```python
python main.py --ur1 bit.Ly/3uujaSR
```

## Переменные окружения
Часть настроек проекта берётся из переменных окружения
Переменные окружения - это переменные, значения которых присваиваются программе Python извне.
Чтобы их определить, создайте файл env рядом с main.ру и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.
Пример содержания файла .env:
```python
BITLY_TOKEN=21ecde8d68b8de54395928e7e4199dd7e27f9e78
```
Получить токен BITLINK можно на сайте [Bitly](https://bitly.com/)


## Цель проекта
Код написан в образовательных целях.

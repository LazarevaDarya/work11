#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date


def get_worker():
    surname = input("Фамилия: ")
    name = input("Имя: ")
    number = int(input("Номер телефона: "))
    date_obj = input("Дата рождения: ").split('.')
    return {
        'surname': surname,
        'name': name,
        'number': number,
        'date_obj': date_obj,
            }


def main():
    workers = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            worker = get_worker()

            workers.append(worker)

            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            for num, elem in enumerate(workers):
                print(f"{num+1}.\n{str(elem['surname'])} {str(elem['name'])}\n"
                      f"Номер телефона: {str(elem['number'])}\nДата рождения: {elem['date_obj']}")

        elif command.startswith('select'):
            surname = input("Введите фамилию: ")
            for elem in workers:
                if elem['surname'] == surname:
                    print(f"Имя: {str(elem['name'])}\nНомер телефона: {str(elem['number'])}\n"
                          f"Дата рождения: {elem['date_obj']}")
                    return
                else:
                    print("Фамилии не найдено")

                    if command == 'exit':
                        break

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список всех людей;")
            print("select - найти данные по фамилии;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()

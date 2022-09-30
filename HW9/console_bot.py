# Отвечать на вопросы
# окончание игрового цикла
# Хранение данных вопросов и ответов
# Перевести все это на функции
# хранение данных в массивах
# создать массив в массиве для хранения репилек
# обучение бота. Запоминание новвых ответов

import time
import random


replys = ["привет", "как тебя зовут?", "как дела?", "пока"]
answers = [["Здраствуйте", 'Привет', 'Hello', 'Доброго дня, ми з України',
            'Прювет'], ["Робот"], ["Неплохо!"], ["До свидания!"]]


def learn(an):  # обучаем новым фразам
    global replys
    global answers
    replys.append(an)
    print('Придумайте ответ: ', end=' ')
    r = input()
    answers.append([r])
    print("Запомнил!")


def password(x):
    if x == '123':
        return True


def reply(answer):
    game = True
    if answer in replys:
        index = replys.index(answer)
        print(random.choice(answers[index]))
        if answer == 'пока':
            game = False
    else:
        print('Не понимаю')
        if password(input("Введите пароль: ")):
            learn(answer)
        else:
            print('Невозможно обучить')

    time.sleep(0.5)
    return game


def main():
    gameloop = True
    while gameloop:
        print('Вы: \n(для выхода напишите "пока")')
        rep = input().lower()
        gameloop = reply(rep)


if __name__ == '__main__':
    main()

import time
import random

item = {"привет": "Здраствуйте",
        "как тебя зовут?": "Робот",
        "как дела?": "Неплохо!",
        "пока": "До свидания!"
        }

replys = ["привет", "как тебя зовут?", "как дела?", "пока"]
answers = [["Здраствуйте", 'Привет', 'Hello', 'Доброго дня, ми з України',
            'Прювет'], ["Робот"], ["Неплохо!"], ["До свидания!"]]


# def learn(an):  # обучаем новым фразам
#     global replys
#     global answers
#     replys.append(an)
#     print('Придумайте ответ: ', end=' ')
#     r = input()
#     answers.append([r])
#     print("Запомнил!")


# def password(x):
#     if x == '123':
#         return True


def reply(answer):
    game = True
    if answer in item:
        index = item.index(answer)
        print(index)
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

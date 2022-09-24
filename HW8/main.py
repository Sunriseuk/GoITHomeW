from datetime import datetime
from const import *


def get_birthdays_per_week(users):
    week = {
        '1': 'Monday',
        '2': 'Tuesday',
        '3': 'Wednesday',
        '4': 'Thursday',
        '5': 'Friday',
        '6': 'Monday',
        '7': 'Monday',
    }

    week_days = {'Monday': '',
                 'Tuesday': '',
                 'Wednesday': '',
                 'Thursday': '',
                 'Friday': '',
                 }

    today = str(datetime.datetime.isoweekday(datetime.datetime.now()))
    first = dct_fist[today].date()
    last = dct_last[today].date()

    for i in users:
        for key, value in i.items():
            if int(str(value).split('-')[0]) < current_year:
                value = datetime.date(
                    year=current_year, month=value.month, day=value.day)
                if int(str(value).split('-')[1]) in (first.month, last.month):
                    if first <= value <= last:
                        week_days[week[str(
                            datetime.date.isoweekday(value))]] += key + ', '

    for key, value in week_days.items():
        if value != '':
            value = value[:-2]
            week_days[key] = value
            print(key + ':', value)


get_birthdays_per_week(
    [{'Misha': datetime.date(2000, 8, 20)}, {'Artem': datetime.date(2000, 8, 20)}, {'Dima': datetime.date(2000, 9, 2)},
     {'Grisha': datetime.date(2001, 8, 26)}])


users = [{"name": "Tanya", "birthday": datetime(year=1992, month=9, day=23)},
         {"name": "Kostya", "birthday": datetime(year=1992, month=3, day=8)},
         {"name": "Serhiy", "birthday": datetime(year=1992, month=3, day=8)},
         {"name": "Sasha", "birthday": datetime(year=1994, month=11, day=3)},
         {"name": "Nastya", "birthday": datetime(year=1989, month=9, day=24)},
         {"name": "Vasya", "birthday": datetime(year=1986, month=9, day=24)},
         {"name": "Pasha", "birthday": datetime(year=1986, month=9, day=25)},
         {"name": "Olia", "birthday": datetime(year=1995, month=9, day=24)}]


days_week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday",
             5: "Saturday", 6: "Sunday"}

users = [{"name": "Tanya", "birthday": datetime(year=1992, month=9, day=23)},
         {"name": "Kostya", "birthday": datetime(year=1992, month=3, day=8)},
         {"name": "Serhiy", "birthday": datetime(year=1992, month=3, day=8)},
         {"name": "Sasha", "birthday": datetime(year=1994, month=11, day=3)},
         {"name": "Nastya", "birthday": datetime(year=1989, month=9, day=24)},
         {"name": "Vasya", "birthday": datetime(year=1986, month=9, day=24)},
         {"name": "Pasha", "birthday": datetime(year=1986, month=9, day=25)},
         {"name": "Olia", "birthday": datetime(year=1995, month=9, day=24)}]


def get_birthdays_per_week(some_list):
    current_date = datetime.now()
    birthday_name = []
    birthday_people = ""
    users_str = ""
    day_of_week = ""

    for user in some_list:
        current_date = datetime.now()
        user_date = user.get("birthday")
        if user_date.month == current_date.month:
            if user_date.day == current_date.day:
                birthday_name.append(user.get('name'))
                users_str = ", ".join(birthday_name)
                print(users_str)
            if not current_date.weekday():
                day_of_week = days_week.get(0)
            if current_date.weekday():
                day_of_week = days_week.get(current_date.weekday())
            birthday_people = f"{day_of_week}: {users_str} "
            # if current_date.weekday() == 5 or 6 and user_date.weekday() == 5 or 6
            print(birthday_people)


if __name__ == "__main__":
    get_birthdays_per_week(users)

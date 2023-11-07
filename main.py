from datetime import date, datetime, timedelta 


def get_birthdays_per_week(users):
    if not users: 
        return {} 
    now = date.today() 
    current_week_day = now.weekday() 
    weekdays = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
    }
    birthdays_per_week = {day: [] for day in weekdays.values()} 
    for user in users: 
        name = user['name'] 
        birthday = user['birthday'] 
        new_birthday = birthday.replace(year=now.year) 
        if new_birthday < now: 
            new_birthday = new_birthday.replace(year=now.year + 1) 
        if now <= new_birthday <= now + timedelta(days=7):
            day_week = new_birthday.weekday() 
            day_name = weekdays[day_week]
            
            if day_name in ['Saturday', 'Sunday']: 
                day_name = 'Monday' 
            birthdays_per_week[day_name].append(name) 
    print(birthdays_per_week) 
    return {key: value for key, value in birthdays_per_week.items() if value}
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

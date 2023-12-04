price_list = {
    "bike": {
        "first_hour": 30,
        "hour": 20,
        "day": 100,
        "24hours": 120,
    },
    "trailer": {
        "first_hour": 30,
        "hour": 20,
        "day": 100,
        "24hours": 120,
    },
    "double_trailer": {
        "hour": 30,
        "day": 120,
        "24hours": 140,
    },
    "seat": {
        "first_hour": 15,
        "hour": 10,
        "day": 50,
        "24hours": 70,
    },
    "gokart": {
        "half_hour": 30,
        "hour": 50,
    },
    "double_gokart": {
        "half_hour": 50,
        "hour": 70,
    },
    "grant-tour": {
        "half_hour": 70,
        "hour": 100,
    },
}

commands = ["rent", "return","report"]
rent_list = {}
profit = 0


def report():
    """shows every rent_list entry"""
    for rental in rent_list:
        print(rental)


def rent():
    """Adds an entry to rent_list"""
    name = input("What's your name?")
    print("What do you want to rent?")
    for equipment in price_list:
        print(equipment)
    chosen_equipment = input("Choose equipment. separate with space: ").split(" ")
    rent_time_and_date = input("What's the time? 00:00,00.00 : ").split(",")
    time = rent_time_and_date[0].split(":")
    date = rent_time_and_date[1].split(".")

    hour = int(time[0])
    minute = int(time[1])

    day = int(date[0])
    month = int(date[1])

    rent_list[f"rental_{name}"] = {
        "equipment": chosen_equipment,
        "time": {
            "hour": hour,
            "minute": minute,
        },
        "date": {
            "day": day,
            "month": month,
        }
    }


def calculate_rent_time(return_time_and_date, name):
    rent_hour = rent_list[f"rental{name}"]["time"]["hour"]
    rent_minute = rent_list[f"rental{name}"]["time"]["minute"]

    rent_day = rent_list[f"rental{name}"]["date"]["day"]
    rent_month = rent_list[f"rental{name}"]["date"]["month"]

    return_time = return_time_and_date[0].split(":")
    return_date = return_time_and_date[1].split(".")

    return_hour = int(return_time[0])
    return_minute = int(return_time[1])

    return_day = int(return_date[0])
    return_month = int(return_date[1])

    if rent_month != return_month:
        days = 31 - rent_day + return_day
    else:
        days = return_day - rent_day

    hours = return_hour - rent_hour
    minutes = return_minute - rent_minute

    print(hours,days,minutes)


def return_rent():
    """removes an entry from rent_list, and adds funds to profit variable"""
    name = input("What's your name?")
    equipment = rent_list[f"rental_{name}"]["equipment"]

    return_time_and_date = input("What's the time? 00:00,00.00 : ").split(",")

    calculate_rent_time(return_time_and_date, name)


while True:
    command = input(f"What would you like to do? {commands}")
    if command == "rent":
        rent()
    elif command == "return":
        return_rent()
    elif command == "report":
        report()

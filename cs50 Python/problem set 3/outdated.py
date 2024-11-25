months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        user_date = input("Date: ")
        user_date = user_date.strip()

        if "/" in user_date:
            date_list = user_date.split("/")
            if int(date_list[0]) <= 12 and int(date_list[1]) <= 31:
                print(f"{date_list[2]}-{int(date_list[0]):02}-{int(date_list[1]):02}")
                break
        elif "," in user_date:
            # Split user input into list: ["Month Day", "Year"]
            month_day_year_split = user_date.split(",")

            # Further split the above so you have list of ["Month", "Day"]
            month_day_split = month_day_year_split[0].split()

            # Format Month to start with capital so it matches months list, format day into int & year so it does not have whitespace
            month = month_day_split[0].title()
            day = int(month_day_split[1])
            year = month_day_year_split[1].strip()
            if day <= 31:
                if month in months:
                    month_num = months.index(month) + 1
                    print(f"{year}-{int(month_num):02}-{day:02}")
                    break
    except (SyntaxError, ValueError):
        pass

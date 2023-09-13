"""
    Import date and datetime classes from datetime module.
    Import isleap method from calendar module.
"""
from datetime import date, datetime
from calendar import isleap

try:
    def calc_my_age(user_birthdate):
        """
            Returns the age of the user
            in years, months, weeks, and days.    
        """
        year_months = {0:31, 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, \
            7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        today = date.today()
        user_birthdate = datetime.strptime(user_birthdate, "%d-%m-%Y")

        years = today.year - user_birthdate.year
        months = today.month - user_birthdate.month
        weeks = 0
        days = today.day - user_birthdate.day

        if months < 0:
            years -= 1
            months += 12

        if days < 0:
            months -=1
            days += year_months[user_birthdate.month]

            if (isleap(today.year) and today.month >= 2 and today.day >= 29):
                days += 1
            if (isleap(user_birthdate.year) and user_birthdate.month <= 2 and user_birthdate <= 29):
                days += 1

        if days > 6:
            weeks = days//7
            days = days%7

        user_age = 'You have {}{}{}{}'.format(str(years) + " year(s)" if years > 0 else "\b", \
            ", " + str(months) + " month(s)" if months > 0 else "\b\b", \
            ", " + str(weeks) + " week(s)" if weeks > 0 else "\b\b", \
            ", " + str(days) + " day(s)" if days > 0 else "\b\b")

        return user_age

    birthdate = input('Enter your bithdate as "d-m-Y: ')

    print(calc_my_age(birthdate))
except ValueError:
    print('You should enter your birthdate in dd-mm-yyyy format.')

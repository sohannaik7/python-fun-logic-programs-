from datetime import datetime
def checkdate(date):
    monthNames = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    month, day, year = date.split('/')
    if int(year) % 4 == 0  or int(year) % 400 == 0:
        print("This ",year, "is a leap year")
    else:
        print("This ",year, "isn't a leap year")
    return monthNames[eval(month)-1] + "," + day + ', ' + year

def totaldays(date,date_format,dob):
    a = datetime.strptime(date, date_format)
    b = datetime.strptime(dob, date_format)
    return a - b

if __name__ == '__main__':
    date = input("enter the date..m/d/y")
    dob = input("enter your birth date....m/d/y")
    print("todys date is ", checkdate(date))
    print("..............")
    print("your birth date is ", checkdate(dob))

    date_format = "%m/%d/%Y"
    tot = totaldays(date,date_format,dob)
    print("total number of days from ",dob," to ",date," is ",tot.days)
        
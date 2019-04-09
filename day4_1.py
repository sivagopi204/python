from datetime import datetime
from dateutil.relativedelta import relativedelta

def program2():
	year =input("Enter year:::::::")
	month =input("Enter Month::::::::::")
	day =input("Enter Day::::::::")
	if 0< int(day)<=31 and 0 < int(month)<=12:
		date_string = str(year)+'-'+str(month)+'-'+str(day)

		date_object = datetime.strptime(datetime(year, month, 1).strftime("%Y-%m-%d"), "%Y-%m-%d")
		delta = date_object + relativedelta(months=1)
		delta1 = delta - relativedelta(days=1)
		date_object2 = datetime(year, 12, 1).strftime("%Y-%m-%d")
		if 0 < month <= datetime.strptime(date_object2, "%Y-%m-%d").month:
			if 0 < day <= delta1.day:
				date_object1 = datetime.strptime(date_string, "%Y-%m-%d").strftime("%A")
				print("{} is {}".format(date_string, date_object1))

				if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
					print("{} year is a leap year".format(year))
				else:
					print("{} year is not a leap year".format(year))
			else:
				print("Invalid Day")
		else:
			print("Invalid Month")
	else:
		print("date and month invalid")


    

if __name__ == '__main__':
    program2()

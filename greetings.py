import math
import datetime
print("Hello World")
name = input("Type ur name")
print("Hello , " + name)
print("Your name has" + str(len(name)) + "letters.")
print(str(len(name)) + "!" + " =" + str(math.factorial(len(name))))
birth_date = input("Please, enter your birth date in format (DD.MM.YYYY)")
now = datetime.datetime.today()
then = datetime.datetime.strptime(birth_date, "%d.%m.%Y")
delta = now - then
delta_years = delta.days // 365
print(f"Today is {now}  you`re {delta_years}  {delta.days} year old")
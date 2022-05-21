from datetime import date, datetime, time


d = date(2022, 5, 18)
t = time(17, 44)
reminder = datetime.combine(d, t)
a = datetime.now()


liste = [a, reminder]

liste.sort(reverse=True)

print(liste)


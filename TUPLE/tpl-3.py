from datetime import date
date1 = (10, 4, 2024)
date2 = (20, 4, 2025)
d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

difference = abs((d2 - d1).days)

print("Number of days between the two dates:", difference)

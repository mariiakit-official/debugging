# incident_report.py - T7A starter
# Calculates downtime totals for warehouse incidents (Operations Problem Navigator).
# Heads up: this code is repetitive AND has bugs. That's on purpose.

north_dc = [45, 30, 120, 15]   # downtime minutes per incident
south_dc = [60, 10, 25]
east_dc = [35, 20, 15]
west_dc = [40, 30, 45]

total = 0
for m in north_dc:
    total = total + m
print("North DC total downtime:", total)

total = 0
for m in south_dc:
    total = total + m
print("South DC total downtime:", total)

total = 0
for m in west_dc:
    total = total + m
print("West DC total downtime:", total)


total = 0
for m in east_dc:
    total = total + m
print("East DC total downtime:", total)

print("Most recent North DC incident:", north_dc[3])

new_minutes = int(input("Log a new North DC incident (minutes): "))
north_dc.append(new_minutes)
print("New North DC total:", sum(north_dc))
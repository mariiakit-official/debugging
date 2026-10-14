# incident_report.py - T7A starter
# Calculates downtime totals for warehouse incidents (Operations Problem Navigator).
# Heads up: this code is repetitive AND has bugs. That's on purpose.
 
north_dc = [45, 30, 120, 15]   # downtime minutes per incident
west_dc = [90, 20, 45]          # downtime minutes per incident
south_dc = [56, 30, 25]
east_dc = [67, 21, 17]
 
total = 0
for m in north_dc:
    total = total + m
print("North DC total downtime:", total)
 
total = 0
for m in west_dc:
    total = total + m
print("West DC total downtime:", total)
 
total = 0
for m in south_dc:
    total = total + m
print("South DC total downtime:", total)
 
total = 0
for m in east_dc:
    total = total + m
print("East DC total downtime:", total)

def calculate_total(numbers):
    total=0;
    for number in numbers:
      total +=number;
    return total;


print("North DC total downtime:", calculate_total(north_dc))
print("South DC total downtime:", calculate_total(south_dc))
print("East DC total downtime:", calculate_total(east_dc))
print("West DC total downtime:", calculate_total(west_dc))
 
#print("Most recent North DC incident:", north_dc[4])

 
#new_minutes = int(input("Log a new North DC incident (minutes): "))
#north_dc.append(new_minutes)
#print("New North DC total:", sum(north_dc))
# incident_report.py - T7A starter
# Calculates downtime totals for warehouse incidents (Operations Problem Navigator).
# Heads up: this code is repetitive AND has bugs. That's on purpose.
 
north_dc = [45, 30, 120, 15]   # downtime minutes per incident
west_dc = [90, 20, 45]          # downtime minutes per incident
south_dc = [56, 30, 25]
east_dc = [67, 21, 17]
 


def calculate_total(numbers):
    total=0;
    for number in numbers:
      total +=number;
    return total;


print("North DC total downtime:", calculate_total(north_dc))
print("South DC total downtime:", calculate_total(south_dc))
print("East DC total downtime:", calculate_total(east_dc))
print("West DC total downtime:", calculate_total(west_dc))
 
print(len(north_dc)) 
# index start from 0, not 1, althou the length is 4(function return the count of elements and start from 1)
# index len()-1, it will give us the last element in the list
print("Most recent North DC incident:", north_dc[len(north_dc)-1])
print("Most recent South DC incident:", south_dc[len(south_dc)-1])
print("Most recent East DC incident:", east_dc[len(east_dc)-1])
print("Most recent West DC incident:", west_dc[len(west_dc)-1])

# branch_name= 'North_DC'
# raw = input(f"Log a new {branch_name} incident(minutes): ")
# while not raw.isdigit():
#    print("Please enter a whole number, like 30.")
#    raw = input(f"Log a new {branch_name} incident (minutes): ")
# new_minutes=int(raw)
# north_dc.append(new_minutes)

# print(f"New {branch_name} total:",calculate_total(north_dc))

branches = {
"North_DC":north_dc,
"South_DC":south_dc,
"West_DC":west_dc,
"East_DC":east_dc    
}
branch_name = "North_DC"
while True:
    try:
        new_minutes = int(input(f"Log a new {branch_name} incident (minutes): "))
        if new_minutes<0:
           #keep asking until the user enters a non-nagative integer 
            print("Minutes cannot be nagative.")
            continue # loop will continue until user will type a positive number
        #add validated minutes to the selected branch
        branches[branch_name].append(new_minutes) 
        break # exit loop after successfull input
    except ValueError: # handle exception (invalid input)
        print("Please enter a whole number, like 30")
print(f"New {branch_name} total: {calculate_total(branches[branch_name])}")         
from facade.vacations_facade import *

vacation_facade = VacationsFacade()

#1) get vacations 👍
vacation = vacation_facade.get_vacations_sorted_by_date_desc()  #returns a list
for item in vacation:
    print(item)

print()
print()

#2) add new vacation 👍
new_vacation = vacation_facade.add_new_vacation(3, "explore NYC", "2025-01-03", "2025-01-07", 2400, "nyc.png")
print(new_vacation)

#exceptions1 empty fields:
new_vacation1 = vacation_facade.add_new_vacation(3, "", "2025-01-03", "2025-01-07", 2400, "")
print(new_vacation1)  #Fields cannot be empty. Please try again.

#exception2 invalid countryID:
new_vacation2 = vacation_facade.add_new_vacation("string countryID", "explore NYC", "2025-01-03", "2025-01-07", 2400, "nyc.png")
print(new_vacation2)  #CountryID must be an integer.

#exception3 - invalid price
new_vacation3 = vacation_facade.add_new_vacation(3, "explore NYC", "2025-01-03", "2025-01-07", -2400, "nyc.png")
print(new_vacation3)  #Price must be between 0 and 10,000.

#exception4 - invalid dates
new_vacation4 = vacation_facade.add_new_vacation(3, "explore NYC", "2025-01-07", "2025-01-03", 2400, "nyc.png")
print(new_vacation4)  #Start date cannot be greater than end date.
new_vacation5 = vacation_facade.add_new_vacation(3, "explore NYC", "2009-01-03", "2009-01-07", 2400, "nyc.png")
print(new_vacation5)  #Invalid Date: Dates cannot be in the past.
new_vacation6 = vacation_facade.add_new_vacation(3, "explore NYC", "string", "01.02.2024", 2400, "nyc.png")
print(new_vacation6)  #Invalid Date Format. Date must be in YYYY-MM-DD format.

print()
print()

#3) update vacation 👍
update_vacation = vacation_facade.update_vacation(16, 3, "manhattan","2025-01-03", "2025-01-05", 2200, "manhattan.png")
print(update_vacation)

#exceptions1 empty fields:
update_vacation1 = vacation_facade.update_vacation(16, 3, "" ,"2025-01-03", "", 2200, "manhattan.png")
print(update_vacation1)  #All Fields must be filled except for vacation picture. Please try again.

#exception2 invalid countryID or vacationId:
update_vacation2 = vacation_facade.update_vacation(29.22, "str", "manhattan","2025-01-03", "2025-01-05", 2200, "manhattan.png")
print(update_vacation2)  #VacationID and CountryID must be integers.

#exception3 - invalid price
update_vacation3 = vacation_facade.update_vacation(16, 3, "manhattan","2025-01-03", "2025-01-05", 9999999, "manhattan.png")
print(update_vacation3)  #Price must be between 0 and 10,000.

#exception4 - invalid dates
update_vacation4 = vacation_facade.update_vacation(16, 3, "manhattan","2025-01-17", "2025-01-05", 2200, "manhattan.png")
print(update_vacation4) #Start date cannot be greater than end date.

# exception5 - nonexistent vacationID 
update_vacation5 = vacation_facade.update_vacation(87654, 3, "manhattan","2025-01-03", "2025-01-05", 2200, "manhattan.png")
print(update_vacation5)  #No rows updated

print()
print()

#4) delete vacation 👍
delete_vacation = vacation_facade.delete_vacation(25)
print(delete_vacation)

#exception1 - invalid vacationID 
delete_vacation1 = vacation_facade.delete_vacation("string")
print(delete_vacation1) #VacationID must be an integer.

#exception2 - nonexistent vacationID 
delete_vacation2 = vacation_facade.delete_vacation(9876543)
print(delete_vacation2)  #No rows deleted
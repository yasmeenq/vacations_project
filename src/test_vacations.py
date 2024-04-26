from facade.vacations_facade import *

vacation_facade = VacationsFacade()

vacation = vacation_facade.get_vacations_sorted_by_date_desc()  #returns a list
for item in vacation:
    print(item)
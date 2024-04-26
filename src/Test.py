from facade.users_facade import * 
from facade.vacations_facade import *
from facade.likes_facade import *

class Test:
    def __init__(self):
        self.usersFacade = UsersFacade()
        self.vacationsFacade = VacationsFacade()
        self.likesFacade = LikesFacade()

    def test_all(self):
        def users():
            print("【Ｕｓｅｒｓ　Ｔｅｓｔ：】")




        def vacations():
            print("【Ｖａｃａｔｉｏｎｓ　Ｔｅｓｔ：】")
            #1) get vacations 👍
            vacation = self.vacationsFacade.get_vacations_sorted_by_date_desc()  #returns a list
            for item in vacation:
                print(item)

            print()
            print()

            #2) add new vacation 👍
            print("Adding New Vacation:")
            new_vacation = self.vacationsFacade.add_new_vacation ("explore NYC", "2025-01-03", "2025-01-07", 2400, "nyc.png")
            print(new_vacation)
            
            print("\nExceptions:")            
            #exceptions1 empty fields:
            new_vacation1 = self.vacationsFacade.add_new_vacation(3, "", "2025-01-03", "2025-01-07", 2400, "")
            print(new_vacation1)  #Fields cannot be empty. Please try again.

            #exception2 invalid countryID:
            new_vacation2 = self.vacationsFacade.add_new_vacation("string countryID", "explore NYC", "2025-01-03", "2025-01-07", 2400, "nyc.png")
            print(new_vacation2)  #CountryID must be an integer.

            #exception3 - invalid price
            new_vacation3 = self.vacationsFacade.add_new_vacation(3, "explore NYC", "2025-01-03", "2025-01-07", -2400, "nyc.png")
            print(new_vacation3)  #Price must be between 0 and 10,000.

            #exception4 - invalid dates
            new_vacation4 = self.vacationsFacade.add_new_vacation(3, "explore NYC", "2025-01-07", "2025-01-03", 2400, "nyc.png")
            print(new_vacation4)  #Start date cannot be greater than end date.
            new_vacation5 = self.vacationsFacade.add_new_vacation(3, "explore NYC", "2009-01-03", "2009-01-07", 2400, "nyc.png")
            print(new_vacation5)  #Invalid Date: Dates cannot be in the past.
            new_vacation6 = self.vacationsFacade.add_new_vacation(3, "explore NYC", "string", "01.02.2024", 2400, "nyc.png")
            print(new_vacation6)  #Invalid Date Format. Date must be in YYYY-MM-DD format.

            print()
            print()

            #3) update vacation 👍
            print("Updating Vacation:")
            update_vacation = self.vacationsFacade.update_vacation(16, 3, "manhattan","2025-01-03", "2025-01-05", 2200, "manhattan.png")
            print(update_vacation)
            
            print("\nExceptions:")
            #exceptions1 empty fields:
            update_vacation1 = self.vacationsFacade.update_vacation(16, 3, "" ,"2025-01-03", "", 2200, "manhattan.png")
            print(update_vacation1)  #All Fields must be filled except for vacation picture. Please try again.

            #exception2 invalid countryID or vacationId:
            update_vacation2 = self.vacationsFacade.update_vacation(29.22, "str", "manhattan","2025-01-03", "2025-01-05", 2200, "manhattan.png")
            print(update_vacation2)  #VacationID and CountryID must be integers.

            #exception3 - invalid price
            update_vacation3 = self.vacationsFacade.update_vacation(16, 3, "manhattan","2025-01-03", "2025-01-05", 9999999, "manhattan.png")
            print(update_vacation3)  #Price must be between 0 and 10,000.

            #exception4 - invalid dates
            update_vacation4 = self.vacationsFacade.update_vacation(16, 3, "manhattan","2025-01-17", "2025-01-05", 2200, "manhattan.png")
            print(update_vacation4) #Start date cannot be greater than end date.

            # exception5 - nonexistent vacationID 
            update_vacation5 = self.vacationsFacade.update_vacation(87654, 3, "manhattan","2025-01-03", "2025-01-05", 2200, "manhattan.png")
            print(update_vacation5)  #No rows updated

            print()
            print()
            print("Deleting Vacation:")
            #4) delete vacation 👍
            delete_vacation = self.vacationsFacade.delete_vacation(25)
            print(delete_vacation)
            
            print("\nExceptions:")
            #exception1 - invalid vacationID 
            delete_vacation1 = self.vacationsFacade.delete_vacation("string")
            print(delete_vacation1) #VacationID must be an integer.

            #exception2 - nonexistent vacationID 
            delete_vacation2 = self.vacationsFacade.delete_vacation(9876543)
            print(delete_vacation2)  #No rows deleted


        def likes():
            print("【Ｌｉｋｅｓ　Ｔｅｓｔ：】 \n")
            like_vacation = self.likesFacade.like(9,11)
            print(like_vacation)
            print()
            unlike_vacation = self.likesFacade.unlike(9,11)
            print(unlike_vacation)


        print("\n───────*.｡:｡✱✱*.｡:｡✱*.:｡✧*.｡✰*.:｡✧*.｡:｡*.｡✱✱*.｡:｡✱*.:｡✧*.｡✰*.:｡✧*.｡:｡*.｡✱*.｡:｡✱───────\n")
        users()
        print("\n───────*.｡:｡✱✱*.｡:｡✱*.:｡✧*.｡✰*.:｡✧*.｡:｡*.｡✱✱*.｡:｡✱*.:｡✧*.｡✰*.:｡✧*.｡:｡*.｡✱*.｡:｡✱───────\n")
        vacations()
        print("\n───────*.｡:｡✱✱*.｡:｡✱*.:｡✧*.｡✰*.:｡✧*.｡:｡*.｡✱✱*.｡:｡✱*.:｡✧*.｡✰*.:｡✧*.｡:｡*.｡✱*.｡:｡✱───────\n")
        likes()
        print("\n───────*.｡:｡✱✱*.｡:｡✱*.:｡✧*.｡✰*.:｡✧*.｡:｡*.｡✱✱*.｡:｡✱*.:｡✧*.｡✰*.:｡✧*.｡:｡*.｡✱*.｡:｡✱───────\n")

    def close(self):
        self.usersFacade.close()
        self.vacationsFacade.close()
        self.likesFacade.close()

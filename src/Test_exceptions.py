from facade.users_facade import * 
from facade.vacations_facade import *
from facade.likes_facade import *

class TestExceptions:
    def __init__(self):
        self.usersFacade = UsersFacade()
        self.vacationsFacade = VacationsFacade()
        self.likesFacade = LikesFacade()

    def test_all_exceptions(self):
        
        def users(): 
            print("【Ｕｓｅｒｓ　Ｔｅｓｔ：】\n")

            print("【ａｄｄ　ｕｓｅｒ　ｅｘｃｅｐｔｉｏｎｓ】\n")

            try:
                #exception1 - empty fields:
                new_user1 = self.usersFacade.user_registration("", "Patel", "mia@mail.com",7771)
                print(new_user1) #Fields cannot be empty. Please try again.
            except ValueError as err:
                print(f"ValueError: {err}")

            try:
                #exception2 - invalid email format:
                new_user2 = self.usersFacade.user_registration("Mia", "Patel", "mia_email",7771)
                print(new_user2) #Email is not valid. Please try again.
            except ValueError as err:
                print(f"ValueError: {err}")

            try:
                #exception3 - invalid password:
                new_user3 = self.usersFacade.user_registration("Mia", "Patel", "mia1@mail.com",71)
                print(new_user3) #Password must be minimum 4 characters. Please try again.
            except ValueError as err:
                print(f"ValueError: {err}")

            try:
                #exception4- email already exists:
                new_user4 = self.usersFacade.user_registration("Mia", "Patel", "emily@mail.com", 7771)
                print(new_user4) #Email already exists. Please choose another one.
            except ValueError as err:
                print(f"ValueError: {err}")

            try:
                #exception5 - invalid firstName or lastName
                new_user5 = self.usersFacade.user_registration(123, 25.987, "mia1@mail.com", 7771)
                print(new_user5) #First name and last name must be strings
            except ValueError as err:
                print(f"ValueError: {err}")
            try:
                new_user6 = self.usersFacade.user_registration("Mia34", "Patel2009", "mia1@mail.com",7771)
                print(new_user6) #First name and last name must contain only letters.
            except ValueError as err:
                print(f"ValueError: {err}")

            print()
            print()

            print("【ｕｓｅｒ　ｌｏｇｉｎ　ｅｘｃｅｐｔｉｏｎｓ】\n")

            try:
                #exception1 - empty fields:
                user_login1 = self.usersFacade.user_login("",1234)
                print(user_login1) #Email and password cannot be empty.
            except ValueError as e:
                print(f"ValueError: {e}")

            try:
                #exception2 - invalid email format:
                user_login = self.usersFacade.user_login("john_legend_mail",1234)
                print(user_login)  #Email is not valid. Please try again.
            except ValueError as e:
                print(f"ValueError: {e}")

            try:    
                #exception3 - invalid password:
                user_login = self.usersFacade.user_login("john@mail.com",11)
                print(user_login)  #Password must be minimum 4 characters. Please try again.
            except ValueError as e:
                print(f"ValueError: {e}")

            try:
                #exception4 - wrong email:
                user_login = self.usersFacade.user_login("kjhgfdsdfgdfgvx@mail.com",1234)
                print(user_login) # Incorrect Email or Password. Please try again.
            except ValueError as e:
                print(f"ValueError: {e}")

            try:
                #exception5 - wrong password:
                user_login = self.usersFacade.user_login("john@mail.com",76543234)
                print(user_login)  #Incorrect Email or Password. Please try again.
                print()
            except ValueError as e:
                print(f"ValueError: {e}")
        
        def vacations():
            print("【Ｖａｃａｔｉｏｎｓ　Ｔｅｓｔ：】\n")
            
            print("【ａｄｄ　ｎｅｗ　ｖａｃａｔｉｏｎ　ｅｘｃｅｐｔｉｏｎｓ】\n")

            try:      
                #exceptions1 empty fields:
                new_vacation1 = self.vacationsFacade.add_new_vacation(3, "", "2025-01-03", "2025-01-07", 2400, "")
                print(new_vacation1)  #Fields cannot be empty. Please try again.
            except ValueError as e:
                print(f"ValueError: {e}")
            
            try:
                #exception2 invalid countryID:
                new_vacation2 = self.vacationsFacade.add_new_vacation("string countryID", "explore NYC", "2025-01-03", "2025-01-07", 2400, "nyc.png")
                print(new_vacation2)  #CountryID must be an integer.
            except ValueError as e:
                print(f"ValueError: {e}")

            try:
                #exception3 - invalid price
                new_vacation3 = self.vacationsFacade.add_new_vacation(3, "explore NYC", "2025-01-03", "2025-01-07", -2400, "nyc.png")
                print(new_vacation3)  #Price must be between 0 and 10,000.
            except ValueError as e:
                print(f"ValueError: {e}")

            try:
                #exception4 - invalid dates
                new_vacation4 = self.vacationsFacade.add_new_vacation(3, "explore NYC", "2025-01-07", "2025-01-03", 2400, "nyc.png")
                print(new_vacation4)  #Start date cannot be greater than end date.
            except ValueError as e:
                print(f"ValueError: {e}")

            try:
                new_vacation5 = self.vacationsFacade.add_new_vacation(3, "explore NYC", "2009-01-03", "2009-01-07", 2400, "nyc.png")
                print(new_vacation5)  #Invalid Date: Dates cannot be in the past.
            except ValueError as e:
                print(f"ValueError: {e}")

            try:                
                new_vacation6 = self.vacationsFacade.add_new_vacation(3, "explore NYC", "string", "01.02.2024", 2400, "nyc.png")
                print(new_vacation6)  #Invalid Date Format. Date must be in YYYY-MM-DD format.
            except ValueError as e:
                print(f"ValueError: {e}")

            print()
            print()

            print("【ｕｐｄａｔｅ　ｖａｃａｔｉｏｎ　ｅｘｃｅｐｔｉｏｎｓ】\n")

            try:
                #exceptions1 empty fields:
                update_vacation1 = self.vacationsFacade.update_vacation(16, 3, "" ,"2025-01-03", "", 2200, "manhattan.png")
                print(update_vacation1)  #All Fields must be filled except for vacation picture. Please try again.
            except ValueError as e:
                print(f"ValueError: {e}")
            
            try:
                #exception2 invalid countryID or vacationId:
                update_vacation2 = self.vacationsFacade.update_vacation(29.22, "str", "manhattan","2025-01-03", "2025-01-05", 2200, "manhattan.png")
                print(update_vacation2)  #VacationID and CountryID must be integers.
            except ValueError as e:
                print(f"ValueError: {e}")
            
            try:
                #exception3 - invalid price
                update_vacation3 = self.vacationsFacade.update_vacation(16, 3, "manhattan","2025-01-03", "2025-01-05", 9999999, "manhattan.png")
                print(update_vacation3)  #Price must be between 0 and 10,000.
            except ValueError as e:
                print(f"ValueError: {e}")

            try:
                #exception4 - invalid dates
                update_vacation4 = self.vacationsFacade.update_vacation(16, 3, "manhattan","2025-01-17", "2025-01-05", 2200, "manhattan.png")
                print(update_vacation4) #Start date cannot be greater than end date.
            except ValueError as e:
                print(f"ValueError: {e}")

            try:
                # exception5 - nonexistent vacationID 
                update_vacation5 = self.vacationsFacade.update_vacation(87654, 3, "manhattan","2025-01-03", "2025-01-05", 2200, "manhattan.png")
                print(update_vacation5)  #ValueError: Vacation doesn't exist. try again.
            except ValueError as e:
                print(f"ValueError: {e}")
        
            print()
            print()
            
            print("【ｄｅｌｅｔｅ　ｖａｃａｔｉｏｎ　ｅｘｃｅｐｔｉｏｎｓ】\n")

            try:
                #exception1 - invalid vacationID 
                delete_vacation1 = self.vacationsFacade.delete_vacation("string")
                print(delete_vacation1) #VacationID must be an integer.
            except ValueError as e:
                print(f"ValueError: {e}")
            
            try:
                #exception2 - nonexistent vacationID 
                delete_vacation2 = self.vacationsFacade.delete_vacation(9876543)
                print(delete_vacation2)  #ValueError: Vacation doesn't exist. try again.
            except ValueError as e:
                print(f"ValueError: {e}")


        def likes():
            print("【Ｌｉｋｅｓ　ｅｘｃｅｐｔｉｏｎｓ】\n")
            try:
                #exception1 - invalid userID or vacationID
                like_vacation1 = self.likesFacade.like(15,"stam")
                print(like_vacation1)  #userID and vacationID must be integers.
            except ValueError as err:
                print(f"ValueError: {err}")
        
            try:
                #exception2 - userID doesn't exist
                like_vacation2 = self.likesFacade.like(99999,2)
                print(like_vacation2) #User Doesn't Exist. Please try again.
            except ValueError as e:
                print(f"ValueError: {e}")

            try:
                #exception3 - vacationID doesn't exist
                like_vacation3 = self.likesFacade.like(1,99999)
                print(like_vacation3) #Vacation Doesn't Exist. Please try again.
            except ValueError as e:
                print(f"ValueError: {e}")                




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

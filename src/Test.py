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
            
            # 1) add new user: 👍
            try:
                print("\nRegister New User:")
                new_user = self.usersFacade.user_registration("issac", "scott", "isacc@mail.com","pass123")
                print(new_user)
            except ValueError as err:
                print(f"ValueError: {err}")
            except Exception as err: 
                print(f"General Error: {err}")

            print()

            #2) user login: 👍
            try:
                user_login = self.usersFacade.user_login("john@mail.com",1234)
                print(user_login)
            except ValueError as e:
                print(f"ValueError: {e}")
            except Exception as e:
                print(f"General Error: {e}")


        def vacations():
            print("【Ｖａｃａｔｉｏｎｓ　Ｔｅｓｔ：】")

            #1) get vacations 👍
            try:
                vacation = self.vacationsFacade.get_vacations_sorted_by_date_desc() 
            except Exception as err:
                print(f"General Error: {err}")

            print()

            #2) add new vacation 👍
            print("Adding New Vacation:")
            try:
                new_vacation = self.vacationsFacade.add_new_vacation (3,"explore NYC", "2025-07-03", "2025-07-20", 2400, "nyc.png")
                print(new_vacation)
            except ValueError as e:
                print(f"ValueError: {e}")
            except Exception as err:
                print(f"General Error: {err}")
                
            print()

            #3) update vacation 👍
            print("Updating Vacation:")
            try:
                update_vacation = self.vacationsFacade.update_vacation(44, 3, "explore manhattan","2025-01-03", "2025-01-05", 2750, "manhattan.png")
                print(update_vacation)
            except ValueError as e:
                print(f"ValueError: {e}")
            except Exception as err:
                print(f"General Error: {err}")

            print()

            #4) delete vacation 👍
            print("Deleting Vacation:")
            try:
                delete_vacation = self.vacationsFacade.delete_vacation(46)
                print(delete_vacation)
            except ValueError as e:
                print(f"ValueError: {e}")
            except Exception as err:
                print(f"General Error: {err}")


        def likes():
            print("【Ｌｉｋｅｓ　Ｔｅｓｔ：】 \n")
            # add like 👍
            try:
                like_vacation = self.likesFacade.like(6,8)
                print(like_vacation)
                print()
            except ValueError as e:
                print(f"ValueError: {e}")
            except Exception as err:
                print(f"General Error: {err}")

            # delete like 👍
            try:
                unlike_vacation = self.likesFacade.unlike(6,8)
                print(unlike_vacation)
            except ValueError as e:
                print(f"ValueError: {e}")
            except Exception as err:
                print(f"General Error: {err}")                


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

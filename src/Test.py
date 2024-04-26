from facade.users_facade import * 
from facade.vacations_facade import *
from facade.likes_facade import *

class Test:
    def __init__(self):
        self.usersFacade = UsersFacade()
        self.vacationsFacade = VacationsFacade()
        self.likesFacade = LikesFacade()

    def test_all():

        def likes(self):
            like_vacation = self.likesFacade.like(9,11)
            print(like_vacation)

            unlike_vacation = self.likesFacade.unlike(9,11)
            print(unlike_vacation)

        def stem(self):
            print("weeeeeeeeeeeeeeeeeeeew")

        
        return stem

    def close(self):
        self.usersFacade.close()
        self.vacationsFacade.close()
        self.likesFacade.close()

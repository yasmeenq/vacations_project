from utils.dal import *
from logic.likes_logic import *

class LikesFacade:
    def __init__(self) -> None:
        self.logic = LikesLogic()

    def like(self, userID, vacationID):

        if not isinstance(userID,int) or not isinstance(vacationID, int):
            raise ValueError("userID and vacationID must be integers.")

        print("Like a Vacation ❤")
        like_vacation = self.logic.add_like(userID, vacationID)
        return like_vacation

    def unlike(self, userID, vacationID):

        if not isinstance(userID,int) or not isinstance(vacationID, int):
            raise ValueError("userID and vacationID must be integers.")   
             
        print("Unlike a Vacation ❌")
        unlike_vacation = self.logic.delete_like(userID, vacationID)
        return unlike_vacation

    def close(self):
        self.logic.close()

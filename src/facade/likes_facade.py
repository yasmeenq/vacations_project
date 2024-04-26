from utils.dal import *
from logic.likes_logic import *

class LikesFacade:
    def __init__(self) -> None:
        self.logic = LikesLogic()

    def like(self, userID, vacationID):
        print("Like a Vacation ❤")
        like_vacation = self.logic.add_like(userID, vacationID)
        return like_vacation

    def unlike(self, userID, vacationID):
        print("Unlike a Vacation ❌")
        unlike_vacation = self.logic.delete_like(userID, vacationID)
        return unlike_vacation

    def close(self):
        self.logic.close()

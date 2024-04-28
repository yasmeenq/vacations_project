from utils.dal import *
from logic.likes_logic import *

class LikesFacade:
    def __init__(self) -> None:
        self.logic = LikesLogic()
    
    #👍
    def like(self, userID, vacationID):

        #check if userID and vacation ID are integers
        if not isinstance(userID,int) or not isinstance(vacationID, int):
            raise ValueError("userID and vacationID must be integers.")

        #check if userID exists:
        if not self.logic.check_user(userID):
            raise ValueError("User Doesn't Exist. Please try again.")            
       
        #check if vacationID exists:
        if not self.logic.check_vacation(vacationID):
            raise ValueError("Vacation Doesn't Exist. Please try again.")            

        print("Like a Vacation ❤")
        like_vacation = self.logic.add_like(userID, vacationID)
        return like_vacation

    #👍
    def unlike(self, userID, vacationID):

        #check if userID and vacation ID are integers
        if not isinstance(userID,int) or not isinstance(vacationID, int):
            raise ValueError("userID and vacationID must be integers.")   

        #check if userID exists:
        if not self.logic.check_user(userID):
            raise ValueError("User Doesn't Exist. Please try again.")            
       
        #check if vacationID exists:
        if not self.logic.check_vacation(vacationID):
            raise ValueError("Vacation Doesn't Exist. Please try again.")            
                
        print("Unlike a Vacation ❌")
        unlike_vacation = self.logic.delete_like(userID, vacationID)
        return unlike_vacation

    def close(self):
        self.logic.close()

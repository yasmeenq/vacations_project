from utils.dal import *
from logic.likes_logic import *

class LikesFacade:
    def __init__(self, user_facade):
        self.logic = LikesLogic()
        self.user_facade = user_facade
    
    #👍
    def like(self, userID, vacationID):

        # RoleID Validation - only Users can add likes
        user_role = int(self.user_facade.get_current_role())
        if user_role != 2:
            raise ValueError("Only Users can add likes.")

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

        # RoleID Validation - only Users can delete likes
        user_role = int(self.user_facade.get_current_role())
        if user_role != 2:
            raise ValueError("Only Users can delete likes.")

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

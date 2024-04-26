from utils.dal import *

#start dal - add like - delete like - close dal

class LikesLogic:

    def __init__(self):
        self.dal = DAL()
 
    #👍 put foreign_key on CASCADE
    def add_like(self, userID, vacationID):
        sql = """
        INSERT INTO `vacation`.`likes` (`userID`,`vacationID`)
        VALUES (%s, %s);
        """
        params = (userID, vacationID)
        result = self.dal.insert(sql, params)
        
        if result != 0:
            return f"Last row ID: {result}\nuserID {userID} liked vacationID {vacationID}"
        else:
            return f"No likes added."

    #👍 put foreign_key on CASCADE
    def delete_like(self, userID, vacationID):
        sql = """
        DELETE FROM `vacation`.`likes` 
        WHERE `userID` = %s AND `vacationID` = %s;
        """
        params = (userID, vacationID)
        result = self.dal.delete(sql, params)

        if result != 0:
            return f"rows affected: {result} \nuserID {userID} unliked vacationID {vacationID}."  
        else:
            return f"no rows were deleted"  


    def close(self):
        self.dal.close()
        
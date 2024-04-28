from utils.dal import *

class LikesLogic:

    def __init__(self):
        self.dal = DAL()
 
    #👍 user like a vacation
    def add_like(self, userID, vacationID):

        #check if userID exists:
        check_user = "SELECT * FROM vacation.users WHERE userID = %s"
        user_params = (userID, )
        result = self.dal.get_scalar(check_user, user_params)
        if not result:
            return "User Doesn't Exist. Please try again."
        
        #check if vacationID exists:
        check_vacation = "SELECT * FROM vacation.vacations WHERE vacationID = %s"
        user_params = (vacationID, )
        result = self.dal.get_scalar(check_vacation, user_params)
        if not result:
            return "Vacation Doesn't Exist. Please try again."

        #check if like already exists:
        check_sql = """
                SELECT count(*) FROM vacation.likes
                WHERE userID = %s AND vacationID = %s
                """
        params = (userID, vacationID)
        check_result = self.dal.get_table(check_sql, params)

        if check_result[0]['count(*)'] == 0: #if no existing like
            #add like
            sql = """
            INSERT INTO vacation.likes (userID, vacationID)
            VALUES (%s, %s);
            """
            params = (userID, vacationID)
            result = self.dal.insert(sql, params) #this will return last row id -> int
            
            if result != 0:
                return f"Last row ID: {result}\nuserID {userID} liked vacationID {vacationID}"
            else:
                return f"No likes added."
            
        elif check_result[0]['count(*)'] != 0:
            return "User already liked this vacation."
        


    #👍 user unlike vacation
    def delete_like(self, userID, vacationID):

        #check if userID exists:
        check_user = "SELECT * FROM vacation.users WHERE userID = %s"
        user_params = (userID, )
        result = self.dal.get_scalar(check_user, user_params)
        if not result:
            return "User Doesn't Exist. Please try again."
        
        #check if vacationID exists:
        check_user = "SELECT * FROM vacation.vacations WHERE vacationID = %s"
        user_params = (vacationID, )
        result = self.dal.get_scalar(check_user, user_params)
        if not result:
            return "Vacation Doesn't Exist. Please try again."
        
        sql = """
        DELETE FROM vacation.likes
        WHERE userID = %s AND  vacationID = %s;
        """
        params = (userID, vacationID)
        result = self.dal.delete(sql, params) #this will return rows affected -> int

        if result != 0:
            return f"rows affected: {result} \nuserID {userID} unliked vacationID {vacationID}."  
        else:
            return "Invalid deletion attempt."  

    def close(self):
        self.dal.close()
        
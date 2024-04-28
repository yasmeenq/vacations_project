from utils.dal import *

class LikesLogic:

    def __init__(self):
        self.dal = DAL()

    #👍 check if userID exists:
    def check_user(self, userID):
        check_user = "SELECT * FROM vacation.users WHERE userID = %s"
        user_params = (userID, )
        result = self.dal.get_scalar(check_user, user_params)
        return result

    #👍 check if vacationID exists:
    def check_vacation(self, vacationID):
        check_vacation = "SELECT * FROM vacation.vacations WHERE vacationID = %s"
        user_params = (vacationID, )
        result = self.dal.get_scalar(check_vacation, user_params)
        return result 

    #👍 user like a vacation
    def add_like(self, userID, vacationID):

        #check if userID and vacationID exists:
        self.check_user(userID)
        self.check_vacation(vacationID)

        #check if like already exists:
        check_sql = """
                SELECT count(*) FROM vacation.likes
                WHERE userID = %s AND vacationID = %s
                """
        params = (userID, vacationID)
        check_result = self.dal.get_table(check_sql, params)

        if check_result[0]['count(*)'] == 0: #if no existing like
            #now add like:
            sql = """
            INSERT INTO vacation.likes (userID, vacationID)
            VALUES (%s, %s);
            """
            params = (userID, vacationID)
            result = self.dal.insert(sql, params) #this will return last row id -> int
            
            if result != 0:
                return f"Last row ID: {result}\nuserID {userID} liked vacationID {vacationID}"
            else:
                return "No likes added."
            
        elif check_result[0]['count(*)'] != 0:
            return "User already liked this vacation."
        

    #👍 user unlike vacation
    def delete_like(self, userID, vacationID):

        #check if userID and vacationID exists:
        self.check_user(userID)
        self.check_vacation(vacationID)
        
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
        
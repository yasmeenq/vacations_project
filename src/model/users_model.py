
#Create Model Class: set columns as attributes- str func - dict to object - dicts to objects  #4

class UsersModel:
    def __init__(self,userID, firstname,lastname,email,password,roleID):
        self.userID = userID
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.roleID = roleID
    
    def __str__(self) -> str:
        return f"userID: {self.userID}, firstname: {self.firstname}, lastname: {self.lastname}, email: {self.email}, password: {self.password}, roleID: {self.roleID}"
    
    @staticmethod
    def dictionary_to_object(dictionary):
        userID = dictionary["userID"]
        firstname = dictionary["firstname"]
        lastname = dictionary["lastname"]
        email = dictionary["email"]
        password = dictionary["password"]
        roleID = dictionary["roleID"]
        user = UsersModel(userID,firstname,lastname,email,password,roleID)
        return user
    
    @staticmethod
    def dictionaries_to_objects(list_of_dictionaries):
        items = []
        for dictionary in list_of_dictionaries:
            dictionary = UsersModel.dictionary_to_object(dictionary)
            items.append(dictionary)
        return items
    

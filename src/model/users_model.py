

class UsersModel:
    
    #set columns as attributes
    def __init__(self, userID, firstname, lastname, email, password, roleID):
        self.userID = userID
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.roleID = roleID
    
    def __str__(self) -> str:
        return f"userID: {self.userID}, firstname: {self.firstname}, lastname: {self.lastname}, email: {self.email}, password: {self.password}, roleID: {self.roleID}"
    
    @staticmethod
    def dictionary_to_object(dictionary) -> 'UsersModel':
        userID = dictionary["userID"]
        firstname = dictionary["firstname"]
        lastname = dictionary["lastname"]
        email = dictionary["email"]
        password = dictionary["password"]
        roleID = dictionary["roleID"]
        user = UsersModel(userID,firstname,lastname,email,password,roleID)
        return user
    
    @staticmethod
    def dictionaries_to_objects(list_of_dictionaries) -> list:
        items = []
        for dictionary in list_of_dictionaries:
            dictionary = UsersModel.dictionary_to_object(dictionary)
            items.append(dictionary)
        return items
    

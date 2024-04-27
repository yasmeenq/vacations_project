

class VacationsModel:

    def __init__(self,vacationID, countryID,description,startDate,endDate,price,vacationPictureFile):
        self.vacationID = vacationID
        self.countryID = countryID
        self.description = description
        self.startDate = startDate
        self.endDate = endDate
        self.price = price
        self.vacationPictureFile = vacationPictureFile
    
    def __str__(self) -> str:
        return f"vacationID: {self.vacationID}, countryID: {self.countryID}, description: {self.description}, startDate: {self.startDate}, endDate: {self.endDate}, price: {self.price}, vacationPictureFile: {self.vacationPictureFile}"
    
    @staticmethod
    def dictionary_to_object(dictionary) -> 'VacationsModel':
        vacationID = dictionary["vacationID"]
        countryID = dictionary["countryID"]
        description = dictionary["description"]
        startDate = dictionary["startDate"]
        endDate = dictionary["endDate"]
        price = dictionary["price"]
        vacationPictureFile = dictionary["vacationPictureFile"]
        vacation = VacationsModel(vacationID,countryID,description,startDate,endDate,price,vacationPictureFile)
        return vacation
    
    @staticmethod
    def dictionaries_to_objects(list_of_dictionaries) -> list:
        items = []
        for item in list_of_dictionaries:
            item = VacationsModel.dictionary_to_object(item)
            items.append(item)
        return items
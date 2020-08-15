class Student:
    def __init__(self,name,lastname,year_of_entrance,department):
        self.name = name
        self.lastname = lastname
        self.year_of_entrance = year_of_entrance
        self.department = department

    def display_info(self):
        print(self.name, '' +  self.lastname, '' + 'поступил в ' + self.year_of_entrance + 'г. на факультет:' + self.department)
student1 = Student('Вася','Иванов',str(2017),'Программирование')
student1.display_info()

class User:
    def __init__(self, password):
        # Store the password as a private attribute
        self.__password=password
    
    # Add your methods here
    def check_password(self,input_password):
        return self.__password == input_password

    def change_password(self,old_password, new_password):
        if old_password==self.__password:
            self.__password=new_password
            return True
        return False
    

person1=User("1234")
print(person1.check_password("1234"))  # True
print(person1.change_password("1234", "5678"))  # True
print(person1.check_password("5678"))  # True
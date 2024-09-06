from form_admin import FormAdmin
from user import User
import pickle
class Admin(User):
    def __init__(self, login, pwd) -> None:
        super().__init__(login, pwd)
    def afficherInterface(self):
        print(self)
        FormAdmin(self)

    def ajouter(self,u:User)->None:
        self.users.append(u)  

    def enregistrer(self):
        fichier=open("users.bin","wb")
        pickle.dump(self.users,fichier)
        fichier.close()
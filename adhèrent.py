from user import User
from bibliotheque import Bibliotheque
class Adhèrent(User):
    def __init__(self, login, pwd) -> None:
        super().__init__(login, pwd)
        self.bibliotheque=Bibliotheque("dev","08888","khemisset")
        self.bibliotheque.load()
        
    def afficherInterface(self):
        from form_adhèrent import FormAdhèrent
        FormAdhèrent(self)

    def searchwithnom(self,nom):    
         return  self.bibliotheque.searchwithnom(nom)

    def searchwithAuteur(self):
       return   self.bibliotheque.searchwithAuteur()

   
                

  
from user import User
from document import Document
from bibliotheque import Bibliotheque
class Gerant(User):
    def __init__(self, login: str, pwd: str) -> None:
        super().__init__(login, pwd)
        self.bibliotheque=Bibliotheque("dev","08888","khemisset")
        


    def __str__(self) -> str:
        return super().__str__()

    def afficherInterface(self):
        from form_gerant import FormGerant
        FormGerant(self)
        

    def add(self,document:Document):
        self.bibliotheque.add(document)

    def show(self):
        self.bibliotheque.show() 

    def  remove(self,document):
        self.bibliotheque.remove(document)  

    def save(self):
       self.bibliotheque.save()

    def load(self):
        self.bibliotheque.load()

    def  exists(self,document):
        self.bibliotheque.exists(document)   

    def searchwithnom(self):
        self.bibliotheque.searchwithnom()    

    def emprinter(self):
        self.bibliotheque.emprinter() 
        

                
    

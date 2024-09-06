from document import Document
class Cd(Document):
    def __init__(self, nom, context,capacite,auteur) -> None:
        super().__init__(nom, context)
   

    def getCapacite(self):
        return self.__capacite
    
    
    def setCapacite(self,capacite):
        if capacite>0:
            self.__capacite=capacite
        else:
            raise Exception("Attention le type de CD doit être strictement positif !")
        
    def getAuteur(self):
        return self.__auteur
    
    def setAuteur(self,auteur:str):
        if len(auteur)>0 :
            self.__auteur=auteur
        else:
            raise Exception("attention le champ de  capaciter ne doit pas etre vide!")
        
    def __str__(self):
        return super().__str__()+'\t'+float(self.__capacite) +'\t'+self.__auteur+'\t'

    
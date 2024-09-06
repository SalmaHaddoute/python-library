from document import Document
class Livres(Document):
    def __init__(self, nom, context,pages,auteur) -> None:
        super().__init__(nom, context)
        self.setPages(pages)
        self.setAuteur(auteur)


    def getPages(self):
        return self.__pages    

    def getAuteur(self):
        return self.__auteur 

    def setPages(self,pages) :
        self.__pages=pages  

    def setAuteur(self,auteur) :
        self.__auteur=auteur 


    # def afficherInterface(self):
    #     FormLivres(self)     

    def __str__(self) -> str:
        return super().__str__+'   '+self.__pages+'   '+self.__auteur

    def afficherHorizontal(self):
        print(self)    
                   
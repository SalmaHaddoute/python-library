# from adhèrent import Adhèrent
# from bibliotheque import Bibliotheque
class Emprint():
    def __init__(self,date,adherent,document) -> None:
        self.setDate(date)
        self.setAdherent(adherent)
        self.setDocument(document)
    
       

    def getDate(self):
        return self.__date

    def setDate(self,date) :
        self.__date=date   

    def getDocument(self):
        return self.__document    

    def setDocument(self,document) :
        self.__document=document  

    def getAdherent(self):
        return self.__adherent    

    def setAdherent(self,adherent) :
        self.__adherent=adherent       
    

    def __str__(self) -> str:
        return str(self.__date)+'  '+str(self.__adherent)+'  '+str(self.__document)

    def emprinter(self):
        self.emprinter()

    def saveEmprint(self):
        self.saveEmprint()

    def loadEmprints(self):   
        self.loadEmprints() 

   


    
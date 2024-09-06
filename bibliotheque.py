from document import Document
from emprint import Emprint
import pickle
class Bibliotheque():
    def __init__(self,nom,telephone,adress) -> None:
        self.__nom=nom
        self.__telephone=telephone
        self.__adress=adress
        self.__documents=list()
        self.__emprints=list()

# les getter et les setter 
    def getNom(self):
        return self.__nom  

    def getTelephone(self):
        return self.__telephone 

    def getAdress(self):
        return self.__adress  

    def getDocuments(self):
        return self.__documents   

    def getEmprints(self):
        return self.__emprints        

    def setNom(self,nom):
        self.__nom=nom

    def setTelephone(self,telephone):
        self.__telephone=telephone

    def setDocuments(self,documents):
        self.__documents=documents  

    def setEmprints(self,emprints):
        self.__emprints=emprints      
                                  
    def setAdress(self,adress):
        self.__adress=adress
# transformer tous en str
    def __str__(self) -> str:
        return self.__nom + " à l'adresse : "+self.__adress +'\n'+"et pour contacter"+str(self.__telephone)
# ajouter un document 
    def add(self,document) :
            self.__documents.append(document)
# afficher un doc
    def show(self):
        print("La liste des document du",self)    
        for item in self.__documents :
            item.afficherHorizontal()
# enregistrer un emprint
    def saveEmprint(self):
        fichier=open('emprints.bin',"wb")
        pickle.dump(self.__emprints,fichier)
        fichier.close()
# enregistrer un doc
    def save(self):
        fichier=open("documents.bin","wb")
        pickle.dump(self.__documents,fichier)
        fichier.close()
# charcher le fichier emprints
    def loadEmprints(self):
        fichier=open("emprints.bin","rb")
        self.__emprints=pickle.load(fichier)
        fichier.close()    
#ajouter les emprints  
    def emprinter(self,emprint:Emprint):
        self.__emprints.append(emprint)

# sumprimer doc
    def remove(self,document):
        self.__documents.remove(document)

# sumprimer emprint
    def removeEmprint(self,emprint):
        self.__emprints.remove(emprint)

# charger le fichier des documents
    def load(self):
        fichier=open("documents.bin","rb")
        self.__documents=pickle.load(fichier)
        fichier.close()

# rechercher si il existe    
    def exists(self,nom)->bool:
        for document in self.__documents:
            if document.getNom()==nom:
                return True                
        return False        
# rechercher avec nom
    def searchwithnom(self,nom)->Document:
        #for document in self.__documents:
        ##    if document.getNom()==nom:
        #    return document
        l=list()
        lnom=nom.lower()
        for document in self.__documents:     
            s:str=document.getNom().lower()             
            if s.startswith(lnom):
                l.append(document)
        return l

# rechercher avec auteur
    def searchwithAuteur(self,auteur)->Document:
        l=list()
        for document in self.__documents:
            if document.getAuteur().lower().startswith(auteur.lower()):
                l.append(document)
            return l   






   # def getMaxId(self)->int:
    #    m=self.__produits[0].getId()
       # for i in range(1,len(self.__produits)):
         #   if self.__produits[i].getId()>m:
          #      m=self.__produits[i].getId()
       # return m

           


    
               
       
    
                                                 
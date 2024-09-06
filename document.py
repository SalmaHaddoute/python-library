class Document():
    def __init__(self,nom,context) -> None:
        self.setnom(nom)
        self.setContext(context)

    def getNom(self):
       return self.__nom

    def getContext(self):
       return self.__context

    def setContext(self,context):
       self.__context=context

    def setnom(self,nom):
       self.__nom=nom
   
    def __str__(self) -> str:
       return str(self.__nom)+'   '+self.__context

    
import pickle
# from tkinter import messagebox as msg
class User():
    def __init__(self,login:str,pwd:str,role='') -> None:
        self.setLogin(login)
        self.setPwd(pwd)
        self.setRole(role)

    def setLogin(self,login):
        self.__login=login
    def getLogin(self):
        return self.__login

    def setPwd(self,pwd):
        self.__pwd=pwd
    def getPwd(self):
        return self.__pwd

    def setRole(self,role):
        self.__role=role
    def getRole(self):
        return self.__role

    def __str__(self) -> str:
        return self.__login+'\t'+self.__pwd+'\t'+self.__role

    def afficherInterface(self):
        pass

    def authentifier(self):
        from admin import Admin
        from adhèrent import Adhèrent  
        from gerant import Gerant    

        try:
            self.chargerUsers()
            user :User
            for user in self.users:
                if self.__login==user.getLogin() and self.__pwd==user.getPwd():
                    if user.getRole()=='admin':
                        u =Admin(user.getLogin(),user.getPwd())
                        u.users=self.users
                        u.afficherInterface()
                    elif user.getRole()=='adhèrent':
                        u =Adhèrent(user.getLogin(),user.getPwd())
                        u.users=self.users
                        u.afficherInterface()
                    elif user.getRole()=='gerant':
                        u =Gerant(user.getLogin(),user.getPwd())
                        u.users=self.users
                        u.afficherInterface()    

        except Exception as ex:
            print(ex)
            fichier=open("users.bin","wb")
            self.users=list()
            self.users.append(User("admin","admin","admin"))
            pickle.dump(self.users,fichier)
            fichier.close()
            self.authentifier()



    def chargerUsers(self):
        fichier=open("users.bin","rb")
        self.users=pickle.load(fichier)
        fichier.close()

    # def ld(self):
    #     adhèrents=[user for user in self.users if isinstance(user,Adhèrent)]
    #     return adhèrents


     
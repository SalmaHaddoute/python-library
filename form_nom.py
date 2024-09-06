import tkinter as tk
from tkinter import tix
# from bibliotheque import Bibliotheque
# from document import Document
from adhèrent import Adhèrent
class FormNom():
    def __init__(self,adhèrent) -> None:
        self.adhèrent:Adhèrent=adhèrent
        self.root=tk.Tk()
        self.root.configure(bg="orange")
        self.root.configure(bg="dimgray")
        self.root.geometry('600x400')
        self.root.title('chercher par nom')
        self.root.iconbitmap('download.ico')
        
        self.framChercher=tk.LabelFrame(self.root,text="chercher par nom ",fg="chartreuse",bg="white", font='Roman 20 bold ',bd=2,padx=20,pady=10)
        self.framChercher.pack(expand=1)
        #enter valeur
        self.labelNom=tk.Label(self.framChercher,text='nom du  livre :',font='Roman 20 bold')
        self.labelNom.grid(row=0,column=0,sticky=tk.W)

        self.entryNom=tk.Entry(self.framChercher,background="white",fg="black",font='Roman 20 bold')
        self.entryNom.grid(row=0,column=1)

        self.buttonChercher=tk.Button(self.root,text='chercher ici!',background='chartreuse',fg='white',font='Roman 20 bold',command=self.searchwithnom)
        self.buttonChercher.pack(expand=0)
        self.root.mainloop()


    def searchwithnom(self):
        #self.adhèrent.chercherParNom()
        from livres import Livres
        root=tix.Tk()
        root.geometry("600x400")
        root.title("Listes de livres")
        sw=tix.ScrolledWindow(root)
        sw.pack(expand=1,fill=tk.BOTH)
        i=0
        for document in self.adhèrent.searchwithnom(self.entryNom.get()):
            if isinstance(document,Livres):
                    livre=document
                    entryNom=tk.Entry(sw.window,width=10)
                    entryNom.insert(0,livre.getNom())
                    entryNom.grid(row=i,column=0)

                    entryContext=tk.Entry(sw.window)
                    entryContext.insert(0,livre.getContext())
                    entryContext.grid(row=i,column=1)

                    entryPages=tk.Entry(sw.window,width=10)
                    entryPages.insert(0,livre.getPages())
                    entryPages.grid(row=i,column=2)

                    entryAuteur=tk.Entry(sw.window)
                    entryAuteur.insert(0,livre.getAuteur())
                    entryAuteur.grid(row=i,column=3)
                    i+=1
        root.mainloop() 

















    # def chercherParNom(self):
    #     root=tix.Tk()
    #     root.geometry("600x400")
    #     root.title("Listes de livres")
    #     sw=tix.ScrolledWindow(root)
    #     sw.pack(expand=1,fill=tk.BOTH)
    #     i=0
    #     for document in self.adhèrent.getDocuments():
    #         if isinstance(document):
    #             livre=document
    #             entryNom=tk.Entry(sw.window,width=10)
    #             entryNom.insert(0,livre.getNom())
    #             entryNom.grid(row=i,column=0)

    #             entryContext=tk.Entry(sw.window)
    #             entryContext.insert(0,livre.getContext())
    #             entryContext.grid(row=i,column=1)

    #             entryPages=tk.Entry(sw.window,width=10)
    #             entryPages.insert(0,livre.getPages())
    #             entryPages.grid(row=i,column=2)

    #             entryAuteur=tk.Entry(sw.window)
    #             entryAuteur.insert(0,livre.getAuteur())
    #             entryAuteur.grid(row=i,column=3)
    #             i+=1
    #     root.mainloop() 
    # def chercherParNom(self,nom):
    #     self.adhèrent.searchwithnom(nom)



        

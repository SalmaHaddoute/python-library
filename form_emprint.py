 
import tkinter as tk
from tkinter import ttk
from gerant import Gerant
from emprint import Emprint
from tkinter import tix
# from bibliotheque import Bibliotheque
# from adhèrent import Adhèrent
class formEmprint():
    def __init__(self,gerant) -> None:
        self.gerant:Gerant=gerant
        self.root=tk.Tk()
        # self.root.configure(bg="orange")
        self.root.configure(bg="dimgray")
        self.root.geometry('600x400')
        self.root.title('chercher par auteur')
        self.root.iconbitmap('download.ico')
         
         # frrame 
        self.framAll=tk.LabelFrame(self.root,text='emprinter ici !', padx=70,font=('Roman ',18),foreground='chartreuse')
        self.framAll.pack(expand=1)
        stringUser=[]
        from user import User
        u:User
        for u in self.gerant.users:
            stringUser.append(u.getLogin())

        # Combobox Adhérent
        self.labelAdherent =ttk.Label(self.framAll, text="Adhérent:" ,foreground='black',font=('Lucida ',12))
        self.labelAdherent.grid(row=0,column=0)
        self.comboAdherent =ttk.Combobox(self.framAll ,values=stringUser)
        self.comboAdherent.grid(row=0,column=1)
        # Combobox documents
        documents = []
        # from bibliotheque import Bibliotheque
        from document import Document
        d:Document
        self.gerant.bibliotheque.load()
        for d in self.gerant.bibliotheque.getDocuments():
            documents.append(d.getNom())

        self.labelDoc =tk.Label(self.framAll, text="Document:",foreground='black',font=('Lucida ',12))
        self.labelDoc.grid(row=1,column=0)
        self.comboDoc =ttk.Combobox(self.framAll,values=documents)
        self.comboDoc.grid(row=1,column=1)

        self.labelDate=tk.Label(self.framAll, text='Date :',foreground='black',font=('Lucida ',12))
        self.labelDate.grid(row=2,column=0)

        self.entryDate=tk.Entry(self.framAll)
        self.entryDate.grid(row=2,column=1)

        # Bouton Emprunter
        self.lbframeA=tk.LabelFrame(self.root,text='action')
        self.lbframeA.pack(side=tk.BOTTOM)
        self.buttonEmprinter =tk.Button(self.lbframeA, text="Emprunt",background='chartreuse',font=('Lucida ',16), command=self.emprinter)
        self.buttonEmprinter.pack(side=tk.LEFT) 
        # botton pour enregistrer 
        self.buttonsave =tk.Button(self.lbframeA, text="save",background='chartreuse',font=('Lucida ',16), command=self.saveEmprint)
        self.buttonsave.pack(side=tk.LEFT) 
        # botton pour charger
        self.buttoncharger =tk.Button(self.lbframeA, text="charger",background='chartreuse',font=('Lucida ',16), command=self.loadEmprints)
        self.buttoncharger.pack(side=tk.LEFT)
         # botton pour afficher
        self.buttonshow =tk.Button(self.lbframeA, text="show",background='chartreuse',font=('Lucida ',16), command=self.showEmprints)
        self.buttonshow.pack(side=tk.LEFT)           

        self.root.mainloop()

    def emprinter(self):
        self.emprinter()

    def saveEmprint(self):
        self.saveEmprint()

    def loadEmprints(self):   
        self.loadEmprints()  

    def showEmprints(self):
        root=tix.Tk()
        root.geometry("600x400")
        root.title("Listes des Habits")
        sw=tix.ScrolledWindow(root)
        sw.pack(expand=1,fill=tk.BOTH)
        i=0
        emprint:Emprint
        for emprint in self.gerant.bibliotheque.getEmprints():
            if isinstance(emprint,Emprint):
                emprint=emprint
                comboA=tix.ComboBox(sw.window,width=10)
                comboA.insert(0,emprint.getAdherent())
                comboA.grid(row=i,column=0)

                entryD=tix.ComboBox(sw.window)
                entryD.insert(0,emprint.getAdherent())
                entryD.grid(row=i,column=1)

                entryDate=tk.Entry(sw.window,width=10)
                entryDate.insert(0,emprint.getDate())
                entryDate.grid(row=i,column=2)

                i+=1
        root.mainloop()        


     


    
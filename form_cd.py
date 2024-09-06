import tkinter as tk
from tkinter import tix
# from document import Document
from cd import Cd
from tkinter import messagebox as msg
class FormCd:
    def __init__(self,gerant) -> None:
        self.gerant=gerant
        try:
             self.gerant.load()
        except Exception as ex:
             msg.showwarning("warning",ex)   

        self.currentcd:Cd=None
        self.root=tk.Tk()
        self.root.configure(bg="dimgray")
        self.root.geometry('1000x400')
        self.root.iconbitmap('download.ico')
        self.root.title('pour CD')

        self.fram=tk.Label(self.root, text='GESTION DES CD',foreground='black',background='dimgray',font='Roman 20 bold',padx=50,pady=10)
        self.fram.pack()
    

        self.framInfocd=tk.LabelFrame(self.root,text="Information d'un cd",fg="black",background='dimgray', font='Roman 20 bold ',bd=2)
        self.framInfocd.pack(expand=1)

# TOOO ENTER VALUES
        self.labelNom=tk.Label(self.framInfocd,text='nom du cd :',bg='dimgray',fg='black',font='Roman 16 bold')
        self.labelNom.grid(row=0,column=0,sticky=tk.W)

        self.entryNom=tk.Entry(self.framInfocd,background="white",fg="black",width=60,font='Roman 16 bold')
        self.entryNom.grid(row=0,column=1)

        self.labelContext=tk.Label(self.framInfocd,text='context du cd :',bg='dimgray',fg='black',font='Roman 16 bold')
        self.labelContext.grid(row=2,column=0,sticky=tk.W)

        self.entryContext=tk.Entry(self.framInfocd,background="white",width=60,fg="black",font='Roman 16 bold')
        self.entryContext.grid(row=2,column=1)

        self.labelCapacite=tk.Label(self.framInfocd,text='pages du cd :',fg='black',bg='dimgray',font='Roman 16 bold')
        self.labelCapacite.grid(row=1,column=0,sticky=tk.W)

        self.entryCapacite=tk.Entry(self.framInfocd,background="white",width=60,fg="black",font='Roman 16 bold')
        self.entryCapacite.grid(row=1,column=1)


        self.labelAuteur=tk.Label(self.framInfocd,text='auteur du cd :',fg='black',bg='dimgray',font='Roman 16 bold')
        self.labelAuteur.grid(row=3,column=0,sticky=tk.W)

        self.entryAuteur=tk.Entry(self.framInfocd,background="white",fg="black",width=60,font='Roman 16 bold')
        self.entryAuteur.grid(row=3 ,column=1)
    #BUTTONS 
        self.frameButton=tk.LabelFrame(self.root,text="Action",font="Arial 16 bold italic",fg="chartreuse",pady=10,bg="dimgray")
        self.frameButton.pack(expand=0)

        self.btnAjouter=tk.Button(self.frameButton,text="Ajouter",bg="chartreuse",
        fg="white",bd=5,font="Arial 16 bold italic",command=self.add)
        self.btnAjouter.pack(side=tk.LEFT)

        self.btnAfficher=tk.Button(self.frameButton,text="Afficher",bg="chartreuse",
        fg="white",bd=5,font="Arial 16 bold italic",command=self.show)
        self.btnAfficher.pack(side=tk.LEFT)

        self.btnModifier=tk.Button(self.frameButton,text="Modifier",bg="chartreuse",
        fg="white",bd=5,font="Arial 16 bold italic",command=self.update)
        self.btnModifier.pack(side=tk.LEFT)

        self.btnSupprimer=tk.Button(self.frameButton,text="Supprimer",bg="chartreuse",
        fg="white",bd=5,font="Arial 16 bold italic",command=self.delete)
        self.btnSupprimer.pack(side=tk.LEFT)

        self.btnEnregistrer=tk.Button(self.frameButton,text="Enregistrer",bg="chartreuse",
        fg="white",bd=5,font="Arial 16 bold italic",command=self.save)
        self.btnEnregistrer.pack(side=tk.LEFT)

        self.btnCharger=tk.Button(self.frameButton,text="Charger",bg="chartreuse",
        fg="white",bd=5,font="Arial 16 bold italic",command=self.load)
        self.btnCharger.pack(side=tk.LEFT)

        self.btnChercher=tk.Button(self.frameButton,text="Chercher",bg="chartreuse",
        fg="white",bd=5,font="Arial 16 bold italic",command=self.search)
        self.btnChercher.pack(side=tk.LEFT)

        self.btnEffacer=tk.Button(self.frameButton,text="Effacer",bg="chartreuse",
        fg="white",bd=5,font="Arial 16 bold italic",command=self.deleteEntry)
        self.btnEffacer.pack(side=tk.LEFT)

 # frame pour chercher

        self.frameSearch=tk.LabelFrame(self.root,text='RECHERCHE',font='Arial 16 bold italic',
                                                            bd=1,padx=20,pady=20)
        

        self.lblNomcdsearch=tk.Label(self.frameSearch,text="NOM",width=30) 
        self.lblNomcdsearch.grid(row=0,column=0) 

        self.entryNomcdsearch=tk.Entry(self.frameSearch,width=50)    
        self.entryNomcdsearch.grid(row=0,column=1)

        self.BtnOkSearch=tk.Button(self.frameSearch,text="ok",command=self.okSearch,width=30,
                                                               )   
        self.BtnOkSearch.grid(row=1,column=0)

        self.BtnAnnulerSearch=tk.Button(self.frameSearch,text="Annuler",command=self.AnnulerSearch,width=30,
                                                               ) 
        self.BtnAnnulerSearch.grid(row=1,column=1)                                                                                                                     
#frame Fermer et une button fermer :
        self.btnFermer=tk.Button(self.root,text="Fermer",bg="black",
        fg="white",bd=10,font="Arial 16 bold italic",command=self.root.destroy)
        self.btnFermer.pack(side=tk.BOTTOM)
    
        self.root.mainloop()
    
    def add(self):
        try:
            cd=Cd(self.entryNom.get(),self.entryContext.get(),self.entryCapacite.get(),self.entryAuteur.get())
            self.gerant.add(cd)
        except Exception as ex:
            msg.showwarning("Attention",ex)


    def deleteEntry(self):
        self.entryNom.delete(0,tk.END)
        self.entryContext.delete(0,tk.END)
        self.entryCapacite.delete(0,tk.END)
        self.entryAuteur.delete(0,tk.END)

    def show(self):
        root=tix.Tk()
        root.geometry("600x400")
        root.title("Listes des Habits")
        sw=tix.ScrolledWindow(root)
        sw.pack(expand=1,fill=tk.BOTH)
        i=0
        cd:Cd
        for document in self.gerant.bibliotheque.getDocuments():
            if isinstance(document,Cd):
                livre=document
                entryNom=tk.Entry(sw.window,width=10)
                entryNom.insert(0,livre.getNom())
                entryNom.grid(row=i,column=0)

                entryContext=tk.Entry(sw.window)
                entryContext.insert(0,livre.getContext())
                entryContext.grid(row=i,column=1)

                entryCapacite=tk.Entry(sw.window,width=10)
                entryCapacite.insert(0,livre.getCapacite())
                entryCapacite.grid(row=i,column=2)

                entryAuteur=tk.Entry(sw.window)
                entryAuteur.insert(0,livre.getAuteur())
                entryAuteur.grid(row=i,column=3)
                i+=1
        root.mainloop()        

    def save(self):
        self.gerant.save()

    def load(self):
        self.gerant.load()

    def delete(self):
        if msg.askyesno('confirmation ',"etes vous sure de suprimer cette article?"):
            self.gerant.remove(self.currentcd)
            self.deleteEntry()

    def update(self):
        if msg.askyesno('comfirmation','etes vous sure de modifier cette article?'):
           try: 
            self.currentcd.setnom(self.entryNom.get())
            self.currentcd.setContext(self.entryContext.get())
            self.currentcd.setPages(float(self.entryCapacite.get()))
            self.currentcd.setAuteur(self.entryAuteur.get())
           
            
           except Exception as ex:
               msg.showwarning("Attention",ex) 
                 
    
    def search(self ):
        self.frameSearch.pack()

    def AnnulerSearch(self) :
        self.frameSearch.pack_forget()   

    def okSearch(self)  :  
        if self.gerant.exists(self.entryNomcdsearch.get()):
            self.currentcd:Cd=self.gerant.searchwithnom((self.entryNomcdsearch.get()))
            self.deleteEntry()
            self.entryNom.insert(0,self.currentcd.getNom())
            self.entryContext.insert(0,self.currentcd.getContext())
            self.entryCapacite.insert(0,self.currentcd.getCapacite())
            self.entryAuteur.insert(0,self.currentcd.getAuteur())
        else:
            msg.showwarning("message","document innexistant!")  
        self.frameSearch.pack_forget()



import tkinter as tk
from form_livres import FormLivres
from form_cd import FormCd
from form_emprint  import formEmprint

class FormGerant():
     def __init__(self,gerant) -> None:
        self.gerant=gerant
        self.root=tk.Tk()
        self.root.geometry('600x400')
        self.root.title('GESTION DU GERANT')
        self.root.configure(bg="dimgray")
        self.root.iconbitmap('download.ico')
        self.lblBienvenue=tk.Label(self.root,text='BIENVENUR DANS LA GESTION DES DOCUMENTS',font='Roman 20 bold',background='dimgray',fg='chartreuse')
        self.lblBienvenue.pack()

        self.framButtons=tk.Frame(self.root,bg='white',padx=20,pady=20)
        self.framButtons.pack(expand=1)
        self.btnGestionLivres=tk.Button(self.framButtons,text="livres",width=10,
                                              bg="chartreuse",fg="dimgray",font='Script 20 bold',bd=10,padx=15,cursor='hand2',borderwidth=1,
                                                  activebackground="white",activeforeground="chartreuse",command=self.openForLiveres)
        self.btnGestionLivres.pack(side="left")

        self.btnGestionCd=tk.Button(self.framButtons,text="cd",width=10,
                                                        bg="chartreuse",fg="dimgray",font='Script 20 bold',bd=10,padx=15,cursor='hand2',
                                                        borderwidth=1,activebackground="white",activeforeground="chartreuse",command=self.openForCd)
        self.btnGestionCd.pack(side='left')
        
        
        self.btnEmprint=tk.Button(self.framButtons,text="emprint",width=10,
                                                        bg="chartreuse",fg="dimgray",font='Script 20 bold',bd=10,padx=15,cursor='hand2',
                                                        borderwidth=1,activebackground="white",activeforeground="chartreuse",command=self.openForEmprint)
        self.btnEmprint.pack(side='left')


        self.btnQuitter=tk.Button(self.root,text="quitter",width=10,bg="chartreuse",fg="black",font='Script 20 bold',bd=5,padx=10,
                                                          cursor="tcross",activebackground="black",activeforeground="chartreuse",
                                                          command=self.root.destroy)
        self.btnQuitter.pack(side="bottom")
        self.root.mainloop()


     def openForLiveres(self):
        FormLivres(self.gerant)     

     def openForCd(self):
        FormCd(self.gerant)     

     def openForEmprint(self):
        formEmprint(self.gerant)        
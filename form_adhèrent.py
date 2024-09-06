import tkinter as tk

class FormAdhèrent():
    from user import User
    def __init__(self,adhèrent:User) -> None:
    
      self.adhèrent=adhèrent
      #self.biblio=adhèrent.bibliotheque
      self.root= tk.Tk()
      self.root.geometry('600x400')
      self.root.iconbitmap('download.ico')
      self.root.configure(bg="dimgray") 
      self.root.title("Formulaire Gestion des document")
      self.frameChercher=tk.LabelFrame(self.root,text="chercher",padx=20,pady=20,fg="blue")
      self.frameChercher.pack(expand=1)

      self.framButtons=tk.Frame(self.root,bg='white',padx=20,pady=20)
      self.framButtons.pack(expand=1)
      self.btnChercherWhitNom=tk.Button(self.framButtons,text="Chercher avec nom",width=10,bg="chartreuse",
                                                  fg="dimgray",font='Script 20 bold',bd=10,padx=16,cursor='hand2',borderwidth=1,
                                                  activebackground="white",activeforeground="chartreuse",command=self.ChercheNom)
      self.btnChercherWhitNom.pack(side="left")
      self.btnChercherWhitAuteur=tk.Button(self.framButtons,text="chercher par auteur",width=10,
                                                        bg="chartreuse",fg="dimgray",font='Script 20 bold',bd=10,padx=16,cursor='hand2',
                                                        borderwidth=1,activebackground="white",activeforeground="chartreuse",command=self.chercheAuteur)
      self.btnChercherWhitAuteur.pack(side='left')
     
      


      self.btnQuitter=tk.Button(self.root,text="quitter",width=10,bg="chartreuse",fg="white",font='Script 20 bold',bd=5,padx=10,
                                                          cursor="tcross",activebackground="white",activeforeground="chartreuse",
                                                          command=self.root.destroy)
      self.btnQuitter.pack(side="bottom")
      self.root.mainloop()


    def ChercheNom(self):
        from form_nom import FormNom
        FormNom(self.adhèrent)

    def chercheAuteur(self):
        from form_auteur import FormAuteur
        FormAuteur(self.adhèrent)


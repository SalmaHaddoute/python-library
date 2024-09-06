import tkinter as tk
from tkinter import messagebox as msg

class FormAdmin:
    from user import User
    def __init__(self,admin:User) -> None:
      self.admin=admin
      self.root= tk.Tk()
      self.root.geometry('600x400')
      self.root.iconbitmap('download.ico')
      self.root.configure(bg="dimgray") 
      self.root.title("Formulaire Gestion des Utilisateurs")
      self.frameAuth=tk.LabelFrame(self.root,text="Authentification",font=('Lucida ',16),bd=5, relief="solid",highlightbackground="chartreuse",pady=20,fg="chartreuse")
      self.frameAuth.pack(expand=1)

      self.lblLogin=tk.Label(self.frameAuth,text='Login',font=12,fg="black")
      self.lblLogin.grid(row=0,column=0,sticky=tk.NW)

      self.entryLogin=tk.Entry(self.frameAuth,font=12,fg="black")
      self.entryLogin.grid(row=0,column=1)

      self.lblPwd=tk.Label(self.frameAuth,text='Password',font=12,fg="black")
      self.lblPwd.grid(row=1,column=0,sticky=tk.NW)

      self.entryPwd=tk.Entry(self.frameAuth,font=12,fg="black")
      self.entryPwd.grid(row=1,column=1)

      self.lblRole=tk.Label(self.frameAuth,text='Rôle',font=12,fg="black")
      self.lblRole.grid(row=2,column=0,sticky=tk.NW)

      self.entryRole=tk.Entry(self.frameAuth,font=12,fg="black")
      self.entryRole.grid(row=2,column=1)

      self.frameButton=tk.Frame(self.root)
      self.frameButton.pack()
      self.btnAjouter=tk.Button(self.frameButton,text='Ajouter',bg="chartreuse",padx=16,fg='white',command=self.ajouter)
      self.btnAjouter.pack(side=tk.LEFT)
      self.btnEnregistrer=tk.Button(self.frameButton,text='Enregistrer',bg="chartreuse",padx=15,fg='white',command=self.enregistrer)
      self.btnEnregistrer.pack(side=tk.LEFT)
      

      self.root.mainloop()

    def ajouter(self):
        from user import User
        self.admin.ajouter(User(self.entryLogin.get(),self.entryPwd.get(),self.entryRole.get()))

    def enregistrer(self):
        self.admin.enregistrer()
        msg.showinfo('ENREGISTREMENT ETAIT REUSSIT',"enregistree avec succes !!")
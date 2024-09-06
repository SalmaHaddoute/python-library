import tkinter as tk
from user import User
class FormAuth:
    def __init__(self) -> None:
      self.root= tk.Tk()
      self.root.geometry('600x400')
      self.root.title("Formulaire d'Authentification")
      self.root.iconbitmap('download.ico')
      self.root.configure(bg="dimgray")  # Définit la couleur de fond de la fenêtre
      self.frameAuth=tk.LabelFrame(self.root,text="Authentification",padx=20,font=('Lucida ',16),pady=20,fg="chartreuse")
      self.frameAuth.pack(expand=1)

      self.lblLogin=tk.Label(self.frameAuth,text='Login',font=12,fg="black")
      self.lblLogin.grid(row=0,column=0,sticky=tk.NW)

      self.entryLogin=tk.Entry(self.frameAuth,font=12,)
      self.entryLogin.grid(row=0,column=1)

      self.lblPwd=tk.Label(self.frameAuth,text='Password',font=12,fg="black")
      self.lblPwd.grid(row=1,column=0,sticky=tk.NW)

      self.entryPwd=tk.Entry(self.frameAuth,show='*',font=12,fg="black")
      self.entryPwd.grid(row=1,column=1)

      self.btnOk=tk.Button(self.frameAuth,text='Ok',background='chartreuse',fg='white',command=self.ok)
      self.btnOk.grid(row=2,column=0,columnspan=2,sticky=tk.NSEW)
      self.root.mainloop()

    def ok(self):
        user=User(self.entryLogin.get(),self.entryPwd.get())
        user.authentifier()
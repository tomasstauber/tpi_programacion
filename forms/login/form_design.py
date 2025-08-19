import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import utils.generic as utl
from forms.master.form_master import MainPanel 

class FormLoginDesign:
    
    def verif_user(self):
        pass
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesión")
        self.ventana.geometry("800x500")
        self.ventana.config(bg="#fafafa")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)
        
        logo = utl.leer_imagen("./images/logo.jpg", (200, 200))
        
        #frame logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg="#3a7ff6")
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg="#3a7ff6")
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        #frame formulario
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fafafa")
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        
        #frame form_title
        frame_form_title = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg="black")
        frame_form_title.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_title, text="Inicio de Sesión", font=("Console", 30), fg="#666a88", bg="#fafafa", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        #frame campos
        frame_form_fields = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg="#fafafa")
        frame_form_fields.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        
        #data entries
        field_user = tk.Label(frame_form_fields, text="Usuario", font=("Console", 14), fg="#666a88", bg="#fafafa", anchor="w")
        field_user.pack(fill=tk.X, padx=20, pady=5)
        self.user = ttk.Entry(frame_form_fields, font=("Console", 14))
        self.user.pack(fill=tk.X, padx=20, pady=10)
        
        field_password = tk.Label(frame_form_fields, text="Contraseña", font=("Console", 14), fg="#666a88", bg="#fafafa", anchor="w")
        field_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fields, font=("Console", 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")
        
        #button
        init_session = tk.Button(frame_form_fields, text="Iniciar Sesión", font=("Console", 16, BOLD), bg="#3a7ff6", bd=0, fg="#fff", command=self.verif_user)
        init_session.pack(fill=tk.X, padx=20, pady=20)
        init_session.bind("<Return>", (lambda event: self.verif_user()))
                
        self.ventana.mainloop()
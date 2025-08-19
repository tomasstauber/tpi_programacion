import tkinter as tk
from tkinter.font import BOLD
import utils.generic as utl

class MainPanel:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Main Panel")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg="#fafafa")
        self.ventana.resizable(width=0, height=0)
        
        logo = utl.leer_imagen("./images/logo.jpg", (200, 200))
        
        label = tk.Label(self.ventana, image=logo, bg="#3a7ff6")
        label.place(x=0, y=0, relwidth=1, relheight=1)
        self.ventana.mainloop()
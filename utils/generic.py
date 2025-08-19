from PIL import ImageTk, Image

def leer_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.Resampling.LANCZOS))

def centrar_ventana(ventana, app_ancho, app_largo):
    screen_width = ventana.winfo_screenwidth()
    screen_large = ventana.winfo_screenheight()
    x = int((screen_width/2) - (app_ancho/2))
    y = int((screen_large/2) - (app_largo/2))
    return ventana.geometry(f"{app_ancho}x{app_largo}+{x}+{y}")

#Programa que permite descargar videos en Youtube
#seleccionando la resolucion
#Creado por NEON48

#Importar clases necesarias
from tkinter import messagebox
from tkinter import ttk
import tkinter.filedialog
import tkinter
from pytube import YouTube
from tkinter import *

if __name__ =='__main__':

    #Inicializamos variables globales necesarias
    varDir=''
    a=''

    #Funcion que permite seleccionar el direcctorio para grabar el video
    def direcctorio():
            directorio = tkinter.filedialog.askdirectory()
            labelDirecctorio.configure(text=directorio)
            labelDirecctorio.pack()
            botonDescargar.config(state=NORMAL)

    #Fucion para verificar si la url es correcta
    #Y determinar las resoluciones del video
    def verificarVideo():
        try:
            yt = YouTube(cajaUrl.get())
            res = yt.streams.filter(progressive=True)
            listaResolucion = []
            for cadena in res:
                 listaResolucion.append(cadena.resolution)
            cajaResolucion['values']=listaResolucion
        except:
            messagebox.showerror(title='ERROR',message='Verifique que la url sea correcta')



    #Funcion para descargar el video
    def descargarVideo():
        yt = YouTube(cajaUrl.get())
        yt.streams.filter(res=cajaResolucion.get()).first().download(labelDirecctorio.cget('text'))
        messagebox.showinfo(title='Descarga Exitosa',message='Video descargado en '+ labelDirecctorio.cget('text'))

    #Instanciamos la clase Tkinter
    root = Tk()
    #Asignamos el titulo a la ventana
    root.title('Descargar YouTube')
    #Tamaño de la ventana
    sWindow= "300x300"
    root.geometry(sWindow)
    #Evitar que la ventana sea de tamaño ajustable
    root.resizable(0,0)
    #Centrar la ventana
    x_ventana = root.winfo_screenmmwidth()+(root.winfo_screenmmwidth()/2)
    y_ventana = root.winfo_screenmmheight()
    root.geometry(sWindow+'+'+str(int(x_ventana))+'+'+str(int(y_ventana)))

    #Instanciamos los objetos, etiquetas y campos necesarios
    imagenLogo = tkinter.PhotoImage(file='Youtube.png')
    labelImagen = tkinter.Label(root,image=imagenLogo)
    labelPresentacion = tkinter.Label(root,text='App para descargar Videos de YouTube')
    labelUrl = tkinter.Label(root,text='Ingrese la URL del Video')
    cajaUrl = tkinter.Entry(root)

    #El botonURL llama la funcion para verificar el video
    botonURL= tkinter.Button(root,text='Verificar video',command=verificarVideo)
    labelResolucion = tkinter.Label(root,text='Seleccione la Resolucion del video')
    cajaResolucion = ttk.Combobox(values=[""])
    #El botonDirectorio ejecuta la funcion directorio
    botonDirectorio = tkinter.Button(root, text='Seleccionar direcctorio',command=direcctorio)
    botonDescargar = tkinter.Button(root, text='Descargar Video',command=descargarVideo, state=DISABLED)
    labelDirecctorio = tkinter.Label(root)

    #Ingresamos los objetos en la ventana
    labelImagen.pack()
    labelPresentacion.pack()
    labelUrl.pack()
    cajaUrl.pack()
    botonURL.pack()
    labelResolucion.pack()
    cajaResolucion.pack()
    botonDirectorio.pack()
    botonDescargar.pack()

    #Se ejecuta la ventana
    root.mainloop()










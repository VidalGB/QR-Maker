#inportaciones
import qrcode as QR
import sys
import os
from tkinter import *

def ruta_archivo(ruta):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, ruta)

#clase de la aplicacion
class AppQR():

	def __init__(self, ventana):
#		parametros de la ventana
		self.ventana = ventana
		self.ventana.title('QR Maker')
		file_path = ruta_archivo('./QR.png')
		self.ventana.iconphoto(False, PhotoImage(file = file_path))

#		Layout
		layout = LabelFrame(self.ventana, text = 'Create code QR')
		layout.grid(row = 0, column = 0, columnspan = 2, pady = 15)

#		contenido del QR
		Label(layout, text = 'QR content: ').grid(row = 1, column = 0)
		self.contenidoQR = Entry(layout)
		self.contenidoQR.focus()
		self.contenidoQR.grid(row = 1, column = 1)

#		nambre del archivo
		Label(layout, text = 'QR Name: ').grid(row = 2, column = 0)
		self.nombreQR = Entry(layout)
		self.nombreQR.grid(row = 2, column = 1)

#		text info
		self.info = Label(self.ventana,text = '', fg = 'red')
		self.info.grid(row = 1, column = 0, sticky = W + E)

#		boton crear
		Button(layout, text = 'Create', comman = self.crear).grid(row = 4, columnspan = 2, sticky = W + E)

#		imagen QR
		self.imagen = PhotoImage(file='')
		self.QR = Label(image = self.imagen)
		self.QR.grid(row = 2, column = 0)

#	validacion
	def validacion(self):
		return len(self.contenidoQR.get()) != 0 and len(self.nombreQR.get()) != 0

#	crear QR
	def crear(self):
		if self.validacion():
			imagen = QR.make(self.contenidoQR.get())
			archivo = open(self.nombreQR.get() + '.png', 'wb')
			imagen.save(archivo)
			archivo.close()
			self.imagen = PhotoImage(file=f'{self.nombreQR.get()}.png')
			self.QR['image'] = self.imagen
			if self.info['text'] != '':
				self.info['text'] = ''
		else:
			self.info['text'] = 'name of the QR and its information is required'

if __name__ == '__main__':
	ventana = Tk()
	AppQR(ventana)
	ventana.mainloop()
"""

Esta utilidad tiene como objetivo lograr
la creacion de Qr con el lenguaje python.

"""

import qrcode  # Importamos el modulo necesario para trabajar con codigos QR

imagen = qrcode.make("Mi texto aqui")  
	
archivo_imagen = open('Qr.png', 'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()
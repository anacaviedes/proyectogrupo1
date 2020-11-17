import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import introduce_clave as ic
import Funciones_de_emparejamiento_y_desemparejamiento as fe
import fun_esc_lec_2 as el

def iter(cadena,i,matriz):
    pf=[]
    f=open(cadena)
    Ca=f.read()
    cadena=fe.emparejada(el.escritura(Ca))
    for i in range(len(cadena)):
        p1 = matriz.dot(cadena[i])
        pf.append(str(int(p1[0])))
        pf.append(" ")
        pf.append(str(int(p1[1])))
        pf.append(" ")
    n = ""
    pf = n.join(pf)
    ar=r"Archivo_Encriptado"+str(i)+".txt"
    En=open(ar, "w")
    En.write(pf)
    return ar

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

    matriz = ic.clave()
    files=input("Ingrese las rutas de sus archivos : ")
    files=files.split(" ")

    for i in range(len(files)):
        base = MIMEBase('application', 'octet-stream')
        nombre=iter(files[i],i,matriz)
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
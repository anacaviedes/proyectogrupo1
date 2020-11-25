import Funciones_de_emparejamiento_y_desemparejamiento as fe
import fun_esc_lec_2 as el

def enc_ruta(cadena,i,matriz):
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
    ar=r"Archivo_Encriptado"+str(int(i))+".txt"
    En=open(ar, "w")
    En.write(pf)
    return ar
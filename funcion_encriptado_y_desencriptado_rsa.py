# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:08:53 2020

@author: ERICK
"""

import matplotlib.pyplot as plt
import numpy as np
import encriptado_y_desencriptado_rsa

def encriptado_imagen(direccion,n,e):
    im=plt.imread(direccion)
    im=im.copy()
    inf_extra = np.zeros((np.shape(im)[0], np.shape(im)[1], np.shape(im)[2],3),dtype=int)
    for i in range(np.shape(im)[0]):
        for j in range(np.shape(im)[1]):
            for k in range(np.shape(im)[2]):
                if im[i,j,k]== 255:
                    im[i,j,k]=254
                a = encriptado_y_desencriptado_rsa.encripta_rsa(im[i,j,k],n,e)
                im[i,j,k] = a[2]
                inf_extra[i, j, k, 0], inf_extra[i, j, k, 1], inf_extra[i, j, k, 2] = a[0], a[1], a[2]
    return(im, inf_extra)


def desencriptado_imagen(im,inf_extra,n,d):
    im=im.copy()
    for i in range(np.shape(im)[0]):
        for j in range(np.shape(im)[1]):
            for k in range(np.shape(im)[2]):
                im[i,j,k]=encriptado_y_desencriptado_rsa.desencripta_rsa(int(inf_extra[i, j, k][0]),int(inf_extra[i, j, k][1]),int(inf_extra[i, j, k][2]),n,d)
    return(im)
a=encriptado_imagen("C:\\Users\\ERICK\\Downloads\\SimpleBMP.bmp",109999,5)
plt.imshow(a[0])
plt.imshow()
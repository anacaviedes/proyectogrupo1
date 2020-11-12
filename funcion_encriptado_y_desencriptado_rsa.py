# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:08:53 2020

@author: ERICK
"""
import matplotlib.pyplot as plt
import numpy as np
import encriptado_y_desencriptado_rsa

def encriptado_imagen(direccion,n,e):
    im=imread(direccion)
    im=im.copy()
    inf_extra = np.ones((shape(im)[0], shape(im)[1], shape(im)[2],3),dtype=int)
    for i in range(shape(im)[0]):
        for j in range(shape(im)[1]):
            for k in range(shape(im)[2]):
                a = encriptado_y_desencriptado_rsa.encripta_rsa(im[i,j,k],n,e)
                if a[0] < 255:
                    im[i,j,k] = a[0]
                elif a[0] > 255:
                    im[i,j,k] = a[2]
                inf_extra[i, j, k, 0], inf_extra[i, j, k, 1], inf_extra[i, j, k, 2]= a[0], a[1], a[2]
    return(im, inf_extra)


def desencriptado_imagen(im,inf_extra,n,d):
    im=im.copy()
    for i in range(shape(im)[0]):
        for j in range(shape(im)[1]):
            for k in range(shape(im)[2]):
                p = encriptado_y_desencriptado_rsa.desencripta_rsa(inf_extra[i, j, k, 0], inf_extra[i, j, k, 1],inf_extra[i, j, k, 2], n, d)
                im[i, j, k] = p
    return(im)
#imshow(encriptado_imagen('',n,d)[0])
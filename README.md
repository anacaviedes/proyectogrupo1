# Proyecto Grupo 1
## Primera Entrega
El objetivo de este programa es ser utilizado para codificación, utilizando matrices y funciones de estas, como la inversa y el producto punto. 
El programa permite al usuario elegir entre codificar o decodificar un mensaje. Para codificar un mensaje de texto el usuario deberá ingresar cuatro números que representan la matriz con la que va a ser codificado el mensaje, en caso de que la matriz que ingrese el usuario no sea válida se le solicita que ingrese un conjunto nuevo de números,una vez haya sido infresada una matriz válida se le solicita al usuario ingresar el mensaje que desea codificar, a continuación el usuario recibirá el conjunto de números que representan su mensaje. Del mismo modo, para decodificar el mensaje, el usuario deberá ingresar los números que le fueron devueltos durante la codificación y la matriz con la que se codificó el mensaje, luego el usuario verá impreso en la pantalla, el mensaje original.
Este método de encriptación asigna, en principio, un número a cada caracter; pero en el mensaje codificado, a un mismo caracter pueden corresponderle diferentes números, lo que hace más compleja la tarea de desencriptado para una persona que no conozca la clave. 

## Segunda Entrega
- Se corrigió la función que asigna números a cada caracter.
- Se agregó la opción de encriptar archivos de texto.
- Se creó un nuevo algoritmo de ecriptación basado en el algoritmo RSA: consiste en la generación de una lista de números primos, la escogencia de dos de ellos al azar y su multiplicación. Este algoritmo arroja una clave pública y una clave privada. Además, los números encriptados se restringen al intervalo [0,255] para poder ser utilizados en encriptación de imágenes. Para esto se usa el residuo si el número encriptado es mayor que 255, por lo cual en la clave también se incluye este valor y el del cociente, con el fin de verificar el valor real.
- Se utilizó el algoritmo RSA mencionado para cambiar de color los pixeles de una imagen.
- Se creó otro algoritmo de encriptación y desencriptación de imágenes consistente en cambiar de lugar los pixeles.
- Se está trabajando en la interfaz de estos programas, para poder manipularlos con botones, subir archivos, etc.

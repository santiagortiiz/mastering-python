from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

class Album:

    fotos: Foto = []

    def agregar_foto(self, foto: Foto):
        self.fotos.append(foto)

    def remover_foto(self, nombre: str):
        for index, foto in enumerate(self.fotos):
            if foto.nombre == nombre:
                self.fotos.pop(index)

    def imprimir_nombres_fotos(self):
        for index, foto in enumerate(self.fotos):
            print(f'Foto {index+1}: {foto}')


class Foto:

    def __init__(self, nombre, ruta_archivo):
        self.nombre = nombre
        self.datos = np.load(ruta_archivo)

    def graficar(self):
        plt.imshow(self.datos)
        plt.show()

    def tomar_canal(self, canal):
        return self.datos[:,:,canal]

    def tomar_submatriz(self, n, pixel: tuple):
        if n < 1 and n%2!=0:
            raise Exception('n debe ser impar y mayor a 1')

        # k: pixeles a tomar a cada lado del objetivo
        k = (n-1)//2
        i, j = pixel
        x = self.datos[i-k:i+k+1, j-k:j+k+1]
        return x

    def difuminar_submatriz(submatriz):
        promedio = submatriz.mean()
        for i in range(submatriz.shape[0]):
            for j in range(submatriz.shape[1]):
                submatriz[i, j] = submatriz[i, j]*promedio

    def reemplazar_submatriz(self, submatriz, n, pixel: tuple):
        # k: pixeles a tomar a cada lado del objetivo
        k = (n-1)//2
        i, j = pixel
        self.datos[i-k:i+k+1, j-k:j+k+1] = submatriz

    def difuminar_pixel(self, pixel: tuple, n):
        submatriz = self.tomar_submatriz(n, pixel)
        self.difuminar_submatriz(submatriz)
        self.reemplazar_submatriz(submatriz, n, pixel)

    def difuminar(self, r1, r2, x0, y0, times, n):
        # Debe iterar sobre cada pixel que desee ser difuminado
        # con el metodo difuminar_pixel
        pass

    def pixelar(self):
        pass

    def __str__(self):
        return self.nombre


if __name__ == '__main__':

    # Punto 3
    # Crear album de fotos
    album = Album()

    # Cargar Foto 1
    file_name = 'jheyston_merry_christmas.npy'
    nombre_foto = 'jheyston_merry_christmas'
    foto = Foto(nombre_foto, file_name)
    foto.graficar()
    foto.difuminar()

    # Agregar foto 1 al album
    album.agregar_foto(foto)

    # Cargar Foto 2
    file_name_2 = 'jheyston_navidad.npy'
    nombre_foto_2 = 'jheyston_navidad'
    foto_2 = Foto(nombre_foto_2, file_name_2)

    # Agregar foto 2 al album
    album.agregar_foto(foto_2)

    # Ver nombres de las fotos del album
    print('Fotos existentes:')
    album.imprimir_nombres_fotos()

    # Remover la foto 2
    album.remover_foto(nombre_foto)
    print('Fotos restantes:')

    # Ver nombres de fotos restantes
    album.imprimir_nombres_fotos()

import numpy as np
import matplotlib.pyplot as plt

class Function:

    def __init__(self, x):
        self.x = x
        self.fx = self.Fx(self.x)

    def Fx(self, array):
        fx = np.sin(10*array)
        return fx

    @staticmethod
    def graficar(x, fx, title=None):
        plt.plot(x, fx)
        if title:
            plt.title(title)
        plt.show()

    def calcularMax(self):
        return max(self.fx)

    def calcularMin(self):
        return min(self.fx)

    def calcularMed(self):
        u = 0
        for i in self.fx:
            u += i
        u = u / len(self.x)
        return u

    def calcularVar(self):
        u = self.calcularMed()
        varianza = 0

        for i in self.fx:
            varianza  = varianza + (i - u)**2

        varianza = varianza/len(self.x)
        return varianza

    def calcularStd(self):
        std = self.calcularVar()
        std = np.sqrt(std)
        return std


class Transformaciones(Function):

    def Fx(self, array):
        fx = np.exp(-1*array)*np.sin(10*array)
        return fx

    def desplazamientoVertical(self, k=0): # OK
        fx = self.fx + k
        return fx

    def desplazamientoHorizontal(self, k=0):
        x = self.x + k
        fx = self.Fx(x)
        return fx

    def reflexionEjeX(self): # OK
        fx = -self.fx
        return fx

    def reflexionEjeY(self):
        fx = self.Fx(-self.x)
        return fx

    def expansión_contraccion_EjeX(self, k=1):
        x = self.x*k
        self.fx = self.Fx(x)

    def expansión_contraccion_EjeY(self, k=1): # OK
        self.fx = k*self.fx



if __name__ == '__main__':

    # Punto 1
    x = np.arange(-3, 3, 0.01)

    func = Function(x)
    fx = func.Fx(x)

    print(f'Max: {func.calcularMax()}')
    print(f'Min: {func.calcularMin()}')
    print(f'Med: {func.calcularMed()}')
    print(f'Varianza: {func.calcularVar()}')
    print(f'Std: {func.calcularStd()}')

    func.graficar(x, fx, 'np.sin(10*array)')

    # Punto 2
    x = np.arange(0, 10, 0.01)
    transf = Transformaciones(x)

    fx = transf.Fx(x)

    transf.graficar(transf.x, transf.fx, 'np.exp(-1*array)*np.sin(10*array)')

    # Desplazamientos
    fx_dezpl_vertical = transf.desplazamientoVertical(k=2)
    transf.graficar(transf.x, fx_dezpl_vertical, 'Desp vert k=2')
    fx_dezpl_horizontal = transf.desplazamientoHorizontal(k=-0.25)
    transf.graficar(transf.x, fx_dezpl_horizontal, 'Desp Horiz k=-0.25')

    # Reflexiones
    fx_ref_y = transf.reflexionEjeY()
    transf.graficar(transf.x, fx_ref_y, 'Reflexion Y')
    fx_ref_x = transf.reflexionEjeX()
    transf.graficar(transf.x, fx_ref_x, 'Reflexion X')

    # Expansiones
    transf.expansión_contraccion_EjeX(k=2)
    transf.graficar(transf.x, transf.fx, 'Contraccion Eje X, k=2')
    transf.expansión_contraccion_EjeX(k=0.5)
    transf.graficar(transf.x, transf.fx, 'Expansion Eje X, k=0.5')

    # Contracciones
    transf.expansión_contraccion_EjeY(k=0.1)
    transf.graficar(transf.x, transf.fx, 'Contraccion Eje Y, k=0.1')
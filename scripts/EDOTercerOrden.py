from scipy.integrate import odeint
from pylab import *            # para comandos de dibujo
def deriv(x,t):                # devuelve la derivada del array Y
    a = -2.017
    b = -1.
    return array([ x[1], x[2], a*x[2] + b*x[0] + x[1]*x[1] ])
    
nodos = linspace(10., 20., 1000)
x0 = array([ 1., 0.,  1. ])        # valores iniciales    
x  = odeint(deriv,x0,nodos)

figure()
plot(nodos,x[:,0])     # se trata de la primera columna de y
xlabel('t')
ylabel('x')
show()

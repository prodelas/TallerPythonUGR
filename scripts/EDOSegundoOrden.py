from scipy.integrate import odeint
from pylab import *        # para comandos de dibujo
def deriv(y,t):            # devuelve la derivada del array Y
    a = -2.
    b = -0.1
    return array([ y[1], a*y[0]+b*y[1] ])
    
nodos = linspace(1., 10., 1000)
y0 = array([ 10., -2. ])       # valores iniciales    
y  = odeint(deriv,y0,nodos)

figure()
plot(nodos,y[:,0])     # se trata de la primera columna de y
xlabel('t')
ylabel('y')
show()

from scipy.integrate import odeint
from pylab import *                     # para comandos de dibujo
def deriv(z,t):                          # devuelve la derivada del array Y
    a = -2.
    b = -0.1
    c = 3.
    return array([ z[1], a*z[2], z[3], b+c*z[1] ])
    
nodos = linspace(0., 10., 1000)
z0 = array([ 0.0005, 0.2 ,1., 2.])                               # valores iniciales    
z  = odeint(deriv,z0,nodos)


figure() 
plot(nodos,z[:,0],'-b')                  # se trata de x(t), la primera columna de z
xlabel('t')
ylabel('x(t)')
show()

figure() 
plot(nodos,z[:,2],'-g')                   # se trata de y(t), la tercera columna de z
xlabel('t')
ylabel('y(t)')
show()

figure() 
plot(nodos,z[:,0],'-b')                  # se trata de x(t), la primera columna de z
plot(nodos,z[:,2],'-g')                   # se trata de y(t), la tercera columna de z
xlabel('t')
ylabel('x(t) e y(t)')
show()
import math
import cmath

def Resultado_Coaxial(a,  b, f, sigma, Er, μr ):
    
    μo=4*3.1416*10**-7
    sigmao=5.8*10**7
    E=8.85*10**-12
    Rs=math.sqrt((3.1416*f*μo)/sigmao)
    R=(Rs/(2*3.1416))*((1/a)+(1/b))
    G= (sigma*(2*3.1416))/(math.log(b/a))
    C= (E*Er*(2*3.1416))/(math.log(b/a))
    L= (μo*μr/(2*3.1416))*math.log(b/a)
    w=2*3.1416*f
    
    return R, L, C, G, w

def Perdidas_Cable(R, L, C, G, l,w):
    
    y=cmath.sqrt((R+1j*w*L)*(G+1j*w*C))
    alfa=y.real*8.6858
    floss=alfa*l
    
    return alfa, floss


def Valores_a_Graficar(alfa,l):
    
    valores=[]
    i = 0.0
    
    while i < l-0.01:     
                                                               
        valores.append(alfa*i)
        i += 0.1
    
    valores.append(alfa*l)
        
    return valores
 
def Resultado_Fibra(n, c, e, J, a, L ):
    
    TA=((n*c)+(e*J)+(L*a)+(3))
    OA=a*L
    CA=n*c
    FA=e*J

    return TA, OA, CA, FA
from Modelos import Models
from fastapi import FastAPI
from Calculos_Valores import Calculos

app=FastAPI()

@app.post("/Coaxial/Calculos")
def Calculo_Coaxial( parametros : Models.Parametros_Coaxial):
    valores_graf=[]
    print(parametros.a, parametros.b,parametros.l, parametros.f, parametros.sigma, parametros.Er, parametros.μr)
    R,L,C,G,w= Calculos.Resultado_Coaxial(parametros.a, parametros.b, parametros.f, parametros.sigma, parametros.Er, parametros.μr)
    R=float("{:.3e}".format(R))
    L=float("{:.3e}".format(L))
    C=float("{:.3e}".format(C))
    G=float("{:.3e}".format(G))
    alfa, floss=Calculos.Perdidas_Cable(R,L,C,G,parametros.l,w)
    alfa=float("{:.3e}".format(alfa))
    floss=float("{:.3e}".format(floss))
    valores_graf=Calculos.Valores_a_Graficar(alfa, parametros.l)
    return {'R' : R, 'L' : L, 'G' : G, 'C' : C, 'alfa' : alfa, 'floss' : floss, 'Val_Graf' : valores_graf}

@app.post("/Fibra/Calculos")
def Calculo_Fibra( parametros : Models.Parametros_Fibra):
    
    print(parametros.n, parametros.c, parametros.e, parametros.J, parametros.A, parametros.L)
    TA, OA, CA, FA= Calculos.Resultado_Fibra(parametros.n, parametros.c, parametros.e, parametros.J, parametros.A, parametros.L)
    TA=float("{:.3e}".format(TA))
    OA=float("{:.3e}".format(OA))
    CA=float("{:.3e}".format(CA))
    FA=float("{:.3e}".format(FA))
    
    return {'TA': TA, 'OA': OA, 'CA': CA, 'FA': FA}







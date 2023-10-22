from Modelos import Models
from fastapi import FastAPI
from Calculos_Valores import Calculos

app=FastAPI()

@app.post("/Coaxial/Calculos")
def Calculo_Coaxial( parametros : Models.Parametros):
    valores_graf=[]
    print(parametros.a, parametros.b,parametros.l, parametros.f, parametros.sigma, parametros.Er, parametros.μr)
    R,L,C,G,w= Calculos.Resultado_Coaxial(parametros.a, parametros.b, parametros.f, parametros.sigma, parametros.Er, parametros.μr)
    alfa, floss=Calculos.Perdidas_Cable(R,L,C,G,parametros.l,w)
    valores_graf=Calculos.Valores_a_Graficar(alfa, parametros.l)
    return {'R' : R, 'L' : L, 'G' : G, 'C' : C, 'alfa' : alfa, 'floss' : floss, 'Val_Graf' : valores_graf}







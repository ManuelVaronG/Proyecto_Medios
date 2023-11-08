from pydantic import BaseModel
from typing import Optional

class Parametros_Coaxial(BaseModel):
    
    a : float
    b : float
    l : float
    f : float
    sigma : Optional[float] = 0
    Er : Optional[float] = 1
    μr : Optional[float] = 1
   
class Parametros_Fibra(BaseModel):
 
    n : float
    c : float
    e : float
    J : float
    A : float
    L : float
    
    
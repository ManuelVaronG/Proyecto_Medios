from pydantic import BaseModel
from typing import Optional

class Parametros(BaseModel):
    
    a : float
    b : float
    l : float
    f : float
    sigma : Optional[float] = 0
    Er : Optional[float] = 1
    μr : Optional[float] = 1
    
    
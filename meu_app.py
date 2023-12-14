from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

class CalculadoraService:
    @staticmethod
    def somar(a: int, b: int) -> int:
        return a + b

@app.get("/somar/{a}/{b}")
def somar(a: int, b: int, service: CalculadoraService = Depends()):
    try:
        # Verifique se a e b são inteiros
        resultado = service.somar(int(a), int(b))
        return {"resultado": resultado}
    except ValueError:
        raise HTTPException(status_code=422, detail="Parâmetros inválidos. Certifique-se de que ambos são números inteiros.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

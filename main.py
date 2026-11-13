
from fastapi import FastAPI

from database import Base, engine
from tags import tags_metadata

from routers import plataformas, jogos, avaliacoes

# Criar as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

# Configuração da API
app = FastAPI(
    title="API Loja de Games",
    description="API para gerenciamento de plataformas, jogos e avaliações.",
    version="1.0.0",
    openapi_tags=tags_metadata
)

# Registrar as rotas
app.include_router(plataformas.router)
app.include_router(jogos.router)
app.include_router(avaliacoes.router)


@app.get("/")
def inicio():
    return {
        "mensagem": "API da Loja de Games funcionando!"
    }

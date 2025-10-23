from fastapi import FastAPI, HTTPException
from datetime import date, datetime
from sqlalchemy import select, insert, update, delete
from database import engine, usuarios, LGPD

colunas = [
    "id",
    "nome",
    "cpf",
    "email",
    "telefone",
    "data_nascimento",
    "created_on",
    "updated_on"
]

app = FastAPI(title="Fatec - CRUD com FastAPI e PostgreSQL")

@app.get("/")
def home():
    """Rota inicial da API."""
    return {
        "mensagem": "API de Usuários - Fatec Rio Claro",
        "descricao": "Bem-vindo(a)! Esta API demonstra um CRUD completo com FastAPI e PostgreSQL.",
        "endpoints_disponiveis": {
            "Listar usuários": "GET /usuarios",
            "Buscar usuário por ID": "GET /usuarios/{user_id}",
            "Criar usuário": "POST /usuarios",
            "Atualizar usuário": "PUT /usuarios/{user_id}",
            "Deletar usuário": "DELETE /usuarios/{user_id}"
        },
        "autor": "Orlando Saraiva Jr",
        "versao": "1.0.0"
    }
    
@app.post("/usuarios")
def criar_usuario(nome: str, cpf: str, email: str, telefone: str, data_nascimento: date):
    """ Criar um novo usuário."""
    with engine.connect() as conn:
        stmt = insert(usuarios).values(
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone,
            data_nascimento=data_nascimento,
            created_on=datetime.now(),
            updated_on=datetime.now()
        )
        result = conn.execute(stmt)
        conn.commit()
        return {"id": result.inserted_primary_key[0], "mensagem": "Usuário criado com sucesso!"}

@app.get("/usuarios")
def listar_usuarios():
    """Lista todos os usuários aplicando a função LGPD a cada registro."""
    lista_usuarios = []

    with engine.connect() as conn:
        consulta = select(usuarios)
        resultado = conn.execute(consulta).fetchall()

        for linha in resultado:
            linha = LGPD(linha)
            usuario_dict = dict(zip(colunas, linha))
            lista_usuarios.append(usuario_dict )
    return lista_usuarios


@app.get("/usuarios/{user_id}")
def buscar_usuario(user_id: int):
    """ Buscar um usuário pelo ID."""
    with engine.connect() as conn:
        stmt = select(usuarios).where(usuarios.c.id == user_id)
        result = conn.execute(stmt).fetchone()
        if result is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        result = LGPD(result)
        usuario_dict = dict(zip(colunas, result))
        return usuario_dict


@app.put("/usuarios/{user_id}")
def atualizar_usuario(user_id: int, nome: str = None, telefone: str = None):
    """ Atualizar o usuário pelo ID."""
    with engine.connect() as conn:
        stmt = select(usuarios).where(usuarios.c.id == user_id)
        result = conn.execute(stmt).fetchone()
        if not result:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        stmt_update = (
            update(usuarios)
            .where(usuarios.c.id == user_id)
            .values(
                nome=nome or result.nome,
                telefone=telefone or result.telefone,
                updated_on=datetime.now()
            )
        )
        conn.execute(stmt_update)
        conn.commit()
        return {"mensagem": "Usuário atualizado com sucesso!"}


@app.delete("/usuarios/{user_id}")
def deletar_usuario(user_id: int):
    """ Remover usuário."""
    with engine.connect() as conn:
        stmt = delete(usuarios).where(usuarios.c.id == user_id)
        result = conn.execute(stmt)
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return {"mensagem": "Usuário removido com sucesso!"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
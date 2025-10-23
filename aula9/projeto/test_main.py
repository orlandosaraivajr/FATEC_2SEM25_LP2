import requests
from datetime import date

# Base URL da API (ajuste a porta se necessário)
BASE_URL = "http://127.0.0.1:8000"

# ---------------------------
# Testar criação de usuário (POST)
# ---------------------------
novo_usuario = {
    "nome": "João Silva",
    "cpf": "123.456.789-00",
    "email": "joao@example.com",
    "telefone": "11988887777",
    "data_nascimento": "1990-05-15"
}

print("\n=== Criando usuário ===")
response = requests.post(f"{BASE_URL}/usuarios", params=novo_usuario)
print("Status:", response.status_code)
print("Resposta:", response.json())

# Guardar o ID para os próximos testes
if response.status_code == 200:
    user_id = response.json().get("id")
else:
    user_id = None

# ---------------------------
# Listar todos os usuários (GET)
# ---------------------------
print("\n=== Listando todos os usuários ===")
response = requests.get(f"{BASE_URL}/usuarios")
print("Status:", response.status_code)
print("Resposta:", response.json())

# ---------------------------
# Buscar usuário por ID (GET)
# ---------------------------
if user_id:
    print(f"\n=== Buscando usuário ID {user_id} ===")
    response = requests.get(f"{BASE_URL}/usuarios/{user_id}")
    print("Status:", response.status_code)
    print("Resposta:", response.json())

# ---------------------------
# Atualizar usuário (PUT)
# ---------------------------
if user_id:
    print(f"\n=== Atualizando usuário ID {user_id} ===")
    novos_dados = {
        "nome": "João Atualizado",
        "telefone": "11999998888"
    }
    response = requests.put(f"{BASE_URL}/usuarios/{user_id}", params=novos_dados)
    print("Status:", response.status_code)
    print("Resposta:", response.json())

# ---------------------------
# Deletar usuário (DELETE)
# ---------------------------
if user_id:
    print(f"\n=== Deletando usuário ID {user_id} ===")
    response = requests.delete(f"{BASE_URL}/usuarios/{user_id}")
    print("Status:", response.status_code)
    print("Resposta:", response.json())

# ---------------------------
# Tentar buscar novamente (deve retornar 404)
# ---------------------------
if user_id:
    print(f"\n=== Verificando se o usuário foi realmente deletado ===")
    response = requests.get(f"{BASE_URL}/usuarios/{user_id}")
    print("Status:", response.status_code)
    print("Resposta:", response.json())

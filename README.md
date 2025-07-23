# 🏋️ WorkoutAPI

Uma API RESTful para gerenciamento de atletas, categorias e centros de treinamento. Desenvolvida com FastAPI, SQLAlchemy Async e Pydantic v2.

---

## 📚 Tecnologias Utilizadas

- **FastAPI** – Framework web moderno e de alta performance
- **SQLAlchemy Async** – ORM com suporte a operações assíncronas
- **Pydantic v2** – Validação e tipagem de dados com performance
- **Uvicorn** – Servidor ASGI leve e rápido

---

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/workoutapi.git
cd workoutapi

# Crie e ative o ambiente virtual
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor localmente (utilizando Makefile)
make run
```

---

## 🔄 Endpoints Disponíveis

### 👤 Atletas

| Método | Rota               | Descrição                            |
|--------|--------------------|--------------------------------------|
| GET    | `/atletas/`        | Lista todos os atletas               |
| GET    | `/atletas/{id}`    | Retorna um atleta pelo ID            |
| POST   | `/atletas/`        | Cria um novo atleta                  |
| PATCH  | `/atletas/{id}`    | Atualiza um atleta                   |
| DELETE | `/atletas/{id}`    | Deleta um atleta                     |

### 🏷️ Categorias

| Método | Rota                | Descrição                             |
|--------|---------------------|---------------------------------------|
| GET    | `/categoria/`       | Lista todas as categorias             |
| GET    | `/categoria/{id}`   | Retorna uma categoria pelo ID         |
| POST   | `/categoria/`       | Cria uma nova categoria               |

### 🏫 Centros de Treinamento

| Método | Rota                        | Descrição                                 |
|--------|-----------------------------|-------------------------------------------|
| GET    | `/centro_treinamento/`      | Lista todos os centros de treinamento     |
| GET    | `/centro_treinamento/{id}`  | Retorna um centro de treinamento pelo ID  |
| POST   | `/centro_treinamento/`      | Cria um novo centro de treinamento        |

---

## 🧾 Exemplo de Payload (Atleta)

```json
{
  "nome": "João Silva",
  "idade": 22,
  "categoria_id": "c540e48e-30b1-4c41-9aa1-562a70f62463",
  "centro_treinamento_id": "a123e48e-30b1-4c41-9aa1-562a70f65432"
}

```
---

## 💡 Funcionalidades Futuras

- [ ] Filtros por query parameters (ex: nome, CPF)
- [ ] Paginação com FastAPI Pagination (limit e offset)
- [ ] Customização de respostas dos endpoints (ex: retornar nome da categoria e centro)
- [ ] Tratamento de exceções de integridade (ex: CPF duplicado com mensagem personalizada)

---

## 🤝 Contribuições

Contribuições são sempre bem-vindas!

Se quiser melhorar algo, siga estes passos:

1. Fork este repositório
2. Crie sua branch (`git checkout -b feature/sua-feature`)
3. Faça o commit (`git commit -m 'feat: nova funcionalidade'`)
4. Envie para o GitHub (`git push origin feature/sua-feature`)
5. Abra um Pull Request

Se preferir, abra uma **issue** para discutir ideias, bugs ou sugestões!

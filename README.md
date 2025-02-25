# Tornado API

Este projeto é uma API desenvolvida em Python usando o framework Tornado. Ele fornece endpoints para verificar o status da aplicação, calcular o Total de Pagamentos Válidos (TPV) e buscar transações por data.

## Sumário

- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Executando o Projeto](#executando-o-projeto)
- [Endpoints da API](#endpoints-da-api)
- [Exemplos de Requisições](#exemplos-de-requisições)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)

## Requisitos

- Python 3.7 ou superior
- MongoDB (local ou remoto)
- Bibliotecas Python listadas em `requirements.txt`

## Instalação

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\ctivate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
MONGODB_URI=mongodb://localhost:27017/
DATABASE_NAME=teste-databuild
```

- `MONGODB_URI`: URI de conexão com o MongoDB.
- `DATABASE_NAME`: Nome do banco de dados.

Certifique-se de que o MongoDB está em execução.

## Executando o Projeto

Inicie o servidor:

```bash
python run.py
```

A API estará disponível em:

```
http://localhost:8888
```

## Endpoints da API

### 1. Verificar status da aplicação

- **Método:** GET
- **Endpoint:** `/alive`
- **Descrição:** Verifica se a aplicação está funcionando.

**Exemplo de resposta:**

```json
{
  "status": "OK"
}
```

### 2. Calcular TPV (Total de Pagamentos Válidos)

- **Método:** GET
- **Endpoint:** `/read_tpv`
- **Descrição:** Calcula o Total de Pagamentos Válidos (TPV) a partir das transações no banco de dados.

**Exemplo de resposta:**

```json
{
  "TPV": 1500.75
}
```

### 3. Buscar transações por data

- **Método:** GET
- **Endpoint:** `/transactions_by_data`
- **Parâmetros:**
  - `initial_datetime`: Data inicial no formato `dd/mm/YYYY HH:MM:SS`.
  - `final_datetime`: Data final no formato `dd/mm/YYYY HH:MM:SS`.
  - `page`: Número da página (começa em 1).
  - `per_page`: Número de itens por página.

**Exemplo de resposta:**

```json
{
  "data": [
    {
      "_id": "653b8f1e4f1a2b3c4d5e6f7a",
      "amount": 100.50,
      "original_amount": 100.00,
      "fees": 0.50,
      "datahora_salvamento_dt": "15/10/2023 14:30:00",
      "datahora_salvamento_timestamp": 1697293800,
      "created_at_dt": "15/10/2023 14:30:00",
      "updated_at_dt": "15/10/2023 14:30:00"
    }
  ],
  "actual_page": 1,
  "total_pages": 5,
  "total_items": 10
}
```

## Exemplos de Requisições

### 1. Verificar status da aplicação

```bash
curl http://localhost:8888/alive
```

### 2. Calcular TPV

```bash
curl http://localhost:8888/read_tpv
```

### 3. Buscar transações por data

```bash
curl "http://localhost:8888/transactions_by_data?initial_datetime=01/10/2023 00:00:00&final_datetime=31/10/2023 23:59:59&page=1&per_page=10"
```

## Estrutura do Projeto

```
projeto/
│
├── .env
├── logging_setup.py
├── db_connection.py
├── run.py
├── requirements.txt
├── app/
│   ├── handler/
│   │   ├── alive.py
│   │   ├── home.py
│   │   ├── read_tpv.py
│   │   └── transactionsbydata.py
│   └── ...
└── logs/
    ├── run.log
    ├── alive.log
    ├── read_tpv.log
    └── transactions_by_data.log
```

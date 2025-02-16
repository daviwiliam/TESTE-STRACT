# API de Relatórios de Contas de Anúncio

Esta é uma API desenvolvida em **Python + Flask** que consome dados de uma API externa e gera relatórios em formato **CSV** sobre contas de anúncio de clientes fictícios.

## 🚀 **Funcionalidades**
- Consulta de plataformas disponíveis
- Listagem de contas e insights de anúncios
- Geração de relatórios detalhados e resumidos
- Exportação de dados em formato CSV

## 🛠 **Pré-requisitos**
- Python 3.8+
- `pip` instalado

## 💻 **Instalação e Execução**

### 1️⃣ Clonar o repositório:
```bash
git clone https://github.com/daviwiliam/TESTE-STRACT.git
cd TESTE-STRACT
```

### 2️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar dependências:
```bash
pip install -r requirements.txt
```

### 5️⃣ Executar o servidor:
```bash
flask run
```

A API rodará em `http://127.0.0.1:5000/`.

---

## 📌 **Endpoints Disponíveis**

### 🔹 **1. Informações do Desenvolvedor**
```http
GET /
```
**Retorno:**
```json
{
  "name": "Davi Wiliam",
  "email": "daviwil42@gmail.com",
  "linkedin": "https://linkedin.com/in/daviwiliam"
}
```

### 🔹 **2. Relatório por Plataforma**
```http
GET /{plataforma}
```
**Descrição:** Retorna todos os anúncios de uma plataforma específica.

### 🔹 **3. Resumo por Plataforma**
```http
GET /{plataforma}/resumo
```
**Descrição:** Retorna um resumo consolidado por conta.

### 🔹 **4. Relatório Geral**
```http
GET /geral
```
**Descrição:** Retorna todos os anúncios de todas as plataformas.

### 🔹 **5. Resumo Geral**
```http
GET /geral/resumo
```
**Descrição:** Retorna um resumo consolidado por plataforma.

### 🔹 **5. Plataformas disponíveis para utilizar como parâmetro na requisição**
```
meta_ads
```
```
ga4
```
```
tiktok_insights
```
---

A API estará acessível em `http://127.0.0.1:5000/`.

---

## 📜 **Licença**
Este projeto está sob a licença MIT. Sinta-se à vontade para utilizar e modificar conforme necessário!

## 👨‍💻 **Autor**
Desenvolvido por **[Davi Wiliam](https://linkedin.com/in/daviwiliam)** 🚀


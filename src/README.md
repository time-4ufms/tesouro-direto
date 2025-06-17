
# 📦 Coleta e Processamento de Dados do Tesouro Direto

Este projeto tem como objetivo automatizar o download, extração e conversão dos dados públicos de investidores do Tesouro Direto, disponibilizados pelo Tesouro Nacional.

O script realiza:
1. Download do arquivo `.gz` disponibilizado pelo Tesouro.
2. Extração do arquivo para `.csv`.
3. Conversão do `.csv` para formato `.parquet`.
4. Salvamento dos dados na pasta `./data`.

---

## 🚀 Pré-requisitos

- Python 3.9 ou superior instalado.
- Git instalado.
- Curl e gunzip instalados no sistema (geralmente já disponíveis em sistemas Linux e Mac. Para Windows, use WSL, Git Bash ou instale manualmente).

---

## 🛠️ Passo a passo para executar

### 1️⃣ Clone o repositório

```bash
git clone <URL-DO-SEU-REPOSITORIO>
cd <NOME-DA-PASTA>
```

### 2️⃣ Crie e ative um ambiente virtual

```bash
# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente (Linux/Mac)
source .venv/bin/activate

# Ative o ambiente (Windows)
.venv\Scripts\activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

**Se você não tiver um `requirements.txt`, você pode instalar manualmente:**

```bash
pip install pandas pyarrow
```

> Obs: O pacote `pyarrow` é necessário para manipular arquivos no formato `.parquet`.  
> Alternativamente, você pode usar `fastparquet` se desejar.

---

## 📥 Executando o script

```bash
python extracao_dados.py
```

O script irá:

- Criar automaticamente a pasta `./data` (caso não exista).
- Fazer o download do arquivo `.gz` diretamente do Tesouro Nacional.
- Descompactar o arquivo para `.csv`.
- Ler o arquivo `.csv` e converter para `.parquet`.
- Salvar o arquivo `investidorestesourodireto.parquet` dentro da pasta `./data`.

O arquivo CSV intermediário não é mantido após a conversão (pode ser adicionado esse comportamento no script, se desejar).

---

## 📂 Estrutura de pastas gerada

```
.
├── extracao_dados.py
├── README.md
├── requirements.txt
└── data
    └── investidorestesourodireto.parquet
```

---

## 🔗 Fonte dos dados

Os dados são públicos e podem ser acessados diretamente pelo portal:

- [Tesouro Transparente - Investidores do Tesouro Direto](https://www.tesourotransparente.gov.br/ckan/dataset/investidores-do-tesouro-direto)

---

## 🧠 Observações importantes

- O arquivo pode ser atualizado periodicamente pelo Tesouro Nacional. Portanto, executar novamente este script garantirá que você tenha sempre a versão mais recente.
- O formato `.parquet` é otimizado para análise de dados, sendo mais eficiente em termos de espaço e velocidade de leitura, especialmente com grandes volumes de dados.

---

## 👨‍💻 Dependências principais

- pandas
- pyarrow ou fastparquet
- curl e gunzip (ferramentas de sistema)

---

## 🏗️ Melhorias futuras (sugestões)

- Adicionar verificação de integridade do arquivo baixado.
- Automatizar a remoção do CSV após conversão para parquet.
- Adicionar logging estruturado.
- Adicionar interface CLI.

---

## 📜 Licença

Este projeto utiliza dados públicos de acordo com as diretrizes do Tesouro Nacional. O código é distribuído sob a licença MIT.

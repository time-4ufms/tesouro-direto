import os
import pandas as pd

# Link do arquivo
url = "https://www.tesourotransparente.gov.br/ckan/dataset/48a7fd9d-78e5-43cb-bcba-6e7dcaf2d741/resource/bc99d7cc-e658-4b65-950e-cbf4bb5ed6d2/download/investidorestesourodireto.gz"

# Cria a pasta 'data' se não existir
os.makedirs('data', exist_ok=True)

# # 📥 Fazendo download do arquivo para a pasta data
gz_path = os.path.join('data', 'investidorestesourodireto.gz')
csv_path = os.path.join('data', 'investidorestesourodireto.csv')
parquet_path = os.path.join('data', 'investidorestesourodireto.parquet')

print("🔽 Fazendo download...")
os.system(f'curl -L "{url}" -o {gz_path}')

# Descompactando para CSV dentro da pasta data
print("📦 Descompactando o arquivo...")
os.system(f'gunzip -c {gz_path} > {csv_path}')

# Lendo CSV e convertendo
print("📊 Lendo CSV e convertendo para Parquet...")
df = pd.read_csv(csv_path, sep=';', encoding='latin1')

df.to_parquet(parquet_path, index=False)

print(f"✅ Processo finalizado. Arquivo salvo em {parquet_path}")

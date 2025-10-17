import json
import gspread
from google.oauth2.service_account import Credentials

# Leer JSON de forma segura
with open('gsa_json.json') as f:
    gsa_creds = json.load(f)

creds = Credentials.from_service_account_info(gsa_creds)
gc = gspread.authorize(creds)

# Abrir Google Sheet
sheet = gc.open("MiHojaDePrueba").sheet1

# Añadir fila de prueba
sheet.append_row(["🚀 Iniciando scraper de prueba..."])

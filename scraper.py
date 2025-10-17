import gspread
from google.oauth2.service_account import Credentials

print("🚀 Iniciando scraper de prueba...")

creds = Credentials.from_service_account_info(
    eval(open('gsa_json.json').read()),
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)

gc = gspread.authorize(creds)

SHEET_URL = "https://docs.google.com/spreadsheets/d/XXXXXXXXXXXX/edit"  # <--- tu hoja
sh = gc.open_by_url(SHEET_URL)
worksheet = sh.worksheet("results")

worksheet.append_row(["🏡 Test automático", "https://ejemplo.com", "500000", "6", "6", "Olot", "GitHub"])
print("✅ Fila añadida correctamente desde GitHub Actions")

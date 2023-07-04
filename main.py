from pix_utils import Code
import qrcode
import os

KEY = '+5551998409482'  # Chave PIX.
NAME = 'Teste'  # Nome do dono do PIX.
CITY = 'Eldorado Do Sul'  # Cidade do dono do PIX. Lembre-se de não usar acentos.
VALUE = 10.00  # Valor da transação.
IDENTIFY = ''  # Identificador da transação (opcional).

# Crie a instância do objeto Code
code = Code(key=KEY, name=NAME, city=CITY, value=VALUE, identifier=IDENTIFY)

# Imprima o código PIX
print(code)

# Crie uma string formatada com os dados do PIX
pix_data = str(code)

# Crie o objeto QRCode com os dados do PIX
qrcode_img = qrcode.make(pix_data)

# Determine o caminho completo do diretório do desktop
desktop_path = os.path.expanduser("~/Desktop")

# Crie o diretório de destino se não existir
os.makedirs(desktop_path, exist_ok=True)

# Determine o caminho completo do arquivo no desktop
file_path = os.path.join(desktop_path, "QRCODE.png")

# Salve a imagem do código QR no desktop
qrcode_img.save(file_path, format="PNG")

print(f"A imagem do código QR foi salva em {file_path}")

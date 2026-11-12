import secrets

# Gerar 16 bytes = 128 bits em formato Hexadecimal
chave_hex = secrets.token_hex(16)

# Gerar 16 bytes = 128 bits em formato URL-Safe Base64
chave_base64 = secrets.token_urlsafe(16)

print(f"Chave Hex (128 bits): {chave_hex}")
print(f"Chave Base64 (128 bits): {chave_base64}")

import secrets

numero = secrets.choice(range(0, 100))
print(numero)

print(secrets.token_bytes(10))
print(secrets.token_hex(10))
print(secrets.token_urlsafe(10))
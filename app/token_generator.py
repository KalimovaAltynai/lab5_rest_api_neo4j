import secrets

token = secrets.token_hex(16)  # Генерация токена длиной 16 байт (32 символа)
print(f"Сгенерированный токен: {token}")

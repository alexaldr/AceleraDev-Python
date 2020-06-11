import jwt


def create_token(data, secret):
    return jwt.encode(data, secret, 'HS256')


def verify_signature(token):
    try:
        return jwt.decode(token, 'acelera')
    except Exception:
        return {"error": 2}


token = create_token({"language": "Python"}, 'acelera')
print(token)

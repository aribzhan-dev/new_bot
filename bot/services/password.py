import secrets

util = 'qwertyuiopasdfghjkl;zxcvbnm,.1234567890-_!@#$%^&*+='


def generate_password(length: int = 8) -> str:
    if length < 8:
        length = 8
    return "".join(secrets.choice(util) for _ in range(length))



import uuid

def hash_password(password: str) -> str:
    uuid.uuid3(uuid.NAMESPACE_DNS, password)
    print(str(uuid.uuid3(uuid.NAMESPACE_DNS, password)))
    return str(uuid.uuid3(uuid.NAMESPACE_DNS, password))
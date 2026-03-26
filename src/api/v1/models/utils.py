import uuid


def generate_reference() -> str:
    return f"PAY-{uuid.uuid4().hex[:10].upper()}"


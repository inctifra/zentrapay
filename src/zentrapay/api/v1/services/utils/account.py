import random
import string


def luhn_checksum(number: str) -> int:
    digits = [int(d) for d in number]
    odd_sum = sum(digits[-1::-2])
    even_sum = sum(sum(divmod(2 * d, 10)) for d in digits[-2::-2])
    return (odd_sum + even_sum) % 10


def generate_account_number_with_checksum(prefix="01", length=10) -> str:
    body_length = length - len(prefix) - 1  # reserve 1 for checksum

    body = "".join(random.choices(string.digits, k=body_length))
    partial = prefix + body

    checksum = luhn_checksum(partial)
    return f"{partial}{checksum}"



def generate_swift_code(country_code="KE") -> str:
    bank_code = "".join(random.choices(string.ascii_uppercase, k=4))
    location_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=2))
    branch_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=3))

    return f"{bank_code}{country_code}{location_code}{branch_code}"
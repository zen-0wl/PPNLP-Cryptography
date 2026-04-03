def bytes_to_hex(data: bytes):
    return data.hex()


def hex_to_bytes(data: str):
    return bytes.fromhex(data)
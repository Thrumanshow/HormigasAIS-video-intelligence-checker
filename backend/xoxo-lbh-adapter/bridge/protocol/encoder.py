# bridge/protocol/encoder.py
def encode_packet(header: str, type_code: str, payload: str) -> str:
    """Motor de codificación LBH-Lite para HormigasAIS."""
    payload_hex = payload.encode('utf-8').hex()
    length = format(len(payload_hex) // 2, '08x')
    return f"{header}{type_code}{length}{payload_hex}"

def decode_lbh_packet(frame: str) -> dict:
    """Motor de decodificación LBH-Lite."""
    try:
        header = frame[0:8]
        type_code = frame[8:16]
        length = int(frame[16:24], 16)
        payload_hex = frame[24:]
        payload = bytes.fromhex(payload_hex).decode('utf-8')
        return {"header": header, "type_code": type_code, "payload": payload}
    except Exception as e:
        return {"error": str(e)}

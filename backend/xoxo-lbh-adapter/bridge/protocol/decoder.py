# bridge/protocol/decoder.py
import json

def decode_lbh_packet(frame: str) -> dict:
    """Motor de decodificación LBH-Lite."""
    try:
        # Estructura: [HEADER 8][TYPE 8][LENGTH 8][PAYLOAD...]
        header = frame[0:8]
        type_code = frame[8:16]
        length_hex = frame[16:24]
        payload_hex = frame[24:]
        
        # Convertir de Hexadecimal a String UTF-8
        payload = bytes.fromhex(payload_hex).decode('utf-8')
        
        return {
            "header": header,
            "type_code": type_code,
            "payload": payload,
            "length": int(length_hex, 16)
        }
    except Exception as e:
        print(f"[decoder] Error decodificando frame: {e}")
        return {"error": str(e)}

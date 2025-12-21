import os
import glob

def decodificar_ultimo_log():
    # Buscamos el archivo más reciente en logs_binarios
    lista_archivos = glob.glob('logs_binarios/*.lbh')
    if not lista_archivos:
        print("❌ No se encontraron archivos .lbh")
        return

    ultimo_archivo = max(lista_archivos, key=os.path.getmtime)
    print(f"🔍 Analizando: {ultimo_archivo}")

    with open(ultimo_archivo, 'r') as f:
        hex_data = f.read()

    # Extraemos las partes según el protocolo LBH
    header = hex_data[0:8]
    tipo = hex_data[8:16]
    longitud = hex_data[16:24]
    payload_hex = hex_data[24:]

    # Traducimos el payload de Hex a Texto
    try:
        payload_texto = bytes.fromhex(payload_hex).decode('utf-8')
    except:
        payload_texto = "Contenido binario no legible"

    print("-" * 30)
    print(f"🐜 SISTEMA HORMIGAS AIS - DECODER")
    print("-" * 30)
    print(f"🆔 Header LBH:  {header} (ORIGEN VÁLIDO)")
    print(f"📡 Tipo Msg:    {tipo} (ACCIÓN)")
    print(f"📦 Payload:     {payload_texto}")
    print("-" * 30)

if __name__ == "__main__":
    decodificar_ultimo_log()

import base64, marshal, zlib, os, sys
_EXP = "utils.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("441a89b354753e0f57a28b0c094daa0bbbb246c5cf168d9e0803564e9aa006e5")
_K2 = bytes.fromhex("833c87b568f881df1ad69d4eaea40a6129d360c774ca99eacd8f42b210d35de4")
_K3 = bytes.fromhex("879f99457327d3063eb46d0580dc45922f5b0df5330ff3b3770d44945bf8fe4e")
_S = """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"""
try:
    _raw = base64.b64decode(_S)
    _dec = bytearray(len(_raw))
    for i, _b in enumerate(_raw):
        if i % 3 == 0:
            _dec[i] = _b ^ _K1[i % len(_K1)]
        elif i % 3 == 1:
            _dec[i] = _b ^ _K2[i % len(_K2)]
        else:
            _dec[i] = _b ^ _K3[i % len(_K3)]
    _code = marshal.loads(zlib.decompress(bytes(_dec)))
    exec(_code)
except Exception as _e:
    print(f"[ERR] Dekripsi gagal: {_e}")
    sys.exit(1)

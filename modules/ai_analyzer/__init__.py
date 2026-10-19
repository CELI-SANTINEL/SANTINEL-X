# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("9cae592575333f61a2ed01e5df82a3451fbb7557f8e0f05b7cb1730b9906e307c43598991b9f3fbe055a4eee3eca316dffb8d39e383305b6e541747ec478282d")
_K2 = bytes.fromhex("0d549a53731f3e781c3bf5b7d41322654b00d9c4056338d79966adc694c1099a2c13e69f567dab3d414161a653191192606496efff521acbfdfa4f0817914c70")
_K3 = bytes.fromhex("6fa274365ffbefcb39cff20d1e8b19c5b593f3977609473c8383bbb8afedd18fab514fad215895bcb799d6d7dbc36e2566cf4997f5fb2062d69cf68334d642bc")
_S = """hJySi8P#HfeJUN#eR`0Gu}+U*f6+$ZV#b|$Fq8gq(CDT8HYS~CVHlg}J=19I#<n=Y=QOt(WSUjruR}zK
nmn5#TV?KK-U*Q"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

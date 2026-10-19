# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("9f4a5ac439d5fe2d0ebd79bdc47d78174d81a8a30ff09c8d3effacaed6d8c9206894073eb8f1ed7341d6f271059c2daf49a1eb7eed3045559a60ccaefd820c11")
_K2 = bytes.fromhex("acf7a522bf978cc07dafc1570396f8bc9c7a7cdc3e941d2865dd26b0a565161a10a39b6b454f1d11e2cc422742e824471375281ab92190b0b0f4cd5a6bd46a77")
_K3 = bytes.fromhex("7666f65b02bb3344a1300e8e0347eb6b04b05ff409211dfde1aa1ff4def49fc2bd1cd78974e58bd716dca18de9aea650e64a4ffe7dda097f37961c9b679ebcb2")
_S = """Jpn@7#QV+pC=spntjuGgg)Lj}%pO$;z8Y=jKk$W{R<z%W)5quSCtP!^B^im2gFCpr{AE<1x4(sYxwN>l
A-^TxhD$*oi!vb"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

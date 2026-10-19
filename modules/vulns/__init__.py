# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("6f33c821c1a578cc2ee439a2bc5005e2f592ad34961eb6bd30b9d4c41021bddcf76d7dc0b7972ad28ece3296c111cc3fa21de7b7cd7fa5ef2ac859cb9829b2db")
_K2 = bytes.fromhex("b6d436b80e923cf58e19ce52f6caab9843b74d621f2006620adc182f08f2c325fd651c744a6504af849d0705b72c2fd285cdf14c50e2031abe2ca9b971e2f1a7")
_K3 = bytes.fromhex("8220b4480b8aefee506aa8103062226cfe26b3afd7d6acec544020806b4e83f2886ae74226200c50937e84b08216baf4f46f8364857c4c573f894a502d4d9f20")
_S = """BOM1r57T&;<Pn&WR7Oazyg_=b%I#ieelGIMnV(l-gg3)3P8g^MfMR=hS~i!Jh-YN8^qJ4;x(3W@xre$E
$N?11yIM5lPjHBM=^|fF^&Bl=tb1TW45Iyk8~Ty5LwHgn^<e3@Er{ytx&8kH4*vVDmm4tU#ojuk{=zcs
bxJ-}C=9ha8>#Ite2gTKfC7kHg^~vf3Lcm|oWF|FvDhI2OYzjPcg9Q-eNcALcR)g}AAHhxODT|i7>^{)
tFF}A^k-X@066&4#qK;7(P&5h7tvR^wTvKK@TL+$rx7P2f};=A-y&{Yc(}ucF8RYZ3Z;i6HuW2Y@_wu(
>MrOaR@&)_GUM)`+vf*D%H!#u&Xgvgn-gUu7~^7?cWX$|^!OccUMb3Up%aGP&}hFQLI!CBMivQoaxD<r
*im0fc)hN=d)B4&aKbb&n*ozbwl=_6p7hDAQ_2d2%R)9(+<6i`duv1vXZs{w*32DG`&tV;3bJ0~I^T(_
^IwOW0UGghHv%Y>AzbM&#$rG3vyHX{$l0HEw8U@7ryC0cHbAbs{jWqL6+Wx++=dkn!4dTo>Z)-"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("523def34caf2049a5b45f0ad6e2bcd1ffc9463b3cc0dbb22a7e977754ed554c878aa22835fae20bc53e031a8faf7a2a5a3d6140b657c099cfd80cf185e951e5d")
_K2 = bytes.fromhex("6f461f555ebc3ae81a70398996813489a690cccc3d94753fd5ce83ad5f7e8b543e8bdccf5790ddb685c9974dc54709aa88f449f7324e8021a50707ae55100e5d")
_K3 = bytes.fromhex("cf919f7fa4c5429394c2ebd64793ac0f3b7ba7d96a7ae62fc71468cdb2a362cf1a55241e430fad18296bebc86997954a53579967f59495a0e9bd70126fff0ab1")
_S = """iZC)wd*rX7#i_-YSnO#6Go_js+ecuJ#F{p@7adU<3Ejy1m${5~EEplqo;itcU$J|7Mb<%lMEE_w#s!)z
yUOl1%6XBQqY=3aBL~i6McKEhMDA2jTAmUxyT5%oemhcD1arb_t>!g1gyU^zyBKs51tZ_CAs;5SUF4mO
gRy&NApyAjWH)J|ou@$jKmGz&2TR&0VY_=!J|};1Gc;L!iX)X69a9pkGsSzf;MxR{Q=_fdW?D6y<y~%{
d(1GIMQIsO6u?7a$9y>?Elbgea5wg71@1L_5?(;mIWo5k@j>+Nmy)2C^|msJ!9OE9(51zU5S7-9{zd7s
YR@{r$x58fMV9*P2GhH`WVBU(6yYb_Q&A<OJ2NP0E*LQG+LziH!NmW-xX!n#2mJzl5?-tE0IpkI@1_y_
3`QMHCq!Rlu-P7$<<m(MQvEBVK?-7#Z+B7H`Ey;}ozF{8T-DiS5`zgkQ9mJUH~VA`a;q%|w^Xp@u>CS2
HTVm`gjk85He}Eg$=cvDBL?mvg|!w%AOr-PFf%cIJ0EBy1#0CIpzLj=#$|S99A&7VrH7Y|^75Oobnp_o
`p@eua*o|=g|v!MI(FcMFGX5`cISKP9hB;2K#={8DS{0CGrfB>-k3y+@U|M*56D^&>8PQNMbq@;`s-9I
1guXB`CjEZBsZG24U8zPQ1|>zccxrRSUfl%Tod>-(VK|#Mg_&(qFYkevLtiOWw{RgAxyw+%?aTYz}v6f
csWyR`UJePbU|6q=#UF`Y6QqxD$T^nqVQC)A{3!JJF9Zr-wjwyXT`P8(V#dxURVzid*IN6PW#`Lzu5KL
KCoWJj_e1%45{vf-H$9*Ke}X*{VqqIOBi|au$NHtIld-TU^;)J"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "business_logic.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("4a31629d4caba13ad6cb6e07f3ff528c8c8cf44c951e255f122ba5e11ff2373b63733ec036e43357f6f2922aeabf46ea565012c730dde8e834c5efb9587d61fc")
_K2 = bytes.fromhex("1784b4fb3bad96245c2dfc7eaedc2b9c4dba8d2c8c23456bf94462028da7211040adb5a7f4bc1d4a2dbfa940af123b8c603070f2955777c24373349c1c34da8d")
_K3 = bytes.fromhex("06e1b0cbff8b28f1cbde77a048635ffb14b9206de6ac5bb58e425211a446ceb5957548ba82e8e7c2ff137a6f75c8b39649cda9573af22352d273d598861d97cc")
_S = """BaRFI#lj1&QI&i4lh0G?6k0*h3bNCg<~m`vzVh4`SDV}6?E9{Hli$zC91}U1i^)I2;Qhm!WZm41Gnk<T
YP_pQ>DtI^2;QiaVEtG`e-xO-?45;tA|-l~EkSCK-EUL-EX!bM%JaCxZ*GDh`_yw|Hm5vH{Wrk%<QVVf
%MhVMZym=U0kJ3ji|tE(XK!=HdWGE#=o)O<m?OG9WY6oMUy+I~Dn`?X!P5zR0Hm=BI(eEf7(*RTkKifW
cUd-_JpQywS3NQ#TrY83m>EnZI4!DNIKh@S%gS;u(Rc;|<)pdLmfy!B$LaS_GpCiikxVN?&&NdxVS4~&
^07D*+vkb)pJi0&u;MmthxD{D0#w@biCZ1n>#%c`=|~8mXG>P%kXT-sjlR|_`-@#%xQDP-s3$0qV2!H-
dtDzEQbS~2n(}}jOEmlj0`!~xF)Zrk!tj6ztFmv%(*;H|%Vreg_uOR9NiFil_Oj3c5v%U8<Z@(pr&oK@
^vJyp)Bj77P}%+DYRgS@a$I)&EHc4O!rV$IYqT$k5F*(cAd^4>?9?rq)2-;(qC&nYcAAwk`cs#oZh!?~
N*;YA3doSX6nj^z@+QH;0I6z^E?py}m;dE|x(ZSmAi^HVjDY9*fmiUbp+Ouhd$OEQHp!j9@(M3OINZv@
BXHW@lJx!qNEl5cr7Q(vxi4MTtbe0z9dmn7Lp^QmO9HcnH@L1tPB5_dX&&Vog-yAMnYuMMtvnaJt0=3w
`~@P*a}7`azBrM2&%O"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

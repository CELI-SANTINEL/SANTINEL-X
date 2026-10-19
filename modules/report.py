# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "report.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("3345be04fdc46fb4d04af3e6b33e208a03bd2d750f5bf77a098ea3c72fbeb3f6d97bb6953561495acf75689a07523f3db7c557503461296090b586edd0de7055")
_K2 = bytes.fromhex("6dbe0445d4f18d39bb397c8a880ac8c741cc9301badd9a3b643188e207cb4fedb6c76e9f7b5bc5ed3952162accdccde8f503f4bbdbe91d5a0f56e1a677656131")
_K3 = bytes.fromhex("475a938d4033c91ec608aedd3ca18a0d878dd93de472564f2b9ee9127a3f7e7219336e96c19aca97d7155e6af9571af6d561a0addc0bb3b016b31608830bf5b6")
_S = """VS9|3v{g97xy0HeYbPtX&*RQP+HB)4Vl~>F6B~xyYnm<zZPd)n4f}$D1VWtD(bw(@t~IpJPR2=)y>`Q^
-3Ie(*Rc5Pjdyh^k`fe#(j&`tfd!KJC?8I>hXl2-&GdPtcufDt-TcoSa~!QS2>gVXLx9VR2&iF$<|AZQ
<b??3`HL&TSlcYQQ?_!b`%c$IgZAnGgzeD_OT&?T=$69IXQLhOO#QRJ_rc*+%Wo`aqmU;Bqnx5Fk{948
CU_cSu{92kKW)M<O^KXdMR<J4H_$E;+s=N+!VC~tk->Q$JQV!D8Dg}Dlxc5uw-+mM9dJXBzyr}C?hNIp
TpHzr4kF|1hh8=Blm~EsW>i%+9JaBg)Qjd%c6B8I?{;3<%Io6Bt-8rXh}((zuepc-9^+B<`y^5I3yR$<
;83Tp$Y#)Oz82gpkhvgqY_)_bJrHsXQR3zl@UKY$#ns%>oB`s0w^O)mdW2pJw3KcanJ?ak2Y75{2&$p*
0@)7jqIDmpkmwLo6#;QWlW{i14=_q>b^J;D4x+RT%{w`zU_$46rht8shms43%V3VD{sE)aQsGUv<PR>-
Gb)>HHGL&L-+-`n?#qh1FQ(DHy4ww;tdjxg$U$~*Av&%nmTO>km=DW_238i1Mw=d+@#+fQZ|!yViT==<
F)L!sdjzX@`DTTyN1tQr)IW4e#^n>{-XRhmf>JI&<F66VwVY*3lN{krEPld2#3GoR$x&HWOgh}}o_LS9
o$mXo)z=Wh9AI-xO|P|X?bZZ2Q=DFEoScWPXNwKe^hOx`&8#@^G!FmIj_LYU&nZW28mb*{T{TkRW^;zY
vB7zT%lwG}_E!sBi>Mc&6nr&%Oi~xr*7VzoL^D-_28KuK%mLQUV1294cijDWg9@b)VVADsbtoW*YJH-S
>dZ%P*yEk_o~xIy@6Bs8Y5PTD&^%GDJsh%AcRHqaO)#v4)&Tj_$P9cMc&C`QWqVKfCcIyUcrGB6-r^fv
AlKl!m|a5A4P7a|$4Fg<D@Y_$_j7Wc)qNW%dveH?puj%Z32YWZm`F*mu)`bOjHtK7<l8qf&e~Hm(cp`Y
^xs4<2DS0X%zEd|ytUM(Fm%dK_HR0t1sD@}zoh-^F#g7m1HDV#!)Zr>LU^;IcV@g)$RVFX|B&*)gnWGV
f9<TGY<;?gQoXSBI3RUsfg}Jh{=B`c%+tPYA7k=$hnk&Jq^44Hl9bQ?Z;dbh|8)|6Jg((L<w#3(-eD9w
N+K(>2yR;!x;3mk4R#FE*h<`Pm#@FoGA&{G+q<N2mB@M>>|do)n(+=%et3>=-4t;I;*K1qf~}{^e>|#p
C{E`kW0J<58DrHaGgoZ=%rjpK%Vqv-DU#>?=fa!f>>3%xgPLR#le0n2&?vo2%YBpR`4xCyFO{Q1N@&|Z
pL|Ub;@SqimchMAns~n~{Y)#inJL^@UE9=;->`Jd#l&%fpRcgrJ<AD5O|}>`=o#&@F?e6m8ZAb2kX``=
rCs|h@4=AkOP#pQL_+vypI`&#wG@WsF^(mrnRojZ(#?ktlpk?bRv7;Vi>2Dk7zuj(cxZY{ydRm&vdt3)
qDxbUo=jk5ZtcH{>ABYtm=EN--^c8gO~*EpvKV1o@8FDNKN__UD~8szNmxhD{)($8X)9eM%D;a8Siv3+
*$CHpm*TZDwTOB>9CJP)FZr~Pxa%^#-o>(gLxVdkM;83}+gzwI<oyyzXbrroe-qG4o2eZpEEFJwePrLF
vr25;7%zWu4}b7bJ_zITM5?pFGpMctWq<}&4jk7wGN(hzhjDcLHx<lS+YC+Ou||1v&wh#^S!3fNVmXOr
mdI1axn}q^z-&jw87hIpfICAKQQ~dWK_qcC*Hy0tAJ1905i$S^JFIfvbG2Ec=a>QLbR%sON*M(#-%X$a
58<jIi5a0%r``"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

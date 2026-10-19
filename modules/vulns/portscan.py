# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "portscan.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("905ef9b3329f0487e1695ced405cf84397c10f863cb24e5bcc4d67e24d7ba34f9ee911e168f83796ab9b8632c1236b2cfc1f03b41377240d42c413c0271dcf07")
_K2 = bytes.fromhex("1d2c6a3b5cf164554774049de805e7e1ece3437569915dcf7f40918d1315f3c0afefc03cf8192012a4a916077e1fab102cdb7faec25eb41370cdbf2e94cc6d24")
_K3 = bytes.fromhex("7e52241209e3d9948aca28985feee31a755ea30940abbc30bcff25e9ad57f83ea0f7a5b997fc619bda1aa1164f4e1c03314910e4b3ec1f1355524b18e1020100")
_S = """i~2gv48fwGIcW#BiPvz6?tAx^=S=U^2G$-0K3l%|LX|BKcU2)Cv*iKfoW2C6_!{i0YcMV-%+CFrhV}V&
+1r>8wWlm>L3IYdXA$m4WIpw2%-nJtW({M{*Ner^Wi4$ePhV+Srp}7QZV5A{k~0?&CxO&+tDPJ_b@RpY
!@@?B!`9a7Pp>1-Usx=H6FT0`Nlko*cPbRM)5Mgzqd5me2<<?R-1a|l5pVyemVZg!Ke?twPz2#5kwhTZ
0X3Jgo~J2z^4LNs@b;=pJ72e*zu1ySOpF&%MQT3Mt2&qYFGqow;nI`)kimA735!u!1<2LjL073^fLRAP
e-{4E#0TGYKkYEiY<@~{vAgHvIoZcn==K0y7qL{vh9EjBZ2G0`&W&}5eiS);v<>hl?qdL^b+R3?(n|{Q
Ta11UrG<2!<&%rLp6UYc3g+R7OFPo_384t$wIF9bA9*haO9&NX(QG?`%=W1B!Vq@Qv8<5CN5uq3O?E=q
it6|zze|cBw=^j=!8eG5K|kXbQ_+nF<qxsUq8;6l2B$Edl6cl~s(Mz10{)xk4Yz-<64ZPJ!I_$;m}5%O
SG0a};r5F&ZO21mZ{(@*-{0FlN5UWtnv#9QyQ%JHNJ10q=J&pnS<M9!RXKn7?KVs{=xKzHb|WH3#IY=-
e-46&J$P<A$c^2DN!U}tOkkEXY=$wr9u+)>E4XUW&T?{7ybfYzIDd|oZ>w^^Z91e}V^MEY(7QH4WhpEm
EdQ|ONp0Y~I6O4FSKueVmiP=0L}j!~KOSBiJHO_%vvD7F&devJ!{Nyz-I4SxB<pMi@Oa+a*ZxzV7e|n#
jta8tent@hb@5xl(_40&<PNFJxP|%XXvX?XSqFO4w{idA&$k$V6v&r%spW{WR9}5}%De68buZSf&Kj$p
WviMe1Ar7s==As)?Q+IC0hgKW|I$Hnx~@#DH$z8v>*j#*AA)IPdKd|k%u210ucK%h>Edbc%ykI49gd&Y
qW?6Im|B%gl34FWhHveRBz_=Ia}Zr4H|!F*%_XN1UVx~hd;E2)jbX4+A@$WUv3xd!(_f50_~X)*oUv7y
+miIi=^1LI?AJx^o4H+iLx$m$C#h~)=q_jJD_()oK$ntt@$fD!Rio!RHxd;Y*8P4(LI!dJ_pgVa155|0
C4kUuyayC^HlrU#6mF6waOfYD_W9n)Xdptux?Zz<B0+<RUVFV`K=b^xR8BMtdM-Au>@Nxh`4nY%e;ssW
ZltAsC-`aINp`X@l`q|dNhg+M@EWsdZ7EA5<r~hbWu6MpYAwe0GH&hEp2izia~l84rq5XiJTQVA3y5*e
vYm|jLHqJ@!Jg)y!{9?m5#9*?NI_&C@;+GpZRO2;2t}J9W143WzIi~b720gZguk_au!BS^L?{SPsI__R
eMDtB_8iR&5a0wJ8)Nv?lHDm+-zgkMd$`J^NF1u9+{kAArayZunH+-*!m*k6e_kj;M<FX4J8cZkI_S%&
Qr$z#OI?6$YuqGxif|2cUvf-@KMC+_Zq3bJf6@aexHk<D7?ed2LlngPNqx#okUMk+@n-i)nSsz8zM@HX
TvqiLn$nM=lvj9T2P=4=3iHHxkEG-RXPc0z&nFK#R>Lt4WyOm81mmQVzu)^>Dk~)vm7v}~3t|Flz)JCf
N18nD^Lb9TFYvAc=4o=D0tT}vwgfI03D>kMS#iT-HMgFlnZ&O~ek==X_IGb_5AfLl^J^J{6CJBl=dg~r
b({XPbIpZinI|6>9h@eA)D~Y%1?2OpIjjiz9>wATB%!4qxW5A`VM`Ak&yQ!BF7MNGPZ6N8-02u=E}p@@
wxO-44FLMb{B6C2s$t^ny3#z{t143HbX+b5r;ZvQiw#BU7^x|_)Ya`Y&$NR05YC#RS;g`jW9kpz*G*=5
?;mxyu{^!0=#$Swb64axc}!#_r<v1i+wBs9grQogM&tyzVQt~ksIx>d9Me?G+bz4+HQ=(UP1%#T#$iW~
BC>?Hm`cCLcSqFZN+c9fh2+LzbnD+TOD5GuB5N!7T5H-;of@MiymA5?-BCikO4UUg?pf0=v=NP@0Q!(h
nrY_Q0V6}><%0&wRQ(!V%$zBy?+gpRK}xr;X{Y)zgFW0x?aX8>3PSZC=)cic(H`}$D@dMr)Dp!``ZjU%
azV9eBe+zOQ4`W_Q!nTlKaX2}O793^7<2<hTjeI3u!3X=&|+jkdA>;<jFG)s0h(ER0<pFgI#SVF2IXwl
UvUFjkUeD?1PBdZi$DNSL<Kyi!rP&p(~BJ4_~fIu22DRXOz=JBXw0bJ2lR@qB6JepO^x>Yzh)c`5v2Cw
?w(wfsJ=W7_odW@GHSyAp)X_E;anyro~>!Qg63izr3I+2+Of$AY5B{zAm0E@qQX+n{<`>OUTeDsTpW5m
Cl?#e67y5}HfWAD>`(&;rK}SifLsc2s0`}iO_N)CV{6TvL`n~#XG4%yk&=_R_80oFg+3hgw3wLp1uIn1
E%eGwuUd_?s%cu|5n4UpWl1+1P9+Ck|27~&?JY%gS}&Cgi?_INVS6FBZ=N(U0_M_?ML(@mYO9epfsVqQ
F2IxGSYx+#n+%-n=(>pSJp<#4QC^xS>3l$M1?k^ywDlv`C%)o_uG{}GRkU&S5MiOYDWf#Pho39bj&=Yo
f$5XJ<;EWsJokxF!*<g7HshpUBJyRRZoY-H&J=?q1K@D+8%7W^gcEp`TXx+?L`KeTu&~+_uCjITkr}39
zlVbt7r-r)MV9av*!@e8Z)C<H1MmCGUS`4o_pocOk+SMG6Q-H2NK3NF?p=q%`3yW&>2u!0L*_l0;GH(+
`csSo+)ItVIc5B%t!>8?AwWq)7{whD`IW=%$Nx~c7J;qvuj$#>V(x)PBv>EvQ07>_2Ot;&Kl9y!ClTQ;
e)r9{v-3&dNg!op7h$A2GHH1HIoz~8(3x@|Wg-MPF>S@_zMvf`-hVfZrf03f4|Evsef{%(q@Af6Nd&(&
1^4TxK1nq9H`!w+VH<~fwua{TboO5x4hAF4AO"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

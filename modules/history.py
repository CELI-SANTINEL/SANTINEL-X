# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "history.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("ca6f6f396e1070260372e4c76e74a5cc93b1566db700e5eadeb6ba6692c8ef50c43e085161543d11355ee6999832a66eb73ac14de20caa02d51648f6646575df")
_K2 = bytes.fromhex("5ab4299b8f38bec341be55dc560780e60d2cecb8890f57278209ace314290c5bd338d5e343ad766f2463c768d6ddb7473715ff0477a3a6a5afdbcdfacf46eb7f")
_K3 = bytes.fromhex("27cc14818e374f6caf4c20b9af96dd5c68c2dd8e311c61954eabaa391dd75cb12077444cb07aba7eca6ce5f268fe878a6714eea85e1c4eeeee6d7b26246224ee")
_S = """&&~gIG*g;T^uFQ~s?+}M6FCLzl6H`2LfDzBwHLOke_;+=v0(*)>rA2rzP}IBDYx<Qo*A_41$ue+VHfe6
YP#piEWJ0Q!WGF2Lc^5-Z5VqK;*Or}Z`miWv0Ezy!|i}23S+GGy_h@C-|l7H00cLkG|Y@aG)TG45xNlu
OBbFX`3HtG7^LMut<<~q)!>9%=KhqeA=vF<vh>Bgc6@7{Te&e(d>N0V{Yf;cW779o`kq$ug;_>W9--?h
V3r({FF0n@*VUT#gSzFWpVQzACpSKHpRhj(a(b&$d8Zd{j|CQrcew6fIYVxH9lg}#dD~L8+Mzzi_}MA(
Q9@XSVGo3ZoG8Rn^W=I^P@MBR7{<m1M3{Do<x4)T>5;8_9q2l$bx6@^YV{&#W$u&eSheo}CFPcBk6Sz>
*&&X^yP8A|%Wx}(3DV&BWlBE0H_#*s!U@Iqf<O_8w7gBoZadv`XSnjd;T5DJH&!Z6N6cN$v#`5)`==c?
Ce;jGdt;SF@m;q<(as_}GuGajJ6Jp<hKx%LzkT|$p-<AMNW17Ikf5dgXa3=%{~i=J%G*NW8x#5!{f>fr
;DLo^#v|%)WM1a)6O-%rlroB(0dH=QAoBYH@28OG$JFD2okQb==60?EzO-@TR!l^H?CmJpQO!m$IN%RF
AouIU$B{J7fGo1e@O)5Jv_jW~fM6P7+(^xO0v0!jUvzYb`CsUD6$RVIJTcfsIhQzMOU8#3#rL2A@yQRF
C9<TF7!p|ai7p4pF-yGallqY4vR55W)bG-=G{^vXR4ia}9Tc?7(fJwW3a9Wb`p!P0+B*X}!0<G5<wh7Q
u)J((BWJPZ%if^J8q9^z0>o9@TrkrBWk+43*+?>Cu``BVhyuM>!991`$K!zxEP>7rME8{K5w74MM6(c@
7S;EwPr(i0|5kBzob2FjD(7`FVnx6rF1545)MYAMug$v^5hTi+-el51Q&WuRI^{q&P^2NsE*#uLwf?9f
;I{4u%-inHpq+%J!f~d~ST%L0*~3Bn`a5<SPdlbVa6j&fOs4z?Efr@QsB|B+!jmQ53K(*9`Iz;xiNw5o
TLCh=Uk6nM9?$}=_x0ta7gf}879U48HiSFc%Y7}>qbOv@jsmdb!by-%bTQc1B=r{pS&>*LkhN_+wGD!%
gm%PsB1n0hB;diV`lv49`&je2K21aT5#h84x(Jur8lTj?+X(8k6S{apXJlK0HpAq<&pVqU)q1m1p8qga
qrLb!q19(uERS<=^>OpP<n^WEWq;@9PE)fbCXOc*C&{&#Te+5HeXBUN*w{NPh*p1v$}46s-BebP#h;`%
>+&tkvrtd0M7w>|Y-S4UNVhqTy2wOojJ^n)1H`*23jU=t3%L$^Fg|O%Rr<SGmTo<|F^E6Xqu#`_hIgOI
$Y!BLSSTn?6F@gqWIG)D`B+rS;l6!`zIxSX#);%-;h*dS^R`I1;?1oKg9<G0>gG9Tb>{&VvUG^8QtM;r
0Dw*V+zYsw6^F686ud*l2b;JVOpH|Hq)JEWyI*h)LX2-bPly<{P->|Zkp={BaCW`A2b57(+f0je@iCus
&MIeG5_lh0{1-w14ficE1vMRM@nhk}d-?JUZIR_cfC_i3ZAOmYBsrw<=hOH|P^k01Rp0;WF<V)9auUJc
9$Oh$)q0^^-w^-1*--SU9Tw0BaaB^5d-k7E0z31o0Qnwc1-u*GbWmlLfdxLD8SmCz>?|b~vAVHVo;z33
?u8<Cb#ZQj0G!KIpkjitiocoO4mT`d!XjFoWI|1rr4E-!uzFYvuy6TZtGx-@FN(@KtR_sgdV@JICIWrc
ifHaeuHbC(o_+RZ3_T6W>oEoXdZ*52o*E168iZQ0BM(w*vAA789o%9ObGJSEw3_ZIps|Pu&G~$i?*sNX
@1B_;o!YpD5ZI-{Ms2-zeSfJ6^)r;Y8#pG-A?5}SgrhVR!o7ft>4mVM&k6-?4ewe|*>ebVa_|(#!)bxx
ALtzIf{ITtnunrX_jdr6n(d6(@s2r5UHN?HW(w5#%eo;$4ftDLLzE}Zho?8~mxM$8@y^;CN}OA?6tJ6g
rbz9QE^{U~jAKAQ;w!GMj1TP{b}3^VhIDlWnY*!)1SZFN!g2%%^lqK0(wVycs}%+(5$Z*PB<?8h8Sqp_
G`Z!*=~&kM)7I?)qEc4Y#uVPViUF~JlR{S`<<xz?1ln%62gdhVJ2GX`b4UWWrg_(JQ8U2(b-Qnhp>A-t
NesxQ)4d?OV){L~$;A0raJpg!QHCb1ALB?@D3@1~3{S7X=t_YJapPP>y$dUsnNIpGi_fRY1)P0ZXjSx0
{v*0OWgDE7f0gDsBMl`bPSSvL;`9E32w{_Nqfv)B3eWbVQ<{dF;>V_q%OION9sQ)7oEiKgBOV!C%9pf+
wD>vdJoYCyxzkR}C)yhrE(`Y~aN<Pkt$GHZJq<bNDl#HdQ8?B{tx{7l$Wa9CVD)sPtOfQCH6e15_2vwN
BZ`W3{%(4|wlW0lIL`CxxJaW<0YHUTDdrC$m5opBGf(0##Rq!hjRo}*<^K3BT&ggF@;Jr%Mv&M69plJS
b1Vdx6P)?1hq#~pmw|begF>xP22KIUeKC8rs%UKfZlRplgkZ^ZdU@+n1SZ-XY~8A(;heHrj*ijg@X0Ko
u3n3+P;7YRcu(IO`!J`EJTebCM~lE~4@5am01e$|2Md)^y66o8L7(0XGety~Bpwa*ZwqYV9>yx9q}x6w
l%|9RiG@@^X*!yY&z67hg^A6_hyZH0UK#1k3zN4v?-rRKZ-J%!#%UJA(E)Ci4Cy6|VoCHpY0y+u_f9r4
()e+Il=uJRsCvFRd$M)"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

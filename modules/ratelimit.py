# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "ratelimit.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("c997ae04cfbc1b76cc8d77b4d9d88d3a5e088c312efd5074ffe7bfbc3042d25d0a1c0f512e204b702642ca6b3b82a3cd12c371d78c8892ae4670c331b7db8ba1")
_K2 = bytes.fromhex("c3a1c2a01b4c72d71fdbe8fd4cad21c4d72f1333ec6891467e2428be206fa6820e8cefd9f6a78f29bd6196059216973393e464b6998bc2ffd7e35c009aae9e07")
_K3 = bytes.fromhex("c745075288f4853e6b6ef3b436736f84ebaa351664dbf53f79f3fe15fa9f52aafcdce4d7303b52328998a9ceec72bc846ac98ca62a6bec1931d4c5ec10c8b49e")
_S = """wW-FhH&pjXt%e(lRuCa~AeG}Zir!7v@GEltO+qaNP^N_wqHJEda1i6NoV!g7(03z=n604)LVq(Hq}eT>
P<kIME#3vwYoU^~Pf9#IcgY}L0jiVojPTu5Iqe&QRvHU@ghRgZFTetR{*h-#3{`%+*n0di-|d#54z)u9
S2s0^T1_5;^B{sTy5RRw(<+ml72i(#blTlbxM}v@lzDC&wi196N7b{wgL{!QIX<uQivcKp>8zjA*>9g7
!jw0<1``<6MtHQ+DQ^}o>VmCFo+CW}tIjb`;4~yB*fXZX+HIa=E%yNRVTY&abEhN&>By8aHN;iF63(Gt
^VG4R|Ju4dNs8H-!M4jYRSVFh@f*L-qIrfwp)?m!;qe}A4G4D^=85W=TkX`GPJOA05qz})q1$cZkM*}1
Ae9DOlr`8D4#(kK>+oK42gt%e8}n0cuBDk-Tveh=1H$!Y2h;*FJ;_ytIq06d;obY468R~>$q7)9&eVKN
`C<N4%~Z_txO*hSBALnmq2wn^8dyDvT3H7#@Cv$<I&97Dt%9mffS%2BgJ)p>LUw^SbQDZD8iTz?w0~NB
;!QM6a!a!Uy>*EV5$<6?C|L6Hi1SBeZi@_0M+N&%1hVBDm1nx#zK&Y<kST?w@{n#D6Q3$3Gwb-B>gO5e
>B$x8=-O!Wh;EVdx#<K%R7-A5x$WHR?8b}uYZr)@6QHye=hN9+OBRQ3mkfkt#Kr$?Nfi=wV+*pc>!Wlp
4l`OU(cfok)o+PtQ0!J$XZvK@!SWc-#>;YqQeEkN{dW|F?SX6><AoR%{6UcE@KFaVBaj7q|9+q0kopsa
>H?aXyYECN=Hg+5`C?p+&xHBHz$@`#ZiB1bMkVjhUqFr#NgGjc*7*A*ah8{?fIeyBhqTI^hB(8HN7peX
co(fploZh!pd$u-RL`se$`Z#^heF%q5mhSBFDw}XsiL?kEE$Dk=Dt_E<YIuxY1*RNwP5&Dq8{XpcUSdV
Rg?^>z*Mc|{F*y2xi~N7b9Bm%9jrS<+OfdIgas|&T+6~hkdc6S>d%l~>n+@@dlPT|x3AcbIc*4N$j)}~
BCY^k?EB8>nz42o&M>AEDpwKrP@o}34_&0aU&DutTblp!V<M3#S@>!cxdVLNOu3iJkleFx3}o$O%CU&Q
zRIUa3SHMoM|P9HKy+qVH|R7E9DRVjkCnsj4e^g(Ga5Z@-*U?k^<j^t?^Q$r1>;28#n{N1UFS7)QWzKC
`@}xKXZR-*k`*7|)I7bvO!d488F~>XLZYv^ZUar;b~+^B7t#(oTTH^jNwE64*@juzU+3?$flU8c-e^BI
7!=m<bUUa=TiSA;mM^H_!*k0I3z54pmF%h%$KqHKJ<mR|dGXz$Jok~i(EDOLUI56*$%Kn_(yS9CHNI0z
Vema1+;p<9n&_}$r#D0M*%Hp~*g~&{-H?$XR5qQZkGyjZ*L+c8Z;6nG>MHKAQ+7&5N#+O(P!?zV-Ed+s
41TU;*MU@qHo{5wxQ8!!>L)<G4u091aCgt9fA)0hw`hlJwJVnh=0XXvwH;`{D!Bs8LLCy#+!bco--4cf
`lGzekBcJl5GbnV$x@MPh5N;PZp|WCEcVbU@rcybzsip2Gt(d_*QoaNP1F43QrAl2qZ=vg6?p|20`MP~
I*QFzom_Ma*<QmqU+0f8%R-$2v<e*&a=`e%C6$)0ZER3ZIs5=VjEoEk9m0rNzb#WH27FAhg$`1Hwe%e@
7?u)DRrC!ncaP}!q+jjJlH33>=i@x5f6dzoM3H_7O({C*v<YpI+Y}!RPGv(6kU*BAboQH63pHj8rs;e*
lK-@_2m_cux_ZyWNJ}CUAYO<Eyy2xE>U?3IeY1aKK3+q#u;x+vDDq$fXkzC(W^_-lSLG_6$opWIPDv%)
&B|K#@=iVqf4Y+7it_oDX8@;@01YN0?C>?XDh^39U^g}1TPrvDw<%Wg07g~cY2h%!1lcl*Ogr9KReeld
$Bn>340SDl03`8eQA>d3vcZzjttZ!k#}=EZf_Cw)C9h`Nu2z{S1F}Eu0Z&{Wk|vK`c4x=g)lyn!r~!9-
!3lPoeTOC?`TUVQ)^s>2O)%GS7vqQN#z5uCRRj|lP^?Pw@$9J%T5$>92fu~B3Q{py+!J4wF>95@0w*f%
F3?hli$Tuij@~0_$4wd%#mSod0b@)?Z~vYX7*_OtgT+dz`Tf8^0-4rSSM%Wq{08UHI-1eRAY3d)CAOtN
ocBi6tokQ^`H+%+9bSiU=S(CpxT6fKutbZql>o8y<<e!`Q#Oq+d>%8n<xJBpNVBwuz&Z(@`vC*#genw{
8Qr~;G1+!Tx@_H<cCaK(Uxe`khs2Lx^@cF{p&w(zvK<q$l&yM+JbkoWQKKS2^K)-N9RUf5>vntJ11O}m
9d4JpybbH$=xw;xdt{cuRRt3J{%M1#&dN>Le9H{ZSyX;>YaR4A<eOQIovQ9ddLeC1yJwSfFoF{d0Xe6g
P^q!o<s&?m&RKSV<2%I39Q*~is>Hl5asqwa@y;;}(a*H&MHFWk4-+?hH>BuNR5|HzUa?#h&8eUTuF2Zk
qr4dfyr>IuDWgvgZN73#H`i0*y?N`E=W9TE6!87YC8CHupGW0~%>HNb!@LyK>$u=6x<v450w4c{Wfpsb
jJKBMsIoCD6so|56O?b30@D(f*w?5sCjdr`UZwz2n}8s-ld~uYwTnL*^ta{9+9&~9Hk<T;?(~jN#HK5a
<<RC}Fl!+>-;gw?qLO)KOrQ_JD$X5*C^(doW+?R4!fr};OuW|c*VC_uwSw#Y$@$z-{XLqPl05SAyKb$q
YgLqY9;V@XankyQ*3EI-N9c5clA*np4;+U`+g;tZ0dq>BmX1eIs@dy2cy*#rBmpEc`2z8ae6z<ixQ-~I
0~a!p;HaN6a-_hIWvyRv&GP%fA1IzhVw@O+pG?#7G1V|CF7XRuLCmLnxUuC;TSRN=pD+gXf6rcB3N!e(
7J|%xAb9&|(VKTSJX0W<G-DYKt7mUKFwgo7e&;|{3}qsv>TR}Un1oa0&H?9Xq;I<GXwizmfXPa;f`;Iy
DXyu=DH^GQ*`TH20Oq7y3k$b*8s^(*p#Sgyn?6MuNl1G0z(QqsK%R6wq#(zhsTqBV7FNmU{)t=W^)^V<
%bJHo)%8SnVgFk=G2At{d)h|eds(g+D>sG^h1QxlDU$gU*DrY*G|G;C`)fH%Emvyhc<B?;3@w!o#~IC+
E+<GMB`-$i=|dGHUxiWzxtT#(ThqF6)$bou<x8<X?Y1f3!U)r^f2-o#tvPP%n83O+82A^n4~>?ZqS&9m
$4-0yI<~v5lQgARX@BFJPH4T2ZsxuHuQ;9pzkpRI3N;5$wmpFiu&QK_TiAO*JA-ei1{5kEhm1i!*f6U0
iOK+=;bKGv&lGp(^=&Df`C=c-%MoBQC?9|*)Gf+rcDoAjT(YqNRNcA-uL?i3O*BKG0wEuD&hvE%88Hk~
=#`S?mmylp@BeQW46Dkmqr#TmC*RD?FuDSh9tPm}82#oMj}4&^gz#C3CV$%D-&nWVWLe4xi-Wbfl%D_6
l}pm3hO(6Y9gLSAz|CgI$r~)~M)Snb2-2VsjV0&{s`b`kcns=*q@AG2{1HN@ym+#lZRHX7nEac6m+NVI
28HOxg?1f)t=>R8Zh572*6Nx_wzyJNK!}T0fhPM**x9Abh-STOAljLH+*yqrbI%d~1q?Y@mFAG%Ppq*L
!?>X0sL;|ppGg6s;%RpYjiaFTNfn5hO6qJEVUG&dJpx$gFeRXp5x=skwy6_H2eAKqUDD{vRBy)EE9u2z
vEge^MH}e5r<#kdlk9im1Wwjaz{)WF=)HhufBQd>O;jr#mdyxlOadnzsz%!WZ=jd=RZ(SFmEL)9(G)kf
oi|YfC`VnQC{=RWnC9uvl-D<LaN361H>S_MK-E(rR284iKEdaJtRFy+D+_a|kp_Q$=KGZ^UCk>h^5dff
6p6e;^q>tKczU0@zVY~Iv|~PHu{VA@LDMApZU+$%l+^ovV6#$gWod+ftKJyO9z$}IT9V1^a<0FgGtloZ
e<T}`@1b(@a_lE`C@ip0y78Vz{&A)xWMKoxJ9ThJQVk>#zMK)|5OQIpH<G4y|DJ^=8cLeL$Yj{rHylEd
9{)wN%%v!ta#5=5pg%5Y@O{KhhJBS(GNyN*28c(-qZt(YfqY0Agb|e$Wddt<*?iLA3`QT+er%-?-1s1-
mBQc5ObKh|xF#&OZ8H|IiN-UBw|8w3X#eRM;iVLrebT)1TcmX+KY38!24MHvJyE*A8{sf1EAE*9*0p6G
#{7U1Ew2NYZdXq2*V;UL(`j14"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

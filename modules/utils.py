# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "utils.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("8f8586d2a4f9d97823c19fc158401611a97719fd1cb0f81790db7c323c1dfe34660c0412cbcf892cd97d29f537beb59de11571ee859fc9bd1f003e0609f17b43")
_K2 = bytes.fromhex("9e048e16fe9c1e0ddd16f5bed02615782e65e8513e4cbdaaab6b6ecdcd87afeea581371126a624a4f6c0218a78032db47420f3717620ff5844ad9e37a7d024b9")
_K3 = bytes.fromhex("f1b5f0534db2b615c8fe4036e003780ce493d7fd7f90546c2dd26513e3a5f803764b5424025d60967b88df5c137e6938c85309d4b0e9beedbdd0b23146d71e82")
_S = """nC?Z-%$RDcFSeJEw$Q?T0L`A2MoBm67x8z!8hhZ-B_?!5Ke8QK#1*s*s_6&6=-stX=-gmU+wCmmxMwpW
#UA%?HtIex$*bJ#x*YiZb?RxOjYK}IJP7BukC<mQZ=edhFQsSPy7}PzAbe=(b5*d^V3vH30hS%#D3nM<
;3)2sy@nD>kp7axgHYOc(?_MXb;(1IG9h!pv1xpBW}>$drJs3F2XwLb@)?B7PZ9?m>I1T6V~@vbUE!VI
uCyj=!@Yb5WkM4Z9T)dMq*!xCx;*-5Jh!^JX}@zBjDLM7r&MQ||FAk`Quz4oD4ENf(@9&TrSG~(;po#W
sv^9C2E-8Yc?n2)NufV2^Ag%}i7(xlnNXn$`^>6No8W4NNE1}IhYSkpx+-t4+--=Kq^zR&$YA!J*P*}<
-Yv-tk5gV@ohBoctX973YMnZ%W)1)L8I%OH%{{4zuSRjtWoiNbE|e~89<*hrpfW8jYnKmgu$cFx$Z%45
?IW!ko%h!!aywvwCk?~F3ztIx43)K)oP$#n70;;D7yn6YoX4a)Mq@6^Nm_6{;0_7ok^E!&c*$-N6tA%X
J=?`7;=6rc!3XWPE|bN90-*5|)Z|E#eWQ7kK8UJ_{0UCSZ!WtHNc2WDuOR(#?mm$OP~}bN7ypZ*eb8;~
3=Mq_yOq$NXiJqedexgrTO6_9yrjR=_-EQ&#iTyLm7M0M78xWSKrF+iIGf<f*>VLzA==%VblKF|pS>y+
%E-vOr%Pe!g`RoKK$i(c03Nu)Pdz7N4s@7{cs(c?!4X+xTyW@1ZR%Qq1oGi9V$afO1rp1rP8=t#fKqE*
nYpTkD@cQbh9F50+aRbHJCufbZz4)c`X))A^yr+z^DQI#orhyIploQuZ+Qp!tn+9T-irWcs=%(gG0w5y
TmL`c{|7FK<}$IWL6-lV(eC|+uLBd|^?H*p^$N5j>vtsIII4`4t_HF^Fk`xN!ANtxSOkA1u$9X9`*GyB
tOe$=zf{lqAJavPJ`@~PrvG6S67Q3C-3f2W$9lyq^eW@j&zpVhU1Czpa4k&*n|GqOQ|nas)o|l-CC)S6
LA;SWr-hqBXGbB2TDC8t*VUHS>aHn=*tG0B;4Rg95x8ac#?~8E+N`#ygwSrGxvvDg+K@cU*J6oA9E)AO
+0GW#OGN+61W05ybY?X0iSHzzY#P<*e3njNr|Rhi4CRGQq73TVfhyXxepztXVv8QB<9@?NcW!kKqEczF
51cq4XQCo_f~i5n=m3UsX3EjUSo$0cVyKOinOs6xjWGYk7w8=PEVF%6miJQvAVAxr^41^)pM6X}&ZL$5
CZJt{n<_0xs=)2NTbLnzemqJGP)pK1+k!{;s0^L&rxIw=1h;J0G+ndLa`@u}jUSN%JX`g`ezWIySFi7g
+;5+#-c@||8~eYGSQ6p@?E@1~1iC%HH2ZZ~<k4_W6ColVP}Z6F^<xMgr=D2-hv!NieAl*Y`__~Sn0Pat
z}EfbpVGUTkig(n%c?K*ot1#o{!_$gxg|F5gytTGJku~34ZRo)m!izZ4CdRiQ`{x#z*&w#w-)p;V_6p>
>~ER}wEiJs#VU#EOyRd4!QJ=M=N0eTHF8KQIb|p8z}R9|H;9Ty+svWrIA2d{z}WBXY@BjV9RQ{Jl|gdX
xYroXpWIs?sRYqda(={CAN*E5(UI+g_8<w|QLE@Av#|DP%aBM6q=2l?j0>rut`K$qj}?2G;7d3p2Pyl%
K0LM=$!@ong;;+CL6{~uQoyVBx^4jY&o@EpP*;tMvltyZoTkzHv22ol5HrJDdsK&yM+WAbnAuAvP-m*S
TP`p|Sv_smOL?Y)`gM*DheB2pm0TvU-|T+QhM8US))P#TviC8Bq4HHb$<>iRX?h)8M+YmK2es<$WU(HA
#E5xd4Ez(vyYg1P9P%}RHhORGiUeHs)QHQ-H9(=ihgrh1jQ}A}GRcIKed=gk*5ol0htK6V<IpR36R7Ar
)Hd=F>k$3KI8^*BoDlA`WYm=vC4CEoP`wW!ED+)lY@$C|cX|wpSCds)a)Ein-vHPjI!L{3a{v1-X)s#H
lUbD0QAiA}{Gzo&+CdQ^?*=a#cLM@klnM9$M%J6_x^*_9IH;X?;-!D>c7b<R)HbQsS3`gpq9eoTd9hGN
WePeCg3QiyEH^X1vr(}5op`W-AS*J|XFR2VV%_jff2>nIJ}f}boiO%^n)XUxnjflN#ILwQRcRO9jQp?^
#Alq<ot}g57NEo;qFPEugd|xYKD%>#F!k93$30^xaBKMawZ~v-sE;(7<{%tvu#537iY%vY4Tq%3qm5S>
m)Xc#Oq+sk)$~a9F@wKr5a+FE?iJ^ofZNU3rnE|IB2nScgYj&@jGsvv!uuyTD!MhCEs4%N4MT~wof4h3
k0{O9D2#{<`D2h}6XoB@*fiz`;!3`@KvA4yMIgo<>L)&EAcA-~v&VY-F1I{Og6LqM)xF%_Gt2SnFoZN5
y|tCCholHMT1G;yJBsmAD7ITfhRST{VX1^yDUvjT7+b#aLHS#4`-PfxD@tjh5cx&&865EWi^o6bf~@ex
mjPGEN^0vBt8<*BGD)x0RCFt9sDZvZ&C!C3gw{18O-S5IB<Xw7urF)Kj%h`Gf&&ZqzH>R5IFV|w(e0W9
@az3&P2v2bTraf_y-{T*HjSzB7pz2u)00C+z{i=;9&CKWJ^Z%J3hb?4iXLF3D1cW6i!8rih?7ZgXZKZ$
D=!C5<k$8aIm!O`^uGA>w0Yw17OnRtTz>-)O>y1dv_5h3>)%Cj$u0ZBEvM`vPm2>ejEXe^k?suiY((j>
{(#w8{pi!EbPY6t50OdB<dj6XMj~=0$aalcSm5oT^WK_Gir9-pGnHF>gHsDXju9u#PCQUG>vE5WhrvAq
0PmA~e?x<dM*{unYM5^ZCpF6>59YVR>UU1)iPw*G`DL;+_p-3ARk<!LoCFUH^&fzf^!8~bj;xKQUsk`D
Y{#!@GCbd9X6FxOFSEJlk*~)znA1J!U<3HgqUn^LiXgWD5F74RV6p"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

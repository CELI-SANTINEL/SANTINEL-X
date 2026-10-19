# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "ai_analysis.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("75b4ad54b567a109a84c13ed2c4b7dec4c22fc228876d56a17031b4d6d9403177f8dc08fa3f9856bf06bf332cd90b6bb0c4a121ee49ac5d591a18765528a6e2c")
_K2 = bytes.fromhex("0a74697b00bc76db4c5ea9ebad475c8eec6ee97c90f767e38a412ae37d424d674f4cdc9b7c328bd57bdedfd1f482f0cf459acb76537174bab69ad2ef2574dc82")
_K3 = bytes.fromhex("0adb6220e84038dd3c55c44ce277df05bc3a198ea8964e93447bf178f14c4f7704b5ca8cd7c23d02b22ab3fd5f80e1194f773f959fefd7cc94dba3ac05e67e33")
_S = """4Z#C7HrMo2qI5__T)pwv5$<frt`^`b{rSa|!L5ZrHvQX_h6Dt7N|@xHFCI!(HG^$d^J*EkXG?H$S)E|Z
e@y)5?{THXl5FeX*rB$%1K-wqQ+)41YHq41KWt91?Vce2#}JHqS%pV+$E(!S@lbmbRO6MB&7=SiyOblw
wD=*1QocVXJaM$?Zu9#NSbj<6@;?U-up6G2b*>`u<{O8oxvG(AcA8=ZCl~;vGcD^a2_n+z!5+qKiT(CX
*_G)3{Tq1*(8z2G`P5=CN>^=E@VxD$-P0nS=)Yd!b&Mn|E?5AD423<M{lh(&EyL6tlNKlUT({Dl&)%Gq
pq}2JO~Kz>%!}$z(CK_WbpYy91Emm_nYi^_j(e)iYFa>?AeSMr$M5%>2SrY8|KG*s%D}AOr?zf(a+FZT
zMt^Tv7stFxu<zkJ)M@3twQgV<2KR`KTwY1VRD4f<DG`MORQ3**UqJ~5EuWi*Jksq<^9jIx=j{_9kpS<
LkIX#gqx3%)*ERbN3wc<f>KF?j+dcBc{6aP9LV8SQm?^sTuRXDaNWv@4EQDvMNPEYG~YCCqyc`xg00&t
KjmQmLme)F5)s{W*kNgEPGBv;WRx&C{swa#a;gLBa>mb&S#c-%P>W_V3R!1wIpKE4%n+Qh5!BIjn@Qd{
_Ee_G0@>lM6y(A{n%3;tZos(M&raij6uJ%!-A0JLq2<Ka0k{?QfxFgT09h>+tck=(^rxb;@ikTIICqSp
-Lx27$~<PT7Aam8Uc>%_$B8H@Ds&FlT+6+{qj9Ps1U8Xy0SZ!>6BpIoA_}f%SK_kn9f0!-UbeApy{S%$
&*_a<yRzIZON5^1zrg>*sN9H-Y{uUGD4h<4@20SRiH1I#Ky-Z7xbPWVxqSO77Lu+yTim#Vc;4fu2~1v4
A2L*>F*QPEeTx^~G;>^bu%m%>ENOEvvf$J9ZfCG?6FWUgh>^45D^8u&lJzX?K|B!&CYq3Fq!3;mM`}Y-
lydcPQr_Rtbl@_8f~~UY1-WF!Cd`A#V=E1qb@IquekdAHr82DGo60G$%rH^fV~%c%L38@_FuhR6o=JDf
(djx^E?jV{VU+2GFQ&(z0L0OF?<E;bm!@^ph3hYX`c+}mF5W}3hw;Y1f3ION5)?BoRKiaE?MgU*AJ8_R
AK9~Z;OOBQd$s3H9A8zyd!y8&I?*E7(}I%p3?9Evu?Nabtg!OqI>KrWKyipS{nZd$I!iol^q}}CmXrkj
h#T+<J(k_q*vB7A#qK|09Xd^nJwsrqUcXK|KpRa%Ub@Z+V+^XmZ!vxmh<`Rd@KL|Wbo<67JYP|uX$Kgs
k0z7Tp*v~5H|`%6#X1=zxJxaC!Jsm8_wkh_2qPP=*f#V&=TLH&98}U<%MOpFw}oBXUoM&4;l}-fnpazo
Ez{z@RhFJa1~~qCpM4IvP^$V!)e2anu|Byib(B-$1!sloK+QomK1_iX&ZiKFvq2~@WP1gf;OrQ}OJ!`r
?8)P$%lFpf1v>#*3-44i;@Vsth66R4x}bpW>fvI=u~qAmN8BIc{RsviBSf+E3lu+d!`S-JtrRL6wo1RF
vXbA;fIK7FEHpImG|Q!vyP2A!`{C$~u2=a8QUpBUqR1xsVr$~zc;kIo?`gUD&}TaTwJ%Ie@1Z~vU{eU5
xBQnLIqKwwmk6idH;VKkFk#~vxM&RkkUb8}!Wcj7PG|iFLTiRR<L9Mo(Ja2)HH$LQf}7%c^JG&WJlxb1
xz>QnuUy;2>89=y9aIWW2nZg+VYyV?(lMs@;DprVIta9WCYP4~1{L)m4)i2q#$4vC5$*W4cszm@HtPWL
^>z0)vL`09*fKR{7PT>`!4vYsBgxDABC*bd@p-b#lyPeDZptqM^G%PNGto1uGhrI4C16HNvm<}J0-VAO
<ST7_j7hdXI2L=9eXb<NK}m#EiFbdCdc@oMBK4DO0Abc1f~+8rBKg96vxsOaPO+|^K|3j-lz8Kyd|bEl
&c+ot;k1tP>{;G3<KF!zIOi=DNhk7iKgisf9z%FVRZ0<G^eQ{{jkOXcsE?9EKCu8AHMa`8u|#uLKm-dJ
Be*E+bzACLmHqfjIZVcV1MQO)DF-_lc6?3g`9uk;FkL_v{)N_J+!;}>s<^bT(T)i0cm$yC&w219(lmYN
40tmm;jSHs?*+mV5_#VZr2FZR$cp};9JA+|(R!xeH0`A_&XO`++A-#*XTy~9;bXC72utM_I=0S_qQ1~h
Te;Am%r(@Z!RR#}?rN=xwa49S(%uoXf{q2`244Bo3DbTgGwLSEYB5#^q^nKyoYre2rBdl8@Z9UfZ|hYF
1=k>q(d69K)FkUePRlxY5(fa7rHiGN-O#lbz#km|zg=m%6U)@aGkZe~;LW5(o*`&tcyx9AyyqT{2ZpPJ
O7zye2@`yOf$Fb8)SM%fE(>^A>KQKcEwS3b{Ru6ydQY&r+B9!y1BI9Vp%Ubk{v(ada<PVM2?QvrmO)ld
S>D!6ePmZ3YxQh@bC2|@u0oex@(36p-z5TXRe@kG322#4;F<7qzoxMr?<CWWv?D~l8alvI#Sb0=Y|-gD
NI`jy=2@5FI#u~y^iQ=)FE@&}*m*SX^aat2u#dl)I)7FyLm4)7H8fk(S2<@L!02Oz6o09@9yBUB?Vz=C
qZk%)p?}PEOI&~E(@Koyk(iLBpUthS-CfhmObAk`WoVyUGC3iMTz+O1sRPd#5I@W2F@VmDx1>FLL3Xg?
w+73@F9%bCl_==ji~cPxTGaW8RHhfl^-9j^<E8n7UuZ#?;jk6YW`sKdwbQXP2rgirzvl+TabXf?NRTFh
Cr=eSm>x=4v*r+!Y06Hh4+9B{EyDf+QgC`M(X|wUI1j)G->Z7RnV-&u7zK&*>#g??J=Iv)mb>@^TTi9K
S^k7iaFD=*9d%Sl$p?OVp1katpN`)1&vHWADb<X_BhZ!cQ=RXc5p9l$XJ-y+U?aXe*<_>p0{lLJ3Wj;g
#_Ntk+R`2?8igGhPbOJ;nlIhJ5LH($!sj3a#*q;sIZ>vV%3zEX64#zj+n$A$E{FSV<0y*G_MJco6!K`Z
LX3)u;?rkUpq&`NLICq6kdG7*bQkU9!MhRTumRUkvNXr|mH929qeB%5n<7_<5sXg>)jux|9U>Jxo>LvW
&W@Re^BbLTi(#XMIMGN`a|0Qlr=aVF=i$C)n)hB7;{m#{T2t<C$8uqV$S*7;Yg{oW-cU1cKy{G~$&)vC
4Nhs<@DEO957|zB#MKIViixJK2kTk%TvrdtP9wE=(K%atoqm*vTs206C<^^P;5|Y_6=DeNDO;7moSTOl
tJn`%V|raQx%ugMw3N$wg)Neu7duIzCnoK~MkFp<sy|K<B>eqI;*=>v9DPBv38`}WJA+Fk{JsZ?9T6g!
6v~00Bf9?{=A3R+oT9~J<!TXyF!ow_(>K>}^udRd<%o)9MD%Y<btr_w*^7`HX)+iiMA>}os;rqR-xyJ;
!`~_*6!@sa0QNCe?_>&iN@&8&z1a25(YUzwm0%M=1`&EiRW|`%Ml@z!U+@kPq2}sakH}C^$DNIP+Vl3!
vF;mGm+XoMzMYRX5{A{Z$I#k+K@%#9YvXot9x_1PbESbkaME|MQbz5#{3xb}@i83Wd^X08)r`G7$$APi
h}3u&@@KAwjB<Vx*3BcRliHDsV|eE^r(8V*8xQPEucWJUy)5m78aH*{q<{a@zA+?mVW?wk{(|cl-aFM5
vmu!ZvlPWS%{V$*K5tUjVv+90bI|mkmsuauA*USQDrB0E>(k}ILfu4V<bK(2UG0zXXR8SO&e}v9z(ac~
<j<V3i=m-krro|`3k(A+_kHJ^YaD0FuiBNhJ)pm$d!Yg)T()C>?T*E<cw}P+sK^gPk<imz${ZxFh65eO
{_bDx?p_E0MtY`EUDI+r=D;|48qFKl>fbpmQtzN*)TG2W@^N@aCPlSZ)pm-z6=a-wr<j>Zq-axFdlP~J
m3Sjjvy%+430?^xoZ%t@56sHLyo5vfhc-P0zLJtz_0RTfCNG2Y=k>Bd4gZb?)lrhSf4RLdV>yWY&JTnu
d*1wrzt%Vb=L|}hD<Wl-^y0aZj(%uWGmd8oyFtL+QFjV~-!nZBFmexiZH#1{B609O@_-P;v6E{i2n!V7
8)_WwhjnbE(W;I^(enCHg;i%++c**#%mn8iCy3d9y4dwL<uzlQjmQ*5l=IHh0^wMQbU(teJ#VRcjm0qb
25HP9YcBbaxI-&Pt9!MQij0^<0W(dY!Efgd#R(0ekk!v*0jZBzXuOv4T=M7#oo9JnMNU5t`m2%ZprM1g
Sd62@xP}|zIEpEr%yvby*P|PI%NQT;jyKu~HEq0^Pq`}tZ%(L=V+`3M09H^J@VN`X5NvU|99_pK@zs~;
kRY>d=}}t({`b|TsB24(2jfEEhUkj+e%d>5zE1tC(wn?{C3G}+q6uC}I5U1k?)oG^t>9ac#c#@V4>Fx9
n<k%UqiG<D4mm${6O#do-wAZ66pgkK1EL<y_imO5jLTVOI&+r>5Z**!IPCXN^5|Hr@853%-o7TC_v3PT
2qDmrW645C><|E-A8WReCl&D?$e6dH>l!Gr<aH)a8(}5NPoq{fk^JByzpJr^8noOyE%~BI0-tHvmGSQg
B3aP#!Jr33E}8Vdz43{-3e2k1O{2{Hm-ii6EJr?789kCkF~ajU&@&{7G|H+G-l^CG(x+Y6d0lZyg3}H`
NE1j$JWf<EuquVD#|GK~13zsj?p#juvz5uRFdtlS=0eIViTz(-($uLz?WZK)VtfN`CArt7<FT3<lQ^)w
qbIgtMOPw-x{5u!Wjmxq$aKjDFXO(9SYZQ}9a!N!ueE;Rj}hmlFG0D-Gke)=aJRIgxodm}#i1NB*6S1a
BHB5kyjrE5dcj%?l*RAk^KM1123Gkg!8*xUg$&|^c>LHML7TQ49MoQou+TMe?u`DzA)jr<%Hu*4^1DvC
h*~V{UptWb3x-|;;Vr5_A9Ok>&Fgw@hl=G7=B}2kHv1`MBY7c1jy)r)h$(G6Lyng679p93@pr2a*!f$C
Yp-Hc=d5l2M`jmL%66`5yKA-{wj=`y`0&1QrOWkrV0^57v%3hkZES&`DH}+V1~)FgC;"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

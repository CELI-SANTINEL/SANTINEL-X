# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "disclosure.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("ccc3d41d23af7466f7997b02cc79ce1581788475176580373b0a4be195bb53516d4d0ec766ec0c2cf5678722798d48ca59bdca32c74d8ec056a3eac727455258")
_K2 = bytes.fromhex("6c06f31dac5db8aa9dfe50f7318320607540f0389df2fc23456d0da4c9084a3b5cd96273ce3bb8326489917b543706a53e43694386e9963d440adcf209240af7")
_K3 = bytes.fromhex("2ba7b893fb49221bf0fcd8b37698bbe0667f136d19cd235cc2c37f7be437a14182809064bc534600e678303d5ca2aea23ad53a02c5675abefb74a77abeb1cb03")
_S = """^SCn08Q1lY-~|>ma!&_=*A4Sz;;$|m)GwWrH*9;o-p+3I(KfwDUgCW(S57O~=-LywXzgbxXlvJSz>UaE
87b~%VZ3tKx8cE-iAV)CY?NgR$+{uzIrxAt15H_Z6I5-lUYIh|)~Vd8Uynkr=o5|BbPs-T8WUY~e;i#`
1zO8w$Lt-z;h(WdTR)M7;SW+%(SLvcaeZHREeIQsg_2-n+t%1CoW?s9U3-7Nlab9Nm~Q&{Ij!VpMNQG5
{^|dZbet~I>X^?)q@q&&lD}pl(|LbD)TX^Ybp(hDv3&hx7AA5iH?4+eVH=dszbk{Ifh$C}>8Fs8k|dH=
iVdHE^oVX`8k)0I8({I2bw_|95ZZo-jKn?8p5&|>wG8{56sqztb+9M%agX7eT{2lFMD~JLiO1nmpwkPf
M`J;esJkN6^qHMUHE#`-E=mU=7}|P>hl5gXh2?CnD|q*^dW$KvL0}Xheo`C<x|8Wx#Vd^Q#bdfgRaD-?
L-bm)TL?u}vNI_B;PZ-c_a{Hf2@VTvEnB<;eUpzKyjrhv&^1s9NA7R(gMF^p`H4>(&?n>Y!APgKGI}ci
jw8}sI^0O(HQLJWGekl4if?bFF@CJlqt|b1-Q^93L7p0kaXpFqCEQ;t-D$1mG$zd5HnHgAfKzSdu`*a6
q1jcr$m*OjQGh1sZ8rQz=<cDHq#lwZ%@UW+7KT!A;p5AmZjZNL98L^DnjY(O4`(#Nb17$M*n-X*e|zS(
X^hAG=s>S^Qh;@JL0r(n$L2q9AIOAw4dsNcutAODo2;_P%+AL~^i=KCE>Y!S1%0g?F-vD6J@6+VaJAqm
KJYH<>+cL)_R?GM(nt1KmuvpFs~@c0d`MNlk0GKH+PB#G!UP<1A-Kec0axprxVa%0Fe%(>NntH%7;Hs2
yc#V@t7GJtP&da&9m^npjQDB`1>X`LSt)zITjA|<pe&$)_Or$b*;Z;3dEtCv?QI7n+zyM?qkY{D<0Bz}
LS$+qXne(8!v+))KxgJJs9J&E{I)qYrOTel9C)LPeO+G?dUj}qy7?}GXCmxZi`U;>tZ9zvdqGE&;LbVW
l{>`-Ab!@s#NMO7hSV{MDn~$T8OX?f<h(U${JiO_{M@K-Fb(jj8bak=kkS|~Y3=bo=`!HkRf+}q8ac%F
w}%b8#ljtX0>`>7h2BgB!FLo1K7$GX$+Pm8-6#^x08HjTT_mJLkk5BHrkWMlc-Jtp>et4n!|@#CXTcXq
sARtKweUjs5Bp;*F!={un$@RwCwhv8WQ3e1s@A_q<cXzpuAKOAUJ*F>V+^iY$(dDL_U}Gw+qyc`kfVW(
T<N(N>1zWK_%?b6wu)Tjc}~V#L=WoRk4Z6!B-vT+hOO<C09a44IAMG6C(kO!V{u?OKIqlJw2tC-Ej=b>
*fhk61I+hC%s~iv{nzVN;WY!j{UX_ydLG0uZ1NiuJ36P<Ro#%kDIkECL3vS3=g~DD1v#DPL>4Ry_5l%3
{;Qf~pU$^MyMrh$K80ELS}-PqXr5d;B37BKh3{8{`2t*S7a=l$E^VZPWhGh)9Hiww?t0^OZlF-GDy;q?
ebYH<3X-~YI@}PgwkTT@Sbd?Pc75(VD*iEpmNBG-+VC_&-xVnIEZO(HxS&$|LNP5u>IK1C3c$5i&qk+4
k$RwjY)(>r^@qaC()skzlq{wsIA9XAqtH_Y{Ue?Y=fPD;9k*jLcFdFHC$+3OX+|q2=|nu7IeIo;%~yc?
`Me2)792Ke02Cy!e<VR@?XSA#Ck?8;rZUyW-OIS+brRKf=M!a_PIO-DX#xx%D3Qd&;knXSoX03!-NRsR
gG-MZDki2p1m_;*4ce0=lP2uwOh{4Gw9Ti7+8PIB_<x9spGb54<Dq_t=<#z#{Tuy{MwIrmef<)w1~mTG
l}zSit<U@|U)5QI;n(#=auhISt;LOM6O)P*Wh<-JsSzt?T<@cXd!6;29#V<}Hk>}-rvM>JW;0LA$o(|J
92x=_8Udw#obXA(P&UB{PzE=J!0`XV07~@DvZJ#O4+0?-dyb2szh|85&KK^?8g?PAuP|9Zx9yri{##t7
@~;svMs~m?@rd@7HU9!3q#G{3zdogQN<lzfLAi_jm*=eU4Cz<wU2X~$>Mq??T_DmL#otJgG1@@$Nrzx=
8!L0!3?ewo^SHT^2{j~v(_FN<Zt;0grjNzl|9o#+_Mg!rQ5?R;lYh+|wN#Do9*Qpw=sXdZNdiF=WICm2
#On)1OaNMA+LUd5ydr)VR0!uTRWvK3_!I9)>jrry#<5O%lyMp}2?MY}c;qQ6VlFxldW_O%!NgAT@Z*ov
QSUES8vn)_@ONcSLz?SAk9A`u(Gw`Z`pN+vC8$V&T_Im*2%{H&6w{c@N;xu}oLF!L5q#~b=hgqW@{Uz<
$kc=osV8tv;e1sn6#vc)M{YLyalhLGvPKUnHnYpq&&;=cuBwFw;-o3{HA!JE+$0E5BeU-qSP}WRC2lQ}
k)8X0EzW^i!F)<RvR>Vbse($rr#T4cz@{eMUt~xXMw26tYpjnxN^mGg7H;=4cv<({b8L;h3<NflaWF>j
bk~9*W;XMZiBwU~C<>>{rv9uQj$+qtvj+-!86Bnk%n+vfwRAkf5J>j*M&>NmB8Q}e8uaM>oBhr&cP_$=
bxx10fN5b+1>gt^YNYdsIF+;3qoW==d)+lm6$}2f$gkIK^z#*=L}}$b)OAoFf!XlKZ-ld4E%toU1qOG*
^;P79Z55h}GB0eIV87mZFEDpKJf0+1lbWYM4AxOI9-u6bkvX5>*aneB0mNak5X82QWo88^QWJL4d4m-q
c0&1|NdwtyP3+@eBo;Bhe?;=w3Wx5MkKgVw+LMwtT0{D+%?0S)=u$wt22Y~UV%lY^cjWxcs@?>tcoS-)
ZJn#doh3%2UZfrjcSfUj%HqI}(G_8ZgJ~y9_R&Jo#QAgQ8y3L<=Bc|`>qnmZ;#Z-__VY2c2{TI$|8YT|
e>F%A&NV2p1r|P7g{?@LFEY1PFo;l|V%c7iQ}q`4$g%FP7qA<U_przEl1}uarUyySXE@+UoD+bEq_`zd
aFD2)pogWaH*YdvbTsq)lvbSWSFaYc!hEtvZ!!MkO=`^2{kz6`xz*4v$^KH0|16#TgPOoLzuq$3z%@r4
<J*aCSb(6WxL?yh`JZ|&_$2x=KQ8|BaWa+Kbe7@2#u{zt7Ll(zEX#Sj7-g@kGH-U{;h0F)gbMK4XVxf;
E6`ak5diOME121x!A2IRWOD}RvP`NXG{HXtSTMg^JE!1yEyXo#TAq|9%1>i_M#g5~XAO7_#jLW*`o1H;
0C`25l&cB&fpsJ27TM;Xy<8o27j1-sA)jK^NS5Ie;7diKlV6mTT-}<D+pOr2<_+<WG3e_T1C#5@vu+}1
lz=yEbSY(XBUpH%jzCg_xzt{}hSHOW=LF{*$uQ7xlS-olHfSL3J~rGg?ka2qeb=rpx%zSShEp5N5Gmj+
-Qon*6ZZFPzj(LUn3<0y??TshUs8Iidgt3bp~t$a9x@*wFvU71|J?q8U}WtssIzWfEi+k3S4e76tf=$y
794E(sHr+4hA$cKTn!rS>r*s09{u4ul~I#|J}YZ_`|9rxv%8&l3_e;b*xXt}KjQwvU@f>161@GrIJIGk
0yspBUc^c(@fOSywKl8XE6UiJ)BMn|qBR&}rxtjXtldO;E2F@QoVjiU3Kg(AYHwefe3(V^lvfdj?e`KD
Q1f=;o4jV53FJ(d2pjI0HFi*xc^k$bch(5`XJfz!3q)$ZRp@X-VQ4}1KiTVZ_2JMT0|TJ9L>MUQDLm)G
s?n<`+<>>TAyfL)Wjv8uO)`6rt57fQ#Qn}TGSs|$JGbcTn)-$rPpQ@)B;STtp*e@-tSSsMfw;gLbb&DL
9Yr!ktzmRFUNvhS>ZQ{|vET?`imj%5^x9YkmeW{}zRQ*9d>IcmgU84eAN_#avw3V&*1fEm6{_yHSkG+B
^qww$q-0%`BrhnM9NZ@~y1GQ)jG-Xjq@PtL$Ck&pYCXcL@8^x;K5Bobi7BazV6^N7`+@_#`%JJv==PkZ
4HP%r_7>Gn)tDjy)?Ep&m@`-}=M6=Rv)Lxbra48{a|7tQo|;LLoMFvNGSJ^VSRw?>(zyecHV{?e&hlj!
kj)V(g1pmD#lKw`KaCpWkhokrB#>UKquE!&7O4s_kEoaJtr+X*bz#F6o{hPDhdEJ}QpZXSt$bNnHH_VA
yzcHrksvlzd&m7jqhP|WYY2K&n7qF+agK9fSkN{+c1ZG){{l!<pAeZ30tbXr$jezU?F7ZR9vycOO4vD5
z$F<owv<5(*v|`I%0SY%d&4M~TIOTTsa1G#n~oELp+DDb4bV$Typw)%UNV&o%w&(tahJD$BLy0ViA>KQ
jUOFfeK+kjAoD4s86NU)O-zFK^7cI1oGdO7{QQP$O^e+s^Q`~($nT^Z;b7n_7)()x9Ud_c2mwYVcD?jr
w;M)VRlQHm6$aHU0Xg};`}UJX0OL<xfYPE8tTW*Jil6bGOlS~A^V7lY9gQ2ksx1mKbLpuGurW>RRsKwj
rx*-tp^+K%Fk;IlIVzX;^<Ya@f?!7ct@W7Q7)^Q_IMFZ0FZ(NeZuGcR2rEKY)9Ak#YIj;bFTavlyylwc
xC*olQqf$e6<$qq@6*Ko76QPj{0$~gQm_hV08`plR5{9|iL{$JLBRR|&}M7s8)r}c-?$D{OYlc>^kD*L
ovDw5RPGnr_$oQQn}=$9r5*&ERybC}A=&C&+t)l|d^E%(bIByk7$@TYX9HujQL$Upt*-Fp-&W*9$o!_l
IU^$#RVXjbFqb73?m=Rl0Z9bA9>R0fihZJnODu6|f}c4nITFfw##a~j{5i_KVMQwwSfL-l|Hcn)-0Bjk
r24blFBjFiDx7lB-0KRq8n<kuz`3ln(;5wcd;"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "wpdeep.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("9ecae14f90f1a153b325c3a70d421c420cbd98670cb9dd8e010060930c2459615edfa205159232c38bd7d7f917356300be8490ec3c433389f79dab9b2e996c18")
_K2 = bytes.fromhex("b0bad8747e331aaf2e1fc64014869681f421f62dfc50847f01f6092432803f5d8ffa32e09293947efb18df615d14d591fd996e3c09ee7347327c0352c58bfa93")
_K3 = bytes.fromhex("811d0d11ab4ecefbb87c8ef5a48399a3c0b95c9d84caaff3e35c51fd8c29de663889d76cdbfb7a146289309b051ca29171e8de24eb195a0230ea5abc773e74ed")
_S = """*SDE)F5qs^u-KB^O=^MiaIEHBpzu^Da?l56dxM<=XUQBN8_Xdge!w0?eIA~qRdZfM0FqM1p<;0_*8Zvx
eAwpqE9qfx`Dp$5)BU@}oIZt*)OQ~b3IjP!Nuqe98IPPz8A}AxJy{wmg=@}A(oFA7ty`ljYxr*lTd7Bz
`bp;P5{(Q39>ZGd<I9}K0IK2BS%JR^qWO%1FkadK>jcvujfjj6veQf*2WX(0<aHEl@Dve^U#^D%jbv#L
k^nSAOwm7(r1BTMy$A>iD|kDdAy>mHHhPW9WL#r*QTd9RW>(G$`OOL0lXK7~^nOT4#D{e=`5m-2J|d|V
hXUl3{w2V^fZ-yk8u}*F;3J7+H1X_EMzCUV>DK8HveqKrJFS=VtMh?6u|;pPfIyjDdl92~)}StYr-`-D
*;<32BN?t{f{5RD_7r$8LtbUE&4BN8sRdM_vp#TeN_jKx2~=YTr|*rX{4QbY`(NxD+TzWnoW)of8@bC^
8`}Y&^Nt&$vi(u1<|ee1@{`=LL~^FvbxsH3US&9`0pKL*C#i?xc@2vw65E`l{zxc%&HTrO`9tWlkBg`t
{(REyt+4Me<NC8*Z{>09pG_c#MQ-;fLT|VL+k_Zsv!?GA%KLT+_r?-xN}X-AprZN3fH^*k(BpiM#oPL=
-?1d=LEuZE(j)_O`Wms!0i=K<h4>yG|9`+3|GD0seDrMSn}(zt{O<8Y>*r<A5I+cI7bYLi&>>M#QUt41
<-btlPshjd6o;{zEwdl5Kb<dupNp?7Yj?&|6-u8Hrk8$CO`c(^8{Iw1cDwOBOlp9>x~PWpJ+bOEP_u&o
w<Dx3`AuAis#PO0x;-1j(>a<#MIC{{3|q<8>!~P43Na&S=>OTZ#;3}8SM3lNYod44_D|+((ui)pRUZud
ExFa&y|Br|1QKs{31Z4VGCS2FSKTm(DRgL#_$Mx4eny0I+M_NcuHNqZ$q_<aI0x#in_)J!vQg+>POm^j
`2lpF|L*0_Mx3dFbtM(B%^sK#<YL$$j)B?s4FK7YE|W(Pb~e=ab%Fk~!a|2&50I!$doS+P);%O3o?VJ1
CA_}z%#G>8)5f|?za&neXEfh%kbA=<B3!F%-mjfpi(m>!E8}h3=6E;NWEaysN^<CTMSV&O#mGs!1h#l8
=l~Z{Lcnz3k(KC>CMS}N54gndEwDWu7h5zTDC;63KSkX?(C|L6t$ol26h<oGH2D{QhMZJRoq-c@MZ)Pw
iLEy)MOhzHD8tV#z?s@ENvxl{5YU&2JDV|Wk{Q+LmIN}AfJdPzZa^UU=6`9q)d0RL^?vl)<22GSu2C*F
(V#@{H6e*@+*CYtrTM~r4k_*Hb5SS20vbv(AN@d)lE%7jMAQ$W@?R-Su<@aQ!>jE>cSWsd54w%8=jDCv
RoqMI1W9s#8n9#-CKabbEu_$0cBGFdFA>Q8Uk!h=+|)PLSmvtxySx50p`j_~OyA-4v5~;v2)G4D9QP9o
CiB|8rIN4q6f|f$8YyIdI~cqaYA|0R-Hi2bjk&p;dBZEfC$wc4r+b-UO}U9k|6MXUR;)=YZ5nJTj{)d(
MyC;R@bEBcv>k5*MhkseS*l<UGqjbzYMvPAn>G+#XB05PfbWyNwU8J|fe9Ta%=gZ{Ai~BM=hTdY(2`&A
NBnoJxfpPyE=Xw;&*e8c@2)NNGZR5GO)J!1V$*mklL;}~&loP5g8tkO>8(oKm37EuNU6#Ol_Aa5HSh+%
OUGsbZOji6<%KL^Q{E`~4{OiDkA)1GsTV@Q;4;S%+Xjv_Cxscq;n{}St8$j@6a!oJ8$;bpaM=~d%#4p*
#>`~p22AVr?GT=nDG`Mcf<h{{?L|tVLbyX#*TKkF9KWd#Rq_53G@9eiZg@`5q9Iz!4nPRYb%HRs>;g39
!#-U1p=fVLw?3^=UW8z=KE%-^^w$@2Zq*=Bv?@k67nIiG3u#WHr;a`ETKAmo0hKsrwbZvQKcx}Y`fx(p
QJy#<Rh$%VGq#JC>2%H5l@X7{!?r}c%547@x;=y6M{uEAkqS^EWn$Qr>hk}03rPIBm0sJeokA0wU_N-X
-z@XrjA@BN*W7oQK|I+nGEPkEji+^qpJ!mtt&_I1?=M?s!^;V7lN~DuGgD_s+XmCpNJU^!QntR`D??<5
GE1vj!)4lq3M3Y;BI*&yIi)nnt9)aaNQ0w+=d7(D-&qsEFlV^2rE?71*q6_Vf)Wn&;Cq=(_hT_x;#w$N
9)@UDvjhmy(4omd$2-qt|0Z5S2k%1N2$m}<Pmg^gQRO(nmd>pQAvlNB<6qyvkgO4QL#XvAc9$`b>mT5!
t>yO{3z{_(w;`qCKRf*X>88dxHTVu}VlY~_bB(iqb}411%(52k4vC5d%SMR4xsy@o-6eW1^a^cc)SGb;
r4J)WXxDylVah!VL3#wgQE=3eeip6U4a@*o`>9TBPoHZwYy}>B!pSzjI9+|$zcWw~a6I&NUGYmSZjzu|
n0ev+>E#}gU@<=*N^=%#iV{~g=8bLGyt76tO66F&>W4t9Mt}<6P3y6?IKgPoeFFSIBS+F<NxM`K5>UC{
N7HBfH`^wY*wAre*eF-GFL1@W2<Y`dc?~;a$!uDtEF1a18$8zJSp`oCq|*IMoIH*`9O0}(FJ%L2YG@W=
Ndd#5uszH9daH8RBOIk~eoOfkj=i(+zE7&L{Lps?lxak`3a(yvzPoAqG}r~52Va(&qS3Z|jjEN)`&z2D
+M+u35}OH}o<;5~@0VivgXvHFA*ozBodwpy2Vw&!!^gs)g67vYDpTn@{bUAyTp2mYcfU<Kv46?eb}@?N
25f64+7kJhyBM%9pq6V_NPn!&fv|j(WQcUxO&xm9bL;vMntbE?aNNc$a1zwC*Y))hH?Wu5Rng9<1Jbz*
(lxL{KNAJmqTw@mdByB-C+rm{JtBlXP~$llTR2&Iut9{*=pMF~e!ggxKvcc0PEj}yc5fcWO5G7w`rb8Q
cah(4UW(`VjcJVL-u4Evb`knIT3=F=Uw1VzPYV>?T?J8DgOI&Kea$T(I-ko{yOo~eSxq3`6A+Ug8cugW
4w=U;u}7ATP<kwjp*RKH`4a(01ylFejl{57lB?=u80d`+5i&!spKY1c0vVZSI0wPK-rWsBQgSE*kd}>h
YiWF%OIfq_O&93f#}1HvnWwhWe=#*;_02a4su`pqeRSXjM`&D;QVUQ~{1M#g3V%svco=J2#F(*XCum`7
teO=H*u?Z^o-!#qrd@a8jCblhNK2KiIZt6H)H(NKKbs*zU52=TY;V*tPessn3stfrlgxgbAqq&E8ClV6
@2@MV!JUOJWk2iNHfN9&3~@2K3*qEj@Jl}-Plk5<c>%7?FR4=s`y#t~%xdEnh6KF~WH|-f5FfXs`f`7J
{n4RjR>v1q`JnSOS6R+-iZ;)p%Kis;KmCATZd(3Ywd)7t6JA_ctO8_0)VBK}cjw^+$xO?fFf;vh7^Rgc
LiN;~A{Pg=QJbNmW@dWeoHU^EJP&4C;+w0;igUJGj`hzm%rlwc6yEIzGjFz7u+|>;zjH}}pJ_Cnlm;Ka
xQ*-uV$C57J>+8RRN~NI0^IB#(V!Q!-W~n@oKZ#qQAWbSjlPJQlM=(<?zo5Z6=HmYs#0MVSB_5_av`;f
75K|rl*XiZGrA@2ilPFI=^PG$DBWd2Xw8?`4gbco1zQDZz7%W^>40cI!YB?F=@QyDlvi2RV|3sOUhOfQ
^?<Z18cK4F?5%-<Mo>sqm>zWK_o2op2N^U~*6_A`@I9u7+rD~JVMJCnsF<a<J1|1b;eRQjbyVtWZFX`h
)e%~al1E=x?2p#w1bb~E1i;o9M32_>lPYocVQSi5W1~SeeEZXx1&VUFP7%<`IuwBQ2Fg;V6<g+-c#7L6
t(7a@w~(#?emt6Xzb{pALHQ-`T#sd>78P_NCV`!dg~?b>y>ua_ghRD4?!K<@oJRms@Car-0DwV}Aub=?
DuU+y3(!awi+PhQ$zwqdw>`X(eyux5fp0B(lywJw%%6JMJ@*P;3F!~ruLI5ADJ0Zcvs*{@!CXY0;Opwt
964<HGQ%3XgZv>#8-?kCWB&&#1ecb2wOGG4Pa##rGaMgqvTJk`=*WUO8C-~0{(R5l$a$>^zad;e!bNWI
o5P_VYgbkx$TbL~JJI%<Bk%=_L#-;V?|sjQzo1mbHWL$(jV$8-aznm^+NHAj`&JUzVM}xk1sI%Sp5CD|
S7O8qMs<1(wLMgHy)#D2ArBXTfriH2Wu>8lXM2ju7W`le=s?$boecehsk38!sO$X*m6i%uZ)1f@PFS{R
a!Bd!y|SR3XkVRhpJ*oAtP-!uaHNnXg5ZAIysrKkJVgzqLOBA-DRhk2FLz%JmqGOO`oxe$m17PiT&89b
IDOcb!9-JKz>~y>RzI|fTyaUH-6f7uMAeU~=tOPEnPHD){UtF}-<Yt%QS1qwFH3ipgr4A1kbN3XXFOEm
hu+O2;tBLthKmWUI-CiqCk=8rQ<$1tW9O;fH`GLRcq!<arA8>_`L1!sy%~@D?e)UwoMo3#XFpWEo$2ZZ
uAWB!>dQhf%+~?$Y@;<@YVGn(o=7tEZjBfR^jX}c0*Wik>0hLm=V4VbnLI}8i=zupwyh7udQj5T8v=5A
|Ku-cZuo0n0Q8C6{m0_jVLh#uDo;$_>5d|L@%=4Ra3Gjq2*-)XL)nW{BSMTNg#1t40*(e^DHtP2gL&Qg
Watp9PSq2=ld(a}0+=LMEcV#IGR3i=IdBapU!Mmi5m6*w(<iJ}>XLQ%;{FRCY0OrS>;~b44dXk-Upbd5
0#uUdBJgB@8XBDH`8?&(Fb<v2=8T<wUbphJ>~V9I40UN-!^6Z7Yx7c*kHQ5Xf@L3|UT9T6^it!j_A7YT
dKWzc>AGG4Q_tOL_;;*xzua%<%L0mqjZh})DJ5i0)|LAlfbEzI4kWDsC_HFgyDxJ=c|7!!cL*V1qkcu!
+cI~f(PdmamgwFVzQy<oARzIg?NcI5N0qBIwG`~|8LLwx+@TP?7|}2nSj}#Da}h;|Tv+l{mfK9Otr#MJ
0;aEOKoD8TEP_W~8~fTlUp?hxcmC^`k>TSoJ)JCXj!>nBgbbHHJ&R_6Ib*k7Vmk|0L>@1JAX%v~FF|zN
2tD~M`Y{$Z+RN4>kayU>MO$1DmVz_lF$>of>hY1rhB8_K^$7!)?11z1g;#@4O$y-XCps1ecp8|x&N>LI
BY@%#FlbC0AM?d);RwOt>D0Z<94Uy@^Hq>*OvJmUNo{S6#|==@(iQ6G*~jsA{@YL2wz+8M6!!dpr~#TH
+vzx<)yI6FsG2-vh8CKARch#)lzUteZI3Nlw?z!&Vc-29NCqH_^BgW^r%a_?J^>CiH?`Atwq|A7C-|)w
f=FCM>Q@lt9J`&VseY2JF{o>g`2z70FP#_&oNdbz%Ekoy^y}Tl<-WN5F222K{v1O{e~7{?00@p9m9XpL
OO{nU@xesLYX7_O*hD?F7#u{m3oy$x`}i7ia(7#&%<F&?TD$!XSmwM+fGK_e(3v{08zeN*wX<ucT?OeL
&Lsja_Ns+N({|HV^)wgAefC_41SPO6g2rMbZ)mirj!-N17g8KAV6W90*z@M3@sBCaa`4!#&~StDv}EQZ
p-+v|K72XnK)L~ZkTZEZF%6E2umz?p9$1)H+mu|)%b(v$+$ji;=hP-=Rp!+EvGFZ?l734Owr^e6rrGos
Ges`-zyCE$n@9CEeCP$7ECZhQs;s*7aH`JiHXb-}8@!i&Ml0iec`x2nbq9FHH#meVH9>{TJE<wQo{uGO
JGxD<w2q1mV9<`MZlV!-^HwM=KbWu7EHLqf+zziIb8IQ`aB5&IF$17#>hOR-G<C}{Ks7J1yfo!c@E`u;
0l0aEVK69ec|p08aH$z`)$CpPqJAspV8wW!iyF+p2fNUvES0W#JuiUK|B-3G&X3tfB$8t<sk59CWW1l(
jz2~oPZ6#Bpq$gY%r3|h|ES1J!hGxcCM)ANQ*NL5E{l){6MTbH=$y%{$QDZurAyp#+GmXpv=q8T;q?Hr
{T<Eb2u0Yn{)hYPEH~ou7eSgT8O>Pq3%wfN?QI5;6g9lF2v#;IEV^~$xOdAEvnd-v-SY6yiObT6IW7h;
3rl>#w#=qYB6!<4<F2;=hH^ALBWkX_c_laAIoh+H*~5qEA=A=Y_s$~5OaP|UXo-NTYwkTu3?1;Nsx^uO
Fm7iOdFJD{o|i`6g>>+2xMn!Y6g`>*=!IgEj~#gN%esZW@7Piba@ftJ6I{s4yfxxV3M$m>Rqg{gW_21*
zsmet!Ji@n&+2vo*YKyUm*g|(bjSbrb?A{5-q((Vg&=N(*T<I^3D}^qBTO#b0)<PflI;&-9JgC}le3ye
3>n6AoNGTzcv9XA!ssDR*)(SY*voms<{aCKwc}DI7EH1VE8r(adN7tYxq>6KR&Mv(hzd!~|F|aa`pa}1
PoKV1ypU|%^LETU6`@A!L}6hhEFntS#3d1C&6>(K$aDGVPxmNEIn?@sS<GHZD>+vd-Rb^@;>TT|(X50%
%sA#Sy3@a8T+kjDeXKgxERlFgt_dx^)(@=u-YDFa04L+!Bvc~MP4|a+yu(uTBP_U*y*tEU#W5Outf1ck
7gTd~#rZW@NJ!p2yRuf<bS0VqlZ#=188{@rfZgZpSaNO1HU#@grA|hyZFo5!zgBQP&ugv&iq&-+b8aX%
kOICDZvbw7&9^%T`B)qI{;Gq`>Dmqp3@F@Mma3RTY=}>Qpb)H7a5n40;ojv)7vc0ynyA{<%CY=m@%PSX
KfFCu1xJWb=jSoCZyMzt^D<$*)@c=(F|uhK5b=G$TaM+u{e~qopn94&ajS%C%i=iQO^aHHd!qT)Hs;qe
$|+$t(Ax5%@OR!*=@O>KlCPS**70nzSBxGX?Ar(QSC4Y__AU`v8PVP>3bv2K_c&|ge@1GH-ccl9#*X*p
PUrP8;_g4{xm`|G#?j7?LyAeXzTr>7=#Ab5o|w6LixepVb#coa#cY;Wb8Vb8QrALlBGn{RI7rJ=H<iiD
*01$~k0(R+MR_$actFx|uQ2gzeLNZ?w18>!sghKGzSi*wppbc|z-S{4-7;?w-*6PS#SkQRSwTn_)0J7t
X|;ZmwzPiQEU@XsGY$d!8L<tb+g<t{DD9WArhVZDPzvb<^xIE3`6jN!LI8#h7?23i_kD|NF>J5fOqkY|
lqKBuevtRu#Lo1Ky0uy7+ezX+IhS4^ZR0nAL(@0a7*$$_O5^~M(ynsKp@%%XU{|anBExEJ&y4Xmgrg~k
OBCW+e?&$bJ%3d5%|4EN-_we(W55GA|EfK&7uY(T$rq&`*YEkDE`#JvM-8e8N(UL$d42>X(4Pz>-3eD|
&{?=W6mj~UY>anWl;&seG6CixGbYTa5<7hddomDsK{h~<d~&D3QgtB=@to)RP)F9z$Xg3buy%uka7bNm
B^_e+Xw3Djs-*<irD^PAo+m<6=IrQRmo6;_gWrxJ*#K{fHKK*TMA9EITC1eO$inUu!l+NGyXtc!4{KgT
RL@$rh39Kzwd9`cf{%jP^8"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

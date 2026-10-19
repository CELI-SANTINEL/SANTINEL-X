# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "jwt.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("23d628a7acc1b74cfc7dd5e7227164b17aa2520e2e8f4b69d55028cce182179e319da4a09f5922c2d45f0432a248e4937ec52135910610ac9de18c86e2d697ef")
_K2 = bytes.fromhex("d7e5217dd2225063a4f6fe2f1d61db5202946186211a4456c1d5decae693aecff2d1ec4b6d41d9d23d82353e93f6773cf4ffdb90076abc84ecba3c01714483bd")
_K3 = bytes.fromhex("e131d02884f7e809b49850bc32d6c4c3559153a8b989a4741fe8da259d9a035faee495a764910b330f8840e6ff6edf45918c69d385bd33e2b706112f2ea8b738")
_S = """ZP-kzlXw*2`Hi0D#+BKaxsNLL2ad;9y<>N@x6y=ZH2=AWWJ6Z*zNZ(jU=;boi73u21p>K?JpPqBdwss*
dk}%M8B$3ksQ&b#a?H;trv)IP<bC&g0C;NHwREO6C^{oVtUAnRzv1v02}_mJ#m!)lu0A4b!MR-=RLp8d
H?3L$dNE0+aCvg=U7hxfeEc#7V@iM^TE;c<m)M9~U}m-y<jv1dc385k7l=Wy8vPDbcY>B;$MF}u4S?+@
Uy8Mqb1vV46Bz{fIM?wGDPrLK5>26(Y7%UtW(QIki0v4Bx7FqY3@ihm>*DtGT{6_HUD5`s$B%D}E;O?)
ub11aF@7KOT{qcao9U2wFa>6|B$35ykTntUTPq?^^_1?dcZ#@=p~h10Ihjo6RNh8ZfRr94(pGWi-`2g$
jel$I7$|XfyvD3PkGX9+{IzLM8MFLnwyd@KDsNkBtkZ>k<`w8OgWDnoRe~4Un9wh|vzyc;ZlWe>L_Vmo
w-!vJ5M$+(@zeHtbC^K29Il$q`s-vMki_AxS1l&6Lk~iasx4{hEKjCrqi<H)j#H}`+vac_qWQ*hhx#J`
MGGl+<uD|tq%%lmiU8qMCr)=FJnAW52SpZK3ViScSZkIJ;VzOWrRudM#0&tPyy0VVu9J+zH(a&FHN6oi
ktU1B)fc|&_%7@&s20L@U@CP&6%qoSamoET2SOO^hWb&nCg&;GP4i?Fpc~IXt+6%@48?LsFfe)JDrS^7
`p<Wzk84r$QE5^o*j3A$&#|{xIVdlhqP1t-vC^ucT2fcGdTGB^tIFaYUMZpt9OLm_8$j^~{_K4Ik%;R|
2|$BIjEKXP%6PW&`A*C%t*w9tacOWIu-E|l#x+BewDVBTxh=C;5{`zZtG_)qk6EozT(;{LB5U+GU{`LS
GqncEK=ln6!07oTfi}sgL%t-`aTv8hn;cQ550asUfxpWWu1-g191kxr6#|c^uKIlMc^s&Gvptp~=1A@O
0FnLCeS{feHMA=TCE|aaCxSe&$G0lUsq#4>#8p*U+18BSgWKZAz<->e{EF)WX0&``Gb5t&z6`10H!MiT
{Xu2k@gy&IMvSgUK^(3s6%%XHsD%*wD<-B8O=`$#Cm04jKhZ||MFFD#b|!{DOw`mMo%A!OmoRh008B@K
gjyCzgTv^+v088m;3BTGoH|k1$p5_Eu}M(@FvOq)!o7iEF1$lm2eb4K98~WI5Oqy^xGc%FN~dJNfAD8#
87`&NzNn(-KF&W1`VA*ECtb|T+nPi&`K>Ndt(gH8WA*BUef!uv0wzcfI<%UPP-VT{Y)>3{JVV1Hfv9$l
XAJligsQxhHje^7lfNeJQAU>8fX)V%DLmWPbEk4-1tbM_K*xUgP$rrtzH#aT*Y1LDpK*>ik}UV9`ed`e
Dvdf;Dvhy;9ig1OIEo&XF$ky&bBr3ca~Lv6%Ti;Mis0-5NVQMKcw5cl4oo&-xZwi{`w|79!dU0{803lI
PoS*6+imc=P6*{3;w-&w>LxDy!tuZ~i3l=b!ZfYB9k=_T9=$0ydqFer&lEaqRr)z1&n9kI336|MDc(R^
BHp`%LQ(TJ_!qCpZC_`|HbO=wOvNgA80Y#FRq(DnO@#H>!4=~N|F>E*T&AA!GCsAl1B(cNh5NPMRc;e1
a0%b-e_n1bfY2!LLg$=?6a(VGHy$lldLs=op+YW1G(mz!*yU`mA|`t1u|Wrgvwjxhw6<=0W1<Df7?Q`M
X~D%AwE#YMF_pqZ7r3Z3o*EUz{b$0NUEg?8IjNi?niVn!PLopir9L<&zjv^l;zZNbf2JchB1*)MO!#4l
{$-}j<uRNiDWsj^5Ak{HUN}r#O!gKW<U-JHWqf$Cdv5UGXP!SERv9#7Y8^cn$&Fo|wTaTErsPLeT%w3H
O}&RINJ7`N#DDPS0^82<?5etvVq_S4-4M(3cgR%`G(nP_i(*7bYa>(w5V*7K_UbeNY@cwHFBNgcR!&rK
$iMSZQ(?7PVO8*RuRAgeFiacgLF&MQ*{8QA#gO}Fuz&j;!Zq#BRu+x^O$}iVZv(qcy6DJBCN~;?KSr8-
!cFx<#o2r=t-*f4=gf*4ROJWyw0MI2eFm~B9B+b~N^8eIaC$Ix&^nhs%#|!^1Bx&-gTEu{i7m$)khnCb
2~Irm6-BEUJ|uM1wQtsNyF$rdQ07-FWF5zl`sD6o32?Xn$C$HX_iY;HrHT!*C=QVJSY}u!30t=w5na$-
mpg8QwkK6DxHEF?Pk_t`2G(3vo&Sz9XEK($hF5-?UPIccZ(H+dS1-on&uYrwSL5|Lz8;uGTM~HaU|+{4
xtnYr%_&kBRp9yDR#DD?^veEiE9tDe^z(@oRnoB5FCWC|z2eL2@GuHoqF)-3ZDP0(SYtfIa48<q=8qIX
-q%2@LoGCBU|roB2m$^+P&gPj^<wi_Ip>V1-d@DFFAAqbD|lGiMq-`)2(V``0SB|<aQB;q-r`SA@5Tw_
Q>ZBd!mEe*@83&XtmArVxnip##eh7rL%hn=-|FjpT)DS+L%;5H_s=lql3c7C9xoNBLt9QOz`JJTS5so%
Z6S<a$_q;>NIy_pZwt5L&6~bGXY1rezZsd7trD*72wcIba!g=@c6~^~$oaAKPWlbKffd$N=693b4-!~!
(C*CE^<EiFL3nFghM51_1yE>r^x_L+tOraGj%~l8^-_Isor~950V@dcF*?GmYmZtwF=<$Ahb?ZTyZNHU
o@<GEeB6P@e{P02C&^0_9gAxX1zkg0`w{57Knnq&y^44Cm6W`wVf<tbjge&8^Sqrz`SK*&vj*~U5X&}f
%Q^P+;7DjjwCgfQ*PWs8;RlSY+-h=sbj5A%ONRGD*g2ppv+cn;;8p_WD$^2<FoH%zFdJv+TtvC-x-PpL
D|h2FMGQWIxGt~czpgyz^MO-5b=6Q`Ep?5;^T*;sOPJ)(U(me&-fk;6*%-;s+P$>L%q0U+&!-$@F{M;C
i9D{HJ2S=P82zWU<h3i%W0(bK(u<AeX=UB9E}K43RRBvv>cJGV5PdeGPxki^b>WzOtJVy#Gsr=`fCy&-
7IO)mtTgxQR+H&Uj=>8;to;?;M$~(I*Th<q9Z9RwSX^#z@y`m_s1<z~gU0z_OM5e(qgvL$$2@|zR{2Nr
zh5H)N=qUQ!a2Rz&Lj-1YTD>dU=K3ENk)zN+d5nte9+z7uv_nQIxEz?z@!*`zpHox{>#E~h>8w*Nbzw1
LY{ZMDk<c!ayyEoS5nU#j({)$2XX)qxVQn-=f6VFjgJ}|`!?U$tBkfy+-8!(uIC|DDM7R3oktv*2X=+v
Vnp7=R^a-G+c3(fVtb86yp)Lu>F#v9BpQMHbd~Zp_Y0nd1UprV{RX;Gm{|8`k|eID(pG6WNw;uv!q<QK
WeCRpKRR-poP3&>$iCE9fNC4(ps&_@A8@4@9}Mg%!_o13x@NruP0uC)`1(6Hf(Wk5IrLPQ4~JKMBk!IY
^Kxs5EtAo+5sZzh<~xH>k9l?f!z}fZkij)>sLUxf8`i#mz*sLMMVOBw&phb?Z&it_tAib&*XU2sR*%kD
!zqF#&`;n|$T&eGDv*56_C<v!C8;c>aD%hn`Nk$U^8~XHCngwmsFGSST%}_zV%cvKGXG=ln6Aq@Byx3!
OzValpfT+e0ZYfJi38wF+sJ(2P?V4a%(S1<No4|cUq+=pD`B^M=|r)+Ke*KDUX#MT@B*9Swjf>*p{{Ot
%1HsqB)k+9{ABV~tvk*+*x4KGF!an3Hp@CG$x(|+KR0L`4*vwsrxp%GC3_AhME;J{!*O9DpqpOqxWd}&
_7=)DU&I#E!4C{w!9A!Gdnx-h=M6_(2rmrl>su%ztbP5Bc!Z7n7avKa4DhQ9%VmoEAlU%!0-a~sqXnr^
2}Q><74tW;=NSod-0<gbqYaKL9}sF<DYy;MM?@;cQ-00%5Kd%m0Vyp)83k}mwhVC@c&2oK*j(j&2Wo!5
aaNk?M36d!8m0^Y@A3VrUsojBW0O=&%REEVVsm;D@5_bVoWl$&X06EVzk<o_Dqq1tQUH9Jg$j^nIo&hE
5xs5e4#b)_lN{e5T;;0pwiSs%4un;hS+5k)60frCHloczeJRc&461nc!I76$wo%N%Z<+$=PS1v@?yqu{
6$L+6ga"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

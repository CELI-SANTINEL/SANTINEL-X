# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "wafdetect.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("a2197ec342a7cea2ed1805c88461fbffc5f973816bd56f8ad19ffcdcca50f81b451ed02a82f09b0e0d29e06fa7d481e61b2fbfaca58acf01abf436aefebb3927")
_K2 = bytes.fromhex("1a8cad42db01bf8adea98528abc0379e856aa0149ca645dded42ccbede9d191064f0788fcd8f431715777268105e0d9cec25eb52e7471f4ddbd3258f0bb7a98d")
_K3 = bytes.fromhex("83f496363c242f9f4ad001815cb8f7d6b38f8943fde10c51f033f31af2da30d3459de72c6a4ccf957ad79b7ecb943013ee81af479d629807a4da6a63f26fdaae")
_S = """L%Z1R&hABE?EhezLJblo=UHcwWkWEpdy9z9^ImtfJ-oy1?^*+$LHjK<IgfCqNgbjc?iF_dz@ROwEQvgG
ki$-6WZ+5d86LSI1%exX(U)IfZnmxJ7&AFPXHqWl5@jX|*n;rVT+LAPOS7=H-ZC5~q(Sk#N(SV43v&;9
%{{w=>yVm?8|dMw0$X_wk$~oRnub#XZ;F>@Wd2L}eMYNPwO9`!<?Vg-;xEK~m0GyXceX+}A>CJm!}m&A
Jd_(B2J}nRA2ki+S{#8b+JE+M{QkWQI|Bd(3tK2rQgpi_)sq3Md^(%Zwv!bLvnp0Uc4~T{gqGM<3QoVg
Y$D6age?~^FEg|3Gw?k9;P_4VWfa=fz&B#-vL_DC!saH@cL6zSJ`Nins@x#%qp_@xoDy{$qrRlHOTO8!
(9^l9&x?oJ8Rr#M1-qr!$pBsj(>d-Ol05Mo#rDf2S=j?JZE6acnmH|EI$bR>X|6xBL*wN-xNT|%_<8ld
9rmHzzTVC_6sboYP7Q*j+`}l*DD$rkhkz;;a%7fzc5Frh7bc&`wD2chKJ`m(Pj@h)pYgd&mf=$J=3{N|
tU`ngTe(6ER|*HVsuZm_s96*a?iMGU2^$v8Za)-tz4>%WBjqnUN;q3J@QJWS)mo!a?yh{p&q}4PLBCgA
N|J<+@G2UVsM+}P6du#JZ9KgD!5vgeU)!M6&XPYKO~3O%FH%X+>C#?FsRLO5dLR{<U}ed5aUNn57o(Wx
+F@Rz#-nH%q!V%-3p^<Rb6was3kc~k1(ctRZHxKCQwrXO-vU-zu1pI^{aH5Rp%3qt_WQUmH`o9Vw72ql
m+o7x8f-u)^olmU1VId`Cy2d_?8V=%pta3C<ot~Y`$pQfH9FO72M9b*X#9S{g|spA&4`G3LF1}03`OCG
XX*G1Ke_psu`8fUxnml&Q6wc=mtB+kt;Uo<{0%~FB^}BHpqE#DGp_nRfjF2&1%0fsR?9#FW!W%@bwNl&
<RFDX^1}4d?eXh*<{DP##<*aR2|Kvgj)bEObjFsDaL~vkPNSNKq3Yg2^%eAZI4jem%{tvrb%wK2&)8;M
`Q&3URg*tOJ<L%OB1)Si9*Lbaiq%uv&uEo2?ec-H&5~cicPF8~ZL(HZaeUdS`P$kG7Hp~8egBY5yg}VG
<#sC0LS&;9O0wdDr2Hw_U<tcQibLfsFhq!1O;i7DM$`Vxfn{6=F4Tur)7p4xfwqI}305hbByXl|-05uV
@-ikL#<9S|-^*knB#4sOy|h%KzY9zpDIkQ+3*e5TJgCswIN7}tz<><xIhbz@6wJmn^c^O0ehFz4lI+$Y
vNAdf99|r2E51{u=LCQI!uot(F+y?nH9Byz$@yY%N^2NezM$%`ob1d!dtX%GL#a_TbqrF?NGRu|K^TIg
M&IjB_xy?<x5gQ?>^LydZEMWHXkI0nHf!`(r+UO-&-%)gd1bYJCZNSS#mZ_2BW2|5CHwo0=NZ#Jed(f7
-=^x6gShR4f@8e3RP9rAi3ruZ&hh=Y7&cieg@~#)ys3OoTfoCqh_-sC#jmRqVxM*is71ij=2!6OexdJ=
46Q(wr^Pu~VH*PUvl6jG?m_@{<>FQugiM594_6?H$3T?|IX+EpWRdA-O;IrX{k@+cPz#tcgMDj=DuL7<
FVP{Q<+VR3>qgw`%X_;ijh8C_Zx?}8>N%zgwNq+p;nhl$S88bW_kwyNE&mpUC;I#RdjWSm@rPHz<OT`m
ZZ5=1yST>!>7AdoInQ+x2|I;E<Sm?CbA=vdKWe1!ltd6x%B<@z>aY0pjuh@GoHG@_$(IN~JVCv0-bvT@
;2{I4ZYR%T#ii`wyq}P-Z;}W?4$ITi#PL<_O$&{&2uFnsrX7^r<!`C96*s3XXTJB2TrZS%N`2L#m%PYN
Vi80f)r_w!^H2NnEuqY2+g3{V5F&vD*AINuM_r$SAl<X;PEHyX#FOf|yNGV>Bj`?^t2XKSi$RaHY>f7L
Yf!d9PJMb>#M{!FVBWN=%xa_y;_uX9uhCqD5Az;=TLn2b*h$qG$PvKpN5S9{dZw;|YFHBSE1T23;Ucx*
MU0WjT-Kb=-9YWs97je}8L~Zj>q7jI)FWH7=-XUlh7zPKsrISgl#1%lMtv0#%6EOhXhJrGDH~m%ehZ`i
e=41sxzp!qu;*{w;#yFM9bz(gbtD07BR4?S@fiG1G^E4~i-`F#(8^*K(s`eQKymnb$RUwDu-#R(!-xY}
)_&S4f*$P?@mE1FysSlf`kVI{F@9MiM)Nfq2TLgsOOO#NPeT`GQHLY|wjb1gq1g2qDLYGZ2gHJQ$Ph{@
UcK9jQQKA}MwOo+_?G#fRT7H$pF*ebYU$=B&i<EQB<Pe?9M3f@%YbxI#hz5}HI|m+-bQC3TgsG+8u(2_
T#TLTevQw!MiBF+O{;8M%cAX0yd{9@VHLG6B<Bf&m!Ijf5#Z=^9HOPftd^32DjW7ptG&mi_i7()xgc6a
4m(IOQ4^LWIgGEvSrc#U;z`4Eh{@o;hx2UV?iR~|g`{pQ6cN@E;)i(RAl9G4cL$^f{>1M013MNE&Z&c)
KDag9e`PyyzNb94_fL<%`Jhq`=BwJ2c|*=v^gL52-;FFt7f#hq1^M-LwP&3Iekh*8J9NuZe~#WQ{3+O`
2*>wYK<(ix$Tw`gsRwc8{uvk(L}Ae5=({wayr8<5J}BMY?pjnDqjt7A`brd<j*hsC)w?`-zV$j|(+573
(00mz6(dHY+rbaOlO{hZ?&k6oO<oL0qZDv<bC^|#s-e(on>`$OH__Wvj)2ZPbjv*c1~sdP%FkvPAtoLH
yn6Nb@i7LEC0}ICot1bhv?>6;Jq}2TCirUlnDI8b!NR^(z{)_p*<0G>ckcii+1C`gNLobYyI`5PsOB|o
6t{y5RULU<@8o{ii{!a9>N(P{dBz*5LqsK2x7rn)YTW006FI2>56#7+v#tnJc7V^zYnu}N<Ui?eug0DO
Q0xypE551asWun3XG88EhJC~5XgtBGWCTbKuZHdA@`MdBMMzJ>NhPjyDz{GE)lLyR8+|Im9E5xyf32Kj
E5?w}J}+f-i1!>^aoHN&MDBvi358ogqqQ=SRhk}QAfF1e{<v&SEQ?-dQRyj?_0DX*hpny~FIb;KdLk7=
ir+AEF@Uo&yoW<un-i>R0O&5l<IC5IQjQuBW4IGPoItw$-x-NDhDYuX&}&s&Z#1D*p@b<6ye;?ItswZ1
VardNz)~C+%JJ&RU9FR@o}#v8NZX-J`o@w~zo?-e9zc2?mk7oP8%d%Ob+O(X8OS7KC)h=tXbz{#z7npI
(yS}^LIR)qwv(gU#n-)F0_@Nh$bUZ#>@JHJY>&KLKM;6utuu><dLMc?MiHHWuWsX0W@!UysdJaCbYh)2
Bn6VDjFbQpsM?OaV=;%1#>{wO#ypfd!PDlZ#{45$kjJBKY8yxRDS=l7xgu}(+&J$&0#U8kMvSU9L%|JI
d;rG0Z|9pjz;9bUJC`_1-)M6Cx^_Vzr=9Fmg{9BD01&f2ZEB>QYfnq%9A7*vWax#*Ng-2<*rXqo$5+(^
#93&U@|fv5pT6Dif@P5VMHaHWfCW3T%A5l~FbH~f{g;?9^=?kPc?d!ZMcM((`!xK*QBY|CD*RmCMuGSa
4hdT#+%9??`yIh^BY_|5vT408{)!bk`yn4<d#DtknE<R_g0x2EEcq(meTuNieTPbt=vVj~QMbR~Kt_`V
K%jb67_+jh<^T%>2l@(<omY@FKNk900>YOoAd^9K<&$imw^s^iv%yiF7|o7OQ%uy6+4F^EnoH19rFSeP
x57axN`A%C*W$P~ST!dibe)4RRzLP?Sj^F5EcncT<dA8~^tJp?8hGuuZFr2O-Na&GpXSpLf*eyQ)`$A1
D57UgNj-Ays|B|8FHg5PL8v8?f_kxxp!T{P$6H^;G4&-hdakyX6b?Eqnb7d>yZjJ}OH#8G3m9g2Jy0I~
wL=DCNEBb%LKo#!=Kv`!P!{-PJbzN7P(XL9du3}kV{OyMAMWfz(>;7u-Q^Lm7~9Z@+CJO(@|?4p%y7&|
egua@9x$w0)YT$XmT~5om{&68ZwJq`O1hdmr0i;bPnzjiap3>$@xDx`^#vuL*Z%<Nb<&^~IfH^ejS+7m
^g|E<nJ%*YH3ciLPPKt6YhX5bHl~qarZjbR|E;_O@Y0kvPRY~8RtA{n=?y4aTD)FRl!mgISB`>q3pd%k
g2Ibq-ZWX|Eet1`0ectT2DtKAO?>D(C-5|nm{XyB%m6kQVuvun6)xeI!8M~1i=>5IK4*ilAfFp9{Bc6h
4;EVIsIs$t(<R8q$uE+`v6<*|hvyGv5w9RPl;;#*>A%hxWc5k%YI>EoEGyN+FwV|Y89|o?Z+a@M<_EFN
fQHw4_JxXr4Nfi`fQ$_3D)Aw{eK*S+<&^}+TRgC!fP-tYW8j(RD^9$<iIN2s{#RN6_RQgyxrGrc-A#jB
(X!J4F(-4*XRUOBonBvMhVPo>`?;<A-_w$r!zlduuI_+MIlSFbD@J+406OJYi<2-RGL+qO3c)(6l4M~E
RYn-pA{4c!4q3-2`%hZ=!>iz$dA0uKCMnA;vHIEH!ifVqp1akO`U$RDJ7-|ElEKoEYFTZ6osJp^(Dx(l
e5Au83$qPs?ayy5CT<<foVf70E~c-&<#RB}KZ)Vx{UKjJ&esUZ7V)-7Fp{(Q_M$UL6a~NElBrKk2qC<>
f_30R28@<Tl&dj#!Ip6_C_Q1<;HO_!<Ha%9_!n!Y;&(SErTFT_YzzM{-A47`xF6{HcAQspO+QSmRCNi^
5~kX5s#B{Vc5hWlcQ7%zCp*~Hhuu{)^mfbH!NZ6ZeW_P@*#+isR_+XQ@c6jhDz*HJwtin_WL~%B1Xz?T
L1}q7Kxs+(zHU3xRz@cy&vVZ7!bhbT)064=nyq5L<1N1PG0VoBoW5)ENgr2I=;H0yioQ1)lnX`K93RX^
ivWfMkRJPHt0tBXa31X_QanE8D-sj`r*xal`gj3&V#b)55VwF3+JN3oO|}q7VVT30<80xDr{6F;Id7a!
*>Hx7`3FWdoX#L%34|<9{v1i6NrMm$oaC*>(;*#hw{jsALy-Hn+0PDmP~L$}VTbp==cXyeH7tNLnAHE7
ReU_&)A}%Z0&En<6#r7Q`&+$tWCHIeRRYr{qTu}^%t1oY13JI>IA3kTyH!+m)k4K<WjkgLXp8YpS&AU)
)efs!IpcmdThDhrFua4-9oZ8|j5%1J&j3}~vAE?g==n|vs(IS6JfE5EsK{AsL--8gUbCN+N@h|vEsDB)
0a<KkwC5W}H&O5U7I;tolPhDFZqa`@E!e$TWGrpiQB0VPbMF=RH4%*8vs2JX*#g<L2$Y9T>(V+^aC<k!
pJc0Iy{%qVt7losXF*ufj{N~oL9@;D>aD;VU7V%BBo$G64ADb9LuxF}zA_wKLjfzR^A7_=)b&Ye7+%b5
IqP6D06<Nk2aRi>{MO|f^P6RQupa+`+R?q|b0@J9Y5Xsa3;IJMf`+<c;Ie-;5&2T73%!1OQoM262w-er
Is(lFw@B=UWpKA)b~p`Yiw^X%3)l~knPOd?e06=Q&MH7IdUu$4YCkpDC{X{a?H}3WrTrW>HV5c{VG%4U
HDCQi>q`)LHfR4;!ve!bBjMi_piHSivzIWZi801zmTY`L0NwVe)g;2LsJYj*u#t=dd4wI9VJeTTXVL6$
ga>0<JzEG$&cbUp#dFVBsEzF4tUjyH8ZW?;2J|aF`$#Zjne5;^+@e&b<Fr$@wlq(~EG7z)hC@WZQzV+2
CIsUhQzG=rHkeL>@W*89jpwMS^&e9CxJ0}HS!gF{7e$=$TfD7vmySYaAyxB7zpd;l%m8ebpESScgo*E?
QE{|BJTe2Z(X&$$r?l-Lk+_IYsHydGqhu|meQaj(Erg+3cG}$~rcGwF=_TVL&epSRg4dWcgo<3DzxV!F
0kc#gYbNki>L4Qn<>mMg{+RbLSr8IGvx90tv{f%5LuVemC>{+?fDIpE`mBIoZp&nv@_V*iYqJNz_5E$T
2#vKJv2E)oC*)_`B{~s6+nl6`)#5Eu5=pL53qsQ|nGH&#df``fVGI95^%2y&^4o^#u<I>6&A0wi;N(CS
16~oX7__S}A9N!*I!%pMr5jU96{xG&`U^xge#M)57HDM_-EXu&9WAu^W9BwDK}CyVDr@SY4OZRLck-Dk
9{pv3xehY7yFUt%d)?$M04}6A;Y`o}_4!J7Y@cg9x={imx!2hGlTJ~fC8EtHE!MvxX}e>*9Fc~MY`ie(
ls=n)9uQ=p2QT%=134cTL>T+v758hsfCk`I+-0w42!pgb1QLU#-FDnzXVeMt<n{Ahn}&?cZH>LH5Qzmt
U?WkIdd8RNTdZs!k36Kf3*BYk_TVbW)n@69fykeU0A#PJL&B`YyWLIw5_UpH`Eu~AChH2#J-Mc`xatI<
dBpoqA@KBE=RL6_A+T%!%{3)oUIiK7m|AE<*-Z11k;-g~HxFu{pe!Ai+;(YY*MC12?c;#(Ru+8)=Y`2C
-qLyk<*a7ec}KT<0(Qxp9o%1mvpzoVtTnNpnEB8aSYP4Ib?*$jhT)<+L~xNA4FuoP2HLl|QswEF%y=|)
2>O8bhjO{eybw+93~aiC_@>P{sLe@EFzDp?@-#2eAtfe(MfTaE_Ror-*IKJyWWN1Q@Z={C;vL`0+#;jI
0e%}2O2j<1#7)JIGsc6VDtUJ@9DD>V6;DonVc!r%srJ17p@Wj4`dXkl@p*CLr$O<9!{6(a8huGUBT0*B
oyTX!o0dF`gIydIs2c;>>yE@ottlKkQEm5V$m8D%KV&u3(L*DafS<9PbwE~u@?s24gAWg!(5=Pctk|8`
vY&uZ>k7rydL7y8`*OHLi$u7TK7!7l^%V6m5nv=CpUl%)^dME^75oIN?_z}CT;!$&KTz7yZHc?}_dv+R
JhwqpzXtIaopcp}w3Jk!g(=v-(_gPib^x)C7D~h>QiOD!)C7kPd8|Oe0oE?I32wZcTNQlh|AIS$q8BbC
&o6D_M9?QO6I;_uSrtnx8v#n|Nmfy!n(SEiHq2kp0m`l+obSE0keOp@^yUPMPtB|-b43I_i?T1A$M^Jz
_1lQ6OjkI%JvQrFV{TDdWH@mwJNaGI|9o#`qeGNNxAJy6C-j!*h2#5$ch`1^3df?z$|tUu<)0v|W5!L<
kQZ_#us<hpv*R`V>3!gGm)U<BcC3HjvS@>I@Tanxr+sRo>QFLvk+p2&-xE$7l&P|TP-$GxZWo%U$?xFi
GQjF(xmzBpNqh~4U$i-)^ez!UgyiwO2Q$10Detl7jcbM>jbH=Ub8KI$O=K=kQo6=!G-u#qhaplsWirzd
%<bAD-50tJ-et>>f#xJRvZ(d"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

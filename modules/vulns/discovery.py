# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "discovery.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("8188b6c6f144693dc8a90a8d9e1375b69124db2a464385c168d8eff85f22e5d0273917905fd334d69cb182793c398745847bf2fb07d015905153479420e44552")
_K2 = bytes.fromhex("51687d5988f7d60e7e1855093d3dbc8c245d55d7a73d07c00b30a4f804959dbba7289a65ba3ff6fbbfbeaa33f056148ed76238f757fdf57995cb094288350e20")
_K3 = bytes.fromhex("d0eaf720297f61123e204dbc74fba176180cf18cf1a80242aa54632972bcc9fa676fa8a3bb223026b309477b0b05c75a2d87a5e4e2a70c1c89691467d8bb371a")
_S = """c+io=J-o$c{&C*eEY3(ouZe$1?8e0tHLd}0yZ+G98|dA$f6FT^xhiKpjv{oCvyv;~0OpHEguwHB^^~;Y
c9svy=a=>V^74NYj2<Go1KFZgMtpYZ&$><NO0HcxJ=6}X=WLf&>FXtI8i7rnb`1Z`2?RbKGc2b|1)Z0M
_f*S^(v%;*sfKOI{aXoR&XP}i4-&X)4~2B4Acdjw;@PFnMw<Mis8eE-mS+BzN&;z^FxcXsN`=PXFr}3P
uspEs-7HEw$da->2h@N~p>;WN16G-X%iJxQD4(%O<}@TqUaRs&kP$Bkhi??LK8x@35|B*u&GquM*lE;n
XbR-KfW&S#D45ba2ie#|4RGINu-hPBX}?GoX)N)ECx4~YUV-u#l0IWW!-^dd-JYoEJc)4iHJe^md|INZ
QI-$wAJ3>uoHni~NK=q#X*O>LQ|gQ|#&`>gQLsCrw!>@MZJm!B${IHufuC=n6n<~X|ALE9y^EHD3T0U?
JhGhjU|lVc_=Q4kOWZGYqEzP%nVu9S%a6%nv9O)_AeU}p-TtR5Bo^Tp5(t35=2}-Iz{YHTe7M;qZR4?N
jeHGZdTQHbsE?EqCZ&_<P|U|dxs&m0-`I&iN$1n?iSR>GlhWaXUs>ZhjqEZg+L-FN|Jr4_NW?)e`=AX<
E@CCcURGJF;<1_?@04)_-G=>JmUJWnMP`xlEHRrorHW}Z5T1a`!dC0qjOfyId|ny`+3)x0@MVq?z(;Ol
1}Jsni;zZ2mwD&T^VmvOAut%SV^sQO*#Nkq4*ug!adJwxa=NJ|K_i-D8+^+aFf3ay^SMA((^granDjd0
lZXznsr<wbNVH0MWR)8LmA!SVP)5sRSi(iUn0;l^tUv%~rWB-;feA_{B{jbYrqbh!X)?(hCh|d7nD0E)
ZDSox<z0KCfu)&{|2zU030Cf>8wXe+eZg~}7zJ{eE3ZhghnB`-n!tI}_WUwc+CG3`x1~HeA;}nWy5l<v
ff^SV0N#8gvV|OQblh*>t8D~HD$T=jG3Jx32=Y1!?#AcrGy{KCt#FCe7YgI?ju7IhUKjM~P~aAUbt!La
{`)mhlvS@_$7Gy$hgP*;5J>&AE8v)i!pNpOX^O>P>T=9VLHMLo3jI`}OszmFwYGz(9L(@)A3NjH>g^BN
Vs|O0=ES9{A!a)mvQ*NB9;;j-Cef`Is2gcI(}T6ZWM7SuDwfB6Dhzy5woOKpps>fTm5i3$!sGWsH8Qb6
*jU{MFeAgrk%|u_P9^Jf*N!;Y(FpMZOj^9$fonjOhf~Z4wpmzW69?h1Ok3piUy0eRrkr_s<WUtoRF-wF
W4onhR7X}~ua!v%#kH}#K@dP}9TUM&xo~@FlLRr0_glQ<XJDtd!uK^~0X)kit1%i+-^ash_p0ZPBNtRX
ed3>0bLF$-I%ff28mAYU|AX$-F+D6g6i%%pTAD7pSL6a|iLA8nhfWXb;pW7)@>e1-3sGxoh(XGkNKRmP
n2)}r)l_{AK){;;k@1EQBQLX{1P17a)nUnY&Ui&+{~INT#UL+@8icVb%eZt9=av!&hhnoQYm~~R{mflp
Qn1Ulw8t0{*)?5So9!XXsaSftjduedG0A*j9vM<uStbWeRPnN6bH3M$4m8pj|G-rHr#*IZ^(Ighhp=1_
2l?DHOGU>hEdVRI?Y5zVE5TCfu?q4aM)zBY7^Z3Nmy4+XLR^4+SYL=CmD}|=!r&z)C`NmTA=y7KHhKJo
m<sLnr;W}bW<m<Tgw3$2zUke4n^$ma3pH(7XF^!HV)l%FdzR!rHH1HMZcBi}WYCB!iZ@hixO4B8ylfv>
_QBtN5ZE&5z#(Fb{_(gnoL+I6yyF^dQ!W#&WE=KiT1R<|76uBugtnegmIyy`JhZUxH_4_<*t5YMA8tzI
VU*upuB`fP&#2Sj>hDx=mzQ9IUfK*u6L~N?ql=h;i}l1FcGi+fZWf~8ub9yT0*GDHf}!9T9QhC@{-#a~
XxQ*eLR6lfL=snJzPY4<1*4F53m<vDi$!MWox=3_B+m$hTA9RU_*)ok%3YWU*!>eb1AkV|;}Vg3Z}86D
jluS^J-KKvY96Ky1*v*TpQN|bon9>KYo=IY;b?nILd*TaWRYCf&FHKcJ387D(z7bXv;nm>V$tt4%ws*J
1gM>7(rnl7PgA0!M~n#E9L9U8aPF*XW!$KY6c56eZZ|mh{k<+X+m79$gN>wKuU23Q+BGOUVq4~Str$=)
*MYd@cf|`sb6VF2jH#8L7-Ap{;Sn?158r|BO5_@*dxK1!USaRky-ZB;*hvK^KJaox3>{ru@xhg#g1SA8
|5a>8)MIvF8C+Im=5VrJ%|!e&@#M!z77F4#o9L&;9rSCS#&0?=xi9Tw54nJzL~T<X+=G*>d{v0j0sk}I
ePyAs5zz~|`KC2-^fJI&=wA%r&VAZxf9_cvj5WpzH8T99qo04CgqPtBrH26c0ICWtBrc=K8xJa2x)!=Z
A4Gpv@WYF)udG;i&auJ!E}`7#Y+sQPpM`xYK*ABiK?MCR9kGd9fxuGNyux}y`-tDhmL)iXJ+SAYdrw}R
$ThGxMy{Imb=^{&OkC|^R+4<3thR)VSiddI&LwtuL*h>pcPNXmiTzUthHsyZqI-5MGMbzEZi`kUN;t5&
oNBC7*Yn0ISy}sK)pCFOwHY_~Gwvaim6#L?0Uh&};!8L~ce?@q!Y)&`yAH54`1a|Il-l1GU5RdEF2Ay<
#{d6*5ey@vhWsm0v|rZIHG1(#3t7b)p{6CI{DTUMo?(IF>toCQdXXBMm(efAk-jcAx^Yw0_4eUF-p3G)
;)P&zj$m~QYkOXS?FPnAX7&i|#eK^xc1Z4G9@E9#Ftf$W#O)bOLddbyM#k@_o$w-2>A3<3WCo-vJ%wY9
-SO{Hfk3TQ@o_;zG7>(U%3~O}LP;{0W(_xRv&uRsk&CeXHQj}mT`i^ljllvEr%c6PFyWzW_dgEo7tqE-
TTsv3w}bWG`*feNAoI7?QLGEg=DsHN{^|3whvt3<G1DkAM8H-No?>-BU~pPKDM3M@g@%D2843{R<Z-Ii
n@o@fU9D52J7eKudvS`tm${XR%v(8yITP?RG2lilQbT~Q^R!N^)O*D6N19r?`XN4bhRIks`Kvz^g;BW%
r4P1POR<1UGw3(|g9<Fs`abnL^uH^}rIB?w?5`2wZB}&})T4Mpsi(7_U;3Y>-?GVY6nKUmMX$1vJ_;Yc
-QEspfD2YH;M=UZG1e@9NWI9F-0h`__-pI@ae5yGRW1<Vwz(yMJ0LsO{bd(St^wp#;RLzK7c>-9<+CIm
F`oq<PG_Sn9mwr9k)E3n5uNv?mFtmSB#L>{vjVg<dR`3+uh&ukA1x;PhjV>`8#qIJ2iL!P0K~p_${h>E
;`sLT2R9***C!hlvQ3&Gl-!16!va1**Lp|ENUHlwQnq=byp6jV3(UYd@_Yu^@GvyAd+PvQk9^<2p~9ps
d&nFp$yJ>ezcbHR75z|SM+vXX9PEe6pSiSp5vYOIqM6aUzMj3j2kf3cyiM+wdi|l;_K4qsX_#axBgB{(
fC2Kf*8D~GKZ205+@^W<VkTKD39!L29SUS5IvyOx2rRYOEibB{8K>JkiN@)9+MriDU1jnZr0h)`_X0a?
MQXa*es203eV}73XZ?sAJvF{m!Ilif-hR0$lbu-{Df@;t#13BaRS4!blbbMguNQe?>&R`*vCbH9d&uc(
bL}%aH>*dAIthvglJhKU6p|b8Ddc#-I>^|oP0btUyxfR{cM20M=*VZN+CisA95JgtFk@a5RuV0HN(4%j
YSj}-{mTu!uR`?JvJg(~eas1~jx2RZYf%xrSe5IKA1tU31JNm#$%Rr<ZzE0nNN903f|hD&0K_~67G}wq
pFQXi)&5iFX|BycD|_3n0Nbk6T$}spZ-I62SorZb3@VSkiX$<6Dj<PniO$LPzI--x8UNEs_bk?I-M|Br
^pTs;coXfN>uHM-iXbfNN1Q99!#^s};s%7214ysicKP#LDF$o?>&XZoFhK7|2|b98VQ{Pym8r04D7-0^
V~<d1f+!!2BOiSLN1$E4;PTAhExlajh~a&oprWkw=rk1#GYBY`A~3KCJG7<d@HxV-B;VZK9ykzY+7L0(
Hg#_#xg?iVeD$9lc%sK9p4-{wyZ_y(0H(zPPPum@>gmD|9TX>(rBKrZy$N(ejOxYhNMIrFhNe~D>Ru|9
CampNztb9hFJLX?Vr_OT6}wvT_`;C9@`t2lL2S;F88w&bT6Gu8Yb&K{q9D-57QU3e@40A7d?*U(qq%*#
2OJ<ZZ{+XQU%M<w{Do%4j>&0|%b1BZ5L~`7_zH^=;G!Oza7(}LUFa9!<o)=I^2P|Z6JE?OZx-G_j8lE&
Csb5}mDU7KxcWbujt+tw>@Ir98a5(4U8NhV5aH#8GqDcpJZW)Jd|KLl+!?QN3UC~sn_4-v3F>{jnlSgh
EhG<=CW=o1QXv-U&}h|^^!_nBso=)T8v4Pj1WI*;bNKh*y#%lM67~Bdf5IlsqE>&WYdxab7M4h8rLzqV
s!nKc20;pU)SUGa;-$PG+{wpD_WGg-RABoHH9oYBQV-}MyVlsn!4bG!YAg#cDBtnEe4&{0t_z*)vs3}e
ix~??B*`NdC~rZ+6+mn;o{)tXlxSrPuqf%Eh_Q-{amI|+m^R`O<F{VRi|=V-=P8;yKmt+b4kLCCLzqar
53S_^D=vt>9iyi#Zvq(?wqsB*b3gk*@Zx*Wx~Klqes#{Q@{6xSE6IU^PDJpfk>&4N)<&^0OeQv5s=513
$wjDpB_W2L-2Lq^y$a7|7r(!3+iiVKR)2p3lhxZrg=NEitM}+yn-+M-Kl|ya<RxQw1_-Aix*u$Bq5>T4
6k-&Yjbis!KDpq*wBhDI8r;nS@7!>BV=!8K2cfMo<=(gaG~vii0I}4e&_BtJ4@bdT_*)gA$3HdvtW$vN
T^=dAMCgu@v$$Xn3DYdC-X+O%>Wm=VwYXJaD0ZwtkU^*D>P}1*c=1xR88j45erlO-V!`;1&2##zlcd%1
0&~)m^aF8uU&a6XzoXvWGV~4GnS3ID`NQQY(xaz4auiGfOH(y@IwLTiWeTAshg7eU2W5cvzssH@jZp_{
d6%qc<?k_}N0{^ZN-lf8Go8z2rFsWH=ad!2f*WeS@Fiic&w#JW%E+SFTSA4;f@-sd%WeV@DSQ9i%Zar`
URuf+f)d=#wV2^iBrk%VqY9rH!HAz|At$~Qmv$~>GWGvF)ikymc@zBLl=uFVb1o<X>AS~)1CFA^m_fzM
uSF{ueHc^m0_KUgWq^|?e5sM1_HmUnAx*(HbKUA)!9%g^k*RR?XF1Ex#8hVmaESR5o^9NuA7@7+N{`Qk
(41$K@UYp;Ve>$}K~vuO$-T<OM+$R*ICd(hyVYTQU%EWs3D`zCdNptU_BC-8v5LX#IPfs+?KdaO8pz}<
sW}3ywLeFQJFgkdyJVRhVvKX8;}dN@a*}q;8i|}b4J@q@DjOoiHA&b&f-)W|4fi_mdFyr;)rmGPI#l2H
oP&A&w1E0CG@&m6ZtZufMVy(l+&@X9Ec{%P5*xe}q<^b$nJ#L=0zbVX;36gioAy--Ed$6Mup)VQTjjl)
G8eUbMr$pGa}Un{d$<HY>C8~%92=$E;rCu&U7Hd%E~h;e7_B2+>JQR^PZ)5kgDj>wb>h(BE#IPaG3U2;
%oGNrq3->NuJ$}j<8Fn&o$ueKzyZl!OWz{ENj@K`ZH45c5#|n$eEyo!)7-bYI*ODUhlHzoPO2?FtAJSO
Cy$-LSH4w;7fIV~YcYpR-E@~Zd`ZOMUDX`1SHKjuH>@f}w)j;|Y(Xx}YH`Wtj*nm_PR*Eb>}7PHv_Wv0
dRP5zTi}G>1-`AsWuaFsJ6m68(+WIXgE{_mejlAxin-x|bs~Gcec}+XDMnh*j+q;QLnB`oR|;?{&-uhz
zoc*k->X9AH^p+69lnI8L9zyo3N4zrCQxx*=f25`7AaKu95rYOAQ}2dvcMzY(bSZix9Z!t-3Eoh-z<T*
)r#Tmv0SHW3$jk1Ap?UV^aT+3=|I)YIrb{7M;0ZU(HHoyH#gvd4Q7#bd83UdUQVk>**e3IeFz}Ra)DRt
Q;)HI+LV^)^Oe28%WLfM0e3W#%B=WeC-Z8R1Q5{Qq=qYZPNVM$t}PO?3pZGJ@IN49`TGiSodr@TmqV*K
A0ba*d9(@PeQ?LK;6fI4R0{~3a4B2${?XS=(V(6|4S<`|nz2?aVd+_W%@vTj_d-YgU>!<pv7y7{#7cJV
$@U4gj!r%s%5M}sDBQ)anyNnz|LR3Q*4c^DZ4F$jL2Dp8cBZw;?y~3%NXNdFtAZ>$<Ltai0%h)@17J;p
l`$5VNcQ^t?K@U}9?u$nxhv-%;-L4mM>Er&cL~V1JTGMAe2Ic>RDB6kr~Xdu05zj^nHe(ev=l9b0vq9^
d*Rh?epXZ+MRB|ePN;_Yf4d!~rg)Ft)mG)ap;Sdx3Q-MFST*$zWp)7mC-b#60QQ@N84l<Fjr3n3d!W7f
zT4O#7e~icBoSR7UL2n2&+ijHdLP#6!f+>TM37nr!KsS!D2N>4QNcdmhe8PtFv8(GmLeEY+>P56vW9v5
m_}9^BM?B?-c7DCxyxh$m2E#85NDcNRGgK{$}0s=d1CH2qq#zLa@$$_RVOJ=-)}LR-u{q<FCmSJo+DCJ
W(AdFr+};gPur{<@FoWiccuK$NK}cDt#VE;z$|pI9|Vk-;14X7CLt)_=6xZxr*F4vD`rXEd367R6akk$
t7r>@nK4o9FFe1s)7t9*2fg}fQ}GXcN1*LQ6P9M`!vrZ#Ux5(9bak-%%1WIKpp%xkHEOp;(^31&*f-|M
5V8cYH}NA3(E|1^01LFI74ifZ*(dLg*Q!<5*b)fR&+OI3WPH2%SURS-D5@)ZZ$%*%3&(yz-@ILm%A&$>
GZ`{ExMVrdK75=`k+g??35h7Fo^I{xrg2*S&n8uvAs-(P464mAGB-U>yei@XBIfR9mokWeZR3;Nt-7jC
+91OTbMnpXH9{Ht9nRNWBbs4AQQ(RDj*MCu2OB`*1za#9(sFDMgGDUQt8${01ck%rR-JBDDg()v*a$S(
f<ME#eQRDN>oc-91tw%UoX)ca*nnFgsw`UwRCW@<7u?z89W=zOnYQ?n1{xSa^F0VFK`P7fxUCvp@Kmtw
qb4iA_3HLwSf=~qNLM9boeEK_;g-A&j{j=#hx`?Dv}okQ5&V)PtkY^PDKrygk0$SS$*s=mW)apA<xjuV
i9*7$RkKye1Oqz77L7`Vq)_@J*fVLTU*ygdedd>&nO`d=Zzi==)&p`TOuE>qW=#Xoa9dnev6&dPZ9r>R
8>stN;fTV=$dCkahtLb%wRW2L2|rsZ2sG>{1KJ7k30~11>ZB5b&P&AM;61|7`G<Lx9~E)XQV*>KloD3?
b0Y*bs!#zoms7e4JHDB338T9zci;l>HDImfHJmGQHNPQgEl0&9{%-gO67rD`Pf5rmN8#_BKAIeAx&bHK
20_9MvXOmEn^F#26V_yZ{Bc`|!uFrp1~`U|Yg`d|&7f|oLBdh`t^_?0dvy_Px~}B}k?2{ZuLeB!wl<H+
xoolb%O^=R*Sj0#UeYq)F$tuNwl96%#yVFTwPh3k>d|`Y4|9BUbbp=ax4_+VBZ-$WL8Cix0XW~(y{$>*
Y4Np)Mw_+%<uB{>ctG*0PNKtF&f%8Sd;rz$&S4!m#3LLgBd1^e#{m#Px3|f7l;N~fST|BJCafk@u&r@L
Y2DmP(HT{qVr*B}t-g+oZLY~A%Oe3M+EX%BiHxFL4Udt9t)Ru!VRF^<ysf>=NI)8U*)P+85{CV3on0q}
xJArm+B0X?$Sda9B7Ot;hWr%1zUuqFBMznp6!Xd!%=`JT>ZQ`=h+etw8uQ{yDHyyy2tNxN6)H7{uiIiX
R%ceAqQ&WY-T*sOnn0<wMmwg^^(ZXpuMx>c<-jryvMUN%AuL)@QRzA4Yl}Y|K~J&(4au5N=KuCtPT4EP
Uet_;Es%t?Ju4yZQ9<1;K<x0{Yw5QmtVy$P<<<?Y>kUgGa;40=#VHhm;+#L~AV=In?O~&0`Q0tnT~F5&
HztW@$`;G)B69~DEeEo(x;ADKT^xvxwAh5wb&MoM+fGOG4L0QVS5Wwg^(6Qrm8vj00qX!bcUug0-zULZ
wTN4E`<glTP>Syl5CWg_asVW{L$P@9w}Lp!PN>Zd0&Q%FE9(()x#JZ$k>|sy_lO|h!;rz*V!+<xQ?6x-
3kDZRLFaVtWHdSVDFC_oS9pZ)JU{&=`BwmPaPb;gQjjQ-fZ~g1>%ijQT<wdDvkV{wc(hU^zlF?Qss96*
-K$>X&K9;9F&ba4t0(=9V!g%W(Fqd_6#$TT-@tnKHN{8lwaPoB&HSc9@SD%v!K%x3b=-I?r+05lw%JSn
-lc{Dl=G>tcaPuq`XyPy+EPuQ+y8ea_eF{UsWpX14FE?|2t#pvjakU%2-LgmLGCmYeVsCDt5{P{yqSQk
BsE1br?XKmL`>uNBr>WnRadaV(Dnf|>TQ`(CK;@f+-ipi&gr&DuukWH)Koxd_V;^rk#@unQ^3(%?Ma$A
YLKM(f$+~}8DcQv9OLd>)<FXb@n9d^Q(Nl=7Q{f!Wx=tsO_>TH$A_B~yLy4?Z=vc+;ZEO|FuV4SKB|U8
b)<^fytlDg=Uwf@Bd<T|NU@@$Vrc4Onx<1(Eg<sx>*(^qBleW1g3-GDL0iB=I=L!+V9AK+HYeDqH(8Sa
hPS*$WV{7ea~SPusSc>alDaTI;RQi>TAkKVv#g$Cg14&r3Gk(B_5BfE?u)r(7uBrt0qY%oSoS66zvbW~
pZL#U%XO_w4vrqm7Od7_5fnm>P+Mt_b;(R>5-r<97r5M0U<8(_$5g%=E}45_pEc7FcZUJKAJ`>NVs#>n
%|Rz+o30S!&V}^c@=c{wLoglr@-$-gy&p-zQv)EI^AxdJm^LaI|G3kTir~$#;1Hfkikh=w=c}F&o6z;d
!LW`%*Nd9ySZ)42Nn4m{rf#{Jw@}J*y2?w(6?9PBosb|XsAS3*^Q2Wz;mwgEcxiQ3(;^W$oI{32+0U9)
Q@p@;+LpMP47Frog*&z6Pkya4`u9Y}ty4Sj-KZ#~vcT}`_%d7KDlanRQD1Jx)hwwZ1x!0-^F2W9+o#1S
e5GwdGs*Fsf}ljmUuh2EnI;5TMXl(NXA8k-G_isD9u)X|la&~9{ri%d%_f6qt7BaxfdrGSKM-+n4v5#2
YNl4NuZFHH_T<g7?n{uyP}(1X?lK7^{6rVaPLL%ok$zMCnsw!=Pa58@8qKLZFp-ysUvf43sGbo7c*PF&
?O4J|*w$NaA+YtQgL~V{IEpLQR<{$|8d?%kb@G0f(sW3Xe<`iUCShjOc)l!pUhnkq+6rWvd{L^&W$xAD
9tNI-#evRWEJd>DKcFkvbn-_Rs+^&>;Ti9EP|W+|Q6OM=MzH<1yY_eC2x#^YdqjZ$M)Xqwf9Wa`uN6&s
i0*ciE<DjV9vYULqv4Lbo}FPoY9p&Tr&Q9pU_zdB8m#L0qR;#{SD$MMj;fS*i50Q=KwWMXqY9_5ELv#{
LO)1IbTz{50FAONTzguxU24CuXqKoJvZF9q{43ASy4+WaF{Gm6FB<JsX#k8>F1FEkrQw#rfw(S0g~e2m
9l&`gZ1?b1w6_$6Y_qtZqO<#R<hld`CJ-^*NtEzj^=Hw%ac6BryaLVB2(wUx#`k0ZrN^KRAJHP{3ZP(M
LQ7n^%(PLjp@xry@5cKw4RcY%^u`83B|u~)lsV^A<S!qT_KST!xFBl;b9&5@1ZphSLSrm?3nn(b%BUa0
<UL8Vq7Y1&??k^zf7PoDVxa6h<lVt5pGK83sx|hb$&VmRLbmbaJ#syU-vz<%Y*x?DCx({Tg~j=?&Dk6v
6sj{FPT5@#j)>-bT9iLYAvj|r{vi>g2t!rZ=+}jt8{BTnKI~)r++9=gciy0}VgkMh4q^iS_h_E2Tv|q|
GU9F~5yR2B@4@0<|COJP_Ij1oCHCG?L(c-#t?nr$r!f_&MO>Q7AUW)3@qcU|0Y9jid98E|UOiq;k7r+(
4I#&?I}?g}CDlYx4}r*(N#z|Dv%<GtU0!Q<81?-)JSv2aK3R~A%ZvmKmDal<W*u3&E4|t0E8NL|C&%~!
F`rHBcda-Rk>Z02fdWb|z&bbS4uzR@#I8;QygETLqq428$Lc;;x@8Ka^^7_NPOXiKBf7s#!K7?^Xyz)c
tdjN%IbZH-Egh=`#e?bwKxcW>DH=T#3-)<{YRR3y{?!FD@?fjY$_OQC-puCxM7yKDk?C1ze~0?6=Q?Z7
vS+IF$Wcm=GM@|6%NI@fuO_BOJM&DE>EETaJ6$w)AyY&E`9f!yq5x7Qb^sW}%*RZL7hm49dpZJoA$te0
c(pyuOe*g>66C=}=UZH0g|7GqCVezKAxurYf5Qc$ch}yAE~+7`<`h#`cs2G{Urvu^oxvC3H8M@9dat>Z
{|fR>fgS"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

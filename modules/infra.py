# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "infra.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("fd937823705d8fdd56194c6a2ef3f69fa39106fcd1b2dd2bd29e5888e8198e88ddab9d4ca888acfadf6ee9e7011fc8158b9c7f633a7cc53f276be3bbaeb2319c")
_K2 = bytes.fromhex("95c63311419ccc455fd89c2a0f5d15aebd6e5731c6820fb087ee589847662f69ee66be10c6f82e16dced2b093c2ff0cf89ea55aade141ca1fada9c119e15efdf")
_K3 = bytes.fromhex("c8e36827e8fae96469890ea4e06699e1a1e45ec1ef12b21f86340622e8d0e8877a5e8b1e63d039fde779c772bdf6d03dc8048c011f647200ec4a6bfb8c14a187")
_S = """*ld<evUjni_V$a)e#N}zd8a;{=x$J;on)5co{9C9Nx|Wc!PeQjRPn76F&hnK%BdZyL3^I?d~}XI+k_jw
=J(K^k${1wIw9>oCI_sVl=|;DwhK!&0S>Ls#LMgoy7*`RSe6}NMgumK&RdfSF|O5ifZ~c8!-WXDOa6R8
aD*u}Pa*3+^bFHC)0O=jOOt7oX}VfaT^vi2K0Pb{3BLF*t)dg3w8xZ$i1Y4Cia#P!_%aKK<4~N1s-X5!
P?MrZc@3C;{eZ(jq@mhL${llH;a)v-gi3lhJA|moW5Z(<3W{NznQo!^>m2wD)6ssC1G;M|KSeXJS2Ymt
++D){TvVy2t{!SNt?TX!d9!)3T$v-if_Y@U{=YJsWj=tTp$fNHs}P?&Zh~H^_`+*NGv8H|CdZ&Xu)uB8
D#ogjb*8ukD3F~k4V_!@Qt(Y*rn5U(WQH;J!pSiS3vmql$sV#5xW?lFmwpw+DvMV9RJc29@SA*lgo;$3
K&7eWMf2~!oc8l2N;}4=fe(hkeT7088*ATZ)>H}5Ce2tdzU$=)w({!7@<WizbS<h|QqgY4Wg%mI#1zLs
wC~rSB^=p+B8r1V{?Si7B1hBP*IGs8MN{$r|3q~`4;E~WbBQ-=b7A0^FT$g&hPPso#jwQ8R48^uGau<T
<}l(B_yNCf?F#B31WR-7p4hhq**-)D_IUGdFX3IryusP*O%w@!xC+~UJYrX#nCh@9G1AW1duJ|uCrNQ|
@@g1l8g^iR7}IQuQKTpaN{K2VA!G(;1JiZAr}kPESlxb~E%TNL<H6Yr#z0iWDbv~yo4zG)80#7hU%l<@
w*ObPm+3xTcyLr8#n@u;vfZnrzg27~HCUr4%swnant}n_*y^n_$uO3RGyMN`W(?BK=fy6(H&T#f^o2lH
Od2v-7au)xB=4F$QSfa-SznRqnIZBhY*D)@%5uW2@5l?h4A$RafLa<5P}~kc^4h6}iY<b;9~Dm*d)>vq
&uTlB2E}Xa_5T-!IU8EE$LM$jgB|O5yI32~CWhIyOn01$l%mNTERO(qj1J}EE+{rr@x<P~hUbCiSE#Pn
9onm&XhMtdW+~JmW1G5BaMLOagc71lAXVS;hy*<FGLO((GGlfc)vGLdYBGCvlA4Iu?L%vlemjjqz}Hnp
6=MfZqggqx6T!~IFe&k3;gJf@x@z(-*x5~~9dt`uT0|indW_z>C>f{Q#owbIAj4rLbk>*%>&|kDVImE)
#JCAQj=&vP-Qlzg;2y*Bg6I44Uzs+?S}hSP%L#ryPIt8HF~e?ghX)W0o~-dH`!dlr!cNK#XITG*ux9b9
@Tr0x?QoyHd#LvWs9n9HGSS?$BzPGlzU*bdoyL~62Q+>wjdu_&=SBo?;0!LX68K`Sw=gsQ6mm0Q)pom2
>8&%Yy}eBw1X~}V)ie+GnPR)X{uWK|SL`Ctx@Cm|WraCgq04)6`FtVL5>4o?`&h-f%am(v1lOPT&9pT1
X!C$1*;th1^rO}KpSJ1h!<hyw2h|gB%D$;k93|ktnz167-htqFZj0!3@ds$TUt0jNG=!kIRgTDRPxxK|
)LOcv8M(HZN$$5x$=~ond~PuPue@|uZX?66Rr@6=c!tw-Q4p9$v2g6>ZANNuCD4JOFYh~(@SA|jdH6}e
BL$M>g+EzL`3E>$Ns<}exx5P<*lp-`0vtBVB)TH*i?P^$7;+71<!N>Vc($v&RAc}ySuHbOI6;u(tho(V
guJk3%cQDJO$P<V|JrlbAWQ8FpiQ{2>|lH)tQ^fwy&(z`{VHjT0UJpL>pz-7a0@lzhF$V0@LxY_{Oh4`
+(Tw~I(^kf)-xxLXM7l`S6)KTKKm5O#Bh55UmEYxXG40Wg-9|Tn)0|W4mVC14VrsVzGG{`w_Zs}eTF}=
jJ0>#vu09Or@*p+G+MJ??!b>huMAu0<GH%_BrkMg;m5ubc#0bnw5z6m2fld<lgE<b9Ry6Yb^as+1s#tJ
&2J^`y(#d{f<s+lt?};Pc%9>*M+Xgf2YhoTa~y~(Kq>8=-)z#$HRd>!rncvy*lAllL+W<pUy!Fm169-h
R!#X@3v9|uCLC1)^|?1p(Vw>Ftb8D5=2%2qBLZoc`h%7SZ&$-W2slUDyhFW2ozMAh6~=$!GeB<wFKE&%
ZK$tzj<lk;9C!sPGUj*A)?pFn3O=#db+?60-%>x2rtrb3?H39*1&?bP`fgW9HK<-A$fq>o;sUI;?R-en
KO<YKR0bLH4pP{g8G3X=%wvD5FOFOA*S_i_<HmIoav6JWC)Bse6dHx7Z~aKiT_@9&h&S9-k3{oPiEG>1
N%kYqtX6_jmm^pBI}LZB+yJ$$o!W<djkF!~vMMK&Nd_f2#OMU$|2>Fv9uuc_+Z{F8w&TF3U<#^>KnVLt
*etKTVx}SRro&JYH`91_Q*l)P62V$Kt(aVzI{D%gp;?Dhw^FX{IeoBU3<{AE#X$khnJ%;g1_-N?Ff5$i
2Y)VTJR(p(tb#f#`-mq2mUZUa{c^X5OWDVP#1r2lD5)U&`AtvN)rMLhRApY_&4f;^F>#}HfwGE_q&RSN
p)h<??&``-3Vf*BqzQZV(poXW`gpcRbq|u$9|c$wA(x^oU`huQYI+0cTkjdc47>dhxV=7k4JFKCarA~k
7|wG0r>qIvB6&~ir|Y<8p%dw}u)qS}eXkkQCeG51T)*7$``Qs=_(A!`eO!x5z5o4l3YQKu{|XCPWX~y*
?ms*fYM<TL*!jAa_79snT;8WkF0iRgo~}3gi)eU9V{zaOBUZGX5_Pm)VMjI@%Y>l(cT2CA4~ub^Ss{Kq
=t<*!27B6`04%l~C&eS<a@bUfbLE-r3nx&5h%w5_Ih}SkY2w2x0azy#1hN}9!La_Dxs)aBY2Y1TBtF>W
_@sq!6lT<|wuD{A4dVWKfRRz5$ME`CC%<o{8(;K7C<7ULpBnc_Avv69vu`pCQSW6FX0HNJ;E(gE>RyUz
5?yNMrVKVF4xp0JwWdv^8aKMdIc~|f>eP2<V<;Bfqr{wBN_o-pX9=7p1_5Je+@-rCCt7wl$~ZqPrR16i
Wlg9`Ci2X$H<Al+XkrHpLbLRj^SMpAEWXw4x?5IRGfkS%qq=fMGhK@7?AZsY*PYlB16X&YPZDjU8D{>7
RR`pDR{eYj-sj-qpp%ca)l`heLscy-Z*J=d(uU?Qo(y*E;^=N>h<=-9HY~^4<;@;qHkc5BYUE9Zb01)v
9|2A1XNQ5WF}0&12p8QgZGHUp70_${hU~gi@VVSx9<5O*Jabz}3nFdhx^=PGe$d^RM|-KOM--y*E&&@A
aSgxQhaZ;~JyymGJ8u^7FeV5nMjmO&_u+pa3XJhvaX(&{H7P-tB`je<HAfb9k)^@~F1?~JAfO!}hbgDn
siJDV1@AsdY+4BIl0%ToRfd^;K>sgvlL^e<E!pS1nsowIgDUrck1vw4D!&O&@Dgp8qo*bCZfwb~qu@2f
wGqM_3XA?=;S+5%8XP{L1e))<Uh<8Mq#DPpLp*$8p<9|JgW^<3i3HflXb2=Zs{_l^nZd}4QAxU0u?aqA
KQ8Fjpa{?_N=c`MgffQ3YPw`N{_eX%aHSEBs9)H1we_Vl_c{h~&rt5WxdqrEBm3a@hzh4#QtF!$NmK2z
SWxa{?tPsJnWJZ&znn7auK`lN4DS#X+gqE|h!h5{otkl)ia%{B7uoJIim?$dX!W;teWfoU_aA#;#kjj?
|D4%v_Zkz$mn5=sPJ%HWZx;}@(`Lt6SoJ^SdWMgPY?J)274aB@^l`uKQjYi@I^eaEL+vh5irj5)R^{k%
^m3+Gr5Q_lr}EwxDvKtJwbp+}g1!YGT0G}ZFZsI)h{L3EXDVZ_Ak|I2%QpDYC_|3ekPHJ7_E{Ydir4JL
Y6Yt)<aRktP|)q_i>)E}6q)ZJ-~2_~e|CTl1Nzm#eT$AP9Gow7+yg69sTOb~B!Qg`h7exYay|7`-o#ol
o6zK=U=`0&yCmXs_gArq^`sT|nojlG$eK9h(v_dnkV{qee-i;NiQ~-()!=WDR!6BPC$ktxz$g8P$_3b1
P3`T*km$i?$$7K>>lWfb6at^r65hUEOKmSrFA^p@BF;A*l6hMvIj8InZqd!DvaB3Z1lupN=O5O7g6oor
JKYhxUlc5(cHMGtJ}R{OC^e<WK*;h(=n~QB{^BC7?=ns5N<+iwmlo8g)bONVhi_NY3*ET1o`W9Wg-?2C
eG23qj1ysK)wNv=xC(6@#x8?p)-p?B??N`Rjsb02!o=En8p}e6ri)YRkLsG{itPn^v+R5fag%N{jw!Ug
eR##rh#N*L(>&lxrK>^jqAu#8E_VPiCp_<ou%fgTaG)>&o}awM@gIo6)24*Y@w}TDM)dAN1qw}N3t0Ah
EFj1227Sl-gW~`Bvfw^+YUDq#k#bJA6X*Kp_b3DA180MtRw>!p8NSR&LTBHUh4wvF_kX;5$BeARUgich
KWqY=gz)HUk^CvmHV20<S>c#xJa}CY>))NHgWEqtEOKY(OU_^8$IFMgGaBmdGCDlXaU4_+Z7}GtAY~xf
?E{NMM}sEEiVXXAs`7FvdjeB!X2x^YgURXsjW})RJC;<Piodo@+&tE`idTa<VO=^bweT#2EkvM9V*%of
N=W4Y69a&5w?0Dg8V0OH4DMiJmKG0x{o#70@e?#XhiwdN-f$r&Fc;kbTW|}`5rY#)OkfN@k|N^c4%G@S
(Nc2pLQ`PN^5$ZAeOf~?^g@BnPxO;v3lDM89dI+Vk5}7`3j0->EjzI}rWHI@7Y3LekMhEK$9})~x8%rP
4p*sDF^Y5!-2VODIW3}|By_Z4(DznwP9?41J!LsmAj-3d*%luhvCydO|DRNZzf>)@vuxjHom8RzF_D?@
s$qRPkL-`Ins^@_;JHqxWvbI9YLOcR8dM<h-y^k7_~wlXH_<*ee<FX;(;P}L@Hm}}M%w=N`lVyL31-kK
wQR6@;_x4t+dx)!c5*nz8Vo+Jaaz%)U1>r-P>uJi44<svl$<M7h(;%B-gmIBUlIx2N;e@!KEAJmut?-g
LHAcbTM1^LbXgVgfX$p?T#{N;n6|AwEFs4s#bK;%JVDA{qs%FM@j0FBIkGl#X8DZMs*(6tf29BhY3C=V
s$Pwgdy^gdBrzcOc)kyI?IFxmYO&j%ADtcLA1b;MB^#nO>{85z>`lgqr31CfEN)Yy#m+`_p-pIn0vISf
`e~(FI5y&!Ke;ph)ON<X^4I;L#ceqO<YjBu?ZBSOx&24DX*PtCKT`R*>Pj;Eo%yhAR#p}&YG34}1UR)@
xe%SEzRS3)PUH`d7XAjwd9Cf&jK4U8Vll&vHOQp2^ZhHFe&9S@ut;7NG;og*^|_X9G{!C7I5eIXwGQp2
{CNp09Z^#+t&(UdBfgR^bIrbI&H9O9F_|=W+;E#{gC`@xv2pug^X=LyhVDWO$FMR~IP<6r`7&_"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

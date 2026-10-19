# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "sqli.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("633da75f8e7cd263ea9c8eba59a80139e1fb7eacded50cef8f46ac79248ac0fa8cb301ae82bd9100f1d7e9ff64ff3be646c15ff11c5f62dd8f497ce41c8ebd46")
_K2 = bytes.fromhex("9ba4577006e0b5c0d0588898a52dfe47c8dce830c1f3f8efa28508075aa299d658d28e8c86b0052efdea87bdb2680efbf4aff36db8740d5ee7c59cd7ce8e65b0")
_K3 = bytes.fromhex("c3ea178fff9552354e617c5ce51033a3b50b6f54c14593c76f133d767229155a281371ab3e48178aea20a6cbd94e5da69148f87f6c79360d2e116fe2a7490023")
_S = """L#a~vEO{<L4SRpilCHh{oPI^--*HFhQuNW;o+zDUv@qQ2DB%^b@=9DjM7b?_AtyYP;lt?@w>f}tu7~`i
2jY7eWUu(zkWBGlgPRvLD1Iv;HgbLKU~0_Ib?UTxZb=<ab+}B5h#9G_=9O7Uyw%ANSGguYzasp{eC0NB
612G7e9nbo#F9&7hE|C9T4|+5i@|NBmrUbcFKa4)ZR*?1NE4{eolNn3lea#U$tVAd1<p8FZincc*Wl0I
T8BR6D?N7Fu+`vt$QLA?Xbk_@{p)T6P6C^14Y1Cxyq?}98cUOdZWe5WtHg}IYatxOfJG6x4wA?IeM}0{
*>x5mgNiv84CDr0nzgb`oaC@r{;PM7O0<D&2qi#7_CWaiFd?5n^Nky+XuHs3AysbVyWwF!coFerc<TR~
l4qnUArr#(ifpwnJ98VACIQD)y&C3JHlkhB9wl*-jqAF<^9+R~y#$eJ$oxutgcSC??aR8=uaQV%9^kB>
=i-xVt7N;;d{Q&ULRT~C^Vq0E>V|AQWUY9#-HcwCObINM^j_!bo-g#hn+`t<gs^G<07-@W13^0Tn-j@q
^!)WBk{9{-QT&wM#cujFDhEWTU1fERe|7XrIpEDC33!PV_yWep)p(7(KGR_+u?|~8_GiQSyfvg?%#6Tb
C+=wO*ja?VhgK@vy4<>LFvkS)gT^N~b;dEA{{FHgY0wA{m@Ne=Aff0Jr7{rJQ!1u7Q@38ha|GsyW>vR$
xW2>$#gKHVoS$I|P{XJS#I0&wvu>^G!!!I%Z;D%3XsP;Cv(K%T*}{00k#;$zl5`xpkURovpBeW`I3}r9
+7rb)KDpO+yi*fUL5Oq05eZpb0jZ`J`#n^APhcs!0utsNpKo~0oGji3-SX?pouq*x*MCUY7=$AyF$_-p
Pi1noYzM&``(+jH7nxhCwsf7SqCfc?f+#`RSwh!E&*l5#OSWGSzN}7=l0%96Lw-G?-+aaoY==TRw%i+q
xWhhUx<5`dsy3M`R-4V%BGAL`JXc|PxnePXZCJdLk?K|`Z&i^H{9jsMPjSt%D^p<VY0QtzE<O5lM8{F{
VSIUPR}iAPy8`TOb(7GK-gz$V90_X_Ke1jIbzS)oR#@bETH0Y1scZo;E>lsRvS=kytASC{yqn-sS4(m`
&N)HTuDmYIc8O)_W!N6<&<1MS$0ZdLH_J2Z-l^_565J+WN8{*Q<mkTbTLYpKQB>tNLNn>xGl-tVVUCwT
&N#!?n@+YzIx?Xk%ZeL9Hs~Dw9zV^}+GBJs%jDF<$mvHw@}AmM^^fip9i4VIqG1`S4F7ZhnGCz;%v2eA
+2ZPjLb-HLTG>&wsii57T`atKMd7o)hWg%}Tai5q4&GtXV0sx@0>-ldkcC%QJzs|2IwHR(C39cE4y#be
1Lf(A-~x|b$gZO>N}}zcSz2cN2F(Fr-gf`bv}Xl{F(fsZOE8NYtY%qUx~!ccdsTtE9YKi*>`#e&OT@=!
h!tYbaE%S6?XbcnX9**j^?uK0yan?H;dLKX$#V5VXOe~lXieHb35#FIxkSu%k{!LzQ^pY&%?OvhU)d_Z
L(cOB+kqqCmi{I@jn6}I7`_0dYGHPwN4&n~b$^u0w@@B*Q?+13nBtpK_JrEQp`7zP?Tv1+@x4kRvWlm2
<b>IFOB8G_L)oftA|>F<=%+Ih3XBYO@a9HY+Nb8mo@Kd6=<im}4|`)<h=hd@2=_2lS9ta%=>gGJ0bVXI
Gv8p!JlsCOqsB*!&~xDx7B*1rl(6jc@x;JUh12~LwYQC%6E&|pK8-lAu!FI0IaY>2OtoD*Dpx(sc!l2n
3vVdL4!}TC;BbaXh@gWPFVQs~Wq2N`^R4FZ!*-&tf}8-%#fo{W%cF0fP-w+QVEbR;djWRFig({V)8|9O
$wrtaoBum{YLcv_aV~S%M}-;?Oqt(;><W6~hEzW6gds(zQ_5sv)99~h9W{*%gR?mw^`~X;2Ko)T#kkY~
QkjNAvzwG(KJc_$0J7JI*6qOhi7dta?1}WDg4LFiP#Bi0ly~9>%!iD)qQpIDnI0VoOHb_F*3!*yRL9%r
@s_Itb7YHr)&7`dQOu0CIYC|n<Fty=*Vl#m@Y=7O=$uIk&H5JVXP)f7yb#5YG~J%>;~kVoA)42wh>pj0
q?Dx|kU<NhY~X<(ai3!J)f3E&FRL>?(eBeWsGWp|s5oBdt*TGWXb*dxW%xbP0<sgAikpIjY!u(}MhGGE
S?p*64D({pY<*nix)XZ!YkPfD#HltuRJ!pXwI>YDI{0@4Mtz?KaNS2aGfvFEGTuJ$@E>Ucz#TKjc`EtM
OC78Px9XC15~s(Q(2?}1R^eLxBI)~iSk0sR=B6q?b2Kyo0esC>rzdIqvhGaPC?t2sdLqk)cep9&ywN;S
KkO|5aV#j|PcZ)38nRVoad5*^%!cXXVc!}-s+GvdmS;EJOfFBd6m;^v6aWAAYeKf|5BAIOJ8*+;ME1Z;
VwE=D<?w98+tye?n+NU5JW)3zI)W(_G5hM<op|%W8ajuDFu&#*E)?pDQjk!T!oAkDx${liw>-(0Tj<0q
jZk18(Lt9*D<zr@ZEF|X>I3W(<c!%ggX`kk1GP&Vn*^Bxl*_;~5tIY+=hIZmCdkV=cM2(sNWolIqo4&H
T;6Hlz`r6p`X20YHSRR>RI_N$h<t;b?mtFy($^E3<p_>%L$X7~k@bQ8XQsqs7ME*XCwVQxQ$P`HotH6}
+c{<`U~=+^FuPs=U}OzMVO&_VY>RFhRX*wm%J$KXCXW%Fz$eB|tgH{(<HWFF``yPFe^`WXBsyqr=#Q>0
aKDce$hlQ}s<I@GRJ!m*@hS#Y4rcT{tZ6WN^ggd8@0LN4J9x1kw<Xe8ObxWg%JM-J-B8}!<$Jh<U_RIz
S1`dys7f&dAFe{&ztJ2Cjm^!LeFqn=sHzU$hs2pZI#g<RJ<F%+;t&s1RQ8@hc)qx$D!9`X4ePGvB08xx
o47*vTF%B40mdM{aM(hDDf&RR20jp{R4ngC1D7NlwsIt+J6(PI3U@H?v?sThyA=vPZ`*m_jih{@Aj6=-
-G&g)9g0AE=v>m&<lcOFFJ|_v0@ICc%y1+DjcLtT>{AwMKuwP1?FdTQ+&|DNO&3?*$n*JDOve<RS3hBy
5ZC(m3cUvS^f7T1twbS^)M#{o`st`hK}BVaKqPBOYu$(H5(T9!OEz7@=n{y;?bZ9ko(2nGO=Mx$GZ2xu
Nk*k<+@W5C3iz9AwmMCh*m&=CPw=yycty}EVo1q^CTq|{)CtqwlQp!eV9&t%cOYJqSoKSCx`exJA{a}E
`%%R=ufdUaqMF03*}1P(#RkXoOXLX`nebe}&@+R_emWa*?x@#3z4~AfCLlc}ghD#{auMKP61yi*!kFmH
3RqQ101QG80bO%yh0r_bFK7v*xc=nKTf`0gm)HOxFchqS<Ct*QE-qW;As!7Wv3!g<T!t{9WdztaW9!u+
Yu4qyN<YXja<l3R46cObzlA;7```ws?faccD3GmEsQ`2KXZz6S)EXX~L+s8QNm4blkP}Bct)<j)iFNv3
pv$GU$Yelxo;#r;CM`LB>Xgh9LKGbNuIVZL;ZIqcQZYqxvzY$O5hHo>_+4)lH_D3OGnV-0<oy--?^Oqi
M+_D-?w0fDXr7XE$8xg{iBg}^qr##qUypOR{m8?xg2Dqz^V$qai{b@sybt+2y?cqAan;5aJnNtg?jt;M
RGFUJ=$%fe3(Y_wDG0MOc9dc<?huDHoM&dvc@y-w9;gj<?~LR!XXbWvRA%(VHJ*fbdkln;p7Qj04{;)8
#8SLS@1#dTCM3Wj^<W|ZB?A?u;QJdNya;Nz>F^fU2Y~O75!pQQ4o2mR!1!V?A37*IIZ83$r?m=5M1~Mv
MblR|G?C1D|FgCN812BYbHl#?RY{vxOkdZUgY{qbgV%Qjda-Et9#}+m`k`n`oX}6R@I+|LvhtVTl-PgR
YLZ_U-CjXv)ZIyFv&*rF?fEEUv1{AHAQmA4F#5Z^>x7sdK!PehQP_58ZATm!6{mq~uEndA1xS%(LC1C%
nAzP{{dediimG8fz_z2k<M6?p8KsuF$CZ4;^cRHA5H~A0#=SNXiU)DLIjEaKmQ5qons6?&76SGxZ<Vil
m=K_?y&eXs3=$~;O`y1+J-TKnrSs@d<M0;>NRx1_3|1L5h|0r?zD+cMablFWjNedh$ZQ!rkmig<23{dl
gk8A0{6Eq+8AbCGdAhy5m%wXRhyNnCPovzUah9}so0X6~K*nFU=s{}^*@%(Bdy;MpQfz5c{b3$7%$$L}
WD6^u$x}tk4bS)80<h2sa4Vpo4R%>`#2b#n$~(XLQ%*qLO6b2AxMUdvwqqi-@63qS$>h{CcKta3sz94P
!|!>zwDvR!Zi9ud5q;g{67EVciu)V04Bug23NA*q#P&km#0o+v*pICVBf)Ox0EK8q$jL!ykc$-m9%a;~
7`E(!1<I_tw^ei+LrgMnlQU3e+R<3JLCH+PJn0eTwn7fe*cRyj2103|6dFuvj|OnC!DE;!m62=~P&$S4
Z!mmK^|b*i&9^2vlB7TtWLHVj@it#3IhlJ5fxc)%IA8!<o@Aeks}sNrl3j~%DlN6osX~$AJ|v26OqORx
=F!o3tQGL^zDmt1pBI2b9vkBAG6y5Ec@OK4=`!WI26js@Ih=YDOHt|+8of?-2}y8?Temi7izND&i@9#^
gPC|}tb1(NC_+Ql3ZDdUdn?XK&(I|?#F+ev@{%XEK`RPl*zA~nl)BW0;B3^8xOyKqtpX6PFID(=N4Z!w
+SRtcX`Ix~N(!}%^+l#HaovvX%^6@!-XclC*K1#Y`Q{H&@K9!^M;)xdNr0<o!^V;W|Ei4l?Qd?Y40pna
A#W6~dUTrrduzCGg`XUTc+-)hw4HJFX<t<$C+cSna$3U!NN<@xctAi|pw^;fonaDT!(qA&cuQ!$8RR68
MZ*>Mb9|)8C=Faygl!cY=7F>IhHyp-GigIODZ<{w%($vkMk1&?Sdw3C3VhkM3sPaxe;`QcdyW!b$p|5n
9W}vb3!DQV@xb553M-@WRHw5`f2ml+af6b>z|)W<$TqnynKp8aRSlKbfra9=ZRv(!XWpU>^Bf#nNz#y}
Md(At78oW!SQ_}GT}plVk8mIwch>hi&tZ2%si(HnuCZC0A@|%c5_Xefe__!Nb5XVFXfjWWDanBt($T85
U(8RN(DAlGj1sW{6P>>e(`9rk=D!CwQP;uqYuT80%7<YQ(RS}#L%R(pb#~2P)%*dbMdba+_d_ccSbyOw
mbI~hC)Iyn1uVXHLfmJ4O0x56TxqrD?~d50AtIc-H1h8Us1(8q=NM7B&4*f$>-Y0R-o`%P)*jtKV5|Yb
KMK_n)U{)iHTYvkDK~jJ$h<0R{&XR;*9wVZ%Zc)&_4dTM_#SECP8RFOnPYiT;;zN9=MYWE+O>M{k&jRt
sdPr(`{5g#R6)P?#|OiF-S}tMe`6)!Q`-BCw>8Kn^ihPv`ArUliv?-egLxv@E4!9!h&x3u5v}cQ0aJPA
BVx%N{n;_ljPD(9BN80>-h)_qLL`sH%*qw$1Wv6UhM~+C`_u{t)T6*rU1L0YmFQ-DO)fI$=pSMX5ViGe
rlj`X*z6D+Z^+Pz)ylenU0ojE#%Y3Tv~Q>mX}|"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

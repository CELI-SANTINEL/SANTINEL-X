# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "summary.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("f6fe94ed4c1343b03ddafdfdd611370e5c1e69f8633aeeb6cc81d4c50535cea81bd9fbf66a301eac5f17e3929a8ee4d12daecb2c1b7586a1a602540394c686ea")
_K2 = bytes.fromhex("ebb1ff74f36652ddb54c3e80d94ad75c1089644ec7ca11231a53c1a3a519598db70794e21c3465a41719505d9d905e1070108f6343610f26cedcb5215cdb8e7b")
_K3 = bytes.fromhex("6d43c856df2443bd39a57ef2c12bef4c6f14a86cfa9c63a21757bf1cd5cc432bad05bc0938f459081348067259c8035dfc3f61431e26746b0990a84eb3409600")
_S = """2-Y66I{`_FCsS7j9&-kxW4|_CZ>|)eFpjBAbAhl<;m`N0e^{oJ8=Uv=JKSP4YP^`S{Q*~X?_+h>Zkw-w
8+lJ7_D!LITkABZ@P^C-5IFdS<)zdwlrzb(YFp)Besy`n;~m)9=5gkfd-h2`+SfEtZ{5Hf-JtM`<>7hH
jD$<<uPiN(w7DX#*whZ+vx%WeswQQz=?CNCWm^~_@BYGP19RX9p=*`wS5W;qDhrLk%(lD}YieVw-~Gz*
LR^XdS$P@Yv>WIb+~lf8DywipRQQIQ^)GMh-R_4CTfqhWGO*g$_@an^?Pw2r0=L;dS4TDV85lG(ysV=3
c<DGPu)&hcA&|88=mFHbkFm9ct^K`W-*xW?1Nr}{h&$o9PQXqnwy`h)?npnl``dq1D@}!k7*m}q@}0gq
f_7@(d88<bYH}O3N>(cNYUrH2?79YMsW(iZ3bigX<r@49zg;%?-Bd}j=S$XKFz5_^t^rWgJ;}f--D*kh
%IK4m55H;h$Q+klxzsJ&2HBxWzdo_$;tpaI;{H~iVzJOKB=MaT<0|jYM!~mm<sm$s%Vpi9NF2_1OB`j8
O?l+J0hz7B$-Q+n-aNcGs;gveNDvGAOfw-ok%T%m0iAXmkK}L2hm+Q4%bQj{ViTtVcl!hv7-Hi}e|DS4
-f#BaN-f>op(p0O)yfnU{EQT6ZrNUa5%|n`<a|<{?C1Lj--<#yXpSAcALx~fx!uHE$uaIIL_yi}QnwG_
Q={YeX`h;yxHg(~{d7YZO2o49*S?Hg%FjOt=0K~93Ci3*n$Y=kgN{i2L7OU9x?c@N7B2uT(UD%rd}eIy
yxdu0z^PQAcdK$?ZY@;9-11E;tJ5H<hd$Ib-k=A;N^tjvq}prDXL^K)W#ogcCAc`>p5}3%8HjM67{vLV
B!HU<#%*E#MrP~u5y#^Tmv9EOCaA$T$4}Vx&POuR_sMwyJm1S;eybUIpPU6S1ro6MOPHKltvS{TZsSI)
HN5E%Jx-#~QAlu@#rIeHkqj%`X*79#`8l|Lm=tbtocRh5Jl$YWtUB3LL_Z#0)%hI8?9V(L8!m8!*wx>;
dZ+mnK=b*ri}@GFMpsK(`cd%s7V0H^w9@^p2!dVl>|i{;OoZm=d>%lL8^#F=RWLs+-NH47sGfV6SVk^a
F3xEuNECbNpk=+~i$HS$y9+7Y;U}~e(*a^`0mPh0?D5&t1X?Z@UC4sMCc7|@uz+(FOYPXMRia)EHW{|t
ARQ@dX}%A#Qcb153!3Ij1JH$qpJB*63;NQzT|4XcZ6?UEP1?L>VgXHWItw+TfBBL9zSCZ7=oMf$!N2@V
q_f0z(lY2mhrW5*;k(5txSW2)hjXVX_?IBQGdc{DFE9!=bx(12WgBCv$+HycIyRFs3aansr<z+kh7%i!
UGsU}H?M@GhYcYjX0N0sn$XnfcPHlM)L7L-gH6~!o*>NlsO{0&->e1?0YKbL4>jCi{LYcEn9~(LM0Wqh
rR?N76&MaL>$cSbwd$M)?n(-lsK7c)j#fUaL7lN=%dsbd5(wJDd_}6VG6S6P$V|-G0CbKON*$^@ffv;3
prJIz4vczHGaS3ETz>Bi5=sZd%|b>87$>yp_TLe#8;DV&+_h(C5(2Z~SA=~DX$zem6BTcp>^!MxZknf1
p}(uWe-Q!bpBy`anRww32)^3+u~+u?Bkaf3T_BMvxo=C(VFV>!y}I;@<KBe~VX6x;OL6)cR!_N{*pQ7h
ICFRYBd8Fhm4En>&~ibf%S9^Boelh`V8<sJPyF!n8ss^0cD4)OL8mP@8Xw6NUr=AqXYw<EB}BXy_XW7Q
`m85WrZ~`wlCszhn9-qhJI~AjZz&BNrH$Tyi>p*=46j|OIc3rT`~?P>&1S;%WG}@kWk>s>X-iN^tu=nu
QmoWZ_57>Ou>|Q&`=RkJQ?_4*A%lkKT+mQ0d>@IFyWLWWGTVu~6xN;=4{RN*M0q@07pkr9Lr^A%N)GXk
6hA*qACy(|w_xEOW7>xGeCq1_(=~Cv#Snk28)0@guumwMXzG#LjUsl|;~WtZirzk*T*ee>Mp@TlM@0U8
XS))+l{6HED4y2w)C?Wslp-nzue~sdzshya){mZor!I7lRo~X<=s<oNq?`Oo@jgOip94wAkMnsL2L>EP
OUw`Y_-E<oIE=+N+ZOu}WoAYF&yeg}Wq7ooQ}O!6u4Z<@<k=%J(n==YRGMJ5qN+^=Xp8;(Uvu`#ox{pa
BPCqhSXj-VSkXy#F;vaHCHs-u(RzM1Y`E_s0Q|uRSKUqAnl&yQ??RqB4e;p&VqJQ;>BGIVGT`R*kapgh
-I~A9r63EV2^oF->j=5uMELMFP1(EMN-KF%0X-DL(bmj0$Tmf>`rnHPU8D9rV$#c9Q3Mq5Ait1h%ua<X
l9tl~*v(92#9BZh;q*CVrNuZ`sP9Y}PU3u%bXC)}jFldz2_W>l<>uO;tJB3ao{e)NEWh<Mv@Sr2gVe_x
hHggdVBcpRp0+-Y+T1l2W<o>ZNi?}~IqjlBS%8z_tlSbwyWO*3mSw!BQ^x3Ct|L}j8@k)HxSrMP?%d9>
7AAo~AS+jV0FpSZ&hUHE!cU4xb~FecaXtBwi^yCq(IB^JTlKAB`=h<(>zCv(T%jH2Hj<WzNdo8$9#D?3
;tK@^#c@O9uPHCHooh=D4{@$tUrf)MFSQMNZ@t=~hS@_~PYb9o8Reum{#X7uL8^J6T+t~DVrm$z+_<Oz
xbJyL<#Q4U0X3nO-_RvLvCzBpYAhv3#Dzxrdvd?d3f%*^LtY<NSk_aJU(@IF{Iy{{rM8wnWQ>0pv%c@^
OrPyItWe|MvU3c;0D?VQ;A>Z)Zqyw$p2B*LRC)XzVFUg8GeEwJ2{KNA`M7M`+Hxu0G|b3D<hlNORJn@1
Wi4R@Gf^m510Fguqd~WA^Hh5}V!D%3NmE>~B`JV=X4Zwf{Ld+WRQQ`L#U1Cr)7<=LMq)%c`k$RkwRzcZ
3M@tw{-}u=9gUl=1DF&+y68P%jWzEglJ=8v3a?g>l$`^vk_dQ>L#?JT$0T3h@sbCmboQ?&wY$MKycsjg
)W91it+~iw6-!Llk~0Wy5*4<?gJsg!&lGAcg6X)XER}iU7NT_v_Q4jA!^YJ04AICDc6_`_M2YwCZO}9o
1|sz(WnrN5U~BX~nSjb%7bV?YApT%nXqR44NbKd=h496Uy$>Mp&833B$Zy-TY8jCn#V`CF@_7raa|z`s
Zm?l6QQ_^$HZPJ++MQbQYuc>sN8Ao67@mtSb)P*o;-ui2w0$y~tkn5NP+%QjYlS{A#>o(!i3>l#0ove~
q1Wr?&I`s)UNAgF=w}^^#Xu9{B5E&Wyxuhh2FOVuKB3JQd~g+*a7G5(uz7ukE$Nhgin?UnQYeVPTR}8c
98~sb!nsLWr<iyAX0zH`mfk2a-f>CS+tqxSFD`OKMYQEU_YJYSG8Lq^C(SVkys*FdKI;R0_@al0(cewP
fpUvsV(n&FTu5*8(wtOAb)XBPb<{dQaR*HJfLy`g5;Rk$tL;<2LZnf~lSc0i1ZosF=+&d%*<Mt;oT@<G
w}8b|2t^eSFu@cvvuS_b(ekkX8+fpA0lnIJ#YtLoKgdd}QbR<RxW5Q^9x;eWn#4WFhyM6_e1BJMpxA|G
|LPk;|1vEAIWy4?4~;Ag8;CkR<g&u-#QsT4A59ZR-BuW#V2dp1sVkfyNGH}_?1SP$FA_C9Ra>OFP_IgN
Q*3S1F)ri)hP;0L%A7V2K4`S+x#Kj5kpbkt4le_+HkpsvgP+G6p*McK<}^i<DaV5z>HczHMSeTrPT>b{
5DlR;s8OO_GiH$O4O@h;f3>vD3lvGVJovsl8waE2v5>|U5XDb>{KEYR_9<LzN!|wLdB)=r3c;DaZh@Hh
r9Az@szC0>C4B*jLhGfz9@4psYcb&il!=mCnabjLFU*jBV1YgXCz6?>t&vl{RQXt49g3@51YX9I;Nf6;
;jiVkeEyO4#XE}z857vr*Rzsx!)__$M(+jruanbd#K~OJzYg;$+WiJ0`TF;PVk}BIQ4WPEV0J<R7D`3V
_4JBOf_XePjZsj(y$}g0!0R4>LV^B-u9P)}if*I-1J!?#-CDsI@}O(D?G|?DQuije+^q`Xj-IAU4R%33
fdek1P8*;uH|X^u+1;jdYbUI=mcuM<kM<{n64_&8IK;Yx;^brT?(y^xP`QK58i7x#o={m8X|pn&ovKK8
cP<W7_;}n8Hmrpo5G|F8Lw%Zv;&tR0f54j$(FMu$5P7XSkx~7!^BG>OB#c;Ug#ju65<{o9+!HcXXo(=c
fg#<^T6Cp5MLUQ1KIU?2%?V9z;$s06hod6pN#FyNqM(n-`F54QzUX$t)q9pMYErq||1U}l3_i1Tk$g|P
sGM{~9bnD5vY6-Mpe1CLzqzN8MgyM(g?0Hl3t7CIsN|(^H%~kGIstSKgeOlRHS*#_4<~3|9I>+z|B(=;
xZqpN1V4D<Hx!K30%eyM;SKm5PgFlo2EI}3!Z#zdY5k=C)5)p!8!Kvq&oK+{5I%T#Iv3)36hCAps+U0=
2kFzBe_}8vK^+}ZH3&H9BS)6OW6n^=WpH9dcT_l2cfw*tpN+cw#Vn@ZAs$n28hv{rjq?{DIK>r0d(;OE
N04BAQ-6+G%T=1FNx+o0AP&4;tQTfW_cNv68z7iQ<X2orZ&J!MP8gFuTDn;dwu&0YCZs=<qzT$sA*CMg
M{S&%ZYT{LJCUWv5jFT@+0*^y!&iNUZob{(b|!A3Ajk4w5NHU8qRl|<$^&_ujvh>JqhT(hR^_Q)A@S_#
62?H&0mLqXG-fb0=oXU(AFZ~0BF%}_^)53H7A|$~uzL6o0H$OSTI?@|I>ebv`A8WjAJTI_r7EE-M=l<P
>PL}9`PVC>AEK*<P12$+rkAUGLf7;U)mcJ0x|d<Cyk>Op9;1S1dgn6EXa2Z<`M;1j478oz@}LT}si96(
T3y!%k9Ml;tJ$%N>=8W*ro-QuCX9(AlE{!9MK@%rj+A6J(&RU$IS7QXQR2N4SH0;^h=^R$vDaW2uVk&Q
c2wq+!>!7HHXDCvk@aRa3xN)No>XqJ)gIJQ;hdg@!a^8S$6?^K!9Cx*v&5~)t>THg^@&#J49m=K=6l>P
5O|<cY*yOvW_~s;nQ+OaqH|b^0U(m_LdI|Fz5_L1$olz9^XjigV`UfQLzBfM?@?uQcCj^fh&u<pu(sd6
HQX}4Xq{LFDa^E`Gjw*5D>D!B=PDTBz>mQ~&#HvbsjGk91+c%<_tZ)=x7LcUl2VOpAX+;=cC9h32?@{M
4$dl~>C&1(^)@ex#wN}$Jm{r(UFU)*SRdKhrmonFW*>Fi>DKZVFEroTD0J4tN67?`<tglQ!u^XM514G$
k}&KcEDSfk{%d~_XTwBCwyeMZh)&JzJjrP1WtsA;%?EO+djTsuQCK?Oh1r~mK#(8CQ5Sb`%gye@!(K2=
*|v2QTL!gHhELP>s5!}~m~=_m(h<B$w0m8pw)HmYbaOX?6r{)_i>?#HP;)?gk!)OCdf1|FgZa6u<ez+A
ekx5dNreqc2LFovIAXc_*6R8OFF~LvJ9%!&X2}`&^k!vN0xO5KFsDMHf#<xa6?naBM<+X5PUr}qzo-2B
B)nWQR#z3%A7Em5ymx<YGb}AR+Rh$*%LgbgIU3oD;BOw3Drb_CTyhz9J9_M4;9mb;h6Ocp8&xu<dZOvM
PIF~c*&xAbgp9^)IIe;bRqfdtrh=|qU`Z!R;)_WSTTTu*co1{LAcpF!BRJNGeM#Cs?kd>RW)~nMbPbHb
J`;%cZ9DV2OPhiS?gBdm?ao$1!s1MH-sCVfG(T17eB2r4!tACRCH;2nT&(!0Mks$}eJJ;<utTZL1|v{<
^O>(9A`s>0h6l$7+$=?Q4ENs}2OT0f`RusD;7G$pN%cTkF2wXXl-aoiSL*k-MlLyz+U*ZaV|rsO2qS4#
4B}hOw{k}Av;UkAcdX1!&0;KrQQ)AxY=gGK@4J-JV7ik1R>%TQQZXx>PBbq_uy#bjtT<1sT|`&$0*QN%
0ksUZu<)}n7;1{MrmM*G>r>Z41fN}0wL6Lt&9Bl8e{0`l4`p4I`z64-iMvSMy}@bCH!dy+2{;Ho+tTg>
Kez?jcm-RUFr$;c&4~v-B#M7MEO0%P0VShq3^4FIctN;I%mwiY4O5)ut8%2gfk`@Pry?)il7gLB@njh`
Rx3Us@$gFrB`CRwy`WQ6QlyhOMDm>-6m%VWqse+%tq0HppJDzZVSc?W@pp*D=5`k+=WBG<S9G~6g56iQ
_iu0I*udmV8F<Z60kAD$%M)MPNdGL?Z>fS4MY9wfE!+SJ3UO6Hr-d&7ezsWOvTnB=NP^Fn9K#&4h*)1$
(JF(@h{p<T=EJVh{^QRae90jUiPV;XeO0WMO`tBVt=AVyxNiO-oMx=Q=D?XU<k@L|q4f@(R!hbf$v02f
YJrQf#RoHchjaPzs-P6_qJ{IwKgsB$lznNtMJ4|CH;woKuW=PK^S!Ao+=?r?OMn5gha=V~P12qS&LQ3d
dr$Y1%(1`O!SqlpuP}%uU7n~t9Lz3X`EQ{BaHsn+<~Yb8v8*bG4=q$ZX)@x!S>ClzN17dcU(40_WG|`|
!$rTe%-12CZ<Epn#v*{fZ_-P~P4EeuiybD`_y6+;$PqF!82+--YrsMddlZQ^rE);&Ef$3v@SREOl}rP8
4)^S##Xuf$dFHAvCs9*L-RO*^gt&xYrEm;K2m@NMFm}9?g+o-w#hVP?DR5NF*3}4o8|0xCxx0ax1FuiD
qjZ_NT|8{Zp8o4v^TjZ)9QK*3Zo!M?l=#~Rqk<2;bv2789RkHS!mVu*Nd&Lc{d{k!y><p&7hQtHQSK*B
M?ML4ygu|Y<w03|KNsxRB1PBx{f4(S0&v$~wL3>+D5qqwQM7T4K6Vxd$`QS^hHii`y}}I~RydMsVy3%S
0yO~DaxyP{^?7zTX)6{Bxok#~fVC>wx7o~QHf%9ONACZ3M~rMfczNo^=wQTgYEw}QfC~L7_`)Mv5b)&P
PA<G)T?;WveqHum7|yp?cN#sGtH?1>fEaARpl}6RetoJ)6YITrGVg1rfql?J2<U3tGLB7{4+Q&qkB(d1
8QS$w$Qk5zcYzBj3cZ_fSia7&5>&$+Wi$DO4N5oH=>JA1y~m-iP7VyH7KG;~#_9h(au<Q6B&;{S?9aM*
Bu`0&%4Qeid?ezRG|$>T^(}IMnl@q27bfv@7&<nFj=g61(Y#(fni9eq1cWRQ4DNDwcbQf&dxW6|J}^1M
#lS=D1ERdTj!OtI6b2@}p0D@I$MB;E$>$&U3b{()8NAO9!j%xCDa|rc)dc1V-yq(Z$SYy)ciN|(OTeui
6*>S7>&Z~()pJor)RDm)P+@s&Z!t|M7UQ41xPX$~`J$*p%>Pui5b4<n5xe&A?&`YOU<|i68?Bz+0fwP@
Yrdrf1H5tl;w)pjvWP`y8xS8!<e`un^DuPwl;e~KSz`*UEry28#<yn@YcQp941cNGxM{ZWd3pDTEorX>
NU_!=<?yGAs8JB`V@ieBj&&(~yPsm4e`6V_Dt4-<`hNWclJ01u*k4H9=oWs)YkFCT??;&6woX#4-!q^q
iF869BJ*vv{b<K*B;PuSTig?TyTxa|`uw9B-T7ES18}NGxm2uaMmifq6Au<wIj9;>YL(JM#UtV@iPsob
PjOcqq|64B3z3SkSlu!2S95IojT(8*bXpPxn1<;6%^9(0iffGidw3+Kulw5C`l78-N%k{GmaM;sjd)n6
?%nN2ivK?+f`tqN7<I_EvLF&j`o4(@Ff;{^U=h=d!)sq0TNIDI$9K5^8f}hS6AVa`^UY7um`-89$|CJ;
o8~oON`S@p>qO_^@sGy9_86XxF$yyIX5Pi!Iy?$`9tHz{kwFc90{c=Yfv0r){fbQYB#4-u5@aIUM#JW%
;WRK~Ec*d>2XJvuD(C#t?$$%xm;7j4#oRr1J|TlzGudnh(<1#L(<9+W>~)T*9`-|cq5hQ?t(M1Ew=tq!
1n{>{JjV<{PqUp8l1E?gcQwd!Ou<FnXChZMkKsYDbuJ3<yyy2|<6JBAVo&h`>@-XJ;#f*$hAkGdp+F~4
tgvRouVSI@*V?oEIj-T%US(w5z2~h4-+HpXnR2eG{?P5vj#qmrRryQ#Y|#cr&&k?5#O5P-p8!ZzgX@C$
n03yI6c;mucZEim6&OincDMJ*h3^pBo5PWW-%jCoe{4NzWJq~;es~~giSwm}+$I%X_m-Yl68VIwqw=pt
CX{&^?9eXzUTZ-KK)B8-T;f_!qi0)~-AZAoNVAyvHMnSlpOS#}d^ew@6HUThQ_`j~GY^c>{4#rGmWT&G
$;u0(x!bt%BA*YjAJ1IJn$(;Y3Sv763mLTZo*sp5-)Lrd<u)B2q#V+42-|pb3+=GyrNgSZOusn&J1PyD
{OQ4owa#aXLIfhkT^HTh&HL=zuv>}v1KI>idwgZWWRK*R<E*q(LK9BIH|X^T8UPV?l@;dm4l=u(nA*ip
)FTccVw&Q4Q^GjN*=_(LIpe=N^arLOmSBClMlAU;vS&f0`(k+cAfLu+fkRXR)UxvZQB{nJOo-K$az1Cd
({?-JpniViRjzSOQ>2oi9Ddn3v1;r1pW@6E%h<1-i08M{vSgF|Qg&Hyf4>;lixDTzvQ???IKv>njMiXn
AW?gvz5gh#D}vxcrnmW5NwZ4B#2b+MNE{xU7rZ6A$NMXngnX3oJ~PJOXzxuv8)9_D;8sq%QD<Yl>utL~
RIVzj#)nfs5&JC_fWgRTc2l*9h5ZhZG$Kie+SRU)B!IMAl?9Nha(5?*pe+bEPQ-BAWf$F@n{Gf>Ix*+Y
Xb>Zf6{c+3_t+yoySLYb7wi%=C}N|CShM7xa+s$rP)hrFVx2qH@<mj>Mj2(KglnWLbH_WmSTl%+4^oV*
@A8+T3fSGW{O0DwQGSmBSzBNFv9Tv*ClQ#>!Ho*|Zg5O0enkPhU7?=L_30c!r*zmAh4R+D71|o6?RYaj
7g$yZydxQy_0$tkICc~~>9nRT%%iWwc;(~$(diXVJgmOD-%oy1Psstz7tShknw}5OQtmXs1i?i|lFgj$
+DVX^+BuN~I!W=2FvNs(Z-iSA=9lZmg#FMVi)L?n0%9QiWi{Ku&c6=Hq$|#K(a6-l^-A;%&{7`msdZ2W
yulVk&Sw?GQlvS9n=V+`f29M$0RN<*69IC!sUD-^B`l%yia-mjR5LQR$?-j5rg_&6nCeuQaTMOy{*iH0
gtZ(_qq^L=bbA%*#tDhRbPYG#fib9eZx?$Hi*}q~=106mY?(c1E^4Oiq5K`Lt=?7auq_y9q-JHpxj&MJ
UQ{o<54VsmF%X*wRhK>sxj5*}W%)-?SsJh<HD^{&)zmjUvra-@|C-pPjv1GW9K~t`Y2!ahxbe(s?0B}2
f_8K#b-QS+V|GQdxL^2GWa70JU9;{voC*(wXk_bu`Ei?!IRSJqWwJ_GF*6`BVa#&dQHz-y;#^40@FX6f
eLi`PfI;T=cj><^blkdo>{%1JGbaLkj35VDy4`PBRwud3lxP~4>tXtixEK}XT{LNK*rq|MMRXa)YXEgh
uJw@Y)_bC&NA;HRcufqXK*P4p%oOe$^f$++Bi(~P4C_bHRGL){e7Wa(1200|ESX7F>sPY3((U985#-L%
F9nAyecHYd4+C1)cy!3@4b;XT$z6Dlz0_x4Sj`ApD4~K2*>j60g4sQI`U-R)M<QNrq*j=nX&*Bc$x433
05lrxCg!1or~GcxS^<;DKF$_`aiU$?j+7PG(-KqF@)E25e*%casYEjG6ze#z(vYb1<eAAPjzCX58rqyR
xtTLS+jxZvV&*u(L({~6DUKkSP>!8`0*(=kdw2i`u86H4gC*OEWoWcJW#?`*YPk2!nG6=!5w!)>FpJMg
B^ZS?;p#fg05~pd#H^T})J0XZ5sR#geM(z+8gaoAq2$k(91#Lab>);lR@Pl$R5<(3cmNufTb}4Fd;cTe
Tn&RIeh{MvZ)JzqV_!|&Sa<tEf8c2hg0X(Spb1UDAk670qq4(RMockZn)9dFW3`zkQE*a~F^&_c%pX22
8a7q-%@}-<su%zH%b&Xlr@oRf;jDfLf;tYGT2$RY=;RY4Cc%Xyg|)6apgyuV5$<*%0=7&mvtdsj`b?Iq
M%N>}$-GyUNUCB+s>;2|NypB*5}bZZ|M@Vt9T6za&2^<K<=e$>#rt8VY55!-=5RpxVL{v{K80I966uL8
=RU-T#-|(>!Ne%HcCXy3-2emc(E_rRe01Oy`-|JrAx+q0$`Wxe>6)~=pr)>i!GS9Mu)(-mj?~^9bJwA5
e{n0*KKqiyjKQ0K!WM_@IE%kAK%Vcc2etP*CosH$zZ@ArrW~pbxBd0RinH#hp-nfyz}nZP!plUubu(E3
KhgBl+(;O~LCj<O7S#%ck*MHITAN*-eq`Kc;+zzyAn}QW_0S6#4^#t+K(*;5yh$po55Ek`#D69dgVrBD
Jg>vTQym)+ntKe`+ioRwj#*)C<lFLDOty`EY%}pldeRrDKm8TPS*hu-l!(7$zK;2Kvq+>_w)J0P*IIx6
-P>3$+J4HrU`PPZR|Feybp&UGahu~Fh2BA?^BSuiSF63-zM^=%hv0=&*$sGz7&R+uO!BG%grSo!QlP%0
fp$*aHg@>bY?B5v0$W2gHxt6ZfPG;IzJor9=(K*O`jv*X{*Cop^{!15JCYl$-?juP<2VV|J)cR2Jb1Vi
m5UXf<)~-UyM4Tq=*LprfCg-z;8qJeCD58Oh_6ubwwLFrO5iF;e|a6gR9`^nr5AadxiyV@LK*"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

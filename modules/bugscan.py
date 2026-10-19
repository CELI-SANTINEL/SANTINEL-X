# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "bugscan.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("5c85d9c933a79561fd53d58a899776dadfc59aa40fad7bcca2d688808ec7cb6c24d4d6ebfa01aa65202d9cdffdf3205e301968da48969c0a7fe9f7323037e0f6")
_K2 = bytes.fromhex("061962a7d7d75b3f98c982069002f6d1a83622ccb09b7bc92c7d4848e956ce2124d2f6acff6973b748c83dc976fd031fd7d6cb33053b1d29248fe38279eaf702")
_K3 = bytes.fromhex("4f47e576ea9303a1b9f2addae33440b6c77ed6a9f703753464c4b8318bb10ed34adc465dd822d59e3f32634e44c56abb94e0476bc6adb5aa0ead7cfc1e9b1073")
_S = """Z2`k$Rg>1JN-&MJ2Z6~iP<HRfmnA&0rRG`;PS_j28}7TlofxRdR#xPJ*~1AZetl-0U}R>JbGkw}8Y^De
+EurFymhC@xh7x4FNgmRcN4$o6AsmR^FK2)RF=2b2k?2WdB-r)svmprKIu$@O0G-^_+Qf(E+x^c$u;Q$
f)l1N9Xx`JmFj}cLhbMwBb~qYtr0SLd)ru{4TMdK=-38`jBuH6eTGLlT9|ZLVjBF^u(cPn1WXCR1bJnb
7{iDngTVBi((aF#CNTVr-$_ba4#%)fw#g6gU^IanQtV#W{ts?l(OL|;UfKBmuofy%8Zw22mU5=P#!R+_
)}oNopUHgnA5NX4a^!T~h*Bp`5O7|%;qy(}SwbclK}QogC@3+?ni)jNiF%m0XFjq3qAC>;x8))#(VoK>
pkMR+Im`Z;|4mn!*%RUle2>D*xoI^us!*8>=r~=Lv5Uy60<8tbi`@wr9GWL%V0QYqkrDA()l>^Tz$9Sj
lq^;{5fw+CLUo=KEQ-eL3vUlj7ge&d=;#PR&|U=?&cNeNsdVH=td2xg%Cb1xo7e}e88K}IlUxDSM|)-8
Raj7<h%L6eGy1la4rRm_zHRcLs^BCa$yA8*e{qmm`sC=H%y>5dXA~>+F(;j#HHw##ai@lG)>nwRP(z>G
uM64|jmY7E;maFx5&YU)vIas<k^G16rpDZBzF8BDMG}KQpKcWn^ZAw0MX77DLq%e!s{D{4G2czd|0I(a
zrxF~fAVkXbN0N1Wv}m>Hj$lcd*zbzm1;SWb9QMz)#zhLh}l?Ej!!~QZiZ}|QZrx)gOHt{-(1`TMGH$B
AM*_8cEfZ!R8hG^n890&q%PK-g&q2t4qdouPO)0U92#;jQQX~qtsLl{FX@ldk*e$A4{}i-r`JFm=pN~Z
<KJpAbP-;!%lTLrZDUck{6RHUdqC17DuJ>63~Zf_?Y2zQJt-S-cVDb#>x0vuUBBeMTrgz0x;i#Rd1}89
wAM+Q<KxfcF6{q+=dE}KYqv|xl4!I6qFr$FTTs@sLL>)M(r0x0FvheOYdST`vDO)!%(saIJ2`IK6j+uV
;%Fo6j@;D=@z~^ui*>$bmS~QUTSs|ylI*$C@GHxVp)1#>T|9iejUw~Ik(t8e4ZiVv(U>yU(peG&bA^pN
>Vv6ThNK4E#Sw0$F?yPhoJ`2KGq&_Jg#JJEZxQ<N&bzlXXyYmAmo3$x$xl1g0WmEM3)Yf|D({Q^x4K2&
<r!Y49dR2HI%;OVjOs<ySvX0`<7BEv;!Dg34(fc8yGV@f0~T{X^s$ejLAoYf+tc~~H=<R}4ly0+bQoPe
^aiq$Rf+rbLc#6>0F)&&2I0AhtRdQNXLK``IAa;JRZ@L1v-TEyL3&BIayqBsXdHh?G%(6VEwGuwuZ_<j
gofRs92DV#N+Yfzl=ig{nKHUpcW^h+&s@AU=-+e}ybaq1X*V&s$<d8F!YA5I`j)Uc0_-NlNrK!&#-Ch+
{`|DxTe`PJW_rg3L2^XPm(B|YD-lnbijw5tZ$9P~=io0Lcbl^mBu$n|vTqXW)$Q)J9^7^A9gUe*ySQv)
&QTAIkn8(1In2@m+=z6oqkxULXV>YOjXU%Mq@vNSj)Xcp7Z0hbk#~FLOW2)+J=Y$PCi90pGXtY200d+L
0m7<s+!vceSPE^lI<?2Fy_B|e(e1>bOJGqLx5qycQkl%2Jlh{0>;oYUmW>}@h?H<!G6}BQn$vLaR0<EF
B62rd6rU*=9r=|U<XGVl`{qlX;Vkl*<|T`ycG2PTSRQh2^?0NNm_i(Hn7H#VS2p4s>J;48#~=^n>N>QS
phDx5++HeECmoC)6?0E&)@&h*LTfD~DZ97(>4|+9yIe|0jF!JfCFFlM(e99;(2{V&=(<Uu;iRI5?sTud
fo}MuO?KF**_@KEJ!k&Xcx69WU3wsQLrh)L;fbE9@K%NQ1n%W2tBc1$Ei{fUC6CBQ*m8(s5XXxP<?2=G
L&5bc`6Ur9%f7~$Z<ZcPk~`NTq2Ou`8w~~P$Mls{_&o58FL$=YX+;)N>0E%nb$wQaC=XFc%Wp<=G+<HC
>jg_{m$8=?llhMCwuhocmtDmH9i<p1*;+J|hPNH8KbBj`9ezFm+gkga`|$e|4|v5<8R}O@^=-W=QBSly
AHx~`QbJ)eiC~j$F4d%KfDn}%JwTm<L^n?j(43@m+fAynT631@S&cVpvM4S{zm8<P9f=#Te?L%?#^;_$
c+1+Bro{u~@4&<7z26d87rzF!E~JPPy*^GrmYL@nz&)tH^<+Z&?RzR&0xFsqh61_=eW9k=JY$6LQ8beq
X3PI7S?YzVmiI!O+ICoT)o3&R>w1SDGWSVJKgp7>NvVaiF41mEuuo2e9~UjW9akzB8aoHR$XavN?B162
+ZH?gz%7umJA@zxgQw+Mg0(zf`CrybB;^9GZ>xK&Jn;YNJ%VHpLV2)DzG}O;CU=FUNz?>INVvj&1EZ}6
hH{Ken}0gzsYay;3Gww8FLp1Bi}}j=+lM1GU=eYdlJQBlLyu|AieSXMALTPum#EGoZ<PtG1AFW+4zk_l
1D2Y-c4IvYxQctK0v|jUDRg2#5oT|?jQ0hE%GU2QhCX-q1J`b~DkE}jtc<j=>Xg)3TwYiZhm~U#?e&Ql
f9U7;@?Tv}BmPOcMZ1@9$h~E>5ps-=8AmMQMpNEgH1Mg|2=Evio|ld4+mJChxSHNJW=;8ON_sY`0TjDA
gO+?Ne*FSZV-+JX<VlEr1qtZc8n}xHq>z2L*GXxxFA>fYLIC=N{D&VAK_eQjVl!PW#yMV^hpxm2w&H1M
JdRsy0t$l_TKrk5y(jpOIe@5?##@%fiSsG~9QVRzr>Y3R9F#}X%+BG)i|C7!(dX8rzA90W#?jSL@oGcg
1aVYNd~4ntG`Eo6D}FAfZ5`r>1XI~*|6YR0VM~7nY(Rr=j%?cj6h9Hh+)g=)XN@fYbdAd9?4;k$bSqS`
2Vm&OXLIf&HyDQTzahYF=qVxob1H$#0v1OB5Vvjl9ZjZvV?HGRrv+}Wb?iBl>pEG<*I=a|=)2RAc`xBa
o;y?@Vn=Cdfr2uh`2l-#N^q|f13AsZJ$|~ZqI{{@Z2h4dx-RImKvuG4FK#dl8MpDqiZK0%X-b{SF3^??
vgaZg)a;52%WP~p7iLj6Zm|DLVH=e?L}iR2$o<v$B{9XjJvv)cDmt>yLe&u%@Z?A#HlzPn(={cQ!}<b(
0S_zy3M9Z=;AdEP=W-aXo5oZX2QGv5APH+o-ja`w-_}F0fnrMP|MIR9X6kA{^EZmUZ4XYgD=O@fYDd)J
P5Me)T`sv}4Ib4Jlw22uvWz51fQJ;gs>z~TUY0AZ5c1WmmA^-KzXz0~^6g}6eVe7p_Ewl9+1;+-dXy%=
Wg0MvZPh@V%owJF7pywv`J~(y3?U{vV&AN5KId}Vb7JL2?E@XEs^LgCiTi-@XCW7ILu=L21X7DEI|%~&
g%*Dx>tjM(G5gIqN7$py7e7lMEY2}Zp%NPjEADgcf&C$Mz)yU*24tbjGr*KJ2T+ob?lWF%*oJq@XiV6j
=@M3#QvFtC<Jrw(kFDkPr+&$?gl_f|yKcA32UbAj{o!}SuK`N?ti2k$fFG?xt|a)a1AZDwQ%MH<YmX%`
4r<ctwBBzwubZ34?*Xv`YhatYOf<y(;gq!$Qe{D>Q(v|h@T?_(cz+AL$3!(+D(mUypMK9q)as{YA|LFj
6w<&8fh~G>FKA&aYsMKlM(h(cLek_$5N(vp_=m3r+C0WT4_q}eSG#g^;D)6W%+CdWC$FOi>9MGyl>P*&
6Ea&|TA|V{LTzialVMu_oylm<<Y<C#-@l5a?>7hjf1yWe_*zgw6D`g5)C{m1dB}%*)p}x?3>}Bkpuyg8
Ufdk{{S%raM8f+*&Qx){pN1CG&=z6r{?3w=eWBEqpN^R-pwLmi`=^6u%o2rrR!_*vhz|3&6Ha=+^PdtP
MFH7C$r<n1)1-zXN8qPn-;L@|>dST#@*j05f6RGSrOQ760<XkmEf9Lu@b4&jS<6SmG9(&uq*dj>s5lH3
BwHSr2;TGCZWC+(D68y;Hc5q3ZW(^PPMSJr@3k(s3aAHSvpYqeQ?AVvdf11SON}N;8Cq(E97=j=m0&LW
$*KD84#$g2OAe<&yk_ofB3IP|@(gPEEd%^}P%@$elxw*<CO07N&!V2v)AfN~%F3^{_Xa0ojey4l@uH<Y
bX{C@g=<WKU;dSbfWV~WSH{#pwuCg+ijbVC$S2_$97xmwd=O*>%)?XAwH?U3`m-MY4-XkgXLZhBzr$z0
^_Wc}a3jQ8=1YkaLSse$=xFl!__262md;pl%Du4w2|!0>NV)g$NeLwuhBl!2&|6`D`>;)KZ1kW&%6{M%
@Gk=fVo~j4Vs&o95`U5J{K6uIIuk1_PxARLh}AE*o2LanI^P^u_e6EcT`8q5*NdPP29d&w#t7_BpMIpI
uy4+|iv`b%6svh`pIm@yu6}3)j!N-8Ly&P?E42CJ&!$I|Ka%gLpp$+~+N&F)`leVGtfxSrlHM_He*YfX
4q}-PS)MZI@-4B@tFn^vR4UR9TkU3KPo4i9P^q&%Ly2C1y$M~TUW9am&0KFGJ`Oa?X7f>a2rSVGgC&c-
!bjFvrlD6x2=!ZCHf;;}TB9#|?{nl}Nd#MAFhw~!)d+c?<gu20k_`!5LC`1#T2j9l1@seRm~&Psm&@Qe
U8I)SCZG!p*>P7Iqxxz8_RE9gP&g%-pT=NhC*b453|tg*#Lq{IPm8GE*)r5wgr5_~4m2n@nkdrDs{5Nx
`i9}ra|jAo`w6blo)xw~Vd%c7h9`jI*{Q*6I4ytB*u^T;1Hx}h(l1S50@H7Mogd-6t{MKY%$W1E89kF<
h7i38sM6&4vErYX_r}4|$)s5&@!Rqe>tz7<xF7~ZK#w2%AZBsRP7=8=*56HKqjUB{sN;BBasBe>3P!Mi
BSfA@$PK|TrfedLp#E4&5a4hSM8ru8T`uL?H&f@DSl1XE_=2&m2J;C%%dpa+bwXuQ!6pN)?U<59dn<cs
T*2;*o<hV}(Q_KdF6nvRAHmc*kMc6C>5|{RYhZ>UIHVeGwK!xPh1#F1ed^_tCv50(fg>GhxqN+uqg@ou
e%pt<90toWKYk%D#RF)fFFF8O$#L7k!qL529I$Vkfz6dUyl=-JvD6x0ukNHqG*9(6W2_>|jr@plpVTTx
%i6=~clh&7DFYgn`_@t<#iE<rdT)p(Ze4sb70qPcCFfE@K98xRdTDu}?4=Y-IQjyWw5SUG=AhH|I=f3d
uO%Jl^&M8i2fe4~C=WG5$jG}!59><9E53CYqi&^<bd7btYXwp<hqD>>Q*{iK$3TAJX2Wk}mb}KYWx8&E
`-$>p<RF@mU=nfayXWf~4<iMCF;k{YE!-u}US9RjHxa9|HLLCSv!OqMI(qh(2WctydXl~r#|5)>AhmG)
+a>D=lY21`_qk);g<LwG+y0^(^H7+KOW`B_GIw+nxCcGVv)-fe_6e6us$E1Mb(p>IaL_5n>0h=a@1L{2
3G_3hSN7tPW&w4<EX~Xx8)OVIO~3z+LrAhiliN?x9vAk-;~_2v`WVVJu{!tT4SK#08kz&DBJpUY7)iqI
FKsjkwvsC_+g>wi;eRYaziI&A$Kz>qsfs_MV*UL(%^)2v38i`&*Dl>$>&|x8X+^_bBpmpvtJqQG0=VFv
mF08Gt~Y19wG}7!q*$2~swjv*1|5%WsV(O=Sp<n|U`~JoTc(DCoGiB+`3_!BS4&zd*g==3IpJ)VLPkt}
DbUz*&Mxcvg@~(u%ZyRMfTR)k<xxF}gr^K^=@TX=^Ajr&V<!~w4z#c@bqcyYdmjQyTfuj;z1}+~rC$^p
Z5(=I69d{@w_W6u3C-ulR3MG%+L3bfDCBx`RnX(Ms0-^mvI&JwYyxtb>c)n6-o=6YpHQGZoO|RLSAEP#
*sO#r)-pgUp33+d$M1kQdoV=CBQdP#KM%#-w;5Tm{T*+LX#*n+Wv-D%L=Z+C!*Dhwz$DirG744GCj|fH
si;ZHXk4lLFe7{R#TiKB5NX4uP<`ETCoyXvY_CjI)jc<8@2{OxkS)pq4+0!$2k&e~*(qy^jz&igT7|DB
o0i6FjCWT1ZGY6J5}hF|XF<&=Yr1=S^tM99)-ZB9&LSk%?L~gi?ssMeJ3|82yf7wCeE3K;Ycd$gfF!Ne
`naBmoT=I`e$%<%zqUZ*j}c<A#8nRf`~7Cdb+H0GdW04|9m)c<i!YxAT-SPg04-bPKv}{mVvk{~2!!Us
xhkP8Ea70#BL@oN>u7kO#&Vaw%J6R<jIH>*qs8yyNbl1MPab3yQy%K)$GPgCVhiVBK5V;ssmxHKaX>-{
3e}sOmB(E4tTIY{%8h%!yKHGC0;OA?jxQ0L=-w>G;;V1m5jBJfVZK4CFvl2h{4`-zqyPn%w83Bt^>~JY
Tg2aw!T%7oE>T+YITHsyD+nN&(fElDua^d4)^^))6MAXt<UdA2;<pRSJv~&&?k97X{mI)|EIB~)HRbGN
t5l?J{QjmDqzN-EhfX#S*=`r)`HAnGR`n2+gAAl`6ofgZ5%68RCM1QG)Sj5=wDl}i4pjs7<e{%xt5XT-
V;*E5xY^2`S?dZRRnagLLKO4~VZHD6o#S-T7y8W+(c}!E1Uc9BhGU;=(_mGkNFXB<Qo03{{v@&Hxc^$2
zQp2BG5cayQ9aH%uazHx%hnlYHI5fqx0JB0_zjjsdl!mGSGK;ib}Z!;cu{|WofnI=<{vHsfJVjBDChv&
tp-tULJ)SVrPg68k`KMn#<N-$jQC&xnWXMO$@(!aDa4wPv#`{(#>NcX_ol?5nawg(BjbJ@qYU#FAxncY
;PU^j7)<tHM_j-AC9&v~kY`o*CGG(B3Uf?usSDC}2<p)4C!Efw1|d(d)T9qFto7A>N^@BoU8S!$au`)|
iT+pX9?E_j1q0r&GHp)GM%+6lK460Dva^zLwJ&7HMYY(Yuvdl|TY68PBoRM$rGOTw>3KoYEWTekY(MIs
@|UXmOb@S*HwwyZ=_}UaZM>h@t)4C>z06B4PWLG#PAgy|pLa_WL<9Az*x&cGJ&jAtdwJ9%F+mba>6bGC
WEU9!n1Q|?anXt*jD(s2%2FCEBVl{8;^zHjFcGnUuMG-ru&q1c%31YAHSfNxoyk#eEmMUP29Pd?jTXBh
WE?h;73i-yMn#z$Hpv^0YU9`~P`XiJQW^9rS9DrXFDN%}4o&ho6brC$sk$YjZ=lX=1}d$Zj$SXWGE25K
^LA_~F%4RZ9a0xO@*6Fb5h-OC#f}e?TO1`skBWv#{u~UHv7Zo?`R;heNG$m7mVu!aB}c!iZf(Ca3NC)%
a9|(arOwh#Guz=Y&D0xc4Z3<TGV&APhni(1F}~v)0gKT!XR3pmdJrh~p&k@>fzAwQklR7#iyKvD`pngY
Vn-?B;LV6wddtbk0rE5KC%S}0t<u-sfxfQ=J;h6^Qe@et&liD^2&w<F$fB|N6M#XTI=9%p&|1(upl$FV
>57SJdK#Atrc8{hR}3rC@kTurKyUhjK5CNCaOp3=*D-<)C(y1izg%Zvdsk)eGvsYND=>Tvg&aMmBCP1v
`__tut38Q&;)2(r54ZId@Ht}Wwi=}aMi+W#F@bE@=yF;><UP|cu8!;mSwd79_Gn=@kc00G<9?}h3bD3n
HpVhFw9uO&WgZj<q+q&Y#uE!-H4@q%G+fA>27cT_q9=~Ga?m#W8zRbHT%~l)9Y(&HRWV{uzVW#GLNGed
A_nhWd8hVxGr~;2O9^q8k%v9{j;tsgyFbIKJ3T&w#69umWoTyR*f7<nm(<K(zKEMxmo@ELus<hJ1{FX(
OZ9=(*>)>YQB={8vL^qkUVD-~g$}gYZ;BAOjOP>L<hHIGCR?5(PeuA^gC)^@j9nh(F-_4gq8711q`>#$
L?{7Pq3)n&TX!#Gg`GCicf09hJthJkhPpL9MhD%%GjKpq$DE}!9u805@ImF#kjVyjLm#;$#+31ZW);d2
y!|+G*3tL_C}o;Tq5}6TPH8rM?pwA@RmnrAw?Ag4Hf4~~evpd6{3tAFf1;`u%z&yiA*xCr`k+EI5w7)&
Vo=xQ9QvL!2-2TCM@TtuWP9VpPU_eaipNCq5M^qM%()Y%EnT6flEu9t2tUfb<}!cZP?ZT{@3SL2`=j&G
-ZEvMZQ%Z--&-Mj?ZVBf2f^EM1PBCb?X^JkV;Zrk-6RDuUsty#5}BdoVIrza{OM9@F;K01tWQ$y;n-T!
2F~jTxF5VU+n&#(!PuYV+V1!_WqyvUkSHVIBMVVgGdQQ0LQ;k1WHV6&Z8cm7sA$1<xPthm#s|&!UB3BR
rpShPDWc|_Az{Eh%$xJ7oicjz7mE^)7F4V?p<ev@T=A+s+}Na0aY$B6dNwH+#6AKj?1VOb6Bh~*V1OJQ
<t3TxvGcgHnMbw}UB+X0!@Rv@Gm}1!F}m1KGaWjQUx(Re=KviEFrRB8El_`00y#8i>2weiBM8#A9Muwm
+Oned_hu<mxfKUlINrq)TY{B(FD|@(5vP&A0f)?rLgYUwwi<CNa&XNt@L+h_t8wUSL{;IT_~7;;1h~5p
iM5O7vaCcOPjb?!rXrfd?o~1J3mnSXtSTqv+hXyR7t}`Qn0qxZ1Snt}N-G25=g_vtMYLS@{Pnd&&iQSk
a>s<Hyp+uY1H^gL$-D{zS+7qrf9P|ul`2g75Q}YWD0h%e@a<P^BzSJHtw^_I&OHS0wt0oj?xs)?T;Kc&
X_MhRwX+wpf*g|R#x2M)rI<6VAM<-CYV9D-)r(kIM6G59;?By&;6?Jyw@@em*9kf$%Ow-RQB*9vRE#%N
wW7|8HGmkybU0Z=QL9ynP}g<HFe||k)?j480T5R@f7R%XgXY`>5`TXTZb@5nB@JAI`bYMp@IC4k;-IDl
7bE|YN>kS!puo9q<+~IP#W(3VteH&4i|%GPximqu5OR}z8>3jh5^yuI^XKEefEk6Qlg%IP9V$xmc>EMo
*?v5ca|dQMZ|pU6C1QJtEveK)y<R9gxy6M^-NTkFR)bXvnSae3uo~+23FC)h-vA96l4IxsR+feuM>X#3
TUiex+_L&=mt9n!==_q5I&i;#e2e16yD(m>!_42XKloIQH;-KTf1PBNIr&O2RE)H==HyFY(pI~;9RVo1
`(nKL=ISbjI{?MCW<9AKS57(oU{_wVPjnEpDVywF=pD$-LcIJf4IxCahV_LgBoms=Ggs>aHlL#)H<uK5
kcuLN1IO{LoZY^mb*zFWR9H;xI3(k53>Q|t7f=+WQ@-S|7|IJ1T;e-q^Ng}+!d-vdwDnf1N-Qx-u*kvc
;$c5-^L^?Kv>|HK2esK<cg0s3bbNW*3d^=;Oz>uTe>e+|*ue=}Uv*R%?(kQ~yp*9@pAu2##sm21RPoPh
8g<-%k8}GkRbXhiB7@uA9|)Gx+6ac0?vxsl1$bFBH_vu3{hb~Q#dTCGl=d#os2GBLzju#rxuk8V@3}Wv
S(Q*zcMY&X`Wm|OXth46*HPvMenv6WTHN{U7?r~pTUTXAx6DsWpXg-JC)cSR3x6Q4DRr<P7c0?8_Evgc
G|+w$O@SR3+<$>nCX+j;M)#^ASZ!-3><BdX!|Q-TNL?6CyhXi-MrxsL8&OfYp5Ik*>NKK`$+nCd5;PP#
PChjUN~N{NxPMfv*_i1!z}tl}%y$F94Q^d>&bSk(O7KZB)nacS9{qkqFY!)PfDM*1brpUmv`gers0D`1
`D_;*Cpx*<7&L06n=Ce|pTtBM#pBsa+eCpvBpcXN_4ucxL8is+pp1~6IOqQR-ok5BQNDS#WMIR&1}pyQ
JBkY8kPwg<Q>ItHg#4*Q(Cuk%v4fE9ZER=v5K%ED7o$k9@UeMPs&{fMn5LO;P93velZ@j1JNdJ!N%rfE
UIb<0;4-DE2M&k&N=BaCe-8W$FhsCQHq<0-(ps?N@gknUL^4vnT0HqTj~;%C;klZ5qpu(b43_a2-|7e2
%&Z(S9vh^(Ap!BH<Mc-FJ8asVxoloI!{0~*fFTSQM1L4T4&H!ewzo$W_Wgg%8vGT3BV;73y&hU~%Q}gs
l7~*$b{EZP!zuGDmoPE2F`^^qpaOk!ubquJ--=sHw?6h!d|+}?1psQ2xxxV+<R?rwM#fvIP0Ul+YoS^d
mV#smvj%N&DPzJ^+(;0TJAGkFtZHx2s^)J7j4%vcZqMjM6{{w(7602J4q8!zna6g=h0)Y$VnGX(#5W5h
37Z~y1{nCh97)<A)kc9MiIHH7UQPCmYD_(=LVTOzJ6<JUbR-V**VKv;b7bUjOQUe^OZm1nNts%OQuxz4
3e_0Vf75j5_dDj1Xj3I`Jbic1;QW5U?<GizT~gS9*%|yjCG|&e*2NNgklR*h4~4@@H^*>XHffNfU#(<i
#kl<bKZ3Ti1Q)l;CxZ@ymggV1Wy>D-L-P&A%6b%yCl#~#m-ygi)`kAQFv#3^6WI"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

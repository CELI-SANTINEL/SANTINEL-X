# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "scanner.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("e76b480cc649dedd779b88bade2a55205c2fdc94c6bf4dd8a0289ad10fc25235d5b39a617488e95b4fdd404fcb19ea8c65dc8b2ff855eb255172a16379e7c2a8")
_K2 = bytes.fromhex("8b26531319a06e1e33e1a8f1f554478e7607a3cce9a91d6af066b483b29a248cd76326689c5f9310f1af6a98dbec31df28c885878ef233319c416c74750402f2")
_K3 = bytes.fromhex("0be5624f9a7c6e5d555c78f7fe86739c472bf833533718f9c3f0538089e72bb80b2d84065e1d4ce5811c8823df33e626b127d78252a19166493ee53fa91e9820")
_S = """A9B<RDEY<NYq+_RLR=-d`AZJZRH)o;!WcupNp#OXZKkSfjX-o|O|+VlnId<ubZh{3Zg59Sn12_71^l|6
6&MRxB}zXY*-nWBkSQu*aT)kFkRn3c0^L{1H+JZLV+pryvAU#iu+R}dYVT$TpodGeQ<%{2{c6s&3W`5(
A+1IvYbjxY)#-?p!8`(bKR~MrS@i*Nwi;QOJ=PRnhnHzzQI2;6bjgThSLTy8{mJ*EsDVP6RAgPWr#u>0
NQ!V*RQ>Y|xh%~5l*_Ous1cgqcnHm+5DM-(;5=ys5N-aiw{9QCJ2$q#PU<sbeFxs50nJ_D&Y99<!4BCH
MZG{qBX+OQ2`LLR;rxU2mQc+MGx@5r)R_UJm`-aoj30sm2X>&2w!d5KNnXPg@F{sQJqdY0mqhGvo70O4
^*rsJb{vYL14NsyYB;EL?06nvH+>9c&RX6>1e6&=7_(}ed^mrM0CmMtTLw5?WhG$3s77Pp4}|V`oi{5B
E{wFIzG!UcAs1yY$2(1$wIG}*T_1)3GA<#ETr_Jeu;p@wdq6*U6~uhlk+nst$exV<2-p7pYB+z*w*dYh
%6>NTaQ+3ptxK$8^5t#WXOHf?@HicRmT!5KyF$Uuo@JO2$&kI^4VOhS2w8HJ+}#vI%*-HFqMLarZiQyr
@ImfFCGeR3@<u3S#bzqP3{4YqEi<sQKhhW%1aR7;fVg%C1?VAuHp)@P+#}z{F0XNU$RQCr9xfc?Bxsoa
M*Soh3D^}Y3Jc)%!^6<jTh<-Du9jYu%fbpX=<tI0;F4dxNDI2r&wWH<yt3#I)L!Kd{1|*to!^&kZGopv
CmvXTZ48`^o_$(zRZ+^Obmd-2yQL<0knx<HC~H`#f5Dy9Iimuk1u&$kXgBiRU&;F#g9lXC`Q=Pj-Q`TH
^b*DRA3Ran5^`-`q|c<$ZT{_?bOz0=?-S5$C;ZyR{|2h#iUG}L!vcZF9P#kRejL@=dE`y4xY`0C$%W<@
JI))~4Zjpu7kBO1RqCngrq`=XwTG#g@{m*`y@z=!D!HAD9tQe>jjRrAR3H$a!~%FT_5_g3^=Z89ug^|B
Cv<!hJIJ!*y4lr28gj~v-8fJl=;-~eJ%Ey|`@-Y<UMMfiI<dn1K(wC@#>EjH<9<SI7x0*!YE^ajhmk6?
H!l02ig%Ds=3KEXz(?9&TKS+?Jl@8U9)P<-#E>O6^MJ{pFK}849~2wx+^8E#po_tvBsp$5;Yg3AS2U!F
G?ElLo<;6};04S$h@Im|5jQ*;9dm!~pp^z4QZ$#1GgTbwPg|3lZjz=6JMZ9O;Z(<*G-S_?CaDi%lBDu3
HxFc0by9X*D6ow4JmV6}3zq&D7$Avv4f<|3yVO_Hn(53=p&l_e;lq~3TnZj<GZ5|LXi_E6OVQUDa>8)K
J2RbP@xkB{G%Fcj!y+veP#FMsDY_7Pq$Ip>r-~$M^2=kCB}~5*k}2aS{1=S?Vnwq!;p?!(kxt}^U_nUL
B#tf9$M3rfPN5CrgGj3@0G5b|Us@P74*j!jV`=B)CrpNeZLSKM!R<3xp|@%d2m72R-)vokP@U*)-TanU
mP-h(dQ={Lb;aF}p6tDr$!fiNMKaPTRtL0F%280WC8n8N!4bYzI%Zs{-$zd@^N2781C~f4i!=f{vY1m*
`62#Q3)z~9DQ9lF;GXfyb(GH{&Jco#AvyKF<PA(h0*LZXAN&)#aVnZ^S$^*4u<~yuqe4rBBDD-N?Kb*`
)8xEzn5P|Egu4EPJB;P6h~tAww|98To2ICrJvh0ei%ywWG?tfgb^&g~8wUF@#9W=TqN43SmnNW0tOq5K
=o0pcHxi)MD%ZVMSi`#!;=bbq7vQ3m<r&E^*p#|mLcWNq(-$kZNT~=<q%X}ciO?(iF}fR#<^Ju?Fc&Nz
h<fNH*hD-a@{f_mkIMg~!KA#1m4Cgz4U5wU;UH+=y9Dm#t%7b9*|j_YA`Zm^puwd+dh?{c(&HCHT{i)V
;tLba2fHyO0CSEYB1DFZ9r@Lowo0MRPKhrWs_Lrnr2xR)cV(Jb2+GIKBpjmzk$i3@`*1|vy)e(_8Gybx
o=>-y_F)MSyTcF)bJa58+vP72LtW{$5GW#Lm}%*P@(g3>u~g~SX-J)jE+jSz57D#7WUxO<*EW=Lo<}y?
{A0I*^7&JBRF3g6<wuRi5zq^vR-PdWB}@`-{LEc`{?NM<V|qvR<1u)sf463-!_N>@*nK$Q=+hIgZVhL2
hAYA)(k?Gw5Wp()<OoWLM@u+4|E48}h7t54;;qeA*ey5<Va$FnRMjbS;yl(f=3#fS73W{Dv-Q1h$b$E(
3{!&iE0tL`g$Nxvp&|<}XrwS3Yto9M4`sRoCrPX(v#l$MsTc7_GL;%iui1);6b)CL_`!l_`>7Bu*ztOZ
ygka8?RyWv$B!eyJnNT8N2_SI*7u6`%@e2~KnkD#RZDS_lQ)JY9h)f9<qlEncZYL%(~`W>jmpb15z8M)
!;Y~7v=QQAThzqJG9`zVQDCvW#?WLSy2Qbb=8rTv92C28@t(c(puh#owPXxtCk3#jm9}&}zQWp1`yP%1
(Ll=i^&4P$;v4IMus8qUj~FXGhE?*&)<I%n_&?ipPQV!cXZ0Rj(2kzl=Kk`i7D~q+gL0f2kC2>>c6|)j
Xy*igy{?-8Mgm~Kk_UQ1dlQCtjDW5N=UOUsx@(i_fx_8Z$VrwH-=hPVljcP55fh)TB&P&Y+SoU;Ibo<%
X)CD`0glI=X{*jLHaC7wo0=xt4XN}I=gxsjTRFI*Rk^Vx6Y_WFH*ffy=p##Iy-%!*ry7vrE$M8=O$nVM
ACW1-gSW0~;zw>)_CHg5UrwQULJ&?>-hSMwE4{>MOUfxS@;)Sgcxuzo(7YwL(*EXp7z5A{BS=ZO;fhPk
;2^{lNri6_nTJ~2SK3cDNO89E?ZIWt06H8%Q9IR8n>;Yl{NnUs^Tup<5SiUcL~znZu!-44)m@8{h1{Jb
^;Kf+%{VL%AFn5NZ0kPjM$Pioub8g65A#sn8TgaVw#tX|)NqQ|R_Yr20yzePUD5i{j%hx`_PWXz34{V<
^NRk%5hZ}!?XLPetNhYHSKe0~-=MHsfaiwR%&sfulTOi21Duqo=5qUA_@&6x=QOu-Bhb|+lleai{DK#}
xH}iP2tq15j9XXMU<A6Rkq&qK$`|CH^d<W;8)9h%RE1}=W<U2%kZJWv^yo+s$2`6eE7_rmIDXn&N*VH<
UtF=i9GhV!cI%5x^=LB101)*PvMls?Ba-0l$6>^j`!a>%@1=QY<lRUalyk}w5j5-EC#}DepM%8k?quoh
wZx61^iA{SolY@nVN5`&kZ(}Zy_QcLJ^*%4gA=1PZXNkS8wV?9-ZV@~FAnRQFy}XB-#nX~O1YKW<XXy`
@HLK{jV3t&6hw!?j&71c_rlF`C-TcVwsBJE<8*!Oj)vF?i%lsOsw!6l0OUH>0EsM`ExE*fF%|cTB>?Ic
%k9Qu!J4a0h9#ivZV3}%T;jSRHjYjC&mW9)I$76WMullAQgvh@_)=uw!UMUQICrlC9r3Hfp6db%oKmt8
Mpe_#;mR{wa+8#4``z4)dC@3-SCcYCTUBE~(?u&iUovC>CidZVxh9uu)epWpH^M=+-LlJ0eA&whOu&4H
VJ*JqcA~ZnZ{<8cA>$7hu#7<Q<T}Mia#PvK1BGqi)N2WtS8TYN$Vlgg5pvu_$3SYnz`CHeV5FlC>Xs0M
{2lZB5;1`f$}@o&9qxw$4!K_HyPE?g<*00IbGWaL!TEPM3O>;@{o#u_=BmCpjW6CCWC7`NuuUgOrTf@x
2dZsR&y=_x6n0t+*OcL4EgDB<3?YI_hQ3-7G0$Er2;+Df7SLv`&urdwl?Dqn;giSuB=$;Zh1Mx4<?i@n
x2h3U@stFgDkfvS$apVudZV1Xf5}b1l0<xIG`!tF$&>gIc9iyz|9-;DFUH+foGa-lJOfp52n;4GEB)4Z
`Kk3&+mMo;k0o5a68Q46j)ShNb>X|qEWUyF)ViHW$#%G0Hrm#UKV>@dOUEpA`>Vk1?z2LyUi>KU(Tls=
o6FA2;;$@_hDcIp1&LXvwo}bqevYK%e`c|#3vT>4)*gZ^R<5Rb$Vxv@#jFn-hW?%{!-O@-{>&efbd)!F
a8ezv|8klqN2OIUDg3~9a5`lrntn~~pRwTB8Q6nNq~5>tA}b<<OW07m(hP1B57_wUHdsA&3d)azii$A_
dpS~{2uXR<P7ek;f?yb0PA%&Q$B*c>MC!&&OqRoTgjyi#JT8g+->wFLhD;j754k!xv9FA`!8P@}8L^v#
em#slVbd^ZwuRB<OmY!9iFwBV7@}bMAX=x3jk>(TJLtB{m;a;U8EWfN>`#qdNTE8hGT~c0CO-iiLF7Y!
3N*dK9!IxsV1^R1NqcxZUy5b-p0I!)&tf!|Gpo{&F0|-QMf)H|eO!zmT!i0&<?87ngZpa<!mIJTk=nD{
_Du5(p;z}GGR*o8MBmnd9IH~J;qQ5E3MBK8ud)<?R{b@L#=#01H-ki$#x6T<bASG1?+QIi6&X$IZlNUP
=p##Gj^2;x3k*(V%+9a)DAN~nTkJVv>xQzOr;A<|Y`9t+i*o|JS`$uqH_W9+YP%K;KxKPV&b}%SZ%2^M
3#<m!*z=pvcYuLRsnST<3d66@Y_&~j(jgj~Kt9rO02qpp)u{xt8Zq@8KiW3KV$gd^xI;JW1J5A|ux=Hb
BZTkTwueTx*epuKlFHKZs34AGsm@{fq9SkiTm*g6AZ%pna&qpPhNP23t|N0U%JV61?H<bfw>-@<EOK}1
$fnC~WYLz_;U3W%?ABd<L#lJjZ7qk7%irTclofdz?lqj1JqxDqh=|AcLvRnqurVNdFh~ReHX~lLeb-WX
4*ZvZ3^4evbkbBLgxm{jBqyr>cr))R5BEva37cS>>Lm~ZiB}R!U%1xh9^>vsTL~GubX|_wh{3`BAYkDt
?BDmB;FtM3m0r+qdmW^E3|~GMduqeN>mDV_7w+EULk}_5!bY{%2Wh|IO^gHWctE)(&Qo_=ll%(gwsh5L
MBz}l_L=Lu(9&9E8T=x%I&a%=S7$L(LD{tNk?r8cgAST~ab3LZpqpqD``<S1Ael_L>kViG5<w0*L%x<%
xgNNAo1xJsI5ej}gXM!qFp4Atv3>Fd0uHfzvJpo#{Ri#82cJ821-lZTSllydsPH&V@OHK8mUBf0`YOxH
#o~1PUO^5)v!L~%zaUtW>wtW|jNw^+uSDU%nv9iGzmsT|Yi|eHvZx*b)vZ;hq`;S_QSu|+>w@myyE#Jt
5Eo@<XWknmSVNZ9SS?jrq1++biVwv;d~2obNT>F_0i^QSJ)dAt>h_IPeqbPPCyJ6uCjt31i|<cbd9h3*
Gp_R@i9&oY$4J#lIW4&iQHin@bRN^FwsxP2gB9`JqReNqaM0|ViOuboGChqmJwg}R75WwYUxoU5FlY}E
%MK?qNLa-6`1SzXYCab~4323`L3c1xioC`csNvA~zm^o=AN#J=23Vq(R%QN`mYD@>Fq7iGZQgK2Hao&W
Q?68+^vHg;R<jWuCGt}=BbL&?6fG_n9gE4jm<k$Vv<8Vuxmwp|P79jgA%rWEMrgc*9*dks@1c!z#=zTP
yp{W9f8WZttuz5pKIZfbu^B9%7VWQ`%iZP_?!;)<4&J1!^|E?Pbg0+seH@NZiK<JG@s!WrH7rF$9j*%G
N?8X6rzn2KJdXn&Yv3PLxHb8bg|3Q{K}a#X&ziS)U;^FfAwFMq$8$9Uvk#I#s>iVX>><bg?<sR07nz`-
F&^FT7Ic6>Z=L#CSZTyD8n0=Nrq;(SKFi{Z-|4MO<a*4|WTAjuOo$aZ1OZd7mfTHHvVoU9;YKq?Fw69#
drwtA9w%sIor|WvVv3F6n~VWf9$q(lPL2r)f<Q(RdrSI*85D4k)-}JsDX9Uy7|bX2N#z#i32_Iy&UcS>
vnK<f5URklvWaeL)knug;yG^sNk59PVix9Xg49a!;vhz!$vQ(U!@6U16E>UX1BBDx5B}QEY&TpvD*EUO
dQd$4DR2B&kKIz!sGJU@#+@@5H-$Xn!Bwi_a%mmM6Qzwg5l8z(n3!OKuWP8_rWo#%P^k)VeM2q9_7g1>
S$e}V8|fw|*OU3#(6=w4KPEnubfF%8_YxT#$RNgL)lqTj?}R){z|Ce!Zi~43f^ieGkwEl^UKWRqD5w(Y
Wh4W=02{x1ikbrLE1F7WkY4qyVUgOjy*JL|8mrHWOWe(@h`L3F%OogyDOhDTT`Gq<0ruU>{4YE@Ey#?O
9AdOdG>gjFP`_S&%5j+mPti?sVk_ZA=QijPjV2R-e(-Wc^=k%}t_&vogr^g4@wVG?k`iq&wQsOhFPvO3
bPRTK{4XVNzJ{w~Kj0kE+BGY5zt&L5P0P|Aosi<zSX9@wVVyO?Ah=7fA>WLv1G5;=&T~yLwVsLt#qFj;
7!f{h8=jC%^Yjqlxg(K_Kfc3HIS*?7D~u-;b!tC)jmClg;WR_aqO7_rsMd=Mb$MrQGUJAa1RNNK8*<Pt
6I6D2GvK}"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

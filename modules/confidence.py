# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "confidence.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("89ae4dca35af7ef52d26a82b92859a416bdd97a30d2943b48620949d1fc31562cb379ef2cced2e72f9e85ed8156d8d09ca378a76d26df0bd778e5bf2b8d012e0")
_K2 = bytes.fromhex("931777481cbf13489193c07761ae03e8db99cf74a8d41dd8fd48e93f883fb753e5b8c178be44e843bb1a073506dfcd9658281b850332b6e796a9896a16f32076")
_K3 = bytes.fromhex("58d99501a7539ee440a3ee86f4b35c663d31a2773385e486343573682d3e9852c129c5fc5330f0c1e39eccd249efc85b1181343696a3d13e712b86a8aaaa6542")
_S = """I=XV&(+{YCiYP(ku@^d`fx`olim;{RFx<{sDn>L?$sSwqJrP%Sg}6;PDnI0-Sb!(+bPhi=Dn+w;CEN0K
KiD`}8F8Eu5f#(%GR@jmv#9BLTFo?s+6iNyci9Q>Mb&AdlrBqrk`J@4pba66uW=YN9hW$nXQAoF4cY>$
$dW+xslpfW#{$VAuhIX4IwVG7*WIsHUG<!;I`D>x>qE>5tbFT41tvFFW<V})FZV^74y{`g)g;j@JtM%L
kRin-)a4JJFRJ8f+vAtM0eKGl2PwS&D3|hrv4@W{uA?>1k(h(_^Uw0DW$U=R0m(R$NoxAj!E!%cJvXSF
q<HXGGUX9ckD7`RY_s=e?h%gHKJqruhpiO&yd`z-F1^le3C9Ug*~<ho<|wQ}sgaR{is5~x4~|p4!}6EU
J2U@)u-hz%d*$gb#>ybfmJuakkyGXUE1U@tfjA1Axw&wUrxQ6U!U%b4Xy@yopX1`DmJeCPZZ5zc)q6RK
Cy@t3h5kQaw=;{IYW?!~9wZTp<D>N^jSbrZ2bT;Tr9mfLyf>B+JQx$;JKLvt_81PMVI2<<#CCE6#<DQU
I>wFN(&(9Fef=?xwGEtzz^=3&$Ih1#j%s`Tr;EZ0QJ3>d=Wb9=BpZ;jT(^&ZYJom%e8@<S!$M|x*DZa$
EW^PX>+Vy!z}qq7uYlhB)ZM#ETc#;|6pMsz^CUb@G8{PwvQH_fLgb)KS2q2TRZ_67GLz5Ol_4Xj4}xd2
PWgUy>i%q6Vx$ZW2BiK!nIJ~9R!h2N;lGp4BtQlBLqXMX4C(kjtwaVg8#ZyE8CLtOr^ghs!dK&g&IZwR
uV>wDE>0Jh0$ylB(vTC#mftNw4ux(%G%4IB`?+7F(}JOpNhjJug!CLPBN~+#^r?E54DTz8?SDHo?V92*
lHKf_^Q<kNO&~~ToE0NbKL-<SC_qqr4l`YutD!T>m5*eU6$An?PGo7N2gx5=dB-t-<A}yJN^xzArZP=l
?FLQXwo<Inx|05a=T3&EnFu=N)KG9o$`9YtEy%rrQk;ibg{mITW2rZmZpzRlxm_$UBi^~7L(u`s*%haS
>(o0*BJ6aDT1}zDG1~5g#Nj%P-l}G1kk%>uSWq<3yidwZvg2F(?W5%3nyE#v5CW1dTnmv{PGHYhrVd!S
Fg<fG4t?QC=qe{Fomgnbti^6JBAHJ<9dWwmesH`a&1)BZNVuxzgZ`WdMkKBE0(T{nb(}ef&zjMJrt*(i
Vc`uZU%TN|$OH>s)tVCmNv2h8Mcg|XaTO?-qvmptBT{zS&U2#23X2<?o6^8|C%laKr2QUwXTmKFcUPu(
)N_p}jHGB--Hu3qvh4p>7v&aM;c>HjXJ3h3+OF&N$6oh8D0n)02U`N$d-pWVrq1)$4?GRP(=XMZD@t|K
@b-2ws&uN)D9Vb42-FIU9#ZZvRTMtBW_+6{!1|3LUEboUy;cRr6j*#BL8^Lp(L;Sbe@roF*RW$Ag^}+Y
p-V~x&TSw>Ot<t78?6KmEYO{`BX-Pssdfob9WuWQx-Tu1R3Y9i0CU9#4@UiY06Y<qY@mxPz)zkS`79L%
y2A$7y8Y>)Zh#VTMPiO>DV@iMM-wPab5<v|yo^a&Cf1|JoeQ_^sOPB_Gjb=+@_*#l%C_+HqumUYZa~1E
S=m_eqEh{wuC+VQ-k2SQ_;&+d{a`CHWnnS#2(eil8cB7F>?BbgZc<&al-2`PWIZ&Rnge8?X}@=m`-ip2
x2GcBdhCV-2<bz{CLo`mMewt`;KqjWr&;JKq5S}6i=eH~3VPI1Zr9RCv|_b4%)?q0ve2`-Xgn)LRn-lz
JQYH$BRrCni<x-Dnx3pi6oIEZ0<6RZ_p+#!=!|!)q-rJs%_H(U+Dbm68y|v-d6qH|u<_*uNP7jS(IwU|
+Dm|)x_VP@>Yv7eC5BI$xLp8l-NOF3$8sy#l3zg1bReifqEdzkAM9E%C&jQ9OP5_~hOPIRL%ehM;x)w*
`Cw>GwXLNSHt#pngG*K;<W1`EcPeW?cYOxf0@nf@{s=wss$W;@B@Ya1u6~Ix`(hU0TJqz>!l|bdZ4I=@
fT5PyiIHY%qNIp75k!k)I24gX7jjxZrw2Rpjr9pgUU*uv6?Qks(F~Iq#ipE7&F<mBOCJp9G!b9E{V$Q^
g0w99*VABFzJRqN1qLin>Yp48xsZ2sV;&A&GvPa9-4cdX{~dkE;rOET@bZP+>Je2;e`p`0rqLLNb)VUo
dcB+k%(CYPaR{HjwU&zQ6Z7ZrcZ_z<EsXxGY<}ucZsc(^?(HOB+D86hvdrxxwGFU)9A%=HQijx^gzbuM
TVVoV(?K3<Q{M&1uFQ(Y^$rT=Kd^b?HLT*5dT~|a29Nh{JqFaklr}-N{Tr2z0nFi-;Vz%#i9qvn_5EG#
^9qa=UbrRb+85Bu%ruS#6=jW^vsH{=%RE?^Eh0Hmx9t~yCz!uwLgv9}M;1aH><&iF>D}um)OiqlTF#z~
MAV84?4pPZ;U9sK(j$YNPhqc_{pq#wOAUO?5&F@_{D4pM3qF|A^q~gYLcg)^_>&C!*}OyL5zid}p>K#U
MhJ^Uzf*YsH(7vlc%P*;vohzpzU!aeKJ};|=bdI6ox?o?j;L8nHTS<|!Q=S(^7Gp1v7lN%t+i`Rr8qjz
G}Wr)@zTa*$|$t7dbBe<F9-}E3j^Z_$E!8Z%*$5dL01z8+DF)!e_jX7Pmo3f9HL)=GYNYd1Uu`epQT}<
zN%W}Al|&L67ik&jTCriJQ@G040dB4>4iD$Oq@r##?ZxK%*rub9==e0+n^{WEk>JncxoW&60=V0QX%)H
)=ei3K%PLN(d{68@LV#nWspyztsz&BFoWF5<Ulo^&|TgD04hs|R_{pEA;xMQvQOJE#|gubcL%s~v3Caw
kUyG9FaE!WfD^#eIbvEjNc%e-a|A~()8f_wS30Fs8Cfg`WA&;i)_D^dI<a?cGU62F{E-M;@T2MA(%ii_
Ma)<RIQpT+!*-GIiNx!F+O_LQ?uBbmmyfk=a#{3*L0c{C6G4Ec)^LzSz1G8%{EvJ8w7Ed{KH-6_$@L1W
oKzq5aA+W@&-=x{VlEkUny~RRSrm1?ttJl}gunW&^9)a{)^H(q%EQ@f5e5kWUE&T^DC*O)X}7XwwIp~8
J}#4Nw<`rXa-FS8KMo>o^dhdr4fvT{(2}*xf1~B%B%y|e^htz`9?WvJ?3>Rg#y!pg9n9fy{lS4HWBgJO
9J=$2NgTzw^3zbMeBu<jbX1{qp%*>iwd<^F#Cc&~+=>Lqkv1W1LTeMw-OkN<=oyPGoL$BUdK**r!S}d_
92DW5mSyZ0LMogt=LVL00%0QScHwIjm!igXXMd5a^c?7@HiPvaRmu{kl^Q;2JZ2_m=5ixCPGP9q(07N6
Czs94^@cJ+o(0+J%Z8ul&L}irTr?v_6i|`10{?1LRVdEv-`9^HTsKJJof6LhqQJ>tYUFW*aBabJDeU9P
C7G|UJ!Zm8StAh)dnyGr)1OzFX^#~QCYRhcFrZrcQS(abzK=WIeqQ1Dp($1r`8H%ZkkuOwZ_t*0)7a>J
@hub<F{)SCLT9t+&i75Q&z9|JsEX)P1Fl4fqkwPcMc<bux5*n(n=W9xKqae`kny9hW|_Rj<%o{BNVGn=
VtkY=Z(ako7$f_T2nAuZe9oS2Jz!<B+8Enhf;(*L2~75(W7KL=31N*0KoKIYWboueaH=YJM!Jq7P<wgz
hu1x{O?4x<T)@b%8rjevD|83(S+5m-V9_b8?)N}9Cp5iY)-c*tC}@}4%x*P*BGxfRAN7{zlT-^m!LVu0
97AT(sEURg)ZJP+VcN9rYnyKr=9MBEzAaZ??rCy!4X(Y#Ns%Rt1}gh4*=h}(uP-DuVZ3;CUYNUzb7NGX
R1+1m$y$2%UwG75_t0yTsmEEK+P2#`zy^E$xq}sqbXMcB@Tt(sMR!fq+n8;DuUsJV1Px5VivjQh7<k9<
()`fx0JPq93JVXv(i6BJd>C^gYWLyJa}+<ilxb&=%(L_-gBaz{RW>B&&4|cZ3r!y>a;|-y&+x&Dg5q1M
ZA)_17WjHGAiKvkltY^LoIcv9Ju&nD#G6N`ljY;_0gh@^9uHvQNceLXD#~hb@EZxL%DlQHV@qsc+paJs
(y{ec%auiJgT6w4(N-AzD5nF9ZDStp|Ld#s?jvXb6lfnLi2hD5=q8m<fTtxvz|#x~G7_zUV(gL4%G=J-
*17$j<Or5NJJ{B9tFtsZD8~s@*gljU5`|&nFVC*ES(D=)4Gitd)^~ADrO5SV*QoTLfXXa~PKhkn-uI_j
SNN7(FW$k!kI1BX`e6~M-q$bt_Fj;Gkzd`N6t3@fcU<M2%jWoQ*u+Rd3hBI7d*#wH6C&k`F{Yd<8<I)Q
^nOF@`FKTUA?xP#v@d_K?n(g+^+!u)SUO<zVbZzODxI;E%*;oH`~V$5pL;fy(nF@*BGDL2uD0w&Hzqj3
+lD}Mhd=Oo2_(Q!b8V7Tsi=HwoaflM)(P(2BsB2Yjr2n?pFSo8#bobY@O&I0Hkz1lL%||otvz8PF6#e5
;>R{4Df;<jNfNuOtQ)mc4YPMpNxaeH-EU8i!8`x<fI~qJPr+je=gtrAj2$_$6ZIUHh>M$7g@E`SeT%ag
zNyY;)u+9vn&@(B<&^=_r&bio1a*knwMX`CTMutM=klqrJF8p{?L3}`fD|@VJJmqM3T%qVXm}}zfIAj3
&e<u3+ZNZEqs~aYC~8$lg+07_@{lCDjf*$)`H8(XRx679rXf>oNo-@`SD4B*-KmJIXLsE}@(!wWLv4oH
&U%xjyL04}o<xU+Garn~;H0<grlJ^1)4kY;;r6wvbe0idp;c2|r6>X(nFPb@u36_*`OJ@1wJLI)pj3UG
*X{}64ClP`*&s|6Pzq!_HsP?()a%>R&eLR!n0-!EeC*i_D+qIToA9lu9%*?1QJ817|Lq#UM<~gchTu8T
2mwe@s)7N}uMDwQ7ycDQ<z!8MP^W^khFxbT;H`pJPR<wdG+TUQDB*`Weh~;=GE(1pLoto0&>WG#()hgG
26J)|G6lu1yAleKkq)%Hm1g#FzWRH-xEpAne5!sGsjC)<H3KP=6f=i&qEc=kJg#|q-R7z5cA}|I0%bVV
@{1)UC5DMUO}8}y*TivnF{e>2eB`a(8|TsZPYt7)LSx5+A8Nu{X}E%?G2LmQb+a9?WIl^s@^b8>B_+vA
gcma#%QOitlK9#I>PI-g`X8kcsm#R;<_KavhM&Ue;%@5L6J_cTI1_$r+bo_j6+*F}hSMh0V-@J9%)fSR
a_JoBul!fhuzyPf%yUeKt5bFYS=caJZP?L2v{w!;5V6sxulD1?JHl?s)Q`q<KZH$X>bPzjkjl1DD*"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

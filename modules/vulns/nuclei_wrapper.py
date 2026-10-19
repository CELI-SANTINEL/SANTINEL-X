# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "nuclei_wrapper.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("0ce8c064216c4a0b2136a6f26194a6d7d92427966ec5862bac2411c50d21db3112810e2e829a6499f42663e30b6b260a4b6020701e578bed7f46266defc5bde9")
_K2 = bytes.fromhex("4930d9a2816e1832f428fe8a7377286576add71c89545e5c5d8c5a274f87c704e5c598f1e630b3e833544fa3c0999bda124d58f23ac9c6fa19c7695f2c06bd9f")
_K3 = bytes.fromhex("5f23885d582a63c99012e7f0a46bfa5e53a44a1fd59bc49434ac2bac0505b8e41bf4c6e800c00dabf45e32a59888b486c9e208341927dba81d638d2213601d75")
_S = """Vj%>~qj)MOTr$L4ONu-M{tI$b>LMw#9%Oh)7?Z4Z^qVAl08vu1_eP&kL^IF}kr|{o8YKT({4}&8gP4HL
9<+|vX3GDB<8l-m&QeIi?SL+Z=>D+)@)ieZ-W99tt72LX>|75TiqYX5Je`%PYgluG0?ISMjnx*+&<q}x
68bbp>mpzp42k=-uPXLfzM45gdz=>1gqgxct+v_fj9E#_0BHg%P_@0m_&L4ss{2h8B&l2G{Dg)i!vUn}
$~PJPxg37&-}#qOeW0R>Ogajq1#0o0p`F5(9|5N+_b#%2yd|3a9wk>G95`Zfv*`(+1Cky+3HR9EBj}-5
0E#(?K#&QqQ{B#zWP`R4zDQ86KYy2>hs;bEQU3$*$ri>OS8%J*`jyJsnW?tPa;1Hfh#`smHvWfg){7Yk
N^c5}GA(1+qhcRengK3qDVz?Dx{khp+(Ca&%_0Fo!^${115!)P9c1s3$?Y-p*3KnJ3WW`lW{7rLNQY{L
7yg=WtzLGp_r|V?CH(2k?*geExzK{ZrcB5M(J!qkg&4yiR^a-WRaIXFMcS|$8ETV!KaEf*nPA$F#oB2L
t~VO!%KlC8AByce#gXl2*HKup2F`w=msA3Oui0uC^4*QLQlm%z)EY$+?M?mtG5RwI$jKOCOPWZ|W+BSF
^bW4?Qufd6xCdmr+Mpu`MsBgisK_pvg`VtQ)Mx6Z7X*-I5h#n-XfGD^FhvY@-HO;r8(j7p<fRbiP!MJV
a{fT^Xb(gMODp~1>{@{M!9*6~7PnkjEOCiy4EIepF&!HOH6ag730}B;``1JHXA#*InIG|{jxav&W|VN7
INXe&fr|X4tI-3_nak&n{c3W^ivFih-dw}@97u~Cqp7;Z{xWGCfG3%N2w-B1U6Gxtj0`%`Oqr>vrgD2^
0nhx(kKIKYwmQ{%6kYg55%|>hkPpKp81k1IzIp<Z!E3}sAZ5D8pI^S0@J=+lc;f5}G&zR@d%&g_AOeUr
rVXE)*Lhs9W$<zshQTcL$mK8T8I#P{t}NfUq#X!|4X1+@u51UGF~%({c(dIkqNFN17G;zmlWgfY%LI7_
7_+u`b5!T1o8=^%B!N}c^Wd|~bQ2&>%`Ma;?SZJ++9iXg%TYO5Ri)Y7ZzO9x^fpQ8&yc?$-T2rwY-c(;
<b!Fldx;Vpa!*{EGz9FP$>90F5rYnG%rFrJ^}jc0cytqSb$&}t>1PlZ7&r?Z5ZMls5Fe5n->)!*=Jxo=
N<6%1$qCR$2TJJ}S0F#nw69L^3!j*8U5-a84{lf6@}Hw6(Dv1yF+g??0hZOKG)v>YnfiAQEJDn;8pmIu
P|=mbu;P2{9!xX}8gTjkf<x*8_#*Z1SAyN&c8)FS{=s!Qk%Ef2`y^IGQr@^RH5}r{PFWTZhjH>^lc?9|
h&NU%Z3<lp3%U_0SMy${_~Q&vw5$NIv9i3=|BzLmR8YKa6C8KrIO2dgJFDpE>odMbhWh!i1~ekc@`|=}
$tLTp171gkI?}>;fHl$Yl#|Nx)6~vMQFGlEH&zI0mS*C(>W_!LIfDLQc;bHR4Aiee(U$H7t>2$}K70`U
<Ujt@#KvKN$?1Y?fy>SPP)JH!(zmTP_I;-h<92qbhf=ol%dt?Q#e-1T>jL()N-fj<#CPY)1hTIg#Xf_$
+rUuZDV>l1L(`!2j((h=0xBJ6{MlIyTc*qFD=yxl%wI|yikoN6PaCG+po&E(Uys29PK;;Ynj8SiWnY{S
a2(i9gM#TE8rML{VRI?td*77{WcS~R9-WF{^30fS%Lr)$k}@L+`KvV#w+?q|Dn5$ZTrq9S^H~+=4nwAZ
v7C;r9dpX=_jA^j;tgM^i^gqO)Evju1!&bVp07TtTfWh;g7!ZFo+8{2uExlv-`3A&0s&CPvfVU-vtCh~
d6CbfhENVM74)g{P;;b@L98q4RV>8i>K`sy7RiI%T9a_v%+JcpF^jK=sZ=~ul91-qR3$_lfrvj*yI5xr
bKTR;D}5R!T5adG?Y|MJR@cB?aoq71@rR(86Q-1!u>du12WM5c6k|gLV2AcC>V|4Mp37j3@ifR`Q#pN4
I#wEU5~+~(mD5_MH)MWhm0l;k+AYCYj;{7vfjM_$s11ecq6fmbo@=&$Ku&*Ftyjo4!#?YuA?L<THUH10
0CFd?E8EsDMn2n<M5-Cqna2`gFe^x7WSb(cCv2j3i{mo&Q$ZYK7$40x`}SR~3D_H<S|2%0S*SrHMGt~c
Ges!R-m$@jzUY+7j0IH8C(?&eLS6r=hzv?_)T@LU0{q6_qEqp4+`1cd98gdV=l!KS1EEGZc|{5viO{Nt
yRwCi{S8_ilT5RkG1!4e*nQBr$F?|Tc7xx^UQo6khsJOu=x|mO?B^G391=Hn9p;%1^40}UOm#+)i^<t~
fH`OfMzkYh6%!~Ykg-+ip|O6p1!!)C^C`t%PimE~X;<)GA8QCnlI0%JAk)l~+?}vfgv~U&Wb0g8^|K$L
;=A(ueam{Ft~=;h^8r8PSLb5=<_bxrO@npVrKOF(-LW~FEN~pGt?kq0jXL@B1iElZS9lP4Jmy)B*Seu~
0(jc6LQQ_b`P8C67+216N0Zb1W|1<EomxwD-OvS`Z{<BdSoEQ$Vws!LU)3q#5^@b|;|F}>Cb*eywD(%g
u~c96+|K0nY?CkDEgIKS%oZ?%$>*;~O9TG3*%k^dG86igi=|9t@8k%KW57S_E=>nkZdO*D{0M*MG~qmR
d&Ut#5K<9(Q#!{vcBk7PHz-6>+2YffXyn+)w*^PBO;fl{qr0Y^OpUV|H9|hnplOg=Vb0(YwcnboZ(D{}
#DcwyI5r9M3bgRDi8hGTR?||Thht_S*C|?Z{wj-HEXmE!$j2oCoFTp>s81=!saH=z^k><l5ixrmo4X|a
=_@WR;B3oBd4WBAVEBUs)z5i~Jds;IC8zhs7Nl7Ke5>6E5_)+T$Lr8`JBF>_(1Sl_H>05_AyvC%SlO@4
B*D?9!DP_^R0>RlhVV$JU7RJk?K5CLIZ#-#vozeXC~qQ<CMgA|m2`5{#<GDf{6@8C^?g&dzWhnu*)g%>
INt~nJq)cN4;%8bIfu&CddI853VW?vM~=gnOBwIEx6^#_?HhxXJFwhD*J^_IKZP56A7c>gv<ndBL61j(
_ix}e1Kw5``*8XidO6$R;)_ELj11Zq&_wO3k=t3P#W0uZ+}lmGlBgh#7&QV+_xyu?80P}?uC#j^<1f9b
HqWD{`N2_`c?8ODv@6xSGi=azrvc9L3351Hxt)yq#%(_IG*jUHmMDaW=$}3YBZ^_N%=MACfCU2V=@a7?
qD7G=P$p9x@-aG2%VYT$s%mZ%oG5WAn7CCvG(~z@hCxMMF9bgfs2jn#_Ab(>vZB1ROfcmTIM;pP>_m%N
&AU%4g!|>Y{gS?1BE*j4N=m%o"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

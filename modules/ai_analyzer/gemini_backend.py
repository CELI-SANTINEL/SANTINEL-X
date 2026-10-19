# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "gemini_backend.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("a047aebd374143d7e2ce7595a7f4fb13bf74d6f125858c87b348bd7e83a26b0d7726893fd0a27a6133efd6af79333dd99f3d1f960872cf849791beaff96c1342")
_K2 = bytes.fromhex("ce830bd65e74a4d54bbe9556512f546c105e435e9a2fa0be353453d787fca59254e2365c4ade536db0357da925522f408a07e506f01c90c8f3f367b0732bba9b")
_K3 = bytes.fromhex("5862ff3faa3a46bac35b4394846a416e463b54ab1a1020e8e8459ea4c2cf80cb48591948a13e206b05d33ff45a9c9e7015506fe1b2714a9136331f325166fd2c")
_S = """PJHhTm}9!{5EWp|x?nrtY^S9|;?AI1Tzo5=+Em23rqu)oVQ@fe?=X5OJ>wqAYNm93Ju#bjr#BT)QhRtK
Z?dv3cm#z*-X(K2p(dCH!9nHe)|*KSB%lR{#(WJ!gC5K<<6`o)d6jiyl2ItP6n`0zhJ)%st*1NkBJS*U
tXL-D94KCTO5c^OWK(xF+l-#V!BV3Zn&~g1FD$2>Z%ma`M#}!{w8!b)yc9uMd!X$s(^Kwlv0-h_0+yRZ
oJplImhfKPKO8A5l9wc9)H(>WQ7LC3MSn9={af4xyG=YN_VO>h4F`sa-9H3|AD^v5EHv7|6@W<cN~XZ*
rtR?Zh{VjDCjg2C&Xq^ARjq#Yfm5#dv8XiEFc>!%+F-A>bg_S+qc^A9%Gz{bbX*L|BrG<oh4g>f{(yE~
JU<~5k>jEP14@y^V;{;w>j+v;X`SkG;?%o^AoK5y84|6YQu={sFp^xBe)(+EY!I4IN7~dhW->fg{jC_v
*(Wj7G|dz}o$8jKiBR<O>NomJ`PL1_El-Om&t2bhuiyW9ut#t3#3t4=A(E|YZFE>t{|-_w2F4&Xqtm$U
#T*r<>l}NVvEy!G{sxfD(VhWR>d-dJ-eR<;>ILg@P|fyFa(CqS{!RerH&Vo(d#gtTGB`nLaFug#ixuVF
j<tYLv)#2M0}mh3)}8j%7jJs$87xy_;=33}0~$C48`-1K>&)4sTmI?7&*d-3*<fPbvSGz*C;8n|ftK1y
KAA@k1oijCaq3O_5^9K{k~|r?w1!4L;gxlQI{N;zV(iUqn?GmA;UOIc()a9dsaPnP%)kI<Ly4OQps<|=
h(%}RWxw`?nY9cYv3gt1%e6BsKi&2L5-JtYt~w>Yljlq+Tb5*o`_6^5F{Au;1Hv7+pkUdj>-RIG3N$eR
tWiS7TBrV>Si498_%%#-qx)Q8`lh0R^e|YpVo@u`sqsWn5s1@f!AYy|m5GkAg6@zg+aDZU_!(wM+=cH)
SG?>K@Z;g}$k``|o@a`*L-?mga*r`PyUyb{NI`oPFE!)>Am$gHx8Iv$w}9wHXMHQ{O9U|e`2$u!pnDdU
sS{Uf$@pE=j0Am+es(z1Slltp|H5eEQio;}IYhEMsSb@8VBhGRS@I_xYm08CI-4>qcMx;y=pXvW;@65y
iJa{&A>-S3K>+Y*?n(?mj^>iUA$)pVvZky11WI99`4dT47@iTG?xpKc$p*cT;LxHkwUiIlSFNhQF{yow
f9MlM6n|`V5+e<;>-{C7TIZjSQZ_jujgrs!1Oo9DQHkqDb}BO|vR<i9DJrO*qq!)$GocrlVz%8gX}>4Z
1*;bE!$98xYj3*Eh;5oB4RPV*$+Gs?lnFVMfVRGY;@h3SgBh94Af-J-(arhNAR<^9>#Pm5bsdfaH_r*h
UxesIL7mFBe_l=K4PFqed}>~@7z*Lo>cdWEz4+ztoFIN=Sxv+^Sn_l%g(dbL`Tsm_h7D^+s4&c}tJ!@A
vRv%ihVRr;JKPdbkp2}A;G(`dUOi#%;zb#Wr+o3)7@Sgio7WPS_`SP6!$6ZP{Tj-FemXrlaI@p$#G+hf
#Yo##1;VNbc;Q>g=UJ@6zHt@b=IjLRNj{#;sA3Sx8VvK^_PPHJ&=aVo^P;yz)?2Qgm9(gBZtNy{)12I!
Di3*Q8*gi(Ah4R4(3#`S(Mbkj1r)thncXTsCqAgL7`ZqMQhv0kr*Is&`~&+SVqpZ;{}1h(GN%!R0zNA{
?Vy(pZHmq@9~?#C(}GZ!PXC?5!d<d>{CmWoS}c@PmJY(ugfC#hJ{88t71HE?S~g=0`S3G?q}?Ul56)aw
WNlfnj#&%fNR9C3Q09sP<{Th~Gp)Vz_+8wGY`6)J_BYKu$<(ED1EV^pti5c$(m5Q+W-?v|4GGe$7a~!p
6kLH=>mUG{bFKTu1|zk~j$5`#*gBZA`u8BY@wAhoJm|lXvtpz>y$uO*Ea}O*gcnyJiB0y|2mOwlR7vG_
jKU6K7N1os9wiPc)6;q#>%_mT-AGG%aD!}Ek_XsvkbP+3l>fIc4EL)ULjqb9w>(RWK49%GFIMr|#(s~2
%3Hp!efR6wQLEW4t%?_-dOB9Km{;MJQ8tJ1KB{r9rTgAX7Jj*YxV(bQ^BiG3@WWt1y|H?B^(J)+ZTClx
4jF`JIbqRLu7WQ4y60BrF3vpF(uL)#hlZ<MiEbU(DS!<&lq?OX`_nBAjarL1feG3m0p!G*6)G7@r5mZ6
-c_d)-BaH8lA;qSUJqX`7w`(ZA4G!_!MueAZybI7K4U<ELpfT@D1bqSS0Zd2&t!>=#j%#sE?zjv8vPeK
_0>f(Jn2JHiqlE<rH54C7D{>Js$r2~l&&@+{%Sc08$WH>N)_TWA@+Cdh+ys%{~l*S7T}C1k^0*~55wl<
Y0U;Z_g7&HJrt6d4tkxkSibRRd%%NbZRX7SN`}-0^aY?9qE{kukb*YQD4(L>sP2;`e268QfHhuKl64;q
#B-4YIu~z9gTm)w>;Io(*iF?@nJ>WiT}ruGTJ${wMC^ZBtqz)MU&)ZWo}GpcB{#b&Y=TA0Untk2IUN+K
VqpU!`+=svd0gUrOUe$tytqmJcUmmZRtiK9B*9nqa-Lsq>QZ<$t7ATv&Yu|6LrinUU;)&`4~GUz3gL$b
Yn1PNYAW%*R5Afg7xrd3#tNj!yu28fYtL*ikS8uJc$1qTYBZg#&TN_Vjh(0`Rx4Wb7CD!{(>=b4<gPU~
q6`_WW-e2s4|0tl=T^MrsqsK>d0*(&QeF^g;D}RmbyL=Y&|V+9R_!@JFUAerCAS6p_y^KT>xJWW(=CH&
H^yCIjnh3S;7PiR^RjHUWulQ}Cc>6VqezoORvPSjc!L)|9GnX56j1;M9@{as3?*AuYDS;WCpX}Ji0BR5
t-75=l2%}|*dd=5+pz%Q=?TVfc{`9$ogHAmoCV}Wf7A<x`vdc)Tji|&pP43&64R$}7;^7l3TFeiBTaVl
QQ>rxrnYqeiC*e^kqzSL#oNq5f%m!b`Ya)%CfN@MeEAy*F0&LY*DCZvyx9)-Xb8}2&At<XPtJD)n2lU%
t4AYTY=f-Tt5>iw<JtMJG(18!pN7#Pb9$~IGbbBzjUFz6`kP-twW+DZD}MuXaqP+15ETSwlpI;NM{8kW
*cR%dd9IRn^oEQza}i%aKjo52v-0jSZYQ_C#>*7jdqI>N7Ix!x+G^~4%~^G@qBR$jTY5=Ynoyi!v5pFG
Mu?n^l<k=fZp14t7vV+r2oOu8Bee^nx|jN?PW04xBlB;O7E!(GLt;;0*r|nLq6CZyXx?&iA#G9ajzdW;
a5|W&&6Pq_!CriQ;JS<()JbHn<UViJI{jn44m+DvVkye+;xTyprw4?AG!)Rwl_7`w(^Im0!L3v2k1aIL
t3dT6`bD3~O;%R6C~b!@-7pqeIIzR%ZjiW(hv6{w%9>4UHgh!=6HVjQ;2&TaX`-C;sRYb1d%2M&KKkTj
r-MfEx<W9nV|sRlbb1Pdk+JJ4G&vmA9C+aewzWAv`-deAh}$nDq--Cw4X2Dy1RT;W5k2u~R6xhz%8@WF
bKzHblTE83eUdq~R9E~de%BI>d0s%(@f)9Om3Sq65d!SY3)RFyX4b%V5c5b%md1!wrd>Xt!q|ywMP}gq
%95D6XVY|nC_1toBSgHhjRtBtvi~%LY(CiSK`jLhO<Vz!A}&)WAAIkaXUhy)0sDf%si%dOS%tS-!}%ts
9Hspoi5`9$(+8>%Gh)loaAgW{dNb&JGZL)Ng@&aeMR>>fxk8>I`qN$MsD{bpD!E`#GY^`9AlqH&h&_bM
rrB_9#B|6t;wI1jqAITv><Wo6w`FAz3d1_<tiOK|K6(fLQObL>l{5qh7s`3ke9+Lb`6TRSpc>0t*jYXe
!btvt1*ALKFv~J?B++$4@~E~M(@t)C86}@zOqL{F9?!p~i-F1T-@75`pz#HMEBKSI7Ta=?&GAmEhMgFt
60}_Z0uGbB;)Q0gYXf76OHWf+d=N>y0UzhaqO$c3{C6aa4w}E=q)r+hj0FJ`_93I)LUyP$DeFg<Z^#T6
aE2L@oHBg;g2h*W!dl@Z;hs;5WvpAndv#|md&KLN+0Ee@>))+O#{h9tJ+C0+L}X1X7OU~)mS2t$X`;K=
CY9i?_#5^U6}*M_&7+$!y0P%R3A^vn0~SiVi2$sRy7hA3F7CTBgH;ZspQXxMMqHc|-hKSb9!}Us1+6}y
+5&4^t0A@xUH<!eO69pVUTWF?wxbNv;)Mk4Q*c%(IjLp&o=I-0)HfK(Hnt|4Z7CJ!hO>+a?o{jLtbmd6
h-v>bGYgix*DoDe%QUk%eDMa|ghs*Dq2{!lt;3MSCX|u0=!Z;nVNV>6eCtSZiSqd>-k0#_LBc;HRiHW*
NP2gtCvzkBB>0_OF40M`QqUMpP1V$SsW;$*kEEl*$ti|$v3r;G+2*k|IC$w!HFs|)Mt;ACbl|;Dj6z>p
82#<_*8;3axtAuyV;~r$V}(W{-}8u!rZ{xO$ej^Ignt+KoP%l~3Um1_Yrfxvf4e^=M`h<$D9vdZIK{XS
mw{}v$ig@URL_=3OK#30uX^70Yo%;Yuw39OHs86U(8@F<|NYn4M+K>7cs>9}qS;Q_uL^Uf+sLAqr}{i+
KVL2;iGW*8D~Sn;k0lCiy)(wp@ou}V-hJf)OI3kdM%{Up14g9YGIcBjybR`{fjK)6WN5(p?z>6@H2!_Q
^8`1rI4GETV5x3haNKR#l#1bazF_kUCLW1PY>Mc1zz+-}xePZhZw^VFnhA%0{t&1mO&YI2npB4wmV8oI
psE5fTraiw-Fi1%6!5$SsG0M0(bce32i>#JE#ICGwpPbE=UP?S{tk8t-Wp@!yjN(+Y5yuG>Uu6Rpj~tk
+1)0*bMRqTEsVQpb|kWRx%f3~KJ<b|6uS<jL)RHmQ-;tW5ArPEH8O&h1D)9R2x}O>i-)lW6H=(;q`|z)
Ov258_`R<n0}6aCXNaM$$wK5Ch5aq;v_8K!w=L$!#Oq=X*j?$>Yix`ZPwl-0Z##a@>Cwu6Txob7dTc-o
G9yJ$^k06i0P^RoOz;)YWWHj$=#I2kXeR#fG*d}KT}>a++o%FaDXJB}GC>M&KNf7B&EaFUQS2DC0iN1>
S_G0#Nwc0#;UJvQ+j5~%=BgCmS`6#Vn0Bey5D$AGA2vx2%(Kyb{CIyhh6YsbQ&raXH2{q-V(;OlhlnEz
H6i_P>;"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

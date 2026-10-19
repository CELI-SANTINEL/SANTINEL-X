# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "redirect.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("2693c754499295dd7fb4c6df9720ed46b22c5ee7abcbb91f04528b89a0d1faf350de489e239afa6e30b1bf1438616a0dacda73c2c3312515ce3303c125e94ab7")
_K2 = bytes.fromhex("2e1264ed12545c33b99facaa1512c51c9c6646bdee5943435f595ca1547a0c9125dc4c77e7af41ba8a8ed4fb7f7bc573a761983ff4d84e1f3498af5f2a0ff449")
_K3 = bytes.fromhex("d87474cd62e482ce72edc583965b0673832afe535854108653f688f4582ed90ea01480c93b76e403a3c2bab172c46722ce2de867978f028259aca242ffe51d65")
_S = """s4rS9Qf?RLp;%NdGh*d4drW6+GNvjq$kRU?R0O6S*%#*!LDMSD`XP<5Yd#Lk7-QeV%rL-gi8w?fNofW{
y3sJx6n9~<p2HfX_f12yGAl=HXjLGH_qg@;lcx#=F16#%!5cxnVn|KL46QD}TzQ|PljZ9|ow;7(ZvfGN
ZG4jwEi)047Ye7n%y^(#j$8*$aRU5!bd!tXPNgBlW;DCX<1$VFk!EQf9bAl?;1E~ZN#eU}<jO{9B_eX=
TsX{CtN@s*c4z>fcT3{3V^lC&FYvwzVd#y~Z}Bc8m_ALImHGZnSEcMf^J;DEQ?_DE4C>5%Cynccz0_+d
IcbICZ7zO=$fx6nbxy9~9n_71E#$~Hlc3w@Bp08&?^67+`YBBAxr;zq-_E6&+||dwdI!UXa4e*){ivw|
f)Ud!Z2EZv00@o}Xcz8lLMoH1$>T_j{B6dhWF0zZQL><AC>Jy#rCd8Ljns@#|0=#mRFY2bMAeA?<2If9
>d>A)QD)ifbm)9%b|$JP+d9B{5G$3d4r2^gm*dGq8#>{sGFQHrDxr8d9tf(CbkzJly^D~{Bdwu)i_sP=
FRf-+(IS)h-JTd3uEU6p^gXCmicpT{rRP3JWp1@C<%@@g)eeMOt#?Kf%VcseLC^0$oM^SyV*y!@c2x27
!P)#UyL#I<x%C_Ijr1%OxxnaR_?eTjcEhbAN16xIZJ?3Np-d_0BSMH}kBjr|o2|0To8O2vKXOnS#TT3<
yrg+nN6n<-+ua1>tK>_iGK3j2Z||{IgUtvS+7FY@xyrhzF&E1%bX`(&-_CJjqnXual#nU~&6jo#plm0C
%vHM2JW^Fkeg=Ch1T=PJMAAfSBk8Wo&(a5S95ozq{BPZFH8PC3bV03Gt;D{U=6miKFp=Yn0rq1oaat5y
%M96WA>=Fmzj#$mxmG2IbqPcCV<A@*y}ra^JJQ3|ulFiTI=##twn1fmPw_H063qCGTmYVMe(%WF;~0I=
i4t<iM(C)UqBwC=>Hw-NXAJEFoKx~ZYzzHmK{Q2}&pkIu$-#{~>DX1w*^+^~tZ*^qp`$XH$pcgE1}ldU
>QU?yb6n;Q@jM^#wdZV9GsDHt-KD2G<qY3fI%!t{Ch1ghV~}y``t_XeCNdB?-xN-=Wy7(M6jUhQu8iYv
6-~WB#UI9utvwkC_0}!!v%8V5LpLop&-ZRe-m!ns32h+;)U=)lIFIwX&R`0(lDDuWt&=iD&grZXeNk-#
qes2#Br<a;fH<yeBO!X$(zc?q_3m`TA!@f!6)m}yRkJ}Artpy8&XeuEM3qv*F?p~hN-T<0lE6ZI#FVsc
0jc&5TNFgf(F5hIo;;JaMZKB4&7JqDiP3N-&Wl8#R6Vtkd6k-t0UE|p!;2=Ux}MIS>(GOGHL>-cm=Dol
$PJ^ICfma}PmvLN<-|VhjF_#s2VxOXm-K(Z=*Hu8E%UH9yIHKozRWNrum`<@+B3v>sP-4G9B8Nwz$4LE
=P)_LMyOhA$+n~`k}~db&>rahk!9R!uWjEbNXR<t?1c$bWRKk*z46O&*c>Gw1LpQs3vZm>sR)+AOK_!!
uY8}&r*<#>tWG=fTe>p)rG#Ckd}K4}yB2Qc*W6RMCeb=?1$|^LqB)lm%K&KizoFMy>}m4G|5pN=U4D{+
pB{ZJ1ht<*-jp6aj9Ih&zp-=x4x@H3np+r1Nav~HlO++ittlP<SCX%g&)lzX5Uu;zHwIgkI>7*)R;jMq
7Dmlzcv=z&?oZ2_H@f}0@1`{%LF%&MEtz$Dc)@ct2LdJyz3}Ytt57Alx0swJhb(xr_u*K>374D|aw3O_
Du)r#`TJv3na_f6mqcvF?Hg(NllJBFwV8fD)L`X20_SSJkLI?Gn|4DQqm80s2Ca@*?XMl9=z%ZAx)BIH
U7gc3ld9mRHgh}k9_$Jy8c;L+o!uUOP7gnc%<w)+PI)|xd;)s?FThkCc9a`W2H#|}1@z<L^l79{=FGn&
>TUy<JAO^HUl9SQp}$we<yjTeNCpQ025}J8%^vw_#J|A^b`dQ@3rFspYXYbN({jfs`BzY&t%*hdQxI^-
c7~;dJ~d=5Dp_rD{IGaT<gHE3vG$73VZQA$ItwZ}TfJNmB7>R}p;SOy=J0Pk$LCK~$0|n91$uHc4C}~v
NRto5LfQZ1o0NT=iSjy3u4{7GaR;W3i?v@}W#zo@l_gmAF1pD_<_}8WlFz4#D<KTjamJRJ@DKEWKzfKn
W9vIDRR2dlYchr%)rwiLB0HJVr@xFW$IK=_U}@;V%AtBjMEWYd??5+Y`2K%B3T&5M{u#$k95s}8&a=T_
0xD-l&6?`fI^}rguC`HzQejc^_kgJ-6&g%xdeX25zt8TfQ*;_(gNFviPl<<Me+HI)5-Ze`?(|h%2{<4k
YBj7&#mhvKGr^c05*lNOR=V5d<0Mxf59)~oAtU@7Y)Z%beA$vw*Qh`JpV4EA4Z!qcpA+^+mNC&|i0nbM
Q%v+z?o2i{T0i<8b%FnVLy&Jg;#|oAcFRar0$(w(83>b;Vi4xQqN=PxFyX}Vzd_w&Li0w}X@Ma-QvS#^
f2bb<gt(xbF8#ebsS!flShelYoG*qVy`dN@n|q~Cn8_rnpR2^z6HB#Gh);E<lVA>`dsNa<3!j4#zkmz;
Sd6_lxKW2wqpXtxfGR06G89E);!F)8Z`zJsly;kT06Db(!g`x8^Fn=7$pujUTvI%D!H5$NS^f##(45n{
n$A1mPiO1TX8=i;nwHuno~+(B0NzGe&JuLnsjbnxfE{_i%ukEx{w1)<)~!=t{Vvhqq2GYzoCbB&p7_nu
8dCh+LI$E{?hvHQN+7iQ9U+n=yx@39jDTwh#Bs<^sfq%#pwTz4a(DGjw`&n-!MBfZ>6V)qt|R~@wo=x{
Le-cfuM;Xbc|XWow5`AkM8d~GUOZ97OZ8#DwchAo?sb>Bm^Fdn(1AKv?;?jx)qQFFt>=W9idrb8xZG!d
H)iu4<C6jMtW+grSa}1u`z`o;5cdaa`4!=~?E_@WoUXcavYZtWu$5)Xr(;|X3+9whi^L3t?6b0oO<pW5
B|DN<py+unfNfn+Vsk9|NScncu#q<l5?}IPI`#Cu6rfr`2iBS2bUL2uz{7hY82f(RS1i%)DbjIfmq}%7
OZAPi9?lY;+wtf=>@`)5$G&i$`MMnBEf#h9EB@{E7H1vkSWBn&qrJzg`yh0jg~y|%`UVXO7!tTb)jQ5x
qag*VVa{bkD(iNb$W+$MU(shf&7mOAj8+p{z^Mp$_<#NYsHug!-G`yd2!$|?b`!(^5(Z4^a59xbca8yZ
7K2T)&9}<$q2*rJ-Y$#0%KaPgaPw+8je=Cfm_4u@+10q0+=ZmigeH->%T&f<gGap2ZM(<tWifRGE6vQ@
NY-1603a!ePst*}BAW"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

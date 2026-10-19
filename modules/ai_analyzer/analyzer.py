# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "analyzer.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("6538e4d28288e98a8d09d7cc4a91c46b7ba4d93ec386d01431d5e2f0fbbab0507aa67b6d45c3fc1b1ca118b631871b8293633a547a215d1f6494d0d9a6cccbd3")
_K2 = bytes.fromhex("66225e3303f04c67a66f57569f6135b0001751137baacee358a8a80e6173c654fb4a2b46912911e92f2952c79e33d5e00ee42b68d7cd01dcedc83cbdd7341ba0")
_K3 = bytes.fromhex("7b2eb0a670a10682ce3553795e7bd976a3618356469c46d74ca8a387ce0263eb90f667119daa61ffbd70b1789a242489ffeab06dea52ffb4aaccfbe52653130e")
_S = """0Pdd>JeIg9@yrVBP;-kLnYm9nJ>q&mj<29l{$ZC*!%#kKAOd^sg?uV;hyec}Oz^zs&CSX<RyAGB!{}{9
{%7^d?^NLgj>da**YS(&ji~3hglF_(9ifcIjj|?CXhnz(BEm>6%Nr6aCQoUG3az^d#H#IvR539v-v3{J
a;yx&$=9z2tV`2N??W5ylP?aUx-%KUgJ6cjqAblbqQ((vt(UPLwJ9e>?-W}m?et-tt)t`CA~>hK6>iCm
_%+k6GvNbWQW}6|Pw(<Qv2+EKb|E@e_LQH@;vshkPr((}6SlfMVWPz>t?CZAm#x>m{M5h~c+I+Kj-<8-
n3OO$u{GW!3pxs>)`nI2Kc%~v4s8PVq1>(j{OJ{T!j}gF5`#IY=2ZB8olAH$&_`!$#Bm42I-3?>h0g&n
e4W>q#2eITSCFphd4=ADQjjzMe^dkRs~SYKQZfKQpvlE|1?_71u6yeWW)x^z(fLW>^?I|3M|kLRooC?E
TgjF@UzMD-gM11dFHyNu5T2I_S^Rl1pY0Kz8}yX(OC2oQwezi!Sv9_D#{25cO|NLSGRqrdhGJJKTxgJ^
o0Af^bE@%(kSeq50O=ZZt+Ndm8#eJbM((<q|Cd+5jPtIKwZD7U9w$$ukV-w1BLRM=lGOG>o|c*DkH`AZ
ci@sg8%GA|kc0?&6D%ot0x0c|W2ot)ND_lrY(1+Y`_%Yx>zCtlKSCv!etezQ$dArQPl><$Ot07ak0tf<
KKLzaHglEVie~1{##yv2`;lAgIJ06UAZD!bv6-O&BsZ|O%>?OyYN~1I$iH~EY6v|g7On7WhZyoUOF^(-
wfdmL)=e*-sPNi#&1?fPeC>~4!}-}<%t8$2!muoQ?4S;h<_xgY@<1Y5(;t2k#eQzZ$b^)M54!5us)9a<
hSm3(GXrw1zXW_9-DP%ADpP+aWM0>w-gOzv@V`FTZ#C*h&~N)n8FvUG*?c=8fhMkgvUHFz#tASqFwTDN
l54Y(U{{cQ81Vth8>z=BZ;S~+MhHu`L>Vz8#rR{zd+QhHJGao{wXb++=h%F#cpK2k)*creE-MQ-FLcRM
U*`Ft)9yhyr)()EI@NiQ@_4oxOY8I=jG)@Agt9~APu#Wx7u?rZ7$@o#`hH@^fLO%@AW_=$o%wdA4T9mx
8z+^0N3t4mw)et`@vUkJ$OVNb7>;u&+`+n{5K~8uCP3rJkhZ>0s6$Wnll{0j5OF1`AfEyg6OQiYRD}!7
n7Z%~X(3c7^Mnjxuk3b6ovZOKNR$tLdQe*jR#P2p8XMc>MV^&W7m1Az!uZRF!_4p9MmfWGEu)FpPH(*6
v~$&Ejzubb^bsqpolD>HSZmzU*BHkl1D6Q~1bK&C"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

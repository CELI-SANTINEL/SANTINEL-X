# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "loader.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("e04931a5ee02ea7ee2fbdc0143eed9f0c1fc01476e20a002a6dfbbae0e5a85ee4d58e11ec2529d7e7a27287ea29af3f71b867e95ff8537bb5dd83a106934ecb4")
_K2 = bytes.fromhex("aafbbbb7612663047ccf2fe4fbd83f51bd77d0544b011f0884fce08a8ccc5eba2647f3292e37e7a22e1638c49ca7abe3e46ab109aaeef8ce30866d22f4fe8f29")
_K3 = bytes.fromhex("1109422dcd34def4fd465060bc7e9a7d1b57e082c5cd3e2345fb948f8ac8c690bef1a32de0b75bae039c4479444b747ffa06fada13eef2bf37a6c0c255630bf2")
_S = """BVkQxjemsLe+_K9_Ukn_!;$M1#yFsbvt3GgPE84rm4m1U98ieB9;Pg<mPA7ZXNGbFlL1SSd|6h$i%QsW
V|$?^d;C>mY&xl?ot-s+Kr!Jwb=C~xxvM3QpgV3*I+b4W<0aC}XmTgQ4odi)y?b|}4fQBGD)tYE>`#a`
nV(L7S~OR|ZE`)&7X=+pgS{i+6a)FVhIoq3O|8y`^1x8~Lhu7nvxbyMMn<K;8+qA5V==OWtCkyEiaL(Q
THA6*SV3T6QBRuXeldPAhHZ^PSv7JDHcC29Sz@oO7<5C3s#u2}=Rf@DmK0?!>M`ks@5#I(>VEqU^|Cj&
1zjjzK#)&HAT@(pmIf0q)yU~!5F8PP+6u4mH(3CA$;KlTJ6CpJOS5#m^7_dJoFn9Xm{QNem|8VDO3Be%
3M@mJm(9hWM>llXOu}FAtxV+9J!h9MvBS|F^m$j$UW*c%D0c|{^tnOMn}V9@lbB7OH0JR<<ry4YGI8B^
AcVRQ5uZvYru?73^8=8$f*xzFQ66vFpMXly>4(lt+qfBZcI1(RQgubdHAS$Mh)J<q2o>PdacHuKI(xH>
+EzK`;*C)>ev*DP_$c74W#F|_dZ_-yN@|u|Cf9bY(k>|RB&X$4pVkiwSq}a}=m}-UBPVgdccY@h7ksLj
w10-bUitUscO6_;peq+b7B~+x5^dKt@9!*&jV=MU<uwKgGnJH2Xj)zE&l=Peq2@LECaT5y3KaS0pu5<Q
JAgVnoIw_2el@v$b9M_r>)$jZz%y<^-dMY<!#8PzTL#ED7YhtE>&D83<D8sNi{v=Vc+8?PQ<PZbU@4AK
$H4JbwWD^S_P6zFwpSox|CJnm9rV=Ma;_0ds&IXYko=B)Nt?YE!0`8KwfcU#hmcc$o)MrQuWDIZ(A)9%
KLXZ-5j?>1AVcp)rhOru`k8FPtLK+|wLER^(M}1HWK^YDCCG;=du7}}PR5Qx63_l)ET1EH>Cc@)u7fbj
bCm(|>}0++S)LkT!7vK<Jgnd|#66V+Ps2BMIMo6fvRR76T*7q6<lsr2YQe>Hb8(9#yl-)6oZNjpfFyCo
Xc%Mjs)}gVZvULm({CELbZ_Kf(>Y(>I3NI>@|=i$f=^G7yTh!d^r}A+`GdqWDA2=hw6_P7!=tcF6%L6t
W5Hi!`%GB<Ot60jPb2@ISis6}I3^@gKsE!%nf_w12J7=-<CxYJz0ioMWuYXl?n}t?mV2l(%~?jLrv;W{
*@h43VQ?6HH9a5<P<8EbW>~Qyzk_$FH>BL_v^_nTSf0M36M-%v0z-@-q_K;1O1{nskcOI^SzpOtTk(K!
xP~mx(MUh^=L(UtG*t@Y62o_5N2>y%S<^HP*RLR_=$4Q8ms|6_ajP?dj=2qS$Tbb#9AbgYgodX@l8FFV
hQ!uu0S(YyjT-GVBZ)smhLnnd6zI<y&Jv2H(z|@5bPw0;<&cQ}y*)i-q!3KNiH^oTAb(R8=7l7Jdq`)q
<x4%f83%wCy-7-HqW0mYsW6)B76rWD8VD1hALpan=2Sr+jQKJzSMb(zF68E&pa>$ut>A1IBs+IIj-Dhs
a&ZkUAgEH$NoS|T^K;raqy*t1z)b%c@>=gPuJAEXB!iVgO_K@Q^~@ZJyISPIFXG)r=03hdjz}z5q~0B+
dP5oyAegIjc7RgSF7-8y6EGg`Xkza)MKLRpNSf;i!wH!O6QQ>$6f#0-$QJYe^Kr7~Z&1;1NwuI?JlNc;
prOmR;;PmDpm76wGgzgrieLDgU}P-ONc|&b7y"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

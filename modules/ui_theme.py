# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "ui_theme.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("fb1e784a908397b08d93e9c58070ca4fde6cec440c4097e37fc538f602d3afaa752a1988a0cc7e4789e95545c7d7c3e9f1be640ec92748d3ddc27123da498eff")
_K2 = bytes.fromhex("4ba61d5bddbbe705cc4dd14c532282307738ad43dc61348c590987ef820d9c0ebcdfeb9ac8a83f7192845e0e08df18c0a338580e67a73176ec338680df2f4177")
_K3 = bytes.fromhex("25f0d3994a864b242be4b1e2e9df511bcc2492961656b404059f13f2bdc791ebda62497e9692b9473fb7f33bb789be0c0a6b68f5ed2ce38ddf09e35dee5c861c")
_S = """?UKve%JCr9ex-Et&v%N;buy9jh4;gf5mLURb#VWG8l4G+I)`k_3V;-`6f%>4v)Eu>^<L{!hrx!eLO>zz
*0uc@b(SGyx^ZSO8+bvHsH$=RWTC~C)npSKM)q&i4ghL5L1z|<z_oZrGN9+J=)^>13oNMVZt@-eL4Hh_
Z*=lXhp#D==Bt;hWKzZ>pK;V}YD9B;(|@(;0bV3d+yt=f-4fc70m!#`GXv;t+F=$tB1D3(kngl5gD{eo
{VNvL0n;ZXW0Jihluc^w**8IT?9NfGaT51$<!sPQub_JS{K<DdwSk=Kv=Ka4gBps|Fg&3r+ZI+J)`$su
GAaPfIi9f6qAKO`hVlSGS`<?EZ7Z>+g+O-Suu}jfLe1Rtq+pRqj`g9$x`W=o4LZM|WI)jeMwyI7r|hE7
Gh0F}^|h8?&al@A;#+j*SH%iTGA^K*&E>+lyA;pd3A^LHQW4`1Dg-I~ZiQb|?SZ{R9eS1yffK=#%-F6D
10ES#9vJWWFI8OgK2V|=QVC)6ts#Q3504na2rn8rn3AB%o0(vI8kL{i$S(0H>*RObo{cz`R$ULs9vw7C
-j?5yH!qaLf~;RzR;%iHUIOA~Zj<*3rNcf*DTV|FrE~KsLo$3c0vYaV*q8f>J*MQ}04~T>Qf%^7VPozj
&xIIlP4W*8S)&#}scoVCF|KmKvfhVk0F1x$>S~4%k;E2T-$Y~#D3fA-g;LI$sSYTU{zx+Il42+}4}<#%
UJ8I-3$)S@2tcH0!&Iw~vz>%+N5X5Fs4Q31E|C(&4V|_{aL8@0ybSx8<=$j8>1~2`tm^!e0q`~~Uk+m8
!$ps$DYk4Y+t7)W*+@twpZ^JCuW6B0yM%@#y}?BVQXd-y>zI_W9c`K_O-w8O0@wvqwg${+9;?8R%|Fir
=Od3wgPbVaygwn0vPg|b^J1D^65*)|On|mtuL;5(EowU@0w5SChud1RoI5jy6h~oRPdnG^TEg1?pWq=*
gG0n>03<P$OdYOxvx$<pQb%OVHr9GEdN;n4ks`7(8`ubh;RNRc*lnP%4^#?|BX}to15&fxtq{{T747D#
t5W|piSv$*cFl*C;I?eAUd8NbJBQqgpo;s9VixWCL>L%d33CGto3)1?NBC7(`0_ydhHnGwXIta~dImOD
nq;5slm>{xkC~M+^qoJ;OO;_q%jfIH-`@bz^LEj|X(-(~r0}K1GP==#CI4>C5pQ&j;$Pd@nZf>m0$V8x
7dUct!?jC4NGAH!$Pb0%b$)0bdPnejrw~Gh64Tpo<bVckFge(*m(2-wLB789-_>g}y8rdC9ka;o8Q9gc
?S&e@%||0sJB@EP-0_98I)L@5d9B98QZ2Cx<D`S26>yAw5GiAZc1E{R1m}vpFJ`Bl9iM5>;s_!L1<OF<
8z~A^WQW(Ui`D`N18KJ$1XcGZ)5&PGG9@#0J1S*8*Sg5sIu{vOh@$&ZE$y!RPy$wGsp9ObuaEkHGllmY
ZZRPZ+S%n)^tw^~#FyTtIFG1o#i`P@AO"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "fingerprint.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("fc024bfd35e5db73ce052811f9def01c0f3ca957a326faa7cbd22f3ae2e486b2099eebcf24cea5d2ea4fd9ff1d810131b337da7b0fc018811d030a20a00ef7af")
_K2 = bytes.fromhex("17d79dce8803b02f81e206ddaf6b117e50a10816d5faf2707b3fc255b6629887215b77ef9084cb901377d66e43a282b67d7bde582523c943fb2ebf219772d4f7")
_K3 = bytes.fromhex("b5556ca4f7a3e6d3044a5c16fec1926d06f5e99eb2aa1ee646350ed75a05756f8349da6c912a241c2a9c1ca7d7df98f49d025fb2b1b977e13d15441137868bce")
_S = """CR!iQ7ZsLRUK7a(;$Ko9X8O&&zyt~bL`eq+*0QaFS5<DXj5iL>^B7K&%%(Wr$CFNpu4xDEm~pO>CugBs
6>yHE%PcD?crdg_mQX-)D9=aA!S!(VUkeKRDeO-!jYS=!@PGJEqL-G}RY&aYAfV=U=e>GR(z;_0b3}D*
U81pfY{dzPgB4fj>`Pjl6o_utk!VAXtd11xJXUY|vECL>knqf8dm{$siPy#%3rp4^fsAH(gFn2$40Y(8
>Nu02L#`~Eb*lY%7jhen)Yw4<rBf<5X<sB+1v7G|9ZXdsI1JBFcTqPAj3<i~Z>b;RwX)Di2NI}r20f^%
Gl5E5Gj}@X5~lk(Xa$8trCFr^&|EjebTq>)MEqHB+pc|yVi_|4a@o%st{#O&k^g$%4+tPqd=JmpiKbvr
V;>M@ygpDO%6;2fqh<818@FL)50M**a3iJbR9C1+?pHB)1QOWF0YfO5(yozhwIGm?M~Or|F%atyCs@73
3&J9RB>vW@NsOibdOsGh3a;kc-}+|C6+%Dw<V$-+zi$*Ue-<!eZCPp~bFS~QJ90t`73hS7GeZaKy1Vvp
B8fDdW3L61zzbMBy1Eln$x#WZ@64x(?ka_kW5bB%y8vJhxr77@R{V-X1K<GXmNo~+v(g<Y76>xGjCGot
WX*`^P{W*GivOqsjN?wIpZBaUKxe!DII6P#Olgwh3*<pRChF{|#gCWOph0x~UdduWWzc~}7tbs+3A8|D
B$U^uRN8E|0(?`cQ;rWY7RTzK{jCou04zn4P~{8*T;zIML4_VO62G4rK4d)CyUfX{ww=Kn`dzUX7D9+*
-9$abjHLC4q<!zL`^0Db9cjBlOvWC>Wthd7o=Wg+^7%rDbZipde<C-Oov1q5(j-vVfZvWT?utJjWXF88
vQh9_Vp0Lqtf&TRgpNx-5&mRZKU@~sO9GELgVtc5f`rJ=5CSsOgN`wT6`YwO&4u~Kwkvl^3bv^<EF^j~
M!HzUnGA$h%BBanzlCuiYUH{DMYBt^PoB^AX_Tf$##P{_(vZ**Kj}#B68)CJ=}Wtll4$mkWR4c*nMZ==
zGucM=R;a>LTzpcx}#QGC#nO&AcOxAr_et<)GSrYw1aU^^<YSZ(K}2*2Ryy}fd-UjH3LpQd2e*(4)%*1
^ygM;hnZ8#G%Z|2{tF}RL2y&@B}RhaZ->Mg`{?w5tk#I*&^A}f`c#%&xa0ZSYKABRqs5`l%Q<)yJ+RV!
Q1UnZMuozdzC^?10EVDqd{htt#JGesi<N^|se^+Wh?Kq?i<Q|{1<nFZ+5KA47Z}!WRl6R#o}6-M9`lD5
5AbIKeHx(sQ{2jX)!v+xBmwldZsp!(617t};2G+P62Ye&TrrPL@!}?UeXWPcP9)yt1`IAbUZA8T`8Fou
hvE&m!isL3qnEJ8VkvsQ3Q-^Vk|x+ZIOv-3S;SvN&o30~j!2%|Pz(mA=0jf;9+iDZ-Lz1RujP*I(?ge7
qv=Fezxsf2E?wOjvm-3@*%j9!3BF<IexnF{D`EAdxh+;YqCR`jB~j-Ew=<TK{hti+1QiE!VYaxMDmGyp
M5pW$4jj>}Iss}{fDX4eTaz+nxC@*gJd)9uiaW4SzM7?lp~5Ro``wi)^9=(jd#Qfg-CZ>|;rToGP<RZ+
?d*<TW1n#k>1%$_y%!eSF}d|y7t#Lpkqd-Ng}$6AhU@j_0<GwVOu;LPoE1nPcG@sI@J$b7t<OvTp-0tG
AnkeSC!SL>D#a>h7NG1tL=`7L3bveAV+7YFRBsRl{B!Q|M5}!7sYlJ`Q!Lz2$oSG_zv=(nI2{|I(GK3E
jci7Lte6&5hJvia^3H;%_?b%(Kj?$O8Gqd|^R3;3dpDB1{jxfFN}X)q8f{cHg$WG{q+rw34-yKo>$^oH
Xw%hfinXRp;nx=|d(Ecrqve+w+5)kx)iH%vcz)!p-z=k!a&@W(+!c5<TpC{Ri?S~lPfnD_<cfIY|1u|)
r=Wv~8d9jcF5bRFx_XKKMVlO<{e9MH0sTQh(+%j7@ckB&icZ6$ayE+*&EFMW-ZovbaCU$Uxk~VZi((vg
C#pTGhHleIPjb*W{djVvS<X~Z?tDIQ!%=~Q62}98CP@K4vNc>DWfDfo$|vG(2({fj=7Dh1E$9=SM?5m&
xc`eNCcG6h926vD%gDoO<@n)jsG+N&$ALVfvar)Qak}#`fMv%CrA>5CeZ$~we&~Mgs+E9u+REWCQw2K-
rGg-Mxo3a;1f=yOuZ?OEsT(cE`z4XfFIpZDTi5w^l~146xzlG`v<C?S(oQNXCy}ZP`ApvtSS%Z>!^z+X
T`!U<5U29|wjY-VXx42ExV_J5Pfeg2?QY0pxF{r8%4QfK2-YdG3zlV~jy^7t18Tb)cz32RphCrpyEar-
B~U8zX`TXM8s#h&L(lTzfHS}}^2fF-QY`E1a4~~zp?8nTTd!-i@EE#gw5}a6J0rGGO4<k;l&-WHQAEX*
*)HgrVIed{PX{@xS9c|+aMKDhcLB*Y^gaP`BgQh1c<`Re;9Bi(h?_~hGP;x?yq{^RvoPP0CCOT1o+~O>
k?}Kjn&bDcY>GE~b*lLw7fDu9LuXLx8q09DwNL`pT4cLzp^dYJ9J=upCG3#_rC`)7&^iUs$rnh3iWAi;
{R;nt!NMQjB^3`sUy5q74?A_tmxq4&$jyd3JrH<F*qsttY5rzIPdFR+IzIm!noxm!h{$S!-0$V8;5Fnh
mbL*jV7}j<I>^+r_(Af;TG>;eY&9xNEV=YCb6NyLW(H|nCpsG$s_j*832$COs55Y1kn&RC`j=UPVy+2C
g{iB6Zfllv@_*R>w~&z^KSSFIkGN|*y(RvsQoa^D9$_9)J~oZe1|4!kC;IeAfEc_tE+qktq^Xa5w4Op*
6=G--kL05NL1m&(M{KP*b>*f<pF!H3=|i=fH7%uA{A=K^&&IQa#d${bSU`Fm4aX;iAVK|{C5RN_rbEje
;BqbzpTCeu?x3}Q<p+ovB#{|vE#atC1!GLrSXg}X)Y}qs7qspZuubCjN5r5)o#^~i0J%5U!>3=ZwVyC=
oao>U5ZS_9zVdJ1j(dWV-RZJyr^`IkA)L$^@H1(zefKO~F#GtSUJTRuy?vGfyVw2p1IAr)1o*+fCnLb<
m`I95_H9Jo6;1ZyYy7mnFw;Zf4-Y+BpX*>MAgGudt=Thf8ui|1+KszcSx1WIccQSdjMtPe*<+O1An0q(
kyXs~3B*-DAYBjzR%nXpGWzI|xZ5XT5O?^DhSvadSiAEI@7h658baNg9e>p=K*Rxc7|XgzuWL9UI_AFv
8XTR{M%Pgy$*827=1d48iFI-Gu>3{HkziLj#x3D`Be8pI(f`SPTqOuo<yJ8;Oa}noHLMGKC3FU`J;%P<
EeQ^9*)edGQWr>vU$!|nw1%=XVS>g*%*v>L(OYi1=I+J_=y0=iy@K0cRVbdi4g?N7S`dx13Eg`IW`~Z|
1s9b$M(NgIFq7#Oc)>XGu&$dlN_tCz0tyk_v~HpFB_@)fKhjZe{?*u}BEJHu<#NQYLMu7sn5pD*`nF#<
2o3Jc;I2iAsG48Bp`UF}eG{x8#@dp7$^"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

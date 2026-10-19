# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "idor.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("00758a406fb859195e8b2d88136e6d0611a20d7b5ae85c171514d066cf6cb510c9d1da8ecb589a5af452bbcc156a6a27ccbaef9db1717ce019c69bc0dd3a0512")
_K2 = bytes.fromhex("44d489066d002e24ca0ad677d1e5048fd7ee5fe8028596eeadd16056c1e89f7856d17b29948f3998925eab0ab47abc03b2d39e465efdd2e60db2d6f66d31903a")
_K3 = bytes.fromhex("8e7c703693307f21714ffe27556a2347b7d7ad4aba45c20d5cc421ecfaac8aa063b88c931ab792db789a1ae3d094c1208427032ca44abb9f03c7c984c28eef34")
_S = """vIpiU&e#*%{1H9{e%@Qma0$PuVmZLV2A-U1ccl?a@d=>CL=s~fN#`)d{S@=RX~R3js9#w>^BT<|Yi1KJ
ynC8t-g8I>k^)v=qjHS1VjlZE2&VfabG^U^$6<al5hY{t!=xhA;wa@(3O~r|g!Qc{{3OH=2qsrO7>)k2
YwWjT?7+!}3GIK85)FUn*TuDXm_dzNCgeBbhlk~P{GW85in>}#aw~k`F9FqzU$uK7M|Kr87pO$M0)^(B
$Q^iahA0^P<JtsLmj4RJ(T}g+5-N1`+o6q&^&p_){p~F>6>XUq%9MO0n}k+G$L@3INh%X{7GHsea7X$&
itf{OL4sf(3C-!>BNkai(x0mOREq>f<M#k&cRYuKC>s6sDv@$#mc*w_SQ?#9NbV@Yj+=+f3@44dOq^**
@eKzu>YFM^-|LLgvZdh5;P1ous`+`v$}7f+ABfPAY={o=-3ohpk5q`_6Na2k)?6w-6Ye#&e(Ds8QsXvU
nT4?U(XOg5XQYfO>(kesCE#&6D4rDat|m0Znuv)sG8!Csfuz*E)>ZOWHSdn+Lg{<PMKGjI5i^afB&oBv
tj){dmxaO>&+{f2zs+Ok*e*;yYEC>el}xYk-{HB?ZF^0wG$qx(8`HncYm-iKa5e5`Y?CIDOWzx#7Q8^U
6X;f=q9PI4-4>>;pfM=yS65Yy=)$1Vt(n2G)GVnUw&(;|_$=bvO9NcDqST==x<*mAMMj<5pFgHI5)?R+
pY_!u1q_Haro_NXw}_m|qgSo@&jh8c$4MY<lJJ(^DQVi~92TLLIQIWs1J4kgVP3$=VT3K4*rcLB-Q6yi
q|T1Vm|Z!!&F70(9Ao@NS;BXgs&A=&XquK^UYnEg!YRAW?LzgJw!nloVkXsfP$@Y;DrF%V4Cygkz+k(x
W&<?HCNEBT)QFG@J#12-F}PXfK_wp5668<QZ21<~_m;=}oPL3HVJXG+NT2sAh(?qf)zFcRAgv3O)I71x
vWMd{CBn^FykGUevyB*QUOxKJ^k!Ue{W#T@DUfi?O)p-!F>EHGCih&l(>T>dx(F4M{yID^D^3=3tSqg%
w*n@N&u8<qIV^hbE$||ce6LVtR>t8k6rIc|XmwLmr^}ozZcD^@`NvU16}OA?1bw`Wscr#m(;}7F@_!Sn
Z#DZ_-4t)1JtLF#dY3vW`M3Z_<TI?5XEfx@FEs7NwV$ljR!XOho82pC3!NyR&!L!!jl&1Wd~4Dm;txG#
i+_hYNmJT&h|@6#K2`jl+rq>yfU*vIE@%Alc4;OVD|;_5w8HT+bZ1%4(UZYu1v!}sJUs*R$i7G^LyV-r
vA&#wKmC8pS@-U9%Tb0^uCYfpAP16~(A*&L^T+WcG2c6`lbp<Quq6}DDEV@-l%*gyP`+?AClajZ@h{qo
`j_HirO0IK09f$q(yh;?=@G3Omhv33jq_FTwtry0Zu0yWyk2iT(8nc)X-KvPmI>OybM4>B%ZV24lShV{
^*lG&uTL*gT?;ILEUOYZLdE0{1~Eqgmu-nZKl8zOVXzRgvzo5eeOCC!5OdoMoL*>C)vL<i;UFVaf<x3;
<F0uYjk!0$%Z$_dXFxx-PMC2-9^#U$F4+kC)ma$8s@|ku<FkbXySf{$5V=91qxpW%{GALUU{j7}3RlIY
+9+dJPh8(wpXFyGjuPZbx#}9aDzz6~De+;%MPCbDpiy4$o!5qV(>kxHqe878jM#4r9eQX5@D7zp%vocN
xFLV9tM=NfD@OLgNZZvZs>tqLiBWzWFSEk+nz2)2@WurHlD^<yz`>^?uTP-=_nK7jH~oqC@=AAOX!Q0-
F5n``Qh{QB2;Z*DCT|?wnop<LQa>ufgs;3mM$~k0T-HqRyDU2XZOpQM9O%Z2S7j-i=k395*E`O9y@pZQ
cO4)pRf$JJh49k{#u5G_Td%D|eRnZxw<>5jsXa_#uh+#zPYiE<CZO0sWX_CMj>KRVkQi14sSwR+3>Gq&
;H8o2y2%sLowP)(g&R}%_0>N$&5;j1dC%DYQYNCVEsd2N*^<~~{eleAP?_F&oUFUt$<ik<a|_*<)X^A5
3}bsjMtmoqNWE8(pHgEd`N2diIVh32#@&dM2KgAY*d&6m1~T_T{B31K;T=@i5U#39qs-(S^59R^#5!k1
(ZPr@SDSLbPe>i&HnS+=SX$2&(cw_e%Jn*!e`1tl=vGID2%7+2`5X+ld!S8b&VZ8O2jxbl@EhX>{T$j9
7(tGR#k@H+!|3Fl+T7{0g@d+<FnUUohT|1Vt^%xAu-F#We3NKUf~wBx;K<aNiE_5XRi~4kPI949(>zBZ
T5z%L(V3_x9Nsob1NqzEVpo*(16V_c7wW$5MGRw$uDkH1{-g*}Be+8?0$Dm`9Jb~+1obU!a3RxjCwK0I
cxv_O@X=_RVh^Qdx-CY;V@J%x11>4VHMOHjVC)%S-kv@lG#LN2hd5iT>%H9d33LA%Cc##my<WC%CcU3_
fDO!m$5F7hJvYv3TPQZ1W4oNs_h97d)j)Uo#f>?9_AiVp**Xe%k90$Hpg(0yIKpD&zQImMj2XA5&!06~
sex&io!&GC%S-CZYxLG1zOJFct?q01fP-x)9IdOLTA1`NnB9bF>J%>FH+4-Jm<${q$50X91mw|mGP0pz
Og5gIj*^V0Xwnw{(xd@Wkoo$K>8}KrugVRg@u+N?$$1cY&wx9P9Pg`7^N)&dbm$<pY2fr$p4U<AgmdTc
U#%@;yHJuEglWtQr_WLgbYGebW8aizoWlgya=0iC*{=F6kzAVDKvpA5|3&LjxZHU|?@x5+-dFm__SHfN
9v>9*vJ5M|Z~{P@AyFbwzag~mK3$_4URrHNkKY_I7k--?4#nz-5fNm#Dxmq!Wrmq>^XU>^!M*jxmp+I?
RN);2;dkQv*Rm=5+ns}fA8R&@+>yzvp6+|zMfei95<5`a8{I5`X*!&5e%R?~OF4`Ke0bF#I0tUIAAMj;
w@~<u<GAa0xjk^VgO-JrZX-3%>_nWyNtdSaL4`Mem-W+c6rbnt=ZNa^emi9RfSDak_2}V87=xRqt)GOU
wd{%aTRlkccoaS)<veZKCcyzix<loyb?%IVTQJxYW|e}DoEeg8&m!KQC;AVX2is{0mTl`q3{7+xO*ulR
s1u8``gWTKdtGYFm@D?htgJ8v+M6&;y3lQDQwsYeMP}1_zM>i~S^0)rBslEL2pqX8y-Chy<7u`@C)O>>
DP|3d3|ki&SNjN4#1`R=4wr+$x<<psNlI!<9=~h*X@&GuwlesOJ4O3X7gIR4Pw%%)j&v|<S!h;XuTn)~
w{YH9Lh@=kd)K*0_NI945^y8o8e5Cwvv}Z9Pq4XDGW6n5?{nzmzgqf^YDdP=8zvO1gW|C)c8a$a77?v3
zhb$bgF8LxE?D4`ygy&H*JkTCN=eyEFq1d}YlX_Npjw3;IP5Jvdl|QlwHv<dK^X;DXC*2w`O<q|gSgaN
ORl$%y`b2v{D^@4WG_|F1Uk(?nm|ozhs9F<p!(}H+{@LpvEO|Q0fPUK>JzIZ#5*RGk}eWpU=)vefWy-5
Q%IYeHMYAY)!{sjnhUwO(=;?An=d8~V`!dAnN5IqjHM>GzXv85OnlheM>X`X)3EvV<zQnM#Qfz_JPW~y
L>mAf&6GbquY4EJgrjH&07;I;$q=GJER|0fg?M7Q#K35(&PuyIkTEM$(J73Fkvt}G10ev%pLD&v{C@Z`
PYr($PzGYn!Mh*Y@bi!xo?xJw9uzG7UjHyfR4*w{nldvK`xEEMI}HM%2Q9~*I&V8QS}u{{nmA|EpG(R4
6q%Nv+#D?KwiIM}O(&UMLGa%9-4R64A+hPl9sU)FOU}pId_s(Z<%viOb#II!cy4TNTBm9mnI0w4jl|y*
nhsT!=NZ>bGlL(qEUKL#BgTZ<SccM358;o2!=6gABl&QPJv8EiNYb^H7*|fEEiMc(EAwuY0bR6evzxfQ
?bJoL3;=#|^Cs!tI3TurcQEwAPLbP`qx+db;tG0s6>fBO?4ga7-~8YxXYM9kA#d@5)#hPy)*!88E9C#(
;GT7>B3Ebu%HKaNwOcA3)~IL(f;~xh(KU;3UF*QG0-}I)@f`xWEiuhS)P<B$|3jqbo!^$iLs&@b6tyLZ
3wQ8#`rz8c&<S$Y+NFc-b=f579WP9o$?*"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

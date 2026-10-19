# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "local_backend.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("c93d3c8590ce1efdab52d006d55c42cd5a4f5a5e5bb99c1046a0728b2cec96e475a4f549c99f8f6241616165be1ea4035c2dad18cc40d34a30ca20f7b7cfb1ea")
_K2 = bytes.fromhex("2cab6f034d6f49fd65e23cd53efc6e05b12ea9ab4eb56fa3dc3b75b5180855c7268a4d37fcf6f064652b93e55c567e80ead4e32c24e7c333269bdf40f4ecf58b")
_K3 = bytes.fromhex("d7ea60c3b3aa19e7d798188d489e8b716631d8e77a0c7249f2fc5ef2c9cccaf0dfbcf0c68be6c204fe9b914be4e83ff1d9740af03444837a695c8458235d089f")
_S = """N~ZoDHAhvj1GWXzlCorMQ9`+ae+c)OPi8CSw3|3rn1p!DjzJqI!`zk2RWE|B_PlL(v6M`eHJIV2OZ##w
==X&bnTi|CjPJ-OJV=d#q)mP}099U4F3h(t15f$3<l+kN$Jdz*=`MyasYe3tCY|!zixPa0AyoySyjWC>
u4E8#j03O0mpXX;E?zr215FB_3tU{jsG4N5^tdlZXr>mcZ1aB%lSe}Y#bV@|LLm&SQaH`drbn}nA`LB`
|FH`sn>%2?axg;}W;beb^^k9$CQnQACVRi$)OJHTYYXIXIhlo*m2<1}<b<m(y7WOoo{Ityx(I8mNie8P
+G!1FCJ9_(t%z|=2lI%f3BwDzNXIRzaYYw|m<~!2*UQq$K7ezY1abEUfaD21n+%6AuE-A~4F*|&nrs!j
(^<X<r9u#!S+d&8v?=m6UOV}PiiJd0^5;eAQm`Eu4$V??B=N>(JHz_T8x=Hw119IM5f*KN(xa$^&bb&F
A&_E+4}i)!kgSS~L;F?8e-yf-Yt+K(BTz`{&!(}kN{lyw2)Bgc22zc$S_P+}D>5f^beI>b{q6-p<XHkT
isF@)YFM2JWro6QOc$DV-5=PUeS@TwwRwXQ@74lYDP&F9YI2{BXL=|2xbkp7p{I7k9;eF1O5#vH%Ql;-
mN(^gfFb<qFHE~jI{1976v_c0A|=YUo1$o3UV`m#seH`VPhcKdfV>iMEER&N_j}zwdj@nEv_dxeUD&Ux
RXNq7HwyYG=g*_3!{QqD5?}Ienb<8BzQPlC#!(eKVr}t51f{Q0B>PcJ<&}kvr?WV_V%}!~#qd*{%%TS%
7*y^wfi=B~uFpyn|H6b_IjJ%$Qf^A33v$3xzytjMSj<z>(Npf!<0EfY74_fOfCv!oENG+ksDio(0^s-?
Q?{kT9TPh_MxkS8#^Ev!L;`Fkf7g!dta>4z!|~FUFoZg+G+5;SJA1oOKJ4`@js3B1TD;R$FtYm*Ume#;
M&KQy#@vM4q*JONo#f|t+LiIk*Kc+Os_xe-nThr+Xl<_e`wgVtu}h=?S7BVA^OMK~C9}f@YRr<PA`S){
V)}SAY@yNsi2&PIDvo)KM_~Bge~L?t2_gsGZ&W*f`{b)jSfjE9=a4v#9@y}4tW1|M_y(sWH)}SzDmT94
`&h^S4tqrS9ItjC2Z;rT7VY^fTA)__>&U6zQpk#OsY;N`jax1ZFZD76-ta1>KSJm#&}PwjBzjEMdpPfr
vju(~kJ=*9gw9|KFch5;6=hggw6*hm|G(8>m4ZO@+Uh>(E*(F%eoHO@nlb@b7bBD`SkJx*G@;>tb)X<f
jm?>Z2U43$hNH6Bgn52pxhqyCSu!V$Z{+rqa%9c%J5sM99E|nh+l_#jtdL>wE>J~#Ta}uDI8_tQ`<!6+
C2YtssUmvw<o5YXD5S&rV&Z_Ft4GkNxSwrgwZ6x)x9Q}pu+?8Ma1<QY{<B8IKI?qeS1;9}X@_q7(i~1_
>V$@kYOz>;knAMuQr2JH=}fOca~xj7+^Z_wcA`D<MK_o_9{pWHvOu)i%|SSmx7=wLLNN5q<BY_S$SX7E
1OBN8e_pGyEG6Sz5NM{mrlJ6@XSEBoEWkF12s?k5$5C21VBEQ>(QsPl_NeVN%^Zz21ro|HWJC$M7ASRg
46(94)*5|VJ5J@{VYmMG2>T?hPb{Kq`?-;(oK^X>oTFp>Q05(`+O#RGLP#&d5%9}EO4L&A6DY#t$N&2J
MP4$n3ogq53*!tVw>C_)4PzJ&bd5(mOY}jA5^ut2X7wYOYPf+l%UD5R9W~LO_892w-Kn_e2`%@H5_q<-
qEQs<Wn`z?sS$Rc(pMtxxG^HtQ6b8PV$suVi~<u_N%St6HO#f6%F7syi*fDkE$!EP-*|_fIdx!8p})<}
##AkiKi132@CTvnB;~Y!2*vA<Z6pLX<`l(NPc8t*UkGj}BtK{!Spj^vMDC^)Z_d==1cq5{{o`}aoeG4g
6#0CNcodAZDwN)Gsh2o9()}j}+pr7V&menWl@L4Oy@>VRq0PMB^tQ7f_KD#yv<{#FnX&`>58YpcV+-ne
`Me_x^u=qrO4wl)V!_<?s$4UHJvHR(w~`cVHDj+hfs1Y@jY8N?{h=@9DaAJAXbeY=@ik%LIcv&b#${Kp
ry9Sl*>g6hJj~cKvr!(T87Al8db<iAeIgH7(_|{vAI=^qTZCCj=TVFtyJ!>9kEZ0Ej~~5b$>G6`ch^A%
w1J9Nv6JykcGphl+=T|vK<#epQJ`K~<<aWbeCJ9mgs<!dwrfUV90*zn8IQF^<#GRrU5UItfICbVHHr1n
iL)w#pb)9R6xX2NDX2dNcAIc*6#LGVm!5=UvvlwwNQbNM@^N{t3(8P8b*0bDc#)LL1`4cucj9^^Ndfe}
ugZY)^#qfc;PyY~ZL!E-7Jr9BH2y*j2fE@}MwHk`d!6QOz+7*%G%Tw;r;oxPLusFz7F3_E2D%|tjxmvC
FdGC|mz@QtaccvC8p-KbdzOIf*$e6pKAZ?(p4?X%JI#I;0Cm{;ak||mRKjCKK;uH&()evub=f1<J$=)2
UaC!h0|yeEVa0#Q+)G;uE?_V{vv^EmH&f3@y4z+q>%p<fZ<qENvlx>A1B$k!a#8$!?NT}$f$VwOGT71u
9?dGfIyr!9CrtRE`@g+LBmP#I0sP?z)vl~+|5c$Y;O69n9AMEEh2K3BqL(`lce;M!*B3|ip=3w8z&!UX
YBFd7uyiL%uf#XY?nCrNZ-~X1H5&BSAGjqm7@7hg19}skskIvkE}f>Fr6Zm;K=H4y@m`EShWhH_k69fZ
)>+UOwBz3Gt#mPu^S`ZPK#F?3dFaUl4T(t6`a9NVlV44SpmEk}c_0!n#+@=R9VUglLtWJ5w|GvNT!|{s
!wuknm9uXXy1N`kr*#=0kkE6J@!Rf9Qru?7fG|5L(nzFt$<gGgC1=gJtqs!E6IfF424Uo$I+l>7&PA)C
O_4$daZ@GOaGL_Pp#v5K0)_+!t$!lAl>y>%1gqR6+C{ZNM6A1ao)EaT(YM&Zo5+iIFA@QVtP+CK#z1W9
9irWn`Lojo`K?t5KL-i|OB1q;ts3v~f{dfeHnfXEFB1|(N5Nmv<{J5aDqcTzOqklON}iy|_DD6-Yk6S1
=ZuHe3M-mdb$Yt)54@ORq*GI?=Us3~zD5#+O|-B2PS74(>z~qQ168YHZ1SxdX46oe>Z1ugWE`)bASvN~
CM#O>OpaCR=(o#0bYt+w`Dyoc5v1>E29t_Leq25+%u@QRE=0G=yPTEQj;o!+7u(uw7ua%ME{pKSHYF_w
^EIKN(PGTo<-5}#F|+8gF$z)bYDcPGR{"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

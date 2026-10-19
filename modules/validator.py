# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "validator.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("2e741b88e49aa691da6ac33463f5b655e3e4f7fc89d22f7d2c76d24de14acfa3fceee7ec261b5b3fcef22f5d89f9a1e8f7e3446f03de5426c1f757f0d5400dfa")
_K2 = bytes.fromhex("49680068a6d6af05124725dc0696e1e608282ab235c274ea8bca526db13a7067600e5961a6f98bcbf24031faa0e248fea2f1caf60775db38b5dcdb5331006ffd")
_K3 = bytes.fromhex("07b304c152b146b486a3d379bf62ccff11a2ac536fb6d674f75e71d459a66af7a6702b74ec6278676e05a83540b3f218146a5a60d36f42384b270ea5c9ae6d0b")
_S = """7<IaNdy!P<Ur^Ry5+Yvv-u%-;N4vg4y|RDNFkf(+tG!=aaun1tdx(<HKw3Y&;Px0K9&!~X3Rad=tWJLR
Aj><U#aj<Fda=1D<y|{-ZfIPAbEl=KWjnHV?~y8p(x0%;_9TTFoM}IuFxtDS#mr;EWcT(Rgg0^P>%Ypw
(psXH6gV0b%a#`v{{2qKauEEvx?uRx6cn1#WaYPqHdTG$QNx>+l&@wcdj$cgOAzu|PTfZIiB4Hi{8&ua
!DmYnC8m9q4*j3&*abcKsC*=riMDQ$aU?8SSQ|%2HX(`thkh=IGl-YLaEa1I`AW_jZcw4C1I=)?WDo@>
DxNkthlm|))@zad&vw3gZ6^SntK7py>B;EYC#T%%LaC!#7#+VLhgK&VUa$o>GSUm;TSB*`-k-ytGxHV~
YcdBb+FOTlxcqO~z6I4-Nr)pTL$K?HV%*j~kEeCMSPJ=Z*fBq#K8tttM7j*IS#L4`FM+65M5rIbjwoE^
nQK!EHjNf*_aH%_Mjev7fA)}ld<vH7UF3E;h!oqUb@NmUIN(U@w^gTCtkV&MSyT(%Ma;`@rKQ0X#Hwag
EVzx8ocjf;Z`17zfGKW3-@hO^%D#}>2hA#0xPs?0)Z1n?P*2;@&L6IqMy-+_JlB#S^~Kp^LxoGG&;~*-
oQXcl(ek_r2MT~dP+jo~K2!~_dX2E&W6d|0=_|XcTuHHJ_}KnEDaU%!_}v5Q1^ec&7Lj_6!i{SfGsi(%
xXYT}|DDvXAHGIf<kiQPMw2z0zu?^N^V=QW0<vLq8z;n3Wh$JQKO=@S$};VvI8S%;$<Y`{*x4a2^lYux
LW;bq`n$SFi6KaOp$n?^mF|Q}TMcRRHKypvs#!mD(+!7q0{y$a)~#lI6z-NaD7(<dpF2uu?4r1fVLMAb
AP-T)q>E1lGS)to*piT^NQ33BMnF)6dTr0YYi|@8z6yn!axR~9{nBnn+mBXD4(~Eszo%hFoPjgNm(@>?
0|*(13Ke=Arz4M@$3cQm26fWOdrfSJH=&G+PCn<aJ8>eY7Bt56o!_IuI;2cziae=sxn89XR^Ps6l4|19
fpmHFr>q1!k6MqxP>%t+9;53pynNUFa#=Eqd>o4dwx)W|bCb#sF`;f@4bjvAKX2?mP%^q>a$GnQ1Vl|{
c@CDhqPoSreB=4UemrKG7Bq@irCW}|yiwWi)L|Z4;?<6-d!?}627J!6XFOd#S52B&a6W8lLfAqwX=6ig
^ufxsS3Vwg!3^<1rM&Zwt@@|D7d7=&Ns$%5QODF681Rsq4Qi_!JJ&3*54461MXL;R{ez&QPCsO+v>)eY
P3AjrHzdch3W=<>Cd`?l@sF!zvDo|1P9d<Y$+w#0djY7E(6BY#cMD}ZF;t?*N^kn6n~o8}{zhQps1{9t
|08dMgc&HWH9aWm%1B?x9X2FW8gfcrG2`~TP^t3|B94sqr=~Q%Vf9SFTWJzbr{^~+K)uZ2f?*2}3Tio!
p5NJVL%mDY4>>ut8z~xlE_(%tQA4{*n{PmHJEK@*zhO~gq%S$9)0Bj>;836R{rb<MwJcY|M~sd{n)273
#*eO&GO<|FKiMCQRis~{y2p+#>(OkJqSe9D?&)sj0q%YP`NJQ7CAg@~hPC8Um3liOS>EsTn3NJTs6Cy#
_dH8gQvNYO_evSIf#UKq+(*4^+E8Dg+Vzx&n@OC23E8Xo4-4_3j%@{BaQw;_p7?fh|9vhOyOK3Yxs-ur
N?=3=L3d|%dwAJLshY4ul-FaleX{2_ZKiu>>G4p`;_Z(Y{_G@H_fGB@)U4$%RIiGxtM4uK9PGi?qO%%|
f}GlRjuiT6qIkhxah6o`B+@5h_xX}3g=LS4`#>aQ89P^_7w8ME=BYpLM@sMeTo2C(O>aQ%RcujHFc}%`
{g|{G{9sD2gw#Bzf2~%C`t_J?8ZW=rL#bC(piD!aFwPu`bvznW?@6pnQ$JP0=0N4i>ifo4x*M3ch?Z0g
{w}Fak?3DSenCtD%{lJZv>j%CL^R~0_NnS(g(u#DGZWRv@ychlGgCZA<q!OK2-Xr({s`pVHLxZW1lA&q
O6DguqRd8HLjE6)J!ST0^Bthr;lBf{SY<)2N4mqR*yv2D_62vj>LY6z&SvSqcs2siGzw>R77_1X0z{}$
wg!i6D0dcTK7X+@A~^L8%z5m$e+R*nk^zY^IV2~_MowoIHFbE4nXvUdmMTcy%gvaPVG=N91za+{y9O}T
JGpA4`bX-cF(eBil78FQiP++{a&tp}HHLEPTnrTEqeUjbC-^Iki(^clzn37hingI1v`=a*%J=MYZ~=9>
Tk!OL{3e?LHEmzcWcG)!9~8bY9zqs5hIlImL>UWOK&DcsKv*)xFHWU#nLi*u|I{CX>=JQ1Mq_mwLYZNH
#?Q1|GXphTgYhG}!@fv&M1W4_m0AEBpZrk~bg??i^e$;Mu+#$cp_@a71%=Sbvx7^g3_H2!>9B6fnwp`x
6v2hmUiKHo4#2|mg`i#a;zEfZyjHRXzZid6&>)BqF&%D}@ITh=*XxfVw{UI4xjCU41sImML-|uZ_^I&j
l2cdxKy!$iDRdxU&+r_noUlY-6qC@CXFtKKK6!zhYP(sqk4mGe4PfhKTDPJVF5r4%fea|$s?FKpwlP(a
+0x<HKogId^<c*CuXqj8qZx?8$sJ@GRap=o^ZcI;Ofk}CuylwZuM!u1W=&SZD&8`C8hxpLL1w26xH-qE
fCSmZ$cQB2sL;o}<-18e3EwJUNZjCPwSBptzo-YYrkAQhvkk=NrKZy&f8?#xbXA42fRfQ8q-X1PsJ0n@
{_Lik)7Dr|Cz@yu@Vo216(eKGFX5S!#0u$LDyW7mkk$Gwe4#I8zwMDcc3xQbdY|g0=}C0ShY~|$dLd5q
oKem@OpAD8w+XX?H}T?|TyHe;>8{aC{rG`q=B(O2;#p!-7{J$D9JW)hPND8&P~rL~hWh7&n11$~4J9}v
X5A%XF0>)%B%Zz`|1CSSxazB^R`!r%H}1-hhwWd>DgL)3rW>GFA=tm0Je6mHC$tM3Swy_+?=Q$qh+NJw
L{J(Jg|`sCy2wr!n7pRlDkiBW54G%}H(!!v7x2e9rD_7Cd5}6FMUvnHqPFl{^icjp)w4u3dty)>Bw$Lg
ql}_p|9F{wwo_XBzDo~U+HfFGf$aQ(@4R>u3n1Zd)zJxjJ<qMMG4-J|X2_w76z0sKrn;jD86c{sJKPik
&23hF<R4Fls5%%edd5m&Y$UkzjzyD`_ENo;0>PC7K>=PYFsP87Mys`DKqYR5`S;*|wkC5Z(g$W;_c&G7
ju~r>iRV~jO9{pV43@y#2ZjIZZx3*7`5%(z<n1FOS6W642lQ2ykM9P=)?C^79<T)r$d?8B&b10@Z!zJm
8m-&<YG0_3pySVx4tDnfA3Tm$(c5HhY3KR>_v2+6jw{F_miTD%HY3s|{J-_wq}!4BE&$nA=TP$-3M4tq
^)!1`g-?_Zt_`I=c$=K4&wGRC{4k2m4J-72<Sty3coTFuCx6H$DCe-DgCDt}FxsHSpfiPc^bgGnNaI>J
{;<^@L#h0|i59}LWh6lLtrjn23t&U<UlqX<jkj42;peKaAn-(A0@GTv?&1^ea`;DqAq>+Bry05kVIENw
c{A%P2ooxMxvmr8(=CrE;{LOR_ub_z0=%9=+Ac6182P+!o?^ovTF*oqROfISqO#C&JF$mbKTI=5^+6&_
LW<ofEyaUyWDI7Iu|rLP(vuWlLobwa0--;m*~iWAiRp6Ewl+Yf*;M$`5aYmvd*4A(1WRt{zaIAhBrZgP
3hzKy7t<wwCw4?qxK3IoL5K}>GGmB;EV+-Se48S&m!@(T)9n}TzDf*9Jdu3r@0A$73|wkREW7{dHn^~r
6CrZ>GI(|GoE-wKk)QB!<+`Q#$tE!A$(aF~#0KagLyl}A=A7kZPk+{1urB2`*F&k_sJ_3;%jkIad4Pw(
IT4{?*XghK{bX+BJuR454$h<F2@GR3#eP%^C(FmfK^w(V(2lcWp_OniMS}oW7riH`;B_I@KlC*|d-!2p
;)lAkEIR0U7$zPUq+mCwEi?!A?mqyk!g6hD4w~43Oa>TU4DGsF>Z38nuNrIna4*ET+gqM9Ee8x_tlzYR
zmp-_4pEB-R1C-MczOr^gj_WBdLY97P{Vn-jh&zkVpckCnX%at-H>G<Kj7UV>kq}+dBXqR&R1VMilr>=
C#y<-*|$5lqz_vV0ei4oCGQiC_pWdK-Rc^1!7ub#;xvRDKu{j|-Jssps7%${Ucs%&Fukj_>)4nv1SF!@
RF1Vf=am{-mLWigqqLEO{L<}y3?;#2l9r~#)SXBePF`lc-3Jf142I5^cAT#}noNVVNHX8$J3YeMZX`&R
gis%<%TGi"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

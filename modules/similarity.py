# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "similarity.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("9124edd7e58049e3a09278d4e41f53f6a7c94e5cc83f60348edea61a76f71122a56f1156c0f198ad308c3320e937144cc0cf4ebf0740442e1bf564e8d6cd9983")
_K2 = bytes.fromhex("b35f986c692aae1b1db8acd3f22ff859aaa384ef815d5ecb2fae59279943487be78b442d5b36930ce3f1c675bd7e9168a022f3c56bf2ecfaa3cd79c00b07ccc8")
_K3 = bytes.fromhex("8029879889d6172f5d3f6cac1e00bd0ebbf0d7fa36b023049a38d24162290fc9b9c3dd8fdef15a2b00e39d1a83dc1478afdff0c03410c52d7d92264f33e86539")
_S = """+K6X#ND%7~^~<M4`sed*<fV))1}{FMP_^mq<=V%@POGg8ahQE2hg9Y&`NK^~b_e+0F7@5D!R%_s#&d+)
z-huD0?cqTK(#-uHOa;*H<+NqC)-KQJ*sZ}Ppb2}VTUg|N&j^3;;5>OJ1M3!5soxfCCzi{op<y$7tF12
VLd_{!=Gp8L+O2{v^gy+N8T2X?8Cp;Q&<rKk$y_Q+ZGjEl5+?DejF)F4g2$20kKfa&*NK~+zRLyGKP@M
>K7)11TiKCu2q9UU?;W+j6h(TylG@XJ_F85LRM{^q$|7nv=}iH6qKZ89N)``+tGtA!uC19@>aFaq^PRS
hxlFv?xlQvEBSpAu_-_^W4?WtDF9Eo?`(T3A2&Wclhw%f>W#}eucNmS%`Etxk*aJ8TOH1!$uXK~99yha
+Mr+Qi!`+;Y~~ox{aVIw4}8SJu5&J&;@pMX)szYwrt83iLqvrDVoFyn232#==|T1XlQ{b*v1D3aPfltp
7CO%chry7Zt#O=kdYAI_|I^p=el~z|w<6`%EZ!X|*7)#}G+z|OTNp$Fj}im!?()vQ@M(vI91S>}IG=Fw
Y;!H&g1YkhpQ}SGv$gWVL-}Ybfg7lKQ9iRvaEcsmP-1tXmI>-(Nki+n407`JCDAgOWlzEk_azLGo%c(p
HlGj@<%LdRdQq<Qs9nnsFd)=WkdtHgjO$yJn0f&92Z#dL&MT0Fup*0h;nR<r+pg}&h4IFJ<BYdG_>iL|
+?xbDXYM81jWD_L)Nq);S;M82v|m$1BgzfPeUk90Y+~R>plSo&n$pi={Rk*g9W$#e9gHTP>1~u$WQd7#
4=Xa`6zbEm%(9iNSf2fH<wvov{4iYOVqu<8Rm%=n;bHe{2{t!Mri#%L4SfHhNn1C9BF))ZsV>C57+dQt
m>v{QdydHjvNea%GY{`A-{B=c5PrSHWwliaPHevZ5^pSwVN_4ExU2`-PyGPZRsQt%hZ};9%y#At-w)5B
11C+c3pn>?N0$6wB#AlNUhwO6gu}$B9IF*n-YOiAr^+KYD6;+U30GnOwWK{?tNy`3xO^4VN*0u@|Ga>K
CgK67$$46?(tD8YQmzhZ3(JF)_npDV4w)VdXZnh0V8T6}%iu|pg~a~~`UE3jSR4W6xdo%Vq74@v9O!I@
P&avLZ{=lsrIeibx-7R8beGBd7xqs8X^SAg18EHX_H>F_F!lv%_&10@V5^#I@QyiEio}W$R%1ka6-CdX
Tz`y>!K2tE*P~|=X|@4V<;Cho(obZ=&8c;raArld9YYz-ECh`#ykg-@+u*2-ML^9mF2N#Di;|_M5BhyJ
*_-zAtsZ~JFomGa&-F_${SQ;y?_3^~{P_XR?RtWel7v>WF)N+~vjNXxrGU@MlaezQMj1E2rz8VW93p54
s0(!LLWUY;MC%08M{i49eaI~93A_PtY8|iv_()t#N^x`Up-{{pd<ffO$SjvIIuhcjm;iFa4pEWRT-IAw
Pk}(~9T7KW^@vg*;V`mBC1Ei`z_yIG{_QBo&z^5A5sG5t`G_f`IVZqZ{J*)Jxs3k6TAtOF3PZ)FJ%x#L
ZRu;qKsn{2g#oZmY=)s-;%%=%a?DL(ayfj<MJf6cp$jISb<9h?kfk=^7$5r$&$H*gJd2f4%RB@m?y$gK
X<z3km(E19S(U!3nx+|$o$N$?MZc{HCYsF8TR@vKq&_uupCi>c2|aHQD<|1Y3&0w(lYNv)g?ZS{!MnhL
;$pp`a>7|6^QVYjz{Af?@JYI+5@n;3y$8ynLItpwfyP7$nNgBq_yOkC8`V$gELWR;XDot^+4M{ZU9;W%
YC({gcu0?~Cj!KqQ#b&RE!V;S@EKD2j`pMO8n!Gcb_rXLKOJM!S#GUIXsqgyLvE5t2BkJHJ(Y&+s$usy
V~miKavwU|?(k8}$&>9#87JJ%G&#_qd{4kJQe_qUIJnsHJj=VOY<Gv2qhR@L#2~}`^=d+ik(RTXE1*Yg
rS9vWMEAD?+Hkl}&H|X5uW%YI*Q&7F>v^gH^NMOOtr_Bk>Nj=F<g_8ab_9W3it96Ke*sp_sg&HL80-G3
$?|Ph$b<e?EyIHZhs+CcqB!)?49X#=+u>*<Ljdh?!T?v6fSM`6pD%8wl*FQ!ZI!EEKHjZ54hoJpsrxQB
wZgi590zPLT=4y7uO2wYckvn5*@&{SIOquRS%DD@ELU6~iHpH%L@Xe`pZrWrw&Lz!D7WQh9*8IoGf;Ek
@(G!yuNovGp?jOI_71X>-&1dwF-G_sKUF4MoeT`Gfejhb{g&#R!L=~sBh7Ihc}zJ8UZ1=8T-ht@k&*EV
&efajTBTLyM!u{;A+~InxTQRWuZqJ$C~|zAIpXK|efcI6@kn6eRZxu5C}*Z$;|^8i<IxhEIA{&Dh1knP
7Jm)HOLt4ofP_{|36=tx=azvHz`Ps1$(#eY@wAG?_fRF@P1<TyBM6^|*+w9>Br@g%xHOsx%fiY1IOGNo
Kb;T4Fhvg*M!u!W<U@Kpb;aRBg(*61a9DW_)QeJE*e^rvEE8O9?cWeElG(-zGqC+0Fc|#*EBXlM4>oY6
JJNueBxbs`xg+Ybp=@1x9G?ixsvtWlndW+UtGw~q>+Lh}ls4Q%F_d6lhk%7x>lkFSdxOd<N2<kq^N3UM
&tiXFi$16MK4mzrUbpF{31uKbw?&g=1@Et;pP6G96t<A*pL2rO#0C}wZ#+j<-2OWuNiExer5qq9QdGLx
Qj(rj5#MvHq%v))aq;P6uV_AV;qgq2w9=N&+<LbVEp`S?gZ&Q|1O7)zxHT?aNpD|$sh@g(J{9@9G4tP(
+Li1jLdXRus4&pv"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

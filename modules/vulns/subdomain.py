# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "subdomain.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("c7a85d3e85581b24822f875bea5e25080db5ff7a51b4cded8c66b6a448815ba4395c0ac8d450f63a441d7657bfcc295f86a480b289bd15de49d9be537eedd65f")
_K2 = bytes.fromhex("6e8c198ad72f5da1fc5832775803a610a141b29e4034cb9a2ea2361b80d584778420e8e12be98f17941f43762e80ca6e388685a455a9c80445b1e785acd7fefa")
_K3 = bytes.fromhex("bf7bf060df3f6d623baa8f76bbc07deef403721a7e89ded1ee599d980923e8a5de5c4a9783cae4415f68484fe386b02b78776ddc1bdb8dc14bd5b5ab326a6dea")
_S = """ZiP96);KUQJmW#13t4O87zaK4OC(YTXivZIiIw{FhiJ^&u4lC^#x8F#UR<}327BCb*W%?AU7B&P)6H|j
%N2UDVFUz3`>Eo?H?@;cY0T_!2-Dw|9^U7F+<=x@9fO5)M7?=UaI=`tT0_bnUb^%pTk^*yxI%M+9|r_9
XruZmb%!!zD}F=HY`bn7j(hUFqDQDj@K8GT{p`|E=TUj6yG|=h1`sUx?Wo}xhEWj8)el?iMpx_upiosy
l3&%7i5Mi0MZr2A2&}%<c==cSTMB}v;T;)=%;z)GW6dbAJXC#2Pb)onlG^hDR#TkH$;{px$-kC-ozT)w
(O*eaZpbPpWj#^a8XawR3wItqUuoQyMui@m!%sTCWA3PMel3^~k{WX!Z2Db-#wlyM#y?7XRgLKd{a{G<
9+$SVjo*#`9#@zwoggB9>P|i=I*&DLegHLEBt+%zDHHG(<mvOv)^@c!IdD19!}!b-@P1^tneCy!SjEs<
+Q`v)3Gpsm$KVk#$n+1OL2Y9@?@Mne-9G}Xi!$LOdzu>Rx(y@-lrOM6ev(+>jviS)!lFUw9ppkCJ_cx1
Wg0=!dk~#l?KH8%nzrQNyp?7x-cjl57aM>r<aE(4D3CqgrS&xa?tfAEf3gm88vUrMl;TUR&G@G%N?-@i
FYhvAr4wM{2J5lvh4(c^E?$k=47bo_eL4w7=bKs`X*SJuE*_R=>fhC;Do!Lul6XX%?CKLWCEV?cVm1UB
fb_(&E*!7a?)IYR*pkL@p?y~B-iA!`iAxbWa-dSWHbt}bTo*{VZbtd{Qs}!$8HowhY?X0bf<b;KVsmR(
aOyZMm?d&#vgt07bXZh#Ws-a;F9`sRkN+yhY}Qz(_csVPxfU=i<)uhFEgUBiHG*830r7I^73eu=@Sf)>
fxEUcEslrf*Yj>~F&g$wbab&siki+a0O(AVt%MN}=p}@!87Q-)nIg#&p>SP2ZcYAouT6L#RJo~{g}Ba1
826D4uP2W!<8QtL;-xQKIdv~j&z)4v9YppxnVl#w!?0=nuu=x4t(tM8MBNY^3@_TI<mF*4*jV=L%``k`
)AO`(s$=oB%ZG{H%C0N4iT9K$2pxf;e*;gSCc(A9m)MuD4K~WIb%fp}p86niL3$F}t%?~h4C3LKaPE#M
Q<W0&d5T0`s~Cjat~L@l#Sl%Fwe~vxk#1&SEt%bF`Q0SV(!+|oqO%K2-Ck!;aU_f;EL_912w00#e<`rK
-;;0vf!=-V_J!!ilAE~a$XcXCZR6|gsLNOWoWbmo(v=$2D6-inRp>W#8^ryEoDW!a%2djz7v+eCPX247
32wgM*aNzX@a4S!b;JGrl@LxXoHH>4!^hRrviTjrIhwZgjo#%3yi_ISee^GLw!oKp2W%+NA%RhBuRnvd
A-zf4Z%dDmZU}^s_Sha9n6ws8y4N{W6W4I4NIN3{?1-#>3;QFJks^8qhWt4j>lw?pGYRd((7xZ<?xT4J
?L|1P9`WW{V<l?e#4k-Ww!b%>D3dSF(Cqfatx(0*w88;{Do{VpXRs>x*?3ycPhngJ;$M~*HK%`@(Zk&J
f;oGcC^6XTT~Y^O^IhU99UH;~^n-$j61dR5B~@10CM6_;&K)qsDc|1u=970BVrez2*pj>_t({g~VyQ{X
qLM}mX&yigxD?HNKE`pI?CE5+u$G~A)<ls)m$+C%SKa_$lID^^agwG{J{(D)t*eFw{u?NrzGxHr0v}aO
MMQ3@Y$xym#UuP+4;DZ(Jk|4w{Aw`C)Qsau+OX%z@vb+IADcpM7D~!6wTK`m21Rx*NAUAq))##kNJ<38
+9AGo4^Li3_%~qN{82FK<Ba;p&5QJ|a~3ySmwS{21Tg}(%v~nq{$hrLS2B`5wApt*w3e7a2@MyLyg@dt
rR3`DjQj46v=|R@nVz#m1|vDgei6qxuP<MzE|e=(F(7p?^$R-!{wV+x6w~!uF4KUWYmKCM@;B8tS_o-h
L0`&C*(hz{{Bho#iz0c(3lKSP(`(Fg_*y81A=xIAbczjZ(qOgrne#EY_bTu<Z!mrNVJac^%t5eb>$IfS
q{9RB`-_lM__b0YmO6Js<w{(WG=MHqt3!sI_JJ2i*ZGi2$_&VsyS{}VF)0N;e18_${Cg^OY-><t3yRG;
dzsGS?{(bqtDs3Y@8hK#ypPfjD<tFb$7mt13>dMIG!r*Cz8u1{<p2XwgOsshB$A0DAd!T_`cSXzHtV*y
IPyVzFtJKYQ^%DP>H^7Dpa<9vOU9(bU4Wo649oSZ0upONp<?}qi1M+<%G9O^7>q0cmdToY%WkLeGoRPL
Gi(Mh7of*U#JlTOIF4xSf4)=IgW52Zfg*J+EFX#K?H3H9?=Yl=xBVDSVt__;2?-f>e*CN5;f+?Yw}~4Y
bC6BMH#VL6prwGF9p*o|RwOyGj!RhQyR0D=r-?2VbyBM0>0t%Nx6x*Y04Tq7TKASX{#-vgdC%6#FJ)KI
Tza#W@aH^2F3Gu+Y=~irR^aa~phOzs4Op&V8!0c57*6z~h>8M-gpNVZ=l7^Z76@S`p5$l%K35NvsK{QW
@u>*o^|1kbG5MX#qGzc%ZTjHE7QEPREjLZ2jRx7AwzZ9ODwOA%`J^B_8~~}tC^#XDI~&(YjpGYD)Tv7b
hUpZ{Y!twKq+6qA%@WjMKb}F4@o)}PXiO2DZtN3L13WWY0_0x6O|T>?jLB$=H))eLEkO$bXH4Opt?`DT
4#7Glt(SP*B~&zTna})?%E(SY6zj&F$ppg_qKO8F0~~Aw7V`Pe%R<xXkmlxgSI)Y>JUKnguC-z^A%FO<
de@+@$^xy$(s7FfZb|NkVNjk1didcvdaJ^ge;Br%x@=t2ScyyGAa^0v4D}^NZ0Pi}SNG$>KU=4BB@3$;
`30*xe{=oZld_gIn1<mztjFM)T^BLCLPbIlrgimf@X_KyxN>HTkDkz7K5QLEp%AKf%e()~b~)?0EODwe
70f-+T1V6G3U8h^{$H)?X`+Obg>X$EHFnRlA_-XkH0Ouo<~{rhVf>239BvzNC<Btkcm5d362Kz#_vgKv
$L=6ES$Vi!a3?*LclTU;30bSEG!&A1Ud|R_lvt6=Ma#^TGC4GLS5e-q1s6f%hDLv{yoP0l8>|;e5U*7-
-gvx=SzIt#@b@ndj*?bn@-z*)yzhf3A^?c$E=?F5T50$T7$|#lwt<l<LW0}YDMhW==yTxvgB~~(H)uUA
5@!y3;6%CJ3Vp(FI2*a7_~9V|NB>FkN5f$cq`>uq$l?p$2tWmp%36ePiRz1^3@D*_8GM`wPKZgP@2+Jx
X}?o<a(dB6K0lrLVsAqp<s87~kl--jyV)>#X}bPxlH$(89j0z2tJLQgW}xZ8IQAn^W<l4w$q<~0Zm(*x
VQ>o1S8`GfJ1X_Dcgu+Zp771XhUQM0)W&xBiF-?;ksWs(49AP3^Rk1F_cgn>qkF#OnPIiHlLOU;-|767
^QLa7GrsLoAESdzB4Es_-v4MJo6T1mjmKrxe&TI_sbBR)6vb=7^GAiKF@uc|+YOzyGKy5b_<Vq=_wM&W
)t*c6o-n?ElQ#K1PB;trM;3TyI8dfrB)08X&QX4^_^Il<1=S9LFe@&QM)}6<S6Me*4COTA`N1+Uq0qj(
@3i4<IlB*Yit<wYYzoS&jd}yx^ljCFQM~H=z2F~Q`R@~<q6$RX!pAM!C&9H`G^It!m@Sl7QwX@X2XT@{
`nE8=NimWQb8_m~G33?1b`79>0hVYaoMc#c(dB4z9^$M`8Bf0`ID2V`P*=k2UvYm6);E0dI$KAzd?RUw
!po5ZPxY=1XF+dwP`i(Peg=3LI<p9wZ0bx9DrrXZQASp}=9kdHp7MS-LkVvT*G7`g0x(D3dH9j0f?$s!
=YiQ;Sv@*XD^-CndOD@)WE<(Zl+>a|*v1mLx1Gq9p8Kj7|9<mvVjh<5wHB%3@A9_XR-fngHsnm>Qd3NY
gmC2o_}rOUR!OHI%=qlDog9rmZo|5Z*tipQx1T=~-hT^Hm>OHju}+2AnU+O%WckfkbpcM%$w|L^=Z_?e
aYiF999Z+|{qZjOB?DYq`*4ljs360-Im8Vvf10PgpD|*jW?J?p-~2%)t81{1%gf59-vPACcdxFd@y7ra
J`|{Sp_ODlh0R}id5?J@OHK(!L)n=Bc-%ylTE(e1scvX+a!%c-pC2SfJd+@hblWxnneiFImzKiz!IA!w
{_PH~M@FBulM8c$$fGoPRi#PXtg-CqSV#Glq3eZ^73%08N1s((>d8&F(+3+8sN&G(8z<la&A~McWZ8QO
MrQ**I`Q9T8U"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

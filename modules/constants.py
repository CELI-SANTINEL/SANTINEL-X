# Protected by SPECTRA
import base64, marshal, zlib, os, sys
_EXP = "constants.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("0aa54875d2de20699b356d404fa1dcf490dc02bc79312bdd933b34516ca7b91c0f4070f421e93c54f26d841add6759cdef2c974883f839b64870607c5b728fbd")
_K2 = bytes.fromhex("9eb6c4a0aa63fc6e87aa24bf5d0eb2a02a132e7fc515da6dea24d64be62a0b8ffc9ad6ff7887dc2eda399626d8ffd98b0c7355bdda7e0a73be1d6f0c2e5c7c11")
_K3 = bytes.fromhex("f16e0abd18508bf5311ed08d7b3e6669f8d38c4ea03f6b570eabf1cc4e84b1f6d3ffa6c69afed9fdbc5c77dac7e7cbc3b0e31026f85ac676012a746282f19bac")
_S = """9j6ODt%6OpIUXD@SBC^8&La>Wa9M%;zND1wj_t(^DT!mL&-nOX{acOv6bDd=H_8tOFNO?bbnMLlu)q~`
9=DmeUoSpZsckUlla^Q-WrJGl<tsCS!k^x)_qO`jxf1ViTD_Y&`=G`-Jas9GT9l2!381fo6NLFA$oaT=
GaV-JlBH*{p1~@VxSU>iKqn&EHlH3wV-X3KzepG)FQ%r*nC@{mR|00AWuMDq*XfP}r!P6aM2(+WT{hP^
f~)eY?u(WYY5<78bKET|px%;_&+}g&^zq)(8S%;2Mrov*_Ufz%xaB{TevjLxFv|DZTqL(Ic&ed+Uh{wB
)&a63?0){%Qfs(s_T8lc8u(bzAl<!03nls8PzafH0pIOfxiCwwYti^Q(p5^c(zqC$F{tX%C)NuMl?(Z?
Tlr9V*5Wn}WwBU;r7HHA$h2sd?sy7&B^YvFUjW_txx~KTh@x&5DxOcrj$@BOV9@qahhEfi^QCMCSL-e}
Fm-p*22u>E@>$RL%e$S^D}sVy96)yS{Q>z<n475}DJlRQz}<i<i~DL-e;%`Yil=pa$f>~{3Uh_j9x|Oq
AHXNuxzfrJLdYdNuA?HW$##$i*|Eq-7J-XLPSRU5S8GRab~+Q%TbKo0l<vU3^m1o2qsl@Tm+jTqLUkHC
*=uSV)7GNF@u<;hdsiCM7^ZWd!ijs|M{m}ul~qvjKrhRvdYYfrA<r7gcj+bXENdN4jtNv59Kk#<wFThL
7|xr8BIcmtSBucH+Nhjcj4#v6oq?}YjJ9U6$*8gW%z(?qZk}`q2sw_j4DWp!4E^Fa$>-tYIZx>v#B6o%
%H1O;abNX0#SkpHq%u@e^?*UHG}xNN39}VCW~FU1>-nZd;zbK{PF*nc^J^2LLSS_FH~3jMuMz9UnuGP@
!wFnm*JE-6TqtkGGdaMwSbQVk=c4SswFFd7Cjo%YO;rk6!~8uKgCox>a9i9ko`pnEP6Ix{1RE;8<7h)r
`1lz6WpH5!VYaxfjg-9(d)w`!j~Oy?P!rq^(;p&)Ppsd`1|kiZo{eA79eF=sym+)t8liqD)$mo?a<Coe
pCEV?QuXOKaAAtYyx`zA6ff5i&$BwA1`mZen2FMPt63xq$Q5jv3b_fOp&K4w0f@1R^XX>maIfwr)F)z8
GD_F&E>GwG-z~riNBFMG#(LVP)&AGAR<UYJJcRDy8B<|Fa*yB4aN@EOsjsP3)7M?R8vu?%NINLKihh5-
wN_cAZ(}N<{<mkSA9Rh-h`mWg=E;niSqq`77QGCcy#MD`wSQ84Py?PK1MG-o5O>3-)ghfn4zG&0PKch5
noA{_`vMP^T5qNs6>00i1N?YvBfV!ocF#4{NcW)(hGBd}jI8aeeOyEJec-FGD1h4>-1=*J1&&uV;OQu1
LIiI#B;iF93n_@<zM7ljSn9G(z7}xUeMwgN;PD^&=*_QD^(Z6WylmHZE;a22I1+lpZW>l1v*zZ2dpYLB
2Yn;@2lb)jMo#M%#32wYBEi^yT{?-Xeh3Ye2pdAH^Q*WhEyk2H$(f4>t7qAEdXtl9Ey%D2>(2@&%aZcl
+M*(bn+6&vm!5Zibev1BG${_db!@q%N2GAk^HN>@_f?F`jO;p7Pyqsr&7+5vJ8N55zuFkxPFJ`OO+=if
W}zb0ZT&>`#vDhQs3b1%Uqa2aF?Csa)PbLnxX#PALfXFo3Sh!~DSPR(-IvUJRCh1_n*"""
_B = base64.b85decode(_S.replace("\n", "").encode("ascii"))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
_Z = zlib.decompress(_D3)
_C = marshal.loads(_Z)
exec(_C)

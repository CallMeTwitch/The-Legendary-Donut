if 1:
             A=B=0;from os\
         import *;u=lambda i,B\
       :(cos(i),cos(B),sin(B));\
     r=lambda i,j,A:(sin(i),cos(j \
  ),sin(A),sin(j),cos(A));from math \
  import*;q=lambda:0;exec((r"""def q(
 ):%sglobal A,B;b,z=[' ']*1760,[0]*176 
 0%sfor j in map(lambda x:x/100,range(
 0,628,7)):%"""+      r"""sfor i in map
(lambda x:x"""+        r"""/100,range(0
,628,2)):"""+            r"""%sc,d,e,f,
g=r(i,j,A)"""+          r""";h=d+2;D=1/
 (c*h*e+f*g"""+        r"""+5);l,m,n=u
 (i,B);t=c*h*g-f*e;x,y=int(40+30*D*(l*
 h*m-t*n)),int(12+15*D*(l*h*n+t*m));o=
  x+80*y;N=int(8*((f*e-c*d*g)*m-c*d*e
   -f*g-l*d*n))%sif 0<y<22 and 0<x<
     80 and z[o]<D:z[o],b[o]=D,'.,
       -~:;=!*$&@'[max(N,0)]%ssy 
         stem('cls');print('\n
             '.join([''.jo

in(b[k:(k + 80)])for k in range(0, 1761, 80)]));A+=0.0704;B+=0.0352;q()""").replace('\n','').replace('  ','')%('\n\t','\n\t','\n\t\t','\n\t\t\t','\n\t\t\t','\n\t'));q()

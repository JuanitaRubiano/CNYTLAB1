#Primer Laboratorio cnyt (2025-1)
#Estudiante Juanita Rubiano
#ID:1000095495

import math

#Suma de números complejos
def sumcplx (a,b):
    return((a[0]+b[0],a[1]+b[1]))

#Resta de números complejos
def restcplx (a,b):
    return (a[0]-b[0],a[1]-b[1])

#multiplicacion de compleujos
def multcplx(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

#conjudago
def conjcplx(a):
    cona= (a[0],-1 * a[1])
    return cona
#Division de números complejos
def divcplx(a,b):
    numerador= multcplx(a,conjcplx(b))
    denominador= multcplx(b,conjcplx(b))
    divreal= numerador[0]/denominador[0]
    divimg= numerador[1]/denominador[0]
    return(divreal,divimg)

# Modulo de numeros complejos
def modcplx(a):
    return((math.sqrt(((a[0]*a[0]+ a[1]*a[1])))))

#Pasar de  coordenadas cartesiana a polares
def coorpaspolarcplx(a):
    if(a[0]<0 and a[1]<0):
        fase= ((math.atan(a[1]/a[0]))+ math.pi)
    elif(a[0]<0 and a[1]>0):
        fase = ((math.atan(a[1] / a[0])) - math.pi)
    else:
        fase = (math.atan(a[1] / a[0]))

    return ((modcplx(a)),(fase))


#Pasar de  coordenadas polares a cartesianas
def coorpascartapolcplx(a):
    return((a[0]*math.cos(a[1]),a[0]*math.sin(a[1])))



def main():
    print(sumcplx((3.5,2.4),(5.1,2.2)))
    print(restcplx((3.1, 2.4), (5.6, 1.2)))
    print(multcplx((2,3),(4,-1)))
    print(conjcplx((1,-2.5)))
    print (divcplx((9,27),(3,9)))
    print(modcplx((-2,1)))
    print(coorpaspolarcplx((45,9.1)))
    print(coorpascartapolcplx((1.2,2)))


main()

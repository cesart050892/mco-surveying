import math
import numpy as np
from data import datos

a = 6378137.0
b = 6356752.314245

def calcN(a,b,phi):
    arriba = a**2
    abajo = (((a**2)*math.cos(phi)**2)+((b**2)*math.sin(phi)**2))**.5
    return arriba/abajo

def grados2rad(angulo):
    return angulo * math.pi/180

def conversiongeo2cart(phi,lam,h,a,b):
    phi = grados2rad(phi)
    lam = grados2rad(lam)
    N = calcN(a,b,phi)
    x =(N+h)* math.cos(phi)*math.cos(lam)
    y =(N+h)* math.cos(phi)*math.sin(lam)
    z =((N*(b**2/a**2))+h) * math.sin(phi)
    return x,y,z

def conversioncart2geo(x,y,z,a,b):
    Longitud =math.atan(y/x)
    Longitud = Longitud*180/math.pi-180
    e2= 1-(b**2/a**2)
    p= (x**2+y**2)**.5
    N_ =a
    h_ = (x**2+y**2+z**2)**.5-(a*b)**.5
    phi_ = math.atan((z/p)*(1-(e2*N_/(N_+h_)))**-1)
    condicion = True
    i = 0
    while condicion:
        Ni = a/(math.cos(phi_)**2+((b**2/a**2)*math.sin(phi_)**2))**.5
        hi = (p/math.cos(phi_))-Ni
        phii= math.atan((z/p)*(1-(e2*Ni/(Ni+hi)))**-1)
        condicion = (abs(hi-h_)>a*10e-20) and (abs(phii-phi_)>10e-20)
        h_ =hi
        phi_ = phii    
        i = i+1
    phi_ = phi_*180/math.pi
    return phi_,Longitud,h_

def gms2dec(grados,minutos,segundos):
    return grados+minutos/60+segundos/3600

def separar(numero):
    grados = numero[:2]
    minutos = numero[3:5]
    segundos = numero[5:7]+"."+numero[7:]
    return grados,minutos,segundos

def separar1(numero):
    grados = numero[:3]
    minutos = numero[4:6]
    segundos = numero[6:8]+"."+numero[8:]
    return grados,minutos,segundos

def dist2p(P1,P2):
    return ((P2[0]-P1[0])**2+(P2[1]-P1[1])**2+(P2[2]-P1[2])**2)**.5

def getXYZ(datos, indices, i):
    lat_g,lat_m,lat_s = separar(str(datos[i,indices[0]]))
    lat = gms2dec(float(lat_g),float(lat_m),float(lat_s))
    lon_g,lon_m,lon_s = separar1(str(datos[i,indices[1]]))
    lon = gms2dec(float(lon_g),float(lon_m),float(lon_s))
    h = datos[i,indices[2]]
    x,y,z = conversiongeo2cart(lat,lon,h,a,b)
    return np.asarray([x,y,z])

def getArrayData():
    data = []
    for i in range(len(datos)):
        PA = getXYZ(datos,[0,1,2],i)
        PB = getXYZ(datos,[3,4,5],i)

        dist_euclidiana = dist2p(PA,PB)
        dist_estacion = datos[i,6]
        diferencia = dist_euclidiana - dist_estacion
        nombre_pa= datos[i,7]
        nombre_pb=datos[i,8]

        renglon = [nombre_pa,nombre_pb,PA,PB,dist_euclidiana,dist_estacion,diferencia]
        data.append(renglon)
        
    npdata = np.asarray(data, dtype=object)
    return npdata
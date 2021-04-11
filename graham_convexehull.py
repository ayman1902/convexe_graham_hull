#algorithme de graham by belhaj ayman
#MPSI2 is the best
import matplotlib.pyplot as plt
import math as mt
import random as rd
def tri(l):
    n= len(l)
    for i in range(n-1):
        k=i
        for j in range(i+1,n):
            if l[j]<l[k]:
                k = j
        l[i],l[k]=l[k],l[i]
    return l
def tri_data_ind(data,p):
    n= len(data)
    for i in range(n-1):
        k=i
        for j in range(i+1,n):
            if data[j][p]<data[k][p]:
                k = j
        data[i],data[k]=data[k],data[i]
    return data
def angle_bet(cord1,cord2):
    if cord2[0]>=cord1[0]:
        if cord2[0]==cord1[0] and cord2[1]==cord1[1]:
            return 0
        elif cord2[1]==cord1[1]:
            return 0
        elif cord2[0]==cord1[0]:
            return mt.pi/2
        else:
            x = abs(cord2[1]-cord1[1])/abs(cord2[0]-cord1[0])
            return mt.atan(x)
    else:
        if cord2[0]==cord1[0]:
            return 0
        elif cord2[0]==cord1[0] and cord2[1]==cord1[1]:
            return 0
        elif cord2[1]==cord1[1]:
            return mt.pi
        else:
            x = abs(cord2[0]-cord1[0])/abs(cord2[1]-cord1[1])
            return mt.atan(x)+mt.pi/2
def produit_vector(cor_i,cor1,cor2):
    return (cor1[0]-cor_i[0])*(cor2[1]-cor_i[1])-(cor2[0]-cor_i[0])*(cor1[1]-cor_i[1])
def clocking_wise(cor_i,cor1,cor2):
    if produit_vector(cor_i,cor1,cor2)>=0:
        return 1
    else:
        return 0
def tren_arr_ind(data,j):
    return [data[i][j] for i in range(0,len(data))]
def lowest_pnt_y(data):
    return data[tren_arr_ind(data,1).index(tri(tren_arr_ind(data,1))[0])] 
def reguler_data(cor,data):
    array = []
    for dat in data:
        if dat[0]!=cor[0] and dat[1]!=cor[1]:
            array.append(dat)
    return array
def sorting_ang(data):
    cor_i = lowest_pnt_y(data)
    angles_data=[[angle_bet(cor_i,cor),cor] for cor in data]
    data_sort=tri_data_ind(angles_data,0)
    return [data[1] for data in data_sort]
def main(data):
    lowest_pnt=lowest_pnt_y(data)
    array_sort_ang=sorting_ang(data)
    array_sort_ang.append(lowest_pnt)
    array_sort_ang.append(array_sort_ang[1])
    array_sort_ang.append(array_sort_ang[2])
    min_connexe_hull=[]
    convexe_hull=[]
    convexe_hull.append(array_sort_ang[0])
    convexe_hull.append(array_sort_ang[1])
    i=1
    while i <= len(array_sort_ang)-2:
        while clocking_wise(convexe_hull[len(convexe_hull)-2],convexe_hull[len(convexe_hull)-1],array_sort_ang[i])==0:
            convexe_hull.pop(len(convexe_hull)-1)
        convexe_hull.append(array_sort_ang[i])
        i+=1
    return array_sort_ang,convexe_hull
def shwing(data):
    x0=tren_arr_ind(data,0)
    y0=tren_arr_ind(data,1)
    x2=tren_arr_ind(main(data)[1],0)
    y2=tren_arr_ind(main(data)[1],1)
    plt.plot(x2,y2,label='enveloppe convexe')
    plt.plot(x0,y0,'ro',label='points')
    plt.title("enveloppe convexe algorithme de graham")
    plt.legend()
    plt.axhline(color = 'k')
    plt.axvline(color = 'k')
    plt.show()
def create_random_data(mini,maxi,point):
    return [(rd.uniform(mini,maxi),rd.uniform(mini,maxi)) for i in range(point+1)]
#main(create_random_data(-1,1,20))
shwing(create_random_data(-1,1,50))
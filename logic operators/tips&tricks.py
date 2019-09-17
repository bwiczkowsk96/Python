v1=126
v2='126'
v3=126.0
v4='126.0'

print(type(v1))
print(type(v2))
print(type(v3))
print(type(v4))

print(type(v1+v3))
print(type(v2+v4))

print(7-1*0+3+3)

print(4**5//2**3)

print(99+9/9)


q="THE EYES"
print(q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7])


q="a gentleman"
print(q[3],q[6],q[7],q[2],q[0],q[4],q[5],q[1],q[8])

q="THE MORSE CODE"
print(q[1:3],q[6],q[8],q[3],q[10:12],q[4],q[13],q[9],q[12],q[5],q[0],q[7])

print(q[1:3]+q[6]+q[8]+q[3]+q[10:12]+q[4]+q[13]+q[9]+q[12]+q[5]+q[0]+q[7])

line='Program "Kropka nad i" nadamy o: 22:00'
time = line[ line.find(':')+2 : ]
print(time)

tmp=line[line.find('"')+1:]
print(tmp)

title=tmp[tmp.find('"')]
print(title,time)


line = 'Program "Kropka nad i" nadamy o: 22:00'



time = line[ line.find(':')+2 : ]

print(time)



tmp = line[ line.find('"')+1: ]

title = tmp [ : tmp.find('"')]

print(title, time)


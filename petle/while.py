firstRow = 1
lastRow = 31

currentRow = firstRow

while currentRow <= lastRow:
    print ('Row number',currentRow)
    currentRow+=1
else:
    print('Now row number is',currentRow)



i = 1
imax=13

liczba = i

while liczba<=imax:
    print('Kwadrat liczby',liczba,'to',liczba**2, ' Sześcian liczby',liczba, 'to',liczba**3)
    liczba+=1



d=0
dmax = 16

x=d

while x<=dmax:
    print(x,2**x)
    x+=1



start = 1
end = 10

wzor = start

while wzor<=end:
    print(wzor*'x')
    wzor+=1
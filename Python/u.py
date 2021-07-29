def printName(f,l,i):
    if i :
        print(f[0]+'.'+l[0]+'.')
    else:
        print(f,l)

printName('Tarun' , 'Kumar' , False)
printName('Tarun' , 'Kumar' , True)
printName(l='Kumar' , i=True , f='Tarun')

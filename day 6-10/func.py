##def sq(x):
##    x=pow(x,2)
##    return x
##
##a=int(input())
##c=sq(a)
##print(c)
##:no input no output
##def myfun():
##    print('this is fun')
##
##myfun()
##
##no input with output
##def outp():
##    a=int(input('enter a value: '))
##    return a
##
##c=outp()
##print('c is equal to=',c)
##
## with input no output
##def inpu(x):
##    x=x**2
##    print(x)
##a=int(input())
##inpu(a)
##
##
## with input with output:
##def sq(x):
##    x=pow(x,2)
##    return x
##
##a=int(input())
##print(sq(a))
##
##
##def a():
##    return 'abc'
##
##a()
##
##
##taking multiple input and returning multiple outputs
##
##def multi(x,y,z):
##    a=x
##    b=y
##    c=z
##    return a,b,c
##
##print(multi(5,6,7))
##
##def third(x):
##    print('hello')
##third(1)
##
##def four(a):
##    return a*10
##print(four(5))
##
##
##def new(x):
##    print('''hi
##hello
##hw r u?''')
##    return x*10
##
##print(new(5))
##
##
##
##def fourth(x):
##    print('hi')
##    return x
##    print('hello world')
##
##print(fourth(4))
##
##def multi(x,y,z):
##    a=x
##    b=y
##    c=z
##    v={a:b}
##    return v.keys()
##
##print(multi(5,6,7))
##
##def multiin(x,y,z):
##    return x+y+z
##print(multiin(1,2,3))
##def multi(x,y,z):
##    a=x
##    b=y
##    c=z
##    return a,b,c
##
##print(multi(5,6,7))
##
##
##def six(x,y,z=1):
##    return x+y+z
##print(six(3,4))
##    
##
##def eight(*x):
##    return x
##print(eight(8,2,3,4))
##
##def nine(**x):
##    return x
##print(nine(name=('vipul','bipul'),email='vipul@gmail.com'))
##print(nine(n1=0,n2=[11,12,14], n3=['ab','xy']))
##
##
##def set(x):
##
##    print('''happy birthday to you
##happy birth day to you
##happy brthday dear''',x)
##
##set(input('enter your name: '))
##
##
##def birthday(name):
##    print(f'''Happy Birthday to you
##Happy Birthday to you
##Happy Birthday to dear {name}
##Happy Birthday to you''')
##    
##birthday(input('enter your name: '))

##def shadi(name1,name2):
##    print(f'''magalam bhagwan vishnu
##magalam trunadhawaja
##magalam pundri kakshat
##manglaya tanohari
##now i pronounce {name1} as husband of {name2}''')
##
##shadi('yash','deepika')
myadd=lambda x,y,z: x+y+z
print(myadd(5,9,7))



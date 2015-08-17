def h(n,f,t,s):
    if n>0:
     h(n-1,f,s,t)
     print f,t
     h(n-1,s,t,f)
h(3,'a','c','b')

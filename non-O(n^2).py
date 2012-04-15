def evaluate(lelist, m):
    lelist.sort()
    i=0
    while i<len(lelist):
        if(lelist[0]+lelist[len(lelist)-1]<m):
            del lelist[0]
        elif(lelist[0]+lelist[len(lelist)-1]>m):
            del lelist[-1]
        elif(lelist[0]+lelist[len(lelist)-1]==m):
            return True
        elif(not lelist):
            return False
    i=i+1

for m in range(34):
    iterable = [1,2,3,5,7,10,19,23,30]
    print(iterable)
    if(evaluate(iterable, m)):
        print("It's possible to add numbers to get "+str(m))
    else:
        print("It's impossible to add numbers to get "+str(m))

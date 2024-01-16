def sum(list):
    sum=0
    for num in list:
        sum += num
        
    return sum
def multi(list):
    multi=1
    for num in list:
        multi *= num
    return multi
list=[1,2,3,4]
l = multi(list)    
s = sum(list)
print(s)
print(l)
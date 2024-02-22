a = int(input())
l = int(input())
p = int(input())
h = int(input()) 
diamantes1 = (a + l+ (abs(a - l)))/2
diamantes2 = (diamantes1 + p+ (abs(diamantes1 - p)))/2
r = diamantes2 * h
re = int(r)
print(re)



# bit wise operators

a=2
b=4

#AND
print(a&b) # prints 0 because 0&0==0, 0&1==0, 1&0==0, 1&1==1

#OR
print(a|b)  # prints 6 because 0|0==0, 0|1==1, 1|0==1, 1&1==1

#XOR
print(a^b)  #print 6 because 0^0==0, 0^1==1, 1^0==1, 1^1==0 becausein XOR the values must be different and if they are same it wilol return 0

#left shift
print(b<<2) # print 16 becasuse b<<2==b*(2**2)

#right shift
print(b>>2) # print 1 because b>>2==b/(2**2)
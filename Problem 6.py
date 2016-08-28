max = 100
SquaresSum = 0
Sum =0

for i in range(max+1):
    SquaresSum += i*i
    Sum +=i
    
SumSquared= Sum*Sum  
  

print (SumSquared - SquaresSum)

#Define the value k which in this case it determines how many pairs will be created with each breed of adult bunnies (Mr bunny)
k = 2
#Python already has a function for the fibonacci Sequence where first you have to define your value of months "n"
def fib(n):
    #Even though its confusing that F1=F2=1 when seing the picture we can prove that in the initial month 0 there aren't any bunnies so this is our initial data
    ni = 0
    n1 = 1
    #a only represents a value in the given range which is the month we are selecting for our iteration
    for a in range(n):
        #Here we include the starting values and how we will be replacing them to continue with the sequence
        #First the value for each new iteration were the ni value (oldest bunny) will have k litters and you add the adult bunnies in existence
            nth = (ni * k) + n1
            #This means that now the initial value will be de last resulting value 0 -> 1 -> 2 , etc.
            ni = n1
            #The adding value will be the one showed above
            n1 = nth
            print(ni)
fib(33)
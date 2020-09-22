import math


def mac(x, es, maxit):
    iter = 1
    sol =1
    ea = 100

    #CALCULO ITERATIVO 
    while(1):
        solold = sol
        sol = sol + (sol**iter) / math.factorial(iter)
        iter += 1

        if sol == 0:
            ea =abs((sol-solold)/sol)*100
        if ea <= es or iter >= maxit:
            break
    sol

print(mac(0.5, 0.05, 7))
    
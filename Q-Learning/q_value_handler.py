import time

def calculate_new_Q(Q,max):
    #Q+=  alpha[r + (beta.max)-Q]





    alpha = .75
    gamma = .85

    #betamax = beta.max
    betamax = gamma*max
    r = (-.04)
    # betamaxQ = (beta.max)-Q
    betamaxQ = betamax - Q
    # maxandr = r + (beta.max)-Q
    maxandr = (r) + betamaxQ
    # alphamax = alpha[r + (beta.max)-Q]
    alphamax = maxandr * alpha

    Q += alphamax

    return Q


#def find_max(position,env):

import numpy as np
islandpop = 25
susceptible = []
infected = []
recovered = []
for i in range(islandpop):
    susceptible.append(i)
#random seed
np.random.seed(2022)
#function to select anyone from the list but themselves
def randint_notitself(m,islandpop):
    ans = np.random.randint(0,islandpop)
    #while loop handles the case where we generate our own index
    while ans == m:
        ans = np.random.randint(0,islandpop)
    return ans
infected.append(0)
susceptible.remove(0)
ans = randint_notitself(0,islandpop)
def next_step(pop,sus,inf,rec):
    x = inf.copy()
    for i in x:
        ans = randint_notitself(i,pop)
        #case where the rumor-spreader tells someone who has already heard rumor
        if (ans in inf) or (ans in rec):
            inf.remove(i)
            rec.append(i)
        #other case
        else:
            sus.remove(ans)
            inf.append(ans)
    return sus, inf, rec

susceptible, infected, recovered = next_step(islandpop,susceptible,infected,recovered)
def sim_end(pop,sus,inf,rec):
    #first case: everyone in island is infected or recovered
    if len(sus) == 0:
        return -1
    #case where no one is infected anymore
    elif len(inf) == 0:
        return 1
    #not done
    else:
        return 0

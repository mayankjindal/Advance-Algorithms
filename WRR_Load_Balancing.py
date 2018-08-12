# Weighted Round Robin Load Balancing Algorithm

def load_assignment(mach, task):
    soln = {}
    for i in range(0, len(mach)):
        soln[str(i)] = []
    mach = mach.copy()
    task = task.copy()
    load = [0]*len(mach)
    k, i = 0, 0
    while i < len(task):
        for j in range(0, mach[k]):
            soln[str(k)].append(i)
            load[k] += task[i]
            i += 1
            if i == (len(task)):
                break
        if k < (len(mach) - 1) :
            k += 1
        else:
            k = 0

    return soln, load


m = 10
n = 100
machines = [0] * m
tasks = [1] * n
machines[0] = 3
machines[1] = 4
machines[2] = 6
machines[3] = 1
machines[4] = 2
machines[5] = 12
machines[6] = 1
machines[7] = 8
machines[8] = 7
machines[9] = 9

soln, load = load_assignment(machines, tasks)

print(load)
print("maxspan = ", max(load))
for key in sorted(soln):
    print(key, " : ", soln[key])
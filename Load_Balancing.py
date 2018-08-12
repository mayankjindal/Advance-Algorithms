# Load Balancing
# Three variants are used : Without Sorting, With Sorting, With Pairing

from random import randint

def without_sorting(mach, task):
    soln = {}
    mach = mach.copy()
    task = task.copy()
    for i in range(0, len(mach)):
        mach[i] += task[i]
        soln[str(i)] = [i]
    for j in range(len(mach), len(task)):
        least = mach.index(min(mach))  # Index of the minimum value in list mach
        mach[least] += task[j]
        soln[str(least)].append(j)

    return mach


def with_sorting(mach, task):
    soln = {}
    mach = mach.copy()
    task = task.copy()
    task.sort(reverse=True)
    for i in range(0, len(mach)):
        mach[i] += task[i]
        soln[str(i)] = [i]

    for j in range(len(mach), len(task)):
        least = mach.index(min(mach))  # Index of the minimum value in list mach
        mach[least] += task[j]
        soln[str(least)].append(j)
    return mach


def pairing(mach, task):
    soln = {}
    mach = mach.copy()
    task = task.copy()
    task.sort(reverse=True)
    s = len(task)
    paired_jobs = []
    for i in range(0, s // 2):
        paired_jobs.append(task[i] + task[s - 1 - i])
    for j in range(0, len(paired_jobs)):
        least = mach.index(min(mach))  # Index of the minimum value in list mach
        mach[least] += paired_jobs[j]
        if str(least) in soln.keys():
            soln[str(least)].append(j)
        else:
            soln[str(least)] = [i]

    return mach


m = 2
n = 6
machines = [0] * m
tasks = [40, 39, 38, 37, 2, 1]
#for i in range(0, n):
 #   tasks.append(randint(0, 1000))


# Use the commented code to take values from the user
'''
m = int(input("Total number of machines: "))
n = int(input("Total number of tasks: "))
machines = [0] * m
tasks = [0] * n
for i in range(0, n):
    tasks[i] = int(input("Enter Load: ")) 
'''

non_sort_load = without_sorting(machines, tasks)
sort_load = with_sorting(machines, tasks)
paired_load = pairing(machines, tasks)


print("Solution without sorting")
print(non_sort_load)
print("makespan = ", max(non_sort_load))

print("Solution with sorting")
print(sort_load)
print("makespan = ", max(sort_load))

print("Solution with pairing")
print(paired_load)
print("makespan = ", max(paired_load))


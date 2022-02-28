import sys
import time
import matplotlib.pyplot as plt

tm = []
memory = []

i = 10
k = 0
while i <= 10**5:
    dt = {}
    t = time.perf_counter_ns()
    for j in range(i):
        dt[j] = j
    tm.append((i, (time.perf_counter_ns() - t) / 1000))
    memory.append((i, sys.getsizeof(dt)))
    i *= 10

x = []
y = []

for i in (tm):
    x.append(i[0])
    y.append(i[1])

plt.plot(x, y)
plt.xlabel('Number of elements')
plt.ylabel('Time in ms')

plt.title('Time for dict')
plt.show()

for i in (memory):
    x.append(i[0])
    y.append(i[1])

plt.plot(x, y)
plt.xlabel('Number of elements')
plt.ylabel('Memory')

plt.title('Memory for dict')
plt.show()

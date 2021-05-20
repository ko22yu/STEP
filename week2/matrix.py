import numpy, sys, time
import matplotlib.pyplot as plt


def dot(n):  # calculate C = A * B
    # print(a)
    # print(b)
    for i in range(n):  # 行
        for j in range(n):  # 列
            x = 0
            for k in range(n):
                x += a[i, k] * b[k, j]
            c[i, j] = x
    # print(c)


if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

sizes = []
times = []
n = int(sys.argv[1])
for k in range(2, n+1, 100):
    a = numpy.zeros((k, k)) # Matrix A
    b = numpy.zeros((k, k)) # Matrix B
    c = numpy.zeros((k, k)) # Matrix C

    # Initialize the matrices to some values.
    for i in range(k):
        for j in range(k):
            a[i, j] = i * k + j
            b[i, j] = j * k + i
            c[i, j] = 0

    begin = time.time()
    dot(k)  # 行列積の計算
    end = time.time()
    print(k, "time: %.6f sec" % (end - begin))
    sizes.append(k)
    times.append(end - begin)

# グラフの表示
plt.plot(sizes, times, label = "time[sec]")
plt.legend()
plt.title("relationship between N and execution time")
plt.xlabel("matrix size")
plt.ylabel("execution time")
plt.grid(True)
plt.show()

max = 300
ta = []
tb = []
tc = []
td = []
te = []
tf = []
tg = []
th = []
ti = []
tj = []
tk = []
tl = []
tm = []

for i in range(1, max):
    ta.append(-1)
    tb.append(-1)
    tc.append(-1)
    td.append(-1)
    te.append(-1)
    tf.append(-1)
    tg.append(-1)
    th.append(-1)
    ti.append(-1)
    tj.append(-1)
    tk.append(-1)
    tl.append(-1)
    tm.append(-1)


def a(n):
    global ta
    if ta[n] < 0:
        if n == 1:
            ki = 1
        elif n == 2:
            ki = 13
        else:
            ki = a(n - 1) + a(n - 2) + 2 * b(n - 1) + 2 * c(n - 1) + d(n - 1) + e(n - 1) + 2 * f(n - 1) + g(
                n - 1) + 2 * h(n - 1)
        ta[n] = ki;
    else:
        ki = ta[n]
    return ki


def b(n):
    global tb
    if tb[n] < 0:
        if n == 1:
            ki = 1
        elif n == 2:
            ki = 5
        else:
            ki = a(n - 1) + b(n - 1) + c(n - 1) + e(n - 1) + f(n - 1)
        tb[n] = ki;
    else:
        ki = tb[n]
    return ki


def c(n):
    global tc
    if tc[n] < 0:
        if n == 1:
            ki = 1
        elif n == 2:
            ki = 2
        else:
            ki = a(n - 1) + b(n - 1) + i(n - 1) + j(n - 1)
        tc[n] = ki;
    else:
        ki = tc[n]
    return ki


def d(n):
    global td
    if td[n] < 0:
        if n == 1:
            ki = 1
        elif n == 2:
            ki = 1
        else:
            ki = a(n - 1) + 2 * i(n - 1) + k(n - 1) + m(n - 1)
        td[n] = ki;
    else:
        ki = td[n]
    return ki


def e(n):
    global te
    if te[n] < 0:
        if n == 1:
            ki = 1
        elif n == 2:
            ki = 4
        else:
            ki = a(n - 1) + 2 * b(n - 1) + g(n - 1)
        te[n] = ki;
    else:
        ki = te[n]
    return ki


def f(n):
    global tf
    if tf[n] < 0:
        if n == 1:
            ki = 1
        elif n == 2:
            ki = 2
        else:
            ki = a(n - 1) + b(n - 1)
        tf[n] = ki;
    else:
        ki = tf[n]
    return ki


def g(n):
    global tg
    if tg[n] < 0:
        if n == 1:
            ki = 1
        elif n == 2:
            ki = 2
        else:
            ki = a(n - 1) + e(n - 1)
        tg[n] = ki;
    else:
        ki = tg[n]
    return ki


def h(n):
    global th
    if th[n] < 0:
        if n == 1:
            ki = 1
        elif n == 2:
            ki = 1
        else:
            ki = a(n - 1) + i(n - 1)
        th[n] = ki;
    else:
        ki = th[n]
    return ki


def i(n):
    global ti
    if ti[n] < 0:
        if n == 1:
            ki = 1
        elif n == 2:
            ki = 3
        else:
            ki = c(n - 1) + d(n - 1) + h(n - 1)
        ti[n] = ki;
    else:
        ki = ti[n]
    return ki


def j(n):
    global tj
    if tj[n] < 0:
        if n == 1:
            ki = 0
        elif n == 2:
            ki = 1
        else:
            ki = c(n - 1)
        tj[n] = ki;
    else:
        ki = tj[n]
    return ki


def k(n):
    global tk
    if tk[n] < 0:
        if n == 1:
            ki = 0
        elif n == 2:
            ki = 1
        else:
            ki = d(n - 1) + l(n - 1)
        tk[n] = ki;
    else:
        ki = tk[n]
    return ki


def l(n):
    global tl
    if tl[n] < 0:
        if n == 1:
            ki = 0
        elif n == 2:
            ki = 0
        else:
            ki = k(n - 1)
        tl[n] = ki;
    else:
        ki = tl[n]
    return ki


def m(n):
    global tm
    if tm[n] < 0:
        if n == 1:
            ki = 0
        elif n == 2:
            ki = 1
        else:
            ki = d(n - 1)
        tm[n] = ki;
    else:
        ki = tm[n]
    return ki


"""for i in range(1, max-1):
    print(i, a(i), sep =": ")"""
print("Kiírja egy 6*n-es járda 2*1-es dominókkal történő lekövezési lehetőségeinek számát.")
q = 300
while q >=298:
    q = int(input("(n<=298):n="))
print(a(q))

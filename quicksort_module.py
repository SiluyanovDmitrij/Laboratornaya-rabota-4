def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        p = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < p:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        f_p = quicksort(x[:i])
        s_p = quicksort(x[i + 1:])
        f_p.append(x[i])
        return f_p + s_p

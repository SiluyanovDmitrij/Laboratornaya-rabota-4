def rascheska(t):
        step = int(len(t)/1.247)
        s = 1
        while step > 1 or s > 0:
            i = 0
            s = 0
            while i + step < len(t):
                if t[i] > t[i + step]:
                    t[i], t[i + step] = t[i + step], t[i]
                    s += 1
                i = i + 1
            if step > 1:
                step = int(step/1.247)
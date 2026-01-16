def calbaselog(base,n):
        p = 0
        ctn = True
        step = 0.1
        while ctn:
            if base ** (p + step) <= n:
                p = p + step
            else:
                step = step / 10
                if step < 1e-6:
                    ctn = False

        print(f"Log{base}({n}) is {p:.6f}")  
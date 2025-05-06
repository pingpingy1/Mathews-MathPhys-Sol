EPS: float = 1e-9


def cont_frac(x: float, n: int) -> float:
    res: float = 2 * n * n * x
    for i in range(n - 1, 1, -1):
        res = 2 * i * i * x - 1 / res
    return res


def find_tolerable_n() -> int:
    n: int = 2
    prev: float = cont_frac(EPS, n)
    while True:
        n += 1
        curr: float = cont_frac(EPS, n)
        ##        if n % 1000 == 0:
        ##            print(f"{n} {abs(curr - prev)}")
        if abs(curr - prev) < EPS:
            break
        prev = curr
    return n


def find_root(n: int, l: float, r: float) -> float:
    l_val: float = cont_frac(l, n)
    r_val: float = cont_frac(r, n)
    assert l_val * r_val < 0

    mid: float = (l + r) / 2
    mid_val: float = cont_frac(mid, n)
    if abs(mid_val) < 0:
        return mid
    if l_val * mid_val < 0:
        return find_root(n, l, mid)
    return find_root(n, mid, r)


if __name__ == "__main__":
    n: int = find_tolerable_n()
    print(n)
    x = find_root(n, EPS, 1)
    print(f"{x} {cont_frac(x, n)}")

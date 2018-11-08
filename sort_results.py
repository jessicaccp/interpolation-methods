def sort_results(x1, x2):
    x1, x2 = (list(t) for t in zip(*sorted(zip(x1, x2))))
    return x1, x2
while True:
    n, m = map(int, input().split())
    if n < m:
        print(['neither', 'factor'][m%n == 0])
    elif n > m:
        print(['neither', 'multiple'][n%m == 0])
    elif n == 0 and m == 0:
        break

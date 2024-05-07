v = [*map(lambda x: sum(map(int,x.split('+'))), input().split('-'))]
print(v[0] - sum(v[1:]))
# ex 5
rivers = {'loire':'france',
        'rhin':'allemagne',
        'dniepr':'ukraine'}
for river in rivers:
    print(f"{river.title()} se situe en {rivers[river].title()}")
    print(river.title())
    print(rivers[river].title())
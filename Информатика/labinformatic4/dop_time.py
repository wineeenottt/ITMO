import time

start_time = time.perf_counter()
for i in range(100):
    import required
end_time = time.perf_counter()
r = end_time - start_time
print(f'Обязательное задание - {r}')

start_time = time.perf_counter()
for i in range(100):
    import dop_lib
end_time = time.perf_counter()
r = end_time - start_time
print(f'Доп. задание 1 - {r}')

start_time = time.perf_counter()
for i in range(100):
    import dop_reg
end_time = time.perf_counter()
r = end_time - start_time
print(f'Доп. задание 2 - {r}')

start_time = time.perf_counter()
for i in range(100):
    import dop_formal
end_time = time.perf_counter()
r = end_time - start_time
print(f'Доп. задание 3 - {r}')

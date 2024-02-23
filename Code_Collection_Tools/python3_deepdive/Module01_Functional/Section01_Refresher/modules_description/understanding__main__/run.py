# print(f'loading file: __nam__: {__name__}')

# import module1
import timing

code = '[x**2 for x in range(1_100)]'

result = timing.timeit(code, 100)
print(result)
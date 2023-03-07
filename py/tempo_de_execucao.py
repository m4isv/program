
import timeit


x='\n'.join([str(x) for x in range(999)])

print(timeit.timeit(x))


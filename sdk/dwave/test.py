import dwave
from dwave import samplers

print(dir(dwave))
print(dir(samplers))

assert hasattr(dwave.samplers, 'ASampler')
assert hasattr(samplers, 'ASampler')

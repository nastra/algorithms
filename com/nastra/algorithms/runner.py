'''
Created on Jan 29, 2013

@author: nastra
'''
import random
import com.nastra.algorithms.sampler

maxRange = 1000000
container = [random.randint(0, 1000) for i in range(0, maxRange)]
i = 0
sampler = com.nastra.algorithms.sampler.Sampler()
# print(container)
for s in container:
    # index = random.randint(0, maxRange)  # pick a randomly chosen sample from the list
    sampler.sample(s)
    i += 1
    if i % int(100):
        print(sampler.samples)


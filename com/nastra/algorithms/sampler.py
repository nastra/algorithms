'''
Implements the random reservoir sampling algorithm of Vitter. Reservoir Sampling is an algorithm 
designed to take K samples from a stream of samples of unknown size in linear time. 

This is a solution to the following interview question:
"You have a stream of infinite queries (ie: real time Google search queries that people are entering). 
Describe how you would go about finding a good estimate of 1000 samples from this never ending set of 
data and then write code for it."

The first K arriving samples are all stored in a reservoir of size 'maxSamples'. Afterwards we randomly 
decide whether a newly arriving sample is going to be added to the reservoir or not.
Having e.g. maxSamples = 1000, we would store the first 1000 arriving samples (first K samples)
in the reservoir with a probability of 1 (due to K/K = 1). Now the K+1 arriving sample has a probability 
of appearing in one particular output slot of 0.999 (due to K/(K+1)). 
Since there are K potential output slots, there is K/(K+i) chance of it being in the output 
and i/(K+i) chance that it wont be.

@author: nastra - Eduard Tudenhoefner
'''
from random import randint

class Sampler:
    def __init__(self, maxSamples=30):  # maxSamples set to 30 by default for better console output
        self.samples = []
        self.counter = 0
        self.maxSamples = maxSamples

    def sample(self, sample):
        '''  '''
        
        if(self.counter < self.maxSamples):
            self.samples.append(sample)
        else:
            index = randint(0, self.counter)
            if(index < self.maxSamples):
                self.samples[index] = sample
                
        self.counter = self.counter + 1
    
    
    

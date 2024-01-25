from dimod.generators import and_gate
from dimod import ExactSolver
bqm = and_gate('in1', 'in2', 'out')
sampler = ExactSolver()
sampleset = sampler.sample(bqm)
print(sampleset)
print(sampleset.first())

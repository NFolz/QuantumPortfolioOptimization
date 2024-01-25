from dimod.generators import and_gate
bqm = and_gate('in1', 'in2', 'out')

from dwave.system import DWaveSampler, EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm, num_reads=1000)
print(sampleset)   
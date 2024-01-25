from dwave.system import DWaveSampler, EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())

linear = {('a', 'a'): -1, ('b', 'b'): -1, ('c', 'c'): -1}
quadratic = {('a', 'b'): 2, ('b', 'c'): 2, ('a', 'c'): 2}
Q = {**linear, **quadratic}

sampleset = sampler.sample_qubo(Q, num_reads=5000)


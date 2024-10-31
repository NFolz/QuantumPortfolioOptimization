from dimod.generators import and_gate
from dimod import ExactSolver
import pandas as pd
bqm = and_gate('in1', 'in2', 'out')
sampler = ExactSolver()
sampleset = sampler.sample(bqm)

data = sampleset.record.tolist()  # Convert the record to a list of tuples
df = pd.DataFrame(data, columns=['sample', 'energy', 'num_occurrences'])

# Display the DataFrame
print(df)

# Assuming df is your DataFrame



def findMaxNum_Occurences(first_sample):
    max =0
    # first_sample = df.iloc['energy']
    for index, row in first_sample.iterrows():
        occ_value = row['num_occurrences']
        # print(energy_value)
        if occ_value>= max:
            max=occ_value

    return max

def findMinEnergy(first_sample):
    min =0
    # first_sample = df.iloc['energy']
    for index, row in first_sample.iterrows():
        energy_value = row['energy']
        # print(energy_value)
        if energy_value<= min:
            min=energy_value

    return min
print(findMaxNum_Occurences(df))
print(findMinEnergy(df))

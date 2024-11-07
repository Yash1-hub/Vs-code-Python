import numpy as np
np.random.seed(42)

puppies = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

p = puppies.mean()
print("Mean", p)
print("Standered Deviation", puppies.std())
print("Varience" , puppies.var())

np.random.choice(puppies, size=(1,5), replace = True)
np.random.choice(puppies, size=(1,5), replace = True).mean()

print("\nSampling Distributions with size 5 \n")
sample_props = []

for i in range(10000):
    sample = np.random.choice(puppies, 5, replace = True)
    sample_props.append(sample.mean())
sample_props = np.array(sample_props)

sm = sample_props.mean()
print("Mean", sample_props.mean())
print("Standard Deviation", sample_props.std())
print("Variance", sample_props.var())

print("\nSampleing Distribution with size 20 \n")

t_s_w = []

for i in range(10000):
    sample = np.random.choice(puppies, 20, replace=True)
    t_s_w.append(sample.mean())

t_s_w = np.array(t_s_w)

print("New Mean", t_s_w.mean())
print("New Standard Deviation", t_s_w.std())
print("New Variance", t_s_w.var())
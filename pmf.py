import numpy as np
from scipy.stats import poisson

lambda_expected = 10
days_total = 30 

prob_12_or_more = 1 - poisson.cdf(11, lambda_expected)

prob_between_12_and_18 = poisson.cdf(18, lambda_expected) - poisson.cdf(11, lambda_expected)

print(f"Probability of observing 12 or more days of rain: {prob_12_or_more:.4f}")
print(f"Probability of observing between 12 and 18 days of rain: {prob_between_12_and_18:.4f}")

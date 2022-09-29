## FreeCodeCamp Project 1
## Mean-Variance-Standard Deviation Calculator

import numpy as np

def calculate(x):
    if len(x) != 9:
        raise ValueError("List must contain nine numbers")
    else:
        y = np.asarray(x)
        y = np.reshape(y, (3,3))

        results = {}

        mean = [np.mean(y, axis=0).tolist(), np.mean(y, axis=1).tolist(), np.mean(y).tolist()]
        results["mean"] = mean

        var = [np.var(y, axis=0).tolist(), np.var(y, axis=1).tolist(), np.var(y).tolist()]
        results["variance"] = var

        std = [np.std(y, axis=0).tolist(), np.std(y, axis=1).tolist(), np.std(y).tolist()]
        results["standard deviation"] = std

        max = [np.max(y, axis=0).tolist(), np.max(y, axis=1).tolist(), np.max(y).tolist()]
        results["max"] = max

        min = [np.min(y, axis=0).tolist(), np.min(y, axis=1).tolist(), np.min(y).tolist()]
        results["min"] = min

        sum = [np.sum(y, axis=0).tolist(), np.sum(y, axis=1).tolist(), np.sum(y).tolist()]
        results["sum"] = sum

        return(results)


x = [9,1,5,3,3,3,2,9,0]

results = calculate(x)

print(results)
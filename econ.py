# This will be for testing the econ simulation.
# I'm thinking about having a finite pool of resources at the beginning
# and then things can be created but take time.
# E.g., maybe a kingdom has 1000 arrows. They can reliably make 100/day, but they might go through
# 500 in a siege, so if they get attacked in the field and in a stronghold, they would have to
# choose how to divy up their arrows (assuming they were close enough for that to be an option).

# Going to read about how to do this plausibly.

import matplotlib.pyplot as plt
import numpy as np

# Equation taken from first youtube vid that popped up: https://www.youtube.com/watch?v=9n-xMt-Sj3
def demand(price: int) -> int:
    return 180 - 25 * price 

def supply(price: int) -> int:
    return (-1)*40 + 30 * price


# Price data
price_data = np.linspace(0, 50, 100)


# For plots
demand_curve = demand(price_data)
supply_curve = supply(price_data)


plt.figure()
plt.plot(demand_curve, price_data, color='r')
plt.plot(supply_curve, price_data, color='b')

plt.show()

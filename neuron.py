import random
import matplotlib.pyplot as plt

# simulation parameters
T = 200                 # total time steps
dt = 1.0                # time step size

# neuron parameters
V = 0.0                 # current membrane potential
V_history = []          # store V over time
spikes = []             # spike history (0 or 1)

V_threshold = 1.0       # spike threshold
V_reset = 0.0           # reset potential after spike
tau = 20.0              # leak time constant (controls decay speed)

# input parameters
p = 0.2                 # probability of input impulse at each step
input_strength = 0.5    # how much each impulse increases V

# simulation loop
for t in range(T):
    # generate random input (Bernoulli process)
    if random.random() < p:
        I = input_strength
    else:
        I = 0.0

    # proportional leak (depends on current V)
    leak = V / tau

    # update membrane potential
    V = V + I - leak

    # check for spike
    if V > V_threshold:
        spikes.append(1)
        V = V_reset  # reset after spike
    else:
        spikes.append(0)

    V_history.append(V)

# visualization
plt.figure(figsize=(10, 5))
plt.plot(V_history, label="Membrane Potential")
spike_times = [i for i, s in enumerate(spikes) if s == 1]
plt.scatter(spike_times, [V_threshold]*len(spike_times), color='red', label="Spikes")
plt.axhline(V_threshold, linestyle='--', label="Threshold")
plt.legend()
plt.title("Neuron Simulation with Probabilistic Input")
plt.xlabel("Time")
plt.ylabel("Potential")
plt.show()
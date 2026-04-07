### Simple Neuron Simulation

This is a simple neuron model for practicing basic neurobiology concepts.

The neuron accumulates input impulses over time. When the membrane potential exceeds a threshold, the neuron generates a spike and resets to `V_reset`. The leak is proportional to the current potential, so higher charge decays faster.

### Requirements

* Python 3
* `matplotlib` for visualization

### How it works

* At each time step, an input impulse may arrive with probability `p`.
* The membrane potential `V` increases by the input strength and decreases by proportional leak.
* If `V > V_threshold`, a spike occurs and `V` is reset.
* The simulation plots the membrane potential over time and marks spikes.

### Usage

Run the Python script. Adjust parameters like `p`, `V_threshold`, `V_reset`, and `tau` to explore neuron behavior.



![alt text](<./pictures for readme/screen.png>)
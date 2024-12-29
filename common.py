import numpy as np

def generate_sinusoidal_data(x = None, n_obs = 10, noise_sd = 0.1, seed = 0):
    np.random.seed(seed)

    if x is None:
        x = np.linspace(0, 1, n_obs)
    else:
        n_obs = len(x)
        
    y = np.sin(2 * np.pi * x) + np.random.randn(n_obs) * noise_sd

    return x, y

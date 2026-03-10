import numpy as np

def generate_remd_temperatures(t_min, t_max, n_replicas):
    """
    Generate REMD temperatures using exponential spacing.
    
    Parameters
    ----------
    t_min : float
        Minimum temperature (K)
    t_max : float
        Maximum temperature (K)
    n_replicas : int
        Number of replicas

    Returns
    -------
    temps : list
        List of temperatures
    """
    # Exponential spacing
    temps = [t_min * (t_max / t_min) ** (i / (n_replicas - 1)) for i in range(n_replicas)]
    return temps

# Example usage
if __name__ == "__main__":
    t_min = 287   # lowest temperature in K
    t_max = 450   # highest temperature in K
    n_replicas = 14  # number of replicas
    
    temperatures = generate_remd_temperatures(t_min, t_max, n_replicas)
    print("Replica Temperatures:")
    print("\n".join(f"{t:.2f}" for t in temperatures))


import numpy as np

print("--- Day 2: Quantum State Vectors ---")

# 1. Defining a Valid Quantum State (The |+> state)
# We use 1/sqrt(2) because (1/sqrt(2))^2 = 0.5
# 0.5 + 0.5 = 1.0 (Valid!)
psi_plus = np.array([[1 / np.sqrt(2)],
                     [1 / np.sqrt(2)]])

print(f"State |+>:\n{psi_plus}")

# 2. Defining a Complex State (Using 'j' for imaginary numbers)
# Example: |psi> = 1/sqrt(2) |0> + i/sqrt(2) |1>
psi_complex = np.array([[1 / np.sqrt(2)],
                        [1j / np.sqrt(2)]])

print(f"\nComplex State:\n{psi_complex}")


# 3. The 'is_normalized' Function (The Validator)
def is_valid_quantum_state(state_vector):
    # Calculate magnitude squared of each element
    # np.abs() gets the magnitude |a|
    # **2 squares it
    probabilities = np.abs(state_vector) ** 2

    # Sum them up
    total_prob = np.sum(probabilities)

    print(f"Total Probability: {total_prob:.4f}")

    # Check if sum is approx 1
    return np.isclose(total_prob, 1.0)


# 4. Test it
print("\n--- Validation Tests ---")
print(f"Is |+> valid? {is_valid_quantum_state(psi_plus)}")
print(f"Is Complex State valid? {is_valid_quantum_state(psi_complex)}")

# 5. An Invalid State (Sum != 1)
bad_state = np.array([[0.8], [0.8]])  # 0.64 + 0.64 = 1.28 (Impossible)
print(f"Is Bad State valid? {is_valid_quantum_state(bad_state)}")
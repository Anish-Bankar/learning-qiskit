import numpy as np


print("\n--- 1. Classical States & Dirac Notation ---")

# Defining the Standard Basis Vectors |0> and |1>
# These are Column Vectors (2 rows, 1 column)
ket_0 = np.array([[1],
                  [0]])

ket_1 = np.array([[0],
                  [1]])

print(f"Ket 0 (|0>):\n{ket_0}")
print(f"Ket 1 (|1>):\n{ket_1}")

# A Probabilistic State (e.g., A weighted coin: 75% Heads, 25% Tails)
# P = 0.75|0> + 0.25|1>
prob_state = 0.75 * ket_0 + 0.25 * ket_1
print(f"\nProbabilistic State (0.75|0> + 0.25|1>):\n{prob_state}")

# Verify properties: Columns must sum to 1
print(f"Sum of probabilities: {np.sum(prob_state)}")


# --- SECTION 2: BRA-KET ALGEBRA (Inner & Outer Products) ---
print("\n--- 2. Bra-Ket Algebra ---")

# Bra is the Transpose of Ket
bra_0 = ket_0.T  # Row vector [1, 0]
bra_1 = ket_1.T  # Row vector [0, 1]

# Inner Product <a|b> (Scalar)
# <0|1> should be 0 (Orthogonal)
inner_prod = np.dot(bra_0, ket_1)
print(f"Inner Product <0|1>: {inner_prod[0][0]} (Should be 0)")

# <0|0> should be 1 (Normalized)
inner_prod_self = np.dot(bra_0, ket_0)
print(f"Inner Product <0|0>: {inner_prod_self[0][0]} (Should be 1)")


# --- SECTION 3: OPERATIONS (Matrices) ---
print("\n--- 3. Deterministic Operations (The NOT Gate) ---")

# We construct the NOT operation (Bit Flip) using Outer Products
# Logic: X maps |0> to |1> AND |1> to |0>
# Math: M = |1><0| + |0><1|

op_0_to_1 = np.dot(ket_1, bra_0) # |1><0|
op_1_to_0 = np.dot(ket_0, bra_1) # |0><1|

Not_Matrix = op_0_to_1 + op_1_to_0

print("NOT Matrix (Transition Matrix):")
print(Not_Matrix)
# Expected: [[0, 1], [1, 0]]

# Apply the Operation: New_State = Matrix @ Old_State
initial_state = ket_0  # Start with |0>
final_state = np.dot(Not_Matrix, initial_state)

print(f"\nApplied NOT to |0>:\n{final_state}")
# Expected: |1> (0, 1)


# --- SECTION 4: STOCHASTIC OPERATIONS (Probabilistic) ---
print("\n--- 4. Probabilistic Operations (The RESET) ---")

# A "Reset" operation forces the system to |0> regardless of input.
# But let's make a "Randomizer": 50% chance 0, 50% chance 1 regardless of input.
# Matrix Columns must sum to 1.

Random_Matrix = np.array([[0.5, 0.5],
                          [0.5, 0.5]])

print(f"Random Matrix:\n{Random_Matrix}")

# Apply to a definite state |1>
state_after_random = np.dot(Random_Matrix, ket_1)
print(f"\nState after Randomizing |1>:\n{state_after_random}")


# --- SECTION 5: COMPOSITION ---
print("\n--- 5. Composition (Multiple Ops) ---")

# Let's do: NOT then Randomize
# Math order: M_total = M_random @ M_not (Right to Left!)

Total_Op = np.dot(Random_Matrix, Not_Matrix)
print(f"Combined Operation Matrix:\n{Total_Op}")
# quantum-random-number-generator
A basic Quantum Random Number Generator (QRNG) implemented using a quantum circuit that leverages superposition and measurement to generate truly random bits.

## 🔹 How it Works
1. A qubit is initialized in the |0⟩ state.
2. A **Hadamard gate (H)** is applied to place the qubit in superposition.
3. The qubit is measured.
4. The measurement result (0 or 1) is used as a random bit.

## 🔹 Technologies Used
- Python
- Qiskit (IBM Quantum)
- Quantum Circuits

## 🔹 Applications
- Cryptography
- Secure key generation
- Simulations
- Randomized algorithms

## 🔹 Future Improvements
- Generate multi-bit random numbers
- Test randomness statistically
- Run on real IBM quantum hardware

!pip install qiskit
import time
from qiskit import QuantumCircuit
!pip install qiskit-aer
from qiskit_aer import Aer
import math
import math
from qiskit import QuantumCircuit
from qiskit_aer import Aer

def generate_quantum_key(num_keys=1, num_qubits=2):
    generated_keys = set()
    keys = []

    max_possible_keys = 2 ** num_qubits

    # Use Aer simulator backend
    backend = Aer.get_backend("qasm_simulator")

    # Number of bytes the key should represent
    num_bytes = math.ceil(num_qubits / 8)
    hex_len = num_bytes * 2   # 2 hex digits per byte

    while len(keys) < num_keys and len(generated_keys) < max_possible_keys:

        qc = QuantumCircuit(num_qubits, num_qubits)
        qc.h(range(num_qubits))
        qc.measure(range(num_qubits), range(num_qubits))

        result = backend.run(qc, shots=1).result()
        bitstring = list(result.get_counts().keys())[0]

        decimal_value = int(bitstring, 2)

        # Format as fixed-width hex
        hex_value = format(decimal_value, f'0{hex_len}x').upper()

        # Group hex like XX-XX-XX
        key = "-".join(hex_value[i:i+2] for i in range(0, len(hex_value), 2))

        if key not in generated_keys:
            generated_keys.add(key)
            keys.append(key)

    # If user requested more keys than possible
    while len(keys) < num_keys:
        zero_hex = "00" * num_bytes
        zero_key = "-".join(zero_hex[i:i+2] for i in range(0, len(zero_hex), 2))
        keys.append(zero_key)

    return keys


# Example Usage
num_keys_to_generate = 10
num_qubits_for_keys = 32

quantum_license_keys = generate_quantum_key(num_keys_to_generate, num_qubits_for_keys)
print("Generated Quantum License Keys:", quantum_license_keys)

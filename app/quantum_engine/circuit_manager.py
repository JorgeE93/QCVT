from qiskit import QuantumCircuit


class CircuitManager:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)

    def add_gate(self, gate, qubit_index):
        # Add gate dynamically based on input
        if gate == "h":
            self.circuit.h(qubit_index)
        elif gate == "x":
            self.circuit.x(qubit_index)
        # TODO: Add more gates

    def measure_all(self):
        self.circuit.measure_all()

    def get_circuit(self):
        return self.circuit

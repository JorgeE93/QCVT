import quantum_engine.circuit_manager as cm
import unittest


class TestCircuitManager(unittest.TestCase):

    def add_gate_h(self):
        circuit_manager = cm.CircuitManager(2)
        print(circuit_manager.add_gate("h", 0))


if __name__ == "__main__":
    unittest.main()

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)

qc.h(0)

state = Statevector.from_instruction(qc)

print(state)
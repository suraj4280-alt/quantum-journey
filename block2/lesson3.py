from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc=QuantumCircuit(2)
qc.x(0)
qc.x(1)

state=Statevector.from_instruction(qc)
print(state)
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc=QuantumCircuit(1,1)
#apply H gate to |0>
qc.h(0)
state1=Statevector.from_instruction(qc)
print(state1)

#apply H gate to |1>
qc1=QuantumCircuit(1,1)
qc1.x(0)
qc1.h(0)
state2=Statevector.from_instruction(qc1)
print(state2)
# Write the Qiskit code (from memory) to apply S to qubit 0 after 
# it's been flipped to |1⟩, and print the statevector.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

#gate S to |0>
qc=QuantumCircuit(1,1)
qc.s(0)
state0=Statevector.from_instruction(qc)
print(state0)

#gate S to |1>
qc1=QuantumCircuit(1,1)
qc1.x(0)
qc1.s(0)
state2=Statevector.from_instruction(qc1)
print(state2)

#gate S to superpostion
qc_S=QuantumCircuit(1,1)
qc_S.h(0)
qc_S.s(0)
state_S=Statevector.from_instruction(qc_S)
print(state_S)
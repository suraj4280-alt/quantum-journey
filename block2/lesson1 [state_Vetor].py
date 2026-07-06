# Without looking at notes, write a program that:

# Imports QuantumCircuit.
# Imports Statevector.
# Creates one qubit.
# Applies H.
# Prints the Statevector.
# Measures the qubit.
# Runs it with 100 shots using AerSimulator.
# Prints the measurement counts.
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

qc=QuantumCircuit(1,1)
qc.h(0)

state=Statevector.from_instruction(qc)
print(state)
qc.measure(0,0)
sim=AerSimulator()
job=sim.run(qc,shots=100)
results=job.result()
print(results.get_counts())
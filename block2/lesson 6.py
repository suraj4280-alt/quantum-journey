#bell state
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
qc=QuantumCircuit(2,2)

qc.h(0)
qc.cx(0,1)

state=Statevector.from_instruction(qc)
print(state)

qc.measure([0,1],[0,1])

sim=AerSimulator()

job=sim.run(qc,shots=1024)
result=job.result()
print(result.get_counts())

plot_histogram(result.get_counts())
plt.show()
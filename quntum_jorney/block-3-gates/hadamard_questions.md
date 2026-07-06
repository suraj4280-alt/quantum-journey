# Hadamard Gate — Practice Questions & Answers

Q1-> Apply H gate to state |0⟩.
---->A1. (|0⟩+|1⟩)/√2 → [1/√2, 1/√2]

Q2-> Apply H gate to state |1⟩.
---->A1. (|0⟩−|1⟩)/√2 → [1/√2, -1/√2]

Q3->  Why does H|1⟩ have a negative sign on one term, but H|0⟩ doesn't?
---->A3.Because of the H gate matrix ([1, 1], [1, -1]). When multiplying with state |1⟩ = [0, 1], we get a negative sign from the matrix's second row. That's why this doesn't happen with |0⟩ = [1, 0].

Q4-> What happens if you apply H twice in a row to |0⟩?
---->A4. We get the original state back: |0⟩.

Q5->Is H its own inverse? How would you prove that from your answer to Q4?
---->A5. Yes. If we apply H to itself, H² = I (H multiplied by itself equals the identity matrix). That proves H is its own inverse.

Q6->If a qubit's statevector is [0.707, 0.707], could it have come from H|0⟩? Could it have come from some other gate too?
---->A5. Yes, and possibly no — other gates/rotations could also produce this same statevector, since matching magnitudes doesn't guarantee it was H specifically.

Q7-> Write the Qiskit code to apply H to qubit 0 and print the statevector.
---->A8.
```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)
qc.h(0)
state1 = Statevector.from_instruction(qc)
print(state1)

# H on |1>
qc1 = QuantumCircuit(1)
qc1.x(0)
qc1.h(0)
state2 = Statevector.from_instruction(qc1)
print(state2)
```

Q-> Predict the statevector for: X → H → H on qubit 0.
---->A8. [0, 1] — X flips to |1⟩, H sends it to (|0⟩−|1⟩)/√2, second H undoes it (self-inverse), landing back on |1⟩.
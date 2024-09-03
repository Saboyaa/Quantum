import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
nq = 2
circuito_grover_ = QuantumCircuit(nq, 2)
# aplicar hadamard nos qubits [psi 1]
for qubit in  range(nq):
  circuito_grover_.h(qubit)
#=================
# ORACULO
#================
# aplicar not nos qubits [psi 2]
for qubit in  range(nq):
  circuito_grover_.x(qubit)
# aplicar Z no qubit 1 controlado pelo qubit 0 [psi 3]
circuito_grover_.cz(0, 1)
# aplicar not nos qubits [psi 2]
for qubit in  range(nq):
  circuito_grover_.x(qubit)
# visualizar circuito
circuito_grover_.draw('mpl')

#=================
# REFLEXAO
#================
# hadamard em cada qubit
for qubit in range(nq):
    circuito_grover_.h(qubit)
# reflexao
for qubit in range(nq):
    circuito_grover_.z(qubit)
circuito_grover_.cz(0, 1)
# hadamard em cada qubit
for qubit in range(nq):
    circuito_grover_.h(qubit)
#======================
# mensurar qubits
#====================
circuito_grover_.measure([0,1], [0,1])
#visualizar circuito
print(circuito_grover_.draw('text'))

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.quantum_info import Operator

qubits = 2
input = 0
output = 1
zero = Operator([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])
one = Operator([
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
])
identity = Operator([
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
])
negation = Operator([
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1]
])

def oracle(type):
    oracle = QuantumCircuit(qubits, name='oracle')
    oracle.append(type, range(qubits))
    return oracle

def deutsch(oracle):
    cbits = 1
    circuit = QuantumCircuit(qubits, cbits, name='deutsch')
    circuit.x(output)
    circuit.barrier()
    circuit.h(input)
    circuit.h(output)
    circuit.append(oracle.to_instruction(), range(qubits))
    circuit.h(input)
    circuit.barrier()
    circuit.measure(input, 0)
    return circuit

def test_deutsch(name, type):
    circuit = deutsch(oracle(type))
    backend = Aer.get_backend('qasm_simulator')
    new_circuit = transpile(circuit, backend)
    job = backend.run(new_circuit)
    print(job)
    # print(name, 'is', 'constant' if job == '0' else 'balanced')

test_deutsch('Zero', zero)
# test_deutsch('One', one)
# test_deutsch('Identity', identity)
# test_deutsch('Negation', negation)

circuit = deutsch(oracle(zero))
print(circuit.draw())
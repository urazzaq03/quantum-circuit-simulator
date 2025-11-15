import argparse
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_state_city
import matplotlib.pyplot as plt


def build_circuit(num_qubits):
    qc = QuantumCircuit(num_qubits)
    # simple example: create Bell state for 2 qubits or apply Hadamard to all
    if num_qubits == 2:
        qc.h(0)
        qc.cx(0, 1)
    else:
        for i in range(num_qubits):
            qc.h(i)
    return qc


def run_circuit(qc):
    backend = Aer.get_backend('statevector_simulator')
    result = execute(qc, backend).result()
    return result.get_statevector()


def visualize_state(state):
    plot = plot_state_city(state)
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Quantum Circuit Simulator")
    parser.add_argument('--qubits', type=int, default=2, help='Number of qubits')
    parser.add_argument('--visualize', action='store_true', help='Visualize state')
    args = parser.parse_args()
    qc = build_circuit(args.qubits)
    print("Circuit:")
    print(qc.draw())
    state = run_circuit(qc)
    print("Statevector:", state)
    if args.visualize:
        visualize_state(state)


if __name__ == '__main__':
    main()

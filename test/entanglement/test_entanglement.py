# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
# pylint: disable=no-name-in-module


"""
Test entanglement functions
"""

import unittest
import qiskit

import qiskit.ignis.verification.entanglement
import qiskit.ignis.verification.entanglement


class TestEntanglement(unittest.TestCase):
    """
    Test entanglement functions
    """

    def test_ghz_simple(self):
        """
        test that get_ghz_simple correctly creates a ghz circuit
        """

        qn = 5
        circ_simple = get_ghz_simple(qn, measure=False)
        backend = qiskit.Aer.get_backend('qasm_simulator')
        shots = 1024
        backend_result = qiskit.execute(
            circ_simple, backend,
            shots=shots).result()
        print(backend_result)









if __name__ == '__main__':
    unittest.main()
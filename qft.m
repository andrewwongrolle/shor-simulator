% Performs a quantum fourier transform on the vector in_qubits in C^M.
% Source: Berkeley EdX course, chapter 5
% M is the size of the vector. The transformation we are perfoming here is
% O(M^2), not O(Mlog(M)) which is the time for the fast fourier transform.

function [ out_qubits,transform ] = qft( in_qubits, M )

    omega = exp((2 * pi * i) / M);
    transform = ones(M);
    for j = 1:M
        for k = 1:M
            transform(j,k) = (1 / sqrt(M)) * omega^((j-1)*(k-1));
        end
    end
    out_qubits = transform * in_qubits
end
% We're going to factor 15! Per http://arxiv.org/pdf/quant-ph/0303175v1.pdf
% we can choose 15^2 = 225 < 2^8 = 64 < 2*1562 = 450, so 8 is the number of
% qubits in the first register.
% The second register will have n = log2(N) = log2(15) = 4 qubits.

% Throughout Shor's Algorithm we will use least significant bits higher up
% in the vector (little Endian).

% This particular file implements the classical part of Shor's algorithm.
% Source: http://arxiv.org/pdf/quant-ph/0010034v1.pdf page 4

N = 15; % number to factor

A = rand_rel_prime(N)
order = dummy_find_order(A,N);

% find a number A with even order and A^(order/2) + 1 (mod N) not equal to 0
while (true)
    if mod(order,2) == 0
        if mod(A^(order/2) + 1,N) ~= 0
            break
        end
    end
    A = rand_rel_prime(N);
    order = dummy_find_order(A,N);
end

factor = gcd((A^(order/2) - 1),N)

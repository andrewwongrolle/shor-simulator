function [ A ] = rand_rel_prime(N)
% Returns a number A in range [2,N-1] relatively s.t. gcd(a,N) = 1
A = randi([2,N-1]); % must be relatively prime to N
while gcd(A,N) ~= 1
    A = randi([2,N-1]);
end

end


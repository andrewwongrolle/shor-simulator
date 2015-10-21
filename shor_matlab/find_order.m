% Given numbers N and A < N such that gcd(A, N) = 1, find the smallest r such
% that A^r = 1 (mod N).
% Quantum register: We use an m + n-qubit register, where m = 3 log N (and hence in
% particular M ? N3). 
% Below we treat the first m bits of the register as encoding a number
% in Z_M = {0,...,M-1}.
% Source: http://www.cs.princeton.edu/theory/complexity/quantumchap.pdf
% section 20.7.2
% Note that M = 2^m and m = 3*log(N).

% Pseudocode:
% Initialized to zero state.
% Call QFT on the M-space.
% Generate vectors in the x tensor f(x) space.
% Compute f(x): 
    % switch amplitudes such that x tensor 0 -> x tensor f(x)
% Partial measure f(x) in the N-space
% Compute the QFT on the M-space.
% Measure M-space.

function [ period ] = find_order(A,N)
    m = 5;
    M = 2^m; % hard coded for now

    % These vectors will be useful for visualization of the tensor space
    % and looking up tensor values.
    x_M = (0:M-1)'; % exists in M-space
    fx_N = (0:N-1)'; % exists in N-space

    x = kron(x_M,ones(N,1)); % exists in tensor space
    fx = kron(ones(M,1),fx_N); % exists in tensor space

    zero_M = zeros(M,1);
    zero_M(1,1) = 1;
    [x_M zero_M] % visualize

    zero_N = zeros(N,1);
    zero_N(1,1) = 1;
    [fx_N zero_N] % visualize

    zero_MN = kron(zero_M,zero_N); % zero state in tensor space
    [x fx zero_MN] % visualize

    % performs fourier transform on zero state in M-space
    [amplitude_M,~] = qft(zero_M,M);
    amplitude_MN = kron(amplitude_M,zero_N);
    [x fx amplitude_MN] % visualize

    % computes x tensor f(x)
    for j = 0:M-1
        y = mod(a^j,N); % computes f(x)
        amplitude = amplitude_MN(N*j + 1);
        % zero out previous amplitude
        amplitude_MN(N*j + 1) = 0;
        % move amplitude over to x tensor f(x)
        amplitude_MN(N*j+1+y) = amplitude;
    end

    % measures f(x), finds index which was "observed"
    observed = measure(amplitude_MN)
    [x(observed) fx(observed) amplitude_MN(observed)] % display results

    % this measuring collapses the space
    measured = amplitude_MN(fx == fx(observed));
    [x1 measured]
    % normalize
    measured_norm = measured / norm(measured);

    % apply fourier transform on the collapsed state
    amplitude_ans = qft(measured_norm,M)

    % measure again
    observed_final = measure(amplitude_ans)

    period = observed_final - 1
    
end
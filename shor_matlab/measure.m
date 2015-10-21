% Measures a superposition vector of amplitudes and returns measured
% position.

% Assumes input state is a bra and is normalized.

% The histogram vector transforms amplitudes into a running sum. The
    % range hist_(vector(i-1),hist_vector(i)) has length amplitude(i) squared.
    % Therefore the probability that a uniformly distributed value in (0,1)
    % is in hist_(vector(i-1),hist_vector(i)) is amplitude(i) squared.

function [observed] = measure(amplitudes)
    seed = rand;
    
    % Therefore all we need to do is find the first value in hist which is
    % larger than the random seed.
    amplitudes = amplitudes .* conj(amplitudes);
    hist = cumsum(amplitudes);
    observed = find(hist > seed,1);
    
end
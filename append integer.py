myAppend(0, L) :- append([],[], L).
myAppend(N, L) :- append([N], [], L), N1 is N - 1, myAppend(N1, L).

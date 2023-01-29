predicates
    gcd(integer, integer, integer)

clauses
    gcd(M, O, M).
    gcd(M, N, Result):-
        Rem=M mod N,
        gcd(N, Rem, Result).

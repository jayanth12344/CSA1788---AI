removeDups([], []).
removeDups([H1,H2|T], Newlist) :- 
    (H1 == H2 -> removeDups([H2|T],Newlist) 
    ; removeDups(T,Newlist)).

?- removeDups([a,b,b,c,c,d,d,e],L).
L = [].

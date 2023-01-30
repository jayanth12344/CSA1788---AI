encode(L1,L2) :-
   pack(L1,L),
   transform(L,L2).

L2= [[2, a], [3, b], [2, c]]

L1=[a,a,b,b,b,c,c].
 using pack I would get 

L=[[a,a],[b,b,b],[c,c]].


%1.rule: 
transform([],[]).
%2.rule:
transform([[X|Xs]|Ys],[[N,X]|Zs]) :-
   length([X|Xs],N),
   transform(Ys,Zs).

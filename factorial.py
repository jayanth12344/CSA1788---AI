fact(0,1). 
fact(X,F) :- X>0, X1 is X-1, fact(X1,F1), F is X*F1. 
INPUT/OUTPUT 
?- fact(5,N). 
N = 120 . 
?- fact(3,N). 
N = 6 
?- fact(0,N). 
N = 1 
?- fact(1,N). 
N = 1 .

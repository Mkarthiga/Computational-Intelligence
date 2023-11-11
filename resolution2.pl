
criminal(X):-american(X),weapon(Y),sells(X,Y,Z),hostile(Z).
owns(nono,m).
missile(m).
sells(west,X,nono):-missile(X),owns(nono,X).
weapon(X):-missile(X).
hostile(X):-enemy(X,america).
american(west).
enemy(nono,america).

%PROVE "west is criminal".


% horses,cows,pigs are mammals.
mammal(horses).
mammal(pigs).
mammal(cows).
% Bluebeard is a horse.
horse(bluebeard).
% Bluebeard is Charlie's parent.
parent(bluebeard,charlie).
% Offspring and parent are inverse relations.
offspring(X,Y):-parent(Y,X).
%An offspring of a horse is a horse.
horse(X):-offspring(X,Y),horse(Y).
% Every mammal has parent.
hasparent(X):-mammal(X).

%infer the following
%1.charile is horse
%horse(charlie).
%2.who is offspring of bluebeard
%offspring(X,bluebeard).
%3.what are mammals?
%mammal(X).
% (change the order of horses,pigs,cows to get different values of X in
% each run)

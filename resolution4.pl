% emily is cat.
cat(emily).
% tuna is cat.
cat(tuna).
% emily has white spots.
hasspots(emily,white).
% spike has balck spots.
hasspots(spike,black).
%tuna has black spots.
hasspots(tuna,black).
% spike is dog
dog(spike).
% mark owns a pet, if it is cat and has black spots.
owns(mark,X):-cat(X),hasspots(X,black).
%ram owns a pet, if it is cat and has white spots.
owns(ram,X):-cat(X),hasspots(X,white).
%if someone owns something they love it.
love(X,Y):-owns(X,Y).

%infer the following.
% 1.what are cats
% cat(X)
% (change the order of tuna and emily to get different op).
% 2.pets having black spots.
% hasspots(X,black).
% (change the order of spike and tuna to get different op).
% 3.who owns whom
% owns(X,Y).
% (change the order of ram and mark to get different op).



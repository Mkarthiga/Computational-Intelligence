% john likes all kind of food.
likes(john,X):-food(X).
% apple and vegetable are foods.
food(apple).
food(vegetable).
%anything anyone eats and not killed is food.
food(Y):-eats(X,Y),not(killed(X)).
% anil eats peanuts and still alive.
eats(anil,peanuts).
alive(anil).
% harry eats everything that anio eats
eats(harry,X):-eats(anil,X).
% from the given sentence we can say that
% "It is not alive,if it is killed".
killed(X):-not(alive(X)).

%prove "john likes peanuts".

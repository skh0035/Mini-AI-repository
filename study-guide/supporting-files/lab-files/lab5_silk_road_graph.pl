% =====================================================================
%  SilkMind Caravan - Lab 5: The Silk Road Knowledge Graph (Stop 5)
%  A tiny knowledge graph plus one rule (L1 from Topic 5).
%  Run it in SWISH: https://swish.swi-prolog.org
% =====================================================================

% ---------- FACTS: thing --located in--> place -------------------------
located_in(registan,   samarkand).
located_in(samarkand,  uzbekistan).
located_in(uzbekistan, central_asia).

% ---------- RULE L1: "inside" follows located_in links -----------------
% X is inside Y if X is located directly in Y ...
inside(X, Y) :- located_in(X, Y).
% ... or if X is located in some Y that is itself inside Z.
inside(X, Z) :- located_in(X, Y), inside(Y, Z).

% ---------- Try these queries ------------------------------------------
% ?- located_in(registan, central_asia).   Is this fact stored?
% ?- inside(registan, central_asia).       Can it be worked out?
% ?- inside(registan, Where).              Every place the Registan is inside
% ?- inside(What, uzbekistan).             Everything inside Uzbekistan

% =====================================================================
%  SilkMind Caravan - Lab 2: BEK's Animal Expert (Stop 2)
%  Same six rules as Topic 2 (R1-R6), written in Prolog.
%  Run it in SWISH: https://swish.swi-prolog.org  ->  Program  ->
%  paste this file  ->  type a query in the bottom-right box  ->  Run!
% =====================================================================

% Lets you add new facts and rules anywhere in the file without warnings.
:- discontiguous fact/2, is_a/2.

% ---------- WORKING MEMORY: facts about the animals BEK has met -------
% fact(Animal, Observation).   Read: "Animal" has this observation.
fact(pingu,   has_feathers).
fact(pingu,   cannot_fly).
fact(pingu,   swims).

fact(hoot,    has_feathers).
fact(hoot,    can_fly).
fact(hoot,    hunts_at_night).

fact(stripes, gives_milk).
fact(stripes, has_hooves).
fact(stripes, has_black_stripes).

fact(tweety,  has_feathers).
fact(tweety,  can_fly).

fact(mystery, gives_milk).
fact(mystery, eats_meat).
fact(mystery, has_hooves).
fact(mystery, has_black_stripes).

% ---------- KNOWLEDGE BASE: the rules R1-R6 -----------------------------
% is_a(X, Kind) :- conditions.    Read ":-" as "IF" and "," as "AND".
is_a(X, bird)    :- fact(X, has_feathers).                          % R1
is_a(X, mammal)  :- fact(X, gives_milk).                            % R2
is_a(X, penguin) :- is_a(X, bird), fact(X, cannot_fly),
                    fact(X, swims).                                 % R3
is_a(X, owl)     :- is_a(X, bird), fact(X, can_fly),
                    fact(X, hunts_at_night).                        % R4
is_a(X, tiger)   :- is_a(X, mammal), fact(X, eats_meat),
                    fact(X, has_black_stripes).                     % R5
is_a(X, zebra)   :- is_a(X, mammal), fact(X, has_hooves),
                    fact(X, has_black_stripes).                     % R6

% ---------- Try these queries (one at a time) ----------------------------
% ?- is_a(pingu, penguin).        Is Pingu a penguin?
% ?- is_a(pingu, What).           Everything BEK can conclude about Pingu
% ?- is_a(Who, bird).             Which animals are birds?
% ?- is_a(tweety, What).          What does BEK know about Tweety?
% ?- is_a(mystery, What).         Watch out for this one!

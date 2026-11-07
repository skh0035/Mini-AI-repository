% =====================================================================
%  SilkMind Caravan - Grand Caravan Challenge: EXAMPLE SOLUTION
%  "Which tea should the caravanserai serve this traveller?"
%  One possible answer; your own expert system can be about anything.
% =====================================================================
:- discontiguous fact/2.

% ---------- WORKING MEMORY: what we know about each traveller ----------
fact(aziz,  feels_cold).   fact(aziz,  wants_caffeine).
fact(lola,  feels_hot).    fact(lola,  wants_no_caffeine).
fact(timur, feels_cold).   fact(timur, wants_no_caffeine).
fact(timur, has_sore_throat).
fact(guli,  wants_caffeine).                 % test case: temperature unknown

% ---------- KNOWLEDGE BASE: tea rules -----------------------------------
recommend(X, hot_black_tea)    :- fact(X, feels_cold), fact(X, wants_caffeine).    % T1
recommend(X, iced_green_tea)   :- fact(X, feels_hot),  fact(X, wants_caffeine).    % T2
recommend(X, mint_tea)         :- fact(X, feels_hot),  fact(X, wants_no_caffeine). % T3
recommend(X, ginger_honey_tea) :- fact(X, feels_cold), fact(X, wants_no_caffeine). % T4
recommend(X, ginger_honey_tea) :- fact(X, has_sore_throat).                        % T5

% ---------- Test queries ---------------------------------------------------
% ?- recommend(aziz, Tea).     expected: hot_black_tea
% ?- recommend(lola, Tea).     expected: mint_tea
% ?- recommend(timur, Tea).    expected: ginger_honey_tea TWICE (T4 and T5 both fire)
% ?- recommend(guli, Tea).     expected: false (a gap: no rule without temperature)

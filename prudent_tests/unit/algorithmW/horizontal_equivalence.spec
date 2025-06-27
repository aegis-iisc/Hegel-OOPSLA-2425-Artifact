type apair;
type plist;

qualifier llen : [a] :-> int;
qualifier pllen : [apair] :-> int;

qualifier lmem : [a] :-> a :-> bool;
qualifier lhd : [a] :-> a;
qualifier plhd : [apair] :-> apair;

qualifier last  : [a] :-> a;
qualifier pllast  : [apair] :-> apair;

qualifier ppr1  : apair :-> a;
qualifier ppr2  : apair :-> a;


qualifier nth : [a] :-> int :-> a;
qualifier lsnd : [a] :-> a;
qualifier pen : [a] :-> a;

qualifier fst : plist :-> [a];
qualifier snd : plist :-> [a];

ep : a;


length : (x : [a]) ->  {v : int |  llen (x) == v}; 

length' :  (x : [a]) ->  {v : int |  llen (x) == v}; 

cons : (x : a) ->  (xs : [a]) -> {v : [a] |  llen (v) == llen (xs) + 1}; 

goal : (n:int) -> (z : {v : [a] | true}) -> { v : apair | true};
           
       
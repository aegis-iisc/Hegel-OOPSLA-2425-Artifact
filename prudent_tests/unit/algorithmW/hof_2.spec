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

length : (x : [a]) ->  {v : int |  llen (x) == v}; 

length' :  (x : [a]) ->  {v : int |  llen (x) == v}; 

map : (f : (x0 : a) -> {v : b | true}) -> 
        (x : [a]) -> {v : b | llen (x) == llen (v)};

application : (f : (x0 : a) -> {v : b | true}) -> (y : a) -> {v : b | true};


qualifier slen : [a] :-> int;


goal : (z : [a]) -> (f0 : (x0 : a) -> {v : b | true}) -> {v : [b] | llen (v) == llen (z)};
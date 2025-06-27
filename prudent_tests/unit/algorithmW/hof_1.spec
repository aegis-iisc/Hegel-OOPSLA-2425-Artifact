type apair;
type plist;
type a;
type b;

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


atob : (x : a) -> {v : b | true};


qualifier slen : [a] :-> int;


map : (f : (x0 : a) -> {v : b | true}) -> 
        (x : [a]) -> {v : [b] | llen (v) == llen (x)};
goal : (z : [a]) -> {v : [b] | llen (v) == llen (z)};
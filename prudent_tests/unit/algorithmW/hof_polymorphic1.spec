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

atobconcrete : (x : int) -> { v : int | gt_0 (v) = true};


map : <p : b :-> bool>. (f : (x0 : a) -> {v : b | p (v) = true}) -> 
(x : [a]) -> {v : [b] | \(u : b). lmem (v, u) = true => p (u) = true };


goal : (z : [a]) -> {v : [b] | llen (v) == llen (z)};


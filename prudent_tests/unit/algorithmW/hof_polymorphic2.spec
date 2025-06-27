type apair;
type plist;
type a;
type b;

qualifier llen : [a] :-> int;
qualifier pllen : [apair] :-> int;

qualifier lmem : [a] :-> a :-> bool;
qualifier lhd : [a] :-> a;
qualifier plhd : [apair] :-> apair;

atobconcrete : (x : int) -> { v : int | gt_0 (v) = true};


map : <qualifier p : b :-> bool>. (f : (x0 : a) -> {v : b | p (v) = true}) -> 
(x : [a]) -> {v : [b] | \(u : b). lmem (v, u) = true => p (u) = true };


goal : (z : [a]) -> {v : [b] | llen (v) == llen (z)};


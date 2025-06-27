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

length_prime :  (x : [a]) ->  {v : int |  llen (x) == v}; 
    
create : (x : int) -> {v : [a] | llen (v) == x};
goal : (z : {v : [a] | true}) -> { v : int| v == llen (v) + 1 };

       
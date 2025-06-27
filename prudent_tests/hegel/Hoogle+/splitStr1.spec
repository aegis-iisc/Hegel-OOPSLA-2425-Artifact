type ipair;
type plist;

qualifier llen : [int] :-> int;
qualifier pllen : [ipair] :-> int;

qualifier lmem : [int] :-> int :-> bool;
qualifier lhd : [int] :->  int;
qualifier plhd : [ipair] :-> ipair;

qualifier last  : [int] :-> int;
qualifier pllast  : [ipair] :-> ipair;

qualifier ppr1  : ipair :-> int;
qualifier ppr2  : ipair :-> int;


qualifier nth : [int] :-> int :-> int;
qualifier lsnd : [int] :-> int;
qualifier pen : [int] :-> int;

qualifier fst : plist :-> [int];
qualifier snd : plist :-> [int];

ep : int;

length : (x : [int]) ->  {v : int |  llen (x) == v}; 

rev : (l : [int]) ->  {v : [int] | 
            llen (v) == llen (l) /\
            lhd (v) == last (l) /\
            last (v) == lhd (l) /\
            lsnd (v) == pen (l) /\
            pen (v) == lsnd (v)

        };



compare_lengths : (x : [int]) -> (y: [int]) ->  
{v : bool | [v=true] <=> (llen (x) == llen  (y))};



cons : (x : int) -> (xs : [int]) -> { v : [int] | llen (v) == llen (xs) + 1 /\
            lmem (v, x) = true /\
            lhd (v) == x /\
            lsnd (v) == lhd (xs) /\
            last (v) == last (xs) /\
            pen (v) == pen (xs)
        };



hd : (l : [int]) -> { v : int | lmem (l, v) = true /\
            lhd (l) == v
            
        };


tl : (l : [int]) -> { v : [int] |
            llen (v) == llen (l) -- 1 /\
            last (v) == last (l) /\
            lhd (v) == lsnd (l) /\
            pen (v) == pen (l)
        };

nth : (l : [int]) -> (n : int) ->  { v : int | lmem (l, v) = true /\
            nth (l, n) == v 
        };

append : (l1 : [int]) ->  (l2 : [int]) -> { v : [int] | 
            llen (v) == llen (l1) + llen (l2) /\
            lhd (v) == lhd (l1) /\
            lsnd (v) == lsnd (l1) /\
            last (v) == last (l2) /\
            pen (v) == pen (l2)
        };

combine : (l1 : [int]) ->  (l2 : {v : [int] | llen (l1) == llen (l2)}) -> 
        {v : [ipair] | \(H : ipair), (L : ipair).
            pllen (v) == pllen (l1) /\
            plhd  (v) = H  /\
            pllast (v) = L /\
            ppr1 (H) == lhd (l1) /\
            ppr2 (H) == lhd (l2) /\
            ppr1 (L) == last (l1) /\
            ppr2 (L) == last (l2) 
        };


splitAt : (y:int) -> (l : { v : [int] | llen (v) > y}) -> 
                {v:plist | \(H : [int]), (L : [int]).
                    (fst (v) = H /\
                    snd (v) = L) =>  
                    llen (H) == y /\
                    llen (L) == llen (l) -- y 
                };

null : (l : [int]) -> {v : bool | [v=true] <=> llen (l) == 0};

last : (l : [int]) -> { v : int | last (l) == v}; 

init : (l : [int]) -> { v : [int] | llen (v) == llen (v) --1}; 

take : (n : int) -> (l : [int]) -> { v : [int] | \(u : int). 
                                            llen (v) == n /\ 
                                            (lmem (v, u) = true) => lmem (l, u) = true}; 


type spair;
qualifier sfst : spair :-> string;
qualifier ssnd : spair :-> string;
qualifier smem : char :-> string :-> bool;

goal : (s : string) -> (c : char) -> { v : spair |
                                      f = sfst (v) /\ sn = ssnd (v) /\
                                       smem (c, f) = true  /\
                                \(u : char). smem (u, f) = true => smem (u , s) = true /\
                                \(u : char). smem (u, sn) = true => smem (u, s) = true };


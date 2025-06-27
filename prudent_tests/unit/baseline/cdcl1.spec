
qualifier slen : [a] :-> int;

length : (x : [a]) ->  {v : int |  slen (x) == v}; 

init : (l : [a]) -> { v : [a] | slen (v) == slen (l) --1}; 

rev : (z : [a]) ->  {v : [a] |  slen (v) == slen (z)}; 

goal : (z : [a]) -> { v : int | v == slen (z) -- 1};

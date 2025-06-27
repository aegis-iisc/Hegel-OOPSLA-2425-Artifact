type fwstate;
type srpair;

type nlrecord;
type user;
type code;

qualifier device : [int] :-> int :-> bool;
qualifier dsize : [int] :-> int;


qualifier lmem : [a] :-> a :-> bool;
qualifier lhd : [a] :-> a;


qualifier fst  : fwstate :-> [srpair] ;
qualifier snd  : fwstate :-> [int];

qualifier central  : [srpair] :-> int :-> bool;

qualifier cansend  : [srpair] :-> int :-> int :-> bool;

qualifier is_central : int :-> bool;

qualifier nlmem : [nlrecord] :-> string :-> string :-> bool;

qualifier ns : [nlrecord] :-> string :-> string :-> nlrecord;

qualifier subscribed : nlrecord :-> bool;


qualifier nletter : nlrecord :-> string;
qualifier code : nlrecord :-> code;
qualifier articles : nlrecord :-> [string];

qualifier email : [nlrecord] :-> user :-> bool;
qualifier promotions : [nlrecord] :-> user :-> bool;


add_device :
  (dtable : [int]) -> 
  (cstab : [srpair]) -> 
  (d : {v : int | device (dtable, v) = false}) ->
    {v : fwstate |\(s : [int]).
      fst (v) = cstab /\
      (s = snd (v) =>  
      device(s, d) = true /\
      dsize(s) = dsize(dtable) + 1) };


diff_device :
  (sr : [srpair]) ->
  (dtable : [int]) ->
  (d : {v : int | true}) ->
    {v : int | device(dtable, v) = true /\ not [v=d] };



add_connection :
  (sr : [srpair]) ->
  (dtable : [int]) ->
  (s : {v : int | device(dtable, v) = true}) ->
  (r : {v : int | device(dtable, v) = true}) ->
    {v : fwstate | \(f : [srpair]).
      snd (v) = dtable /\
      (f = fst (v) => cansend(f, s, r) = true) };




make_central :
  (sr : [srpair]) ->
  (dtable : [int]) ->
  (d : {v : int | device(dtable, v) = true}) ->
    {v : fwstate |\(f : [srpair]).
      snd (v) = dtable /\
       (f = fst (v) => central(f, d) = true) };


delete_device :
  (sr : [srpair]) ->
  (dtable : [int]) ->
  (d : {v : int | true}) ->
  (y : {v : int | not [v = d] /\ device(dtable, v) = true  
                            /\ central(sr, v) = true /\ 
                                device(dtable, d)= true}) ->
    {v : fwstate |\(f : [srpair]), (s : [int]).
      (f = fst (v) /\ s = snd (v)) => 
      (device(s, d) = false /\
      central(f, y) = true )};


select :
  (db : [nlrecord]) ->
  (n  : string) ->
  (u  : string) ->
    {v : nlrecord |
      nlmem(db, n, u) = true /\
      nletter(v) = n /\
      user(v) = u };


nlmem :
  (db : [nlrecord]) ->
  (n  : string) ->
  (u  : string) ->
    {v : bool |
      (v = true <=> nlmem(db, n, u) = true) /\
      (v = false <=> nlmem(db, n, u) = false) };

subscribe :
  (db : [nlrecord]) ->
  (n  : string) ->
  (u  : string) ->
    {v : [nlrecord] |
      nlmem(db, n, u) = false /\
       nlmem(v, n, u) = true /\
        subscribed(v, n, u) = true };

unsubscribe :
  (db : [nlrecord]) ->
  (n  : string) ->
  (u  : string) ->
    {v : [nlrecord] |
      nlmem(db, n, u) = true /\
       nlmem(v, n, u) = true /\
        subscribed(v, n, u) = false };
confirm :
  (db : [nlrecord]) ->
  (c  : code) ->
  (n  : string) ->
  (u  : string) ->
    {v : [nlrecord] |
      nlmem(db, n, u) = true /\
        ((c = Cs => subscribed(v, n, u) = true) /\
         (c = Cu => subscribed(v, n, u) = false)) };        


read :
  (db : [nlrecord]) ->
  (n  : string) ->
  (u  : string) ->
    {v : [string] |
      nlmem(db, n, u) = true /\
      subscribed(v, n, u) = true /\
      v = articles(v, n, u) }; 

remove :
  (db : [nlrecord]) ->
  (n  : string) ->
  (u  : string) ->
    {v : [nlrecord] | nlmem(v, n, u) = false};

goal : 
  (n  : string) -> (u : string) -> 
  (d : [nlrecord]) -> 
  {v : [nlrecord] |  subscribed (v, n, u) = false /\ nlmem (v, n, u) = false
  /\ promotions (v, u) = true => (email (v, u) = true)};

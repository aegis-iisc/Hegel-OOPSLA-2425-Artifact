(*generated using Prudent *) 

 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take  ep  ( goal  size  ( last   ( init  a3 )  )  l )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take  a2  ( goal  a1  ( last   ( init  a3 )  )  a3 )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last   ( init  a3 )  )   ( goal  a11 a2  ( init  a3 )  )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last   ( init  a3 )  )   ( goal  a2 size l )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take  ep  ( init  a3 )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take  a11  ( goal  size  ( last   ( init  a3 )  )  l )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take  a11  ( goal  a11 a2  ( init  a3 )  )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  a3 )   ( goal  a2 size l )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take  a1  ( goal  ep a2 l )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take  a2 a3 ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  a3 )   ( goal   ( last  a3 )   ( last   ( init  a3 )  )   ( init  a3 )  )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take  ep  ( goal   ( last   ( init  a3 )  )  size a3 )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take  a11 a3 ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take  a1  ( goal   ( last   ( init  a3 )  )   ( last   ( init  a3 )  )  l )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  a3 )   ( goal  ep a11  ( init  a3 )  )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last   ( init  a3 )  )   ( goal  a2 a2 a3 )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  a3 )   ( goal  size  ( last   ( init  a3 )  )  l )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  a3 )   ( goal  a2 a2 a3 )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  a3 )   ( goal   ( last   ( init  a3 )  )   ( last   ( init  a3 )  )  l )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  a3 )   ( goal   ( last  a3 )   ( last  a3 )  a3 )  ) 

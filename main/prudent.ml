open SpecLang 
module SEL = SpecElab
module Synth = Synthesis
module Lambda = Lambdasyn 
exception CompilerExc of string  

let learningON = ref false 
let bidirectional = ref false
let spec_file = ref ""
let effect_filter = ref false
let goal_number = ref 0
let usage_msg = "prudent [-cdcl] [-bi] [-effect] <spec-file1> -g <goal-number>"
let anon_fun specfile = 
    spec_file := specfile
let maxPathlength = ref 3   
let nestedif = ref 1
let pbenchmark = ref ""
let sizedbst = ref false
module Printf = struct 
  let printf d s = Printf.printf d s
  let originalPrint = Printf.printf 
  let fprintf = Printf.fprintf
end  


  let speclist =
  [("-effect", Arg.Set effect_filter, "Set the effect-guided filtering to true");
   ("-cdcl", Arg.Set learningON, "Set to CDCL=true");
   ("-bi", Arg.Set bidirectional, "Set bidirectional=true");
   ("-g", Arg.Set_int goal_number, "Set the #goal number");
   ("-k", Arg.Set_int maxPathlength, "Set the max path length");
   ("-nested", Arg.Set_int nestedif, "Allow generating nested if statements")] 
  
let () = 


  Arg.parse speclist anon_fun usage_msg;
  
  let () = Printf.printf "%s" "\n  EXPLORED Args.parser output " in 
  let () = Printf.printf "%s" ("\n EXPLORED learningOn  "^(string_of_bool !learningON)) in 
  let () = Printf.printf "%s" ("\n EXPLORED bidirectionality  "^(string_of_bool !bidirectional)) in
  let () = Printf.printf "%s" ("\n EXPLORED effect-filter  "^(string_of_bool !effect_filter)) in 
  let () = Printf.printf "%s" ("\n EXPLORED specfile :: "^(!spec_file)) in 
  let () = Printf.printf "%s" ("\n EXPLORED goal Number :: "^(string_of_int (!goal_number))) in 
  let () = Printf.printf "%s" ("\n EXPLORED Max path length :: "^(string_of_int (!maxPathlength))) in 
  let () = Printf.printf "%s" ("\n EXPLORED Nested If :: "^(string_of_int (!nestedif))) in 

  (* raise (CompilerExc "Forced"); *)
  let _ = if (String.equal (!spec_file) ("tests_specsynth/Poirot_benchmarks/Poirot_sizedbst.spec"))then 
           sizedbst := true 
          else sizedbst := false  
  in  

  

  let ast = SEL.parseLSpecFile !spec_file in 
  let string_ast = RelSpec.toString ast in 
  let () = Printf.printf "%s" string_ast in 
  let (gamma, sigma, typenames, quals, goals) = SEL.elaborateEnvs ast in 
  let goal = List.nth goals !goal_number in
  let delta = P.True in 
  let () = Printf.printf "%s" "\n INITIAL GAMMA \n " in 
  let () = List.iter (fun (vi, rti) -> Printf.printf "%s" 
                      ("\n "^(Var.toString vi)^" : "^(RefTy.toString rti))) gamma in 


  let () = Printf.printf "%s" "\n INITIAL SIGMA \n " in 
  let () = List.iter (fun (vi, rti) -> Printf.printf "%s" 
                      ("\n "^(Var.toString vi)^" : "^(RefTy.toString rti))) sigma in 

  let () = Printf.printf "%s" "\n TypeNames \n " in 
  let () = List.iter (fun tni -> Printf.printf "%s" ("\n "^tni)) typenames in 
  

  let () = Printf.printf "%s" "\n Qualifiers \n " in 
  let () = List.iter (fun (qi) -> Printf.printf "%s" 
                      ("\n "^(SpecLang.RelSpec.Qualifier.toString qi))) quals in 
  
  let specfilelist = String.split_on_char '/' !spec_file in 
  let filename = List.hd (List.rev (specfilelist)) in 
                     
  let _ = pbenchmark := filename in 
  let (size, outstring, synthterm) = Synth.Bidirectional.toplevel gamma sigma  delta typenames quals goal !learningON !bidirectional !maxPathlength !effect_filter !nestedif !pbenchmark in   
    (*run the initial environment builder*)    
    match synthterm with 
        | [] -> 
          
            let _ = Printf.originalPrint "%s" ("\n *************************") in 
            let _ = Printf.originalPrint "%s" ("\n Failed without Result : ") in 
            Printf.originalPrint "%s" ("\n ************************* : ") 
        | _ :: _ -> 
            let out_directory = "output" in
            let _ = if (not (Sys.file_exists out_directory)) then  
                    Unix.mkdir out_directory 0o777 
                  else () in 
                    
            let outfile = ("output/"^(filename)) in 
            let _ = if (Sys.file_exists outfile) then 
                        Sys.remove outfile
                    else
                        () in  

            let outchannel = open_out (outfile) in
            Printf.fprintf outchannel "%s\n" ("(*generated using Prudent *) \n"^(outstring));
            (* write something *)
            close_out outchannel;
            let _ = Printf.originalPrint "%s" ("\n *************************") in 
            let _ = Printf.originalPrint "%s" ("\n Success : ") in 
            let _ = Printf.originalPrint "%s" ("\n Number of synthesized programs : "^(string_of_int size)) in 
            
            let _ = Printf.originalPrint "%s" ("\n ************************* : ") in 
            
            ()
     
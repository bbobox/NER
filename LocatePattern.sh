#!/bin/bash

while [[ "$#" > 0 ]]; do case $1 in
  -g|--graphpath) g="$2"; shift;;
  -f|--textfilepath) f="$2"; shift;;
  -c|--UnitexLanguageConfigFolder) config="$2"; shift;;

  *) echo "Unknown parameter passed: $1"; exit 1;;
esac; shift; done


filepath=`echo $f`;
path=`echo ${filepath%.*}`;

graph=`echo $g`;
compiledgraph=`echo ${graph%.*}`;



if [ -d $path"_snt" ]
then
	rm -r $path"_snt"; 
	mkdir $path"_snt";
else
 	mkdir $path"_snt";
fi;

./UnitexToolLogger Normalize $filepath -r$config/Norm.txt --output_offsets=$path"_snt"/#normalize.out.offsets -qutf8-no-bom;

./UnitexToolLogger Grf2Fst2 $config/Graphs/Preprocessing/Sentence/Sentence.grf -y -a$config/Alphabet.txt -qutf8-no-bom;

./UnitexToolLogger Grf2Fst2 $graph -y -a$config/Alphabet.txt -qutf8-no-bom;

./UnitexToolLogger Flatten $config/Graphs/Preprocessing/Sentence/Sentence.fst2 --rtn -d5 -qutf8-no-bom;

./UnitexToolLogger Fst2Txt -t$path".snt" $config/Graphs/Preprocessing/Sentence/Sentence.fst2 -a$config/Alphabet.txt -M --input_offsets=$path"_snt"/#normalize.out.offsets --output_offsets=$path"_snt"/#normalize.out.offsets -qutf8-no-bom;

./UnitexToolLogger Grf2Fst2 $config/Graphs/Preprocessing/Replace/Replace.grf -y -a$config/Alphabet.txt -qutf8-no-bom;

./UnitexToolLogger Fst2Txt -t$path".snt" $config/Graphs/Preprocessing/Replace/Replace.fst2 -a$config/Alphabet.txt -R --input_offsets=$path"_snt"/#normalize.out.offsets --output_offsets=$path"_snt"/#normalize.out.offsets -qutf8-no-bom;

./UnitexToolLogger Tokenize $path".snt" -a$config/Alphabet.txt --input_offsets=$path"_snt"/#normalize.out.offsets --output_offsets=$path"_snt"/tokenize.out.offsets -qutf8-no-bom;

./UnitexToolLogger Dico -t$path".snt" -a$config/Alphabet.txt $config/Dela/dela-fr-public.bin $config/Dela/ajouts80jours.bin $config/Dela/motsGramf-.bin -qutf8-no-bom;

./UnitexToolLogger SortTxt $path"_snt"/dlf -l$path"_snt"/dlf.n -o$config/Alphabet_sort.txt -qutf8-no-bom;

./UnitexToolLogger SortTxt $path"_snt"/dlc -l$path"_snt"/dlc.n -o$config/Alphabet_sort.txt -qutf8-no-bom;

./UnitexToolLogger SortTxt $path"_snt"/err -l$path"_snt"/err.n -o$config/Alphabet_sort.txt -qutf8-no-bom;

./UnitexToolLogger SortTxt  $path"_snt"/tags_err -l $path"_snt"/tags_err.n -o$config/Alphabet_sort.txt -qutf8-no-bom;

./UnitexToolLogger Locate -t$path".snt" $compiledgraph".fst2" -a$config/Alphabet.txt -L --all -M -b -Y --stack-max=1000 --max_matches_per_subgraph=200 --max_matches_at_token_pos=400 --max_errors=50 -qutf8-no-bom;

./UnitexToolLogger Concord $path"_snt"/concord.ind -s12 --html -l40 -r55 --CL --merge=$path".out" -a$config/Alphabet_sort.txt -qutf8-no-bom;

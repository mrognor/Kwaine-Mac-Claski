# Kwaine-Mac-Claski
Method Kwaine-Mac-Claski using python
This repo contains 3 files. 
1. DecartovoProisvedenie.py - this files contains code to make permutations between some(2 or more) arrays
A) backend - function transform our uneven matrix into uniform matrix.
B) MakePatricMass - function make permutations between our arrays.
2. library.py - this file contains all to Kwaine method itself
A) interpret_matrix - convert all items into useful format. 
(if we have got element like "0010" and "1", this function convert "1" into "0001")
B) concat - this function concat 2 elements into one
(if its get "010" and "000" its return "0-0"
the function can only concat lines that differ by 1 element)
C) is_vershin_in_nos - this function checks for belonging to an array
D) progon - this function makes one step pf Kwaine method

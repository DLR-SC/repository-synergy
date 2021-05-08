Predicting advertised salaries
==============================

See [http://fastml.com/predicting-advertised-salaries/](http://fastml.com/predicting-advertised-salaries/) for description.

	2vw.py - convert a combined train+test file to VW format
	2vw_loc.py - the same, but for data transformed with update_locations.py
	add_dummy_salaries.py - add dummy salaries columns (2) to a test file; drop headers
	first.py - Take some lines from the input file and save them to the output file
	split.py - split a file into two randomly, line by line
	unlog_predictions.r - convert VW's log predictions back to a normal scale by taking exp()
	update_locations.py - replace location columns from the original file with parsed location (five columns) - slightly buggy
	update_locations_fixed.py - a fixed version of update_locations.py



from util.scrape_data import extract_data


searchList = {"Ben 10", "Dragon Ball Super", "Johnny Bravo"};
for item in searchList:
	f = open("output_data/"+item, "w+");
	genre, pg, rev = extract_data(item);
	f.write("Genre:\n"+str(genre));
	f.write("\n");
	# f.write("Parent's Guide:\n"+pg);
	# to do : convert map to simple file writable strings
	f.write("Parent's Guide:\n");
	for key in pg:
		f.write(str(key)+":\n");
		f.write(str(pg[key])+"\n\n");
	f.write("\n");
	f.write("User Reviews:\n"+str(rev).encode("ascii"));

# print extract_data("Ben 10");
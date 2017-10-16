
def parse_genre(attributes):
	individual_attribs = attributes.split("|");
	individual_attribs = individual_attribs[2:3];
	return individual_attribs[0].encode("ascii")[1:];


def parse_pg(info):
	PG_map = {};
	info = info.split("\n")[7:-2];
	info = [x.encode("ascii") for x in info];
	for i in range(0,len(info),2):
		try:
			PG_map[info[i]] = info[i+1];
		except IndexError:
			pass
	return PG_map;


def find_str(s, char):
	index = 0;
	if char in s:
		c = char[0];
		for ch in s:
			if ch == c:
				if s[index:index+len(char)] == char:
					return index;
			index += 1;
	return -1;


def parse_reviews(all_reviews):
	index = find_str(all_reviews, "Author:");
	all_reviews = all_reviews[index:];
	all_reviews = all_reviews.replace("\n\n", "\n");
	all_reviews = all_reviews.replace('Was the above review useful to you?', '');
	all_reviews = all_reviews.replace("useful:", "useful.\n\n");
	list_of_reviews = all_reviews.split("\n\n\n");
	list_of_reviews = list_of_reviews[:-7];
	return list_of_reviews;
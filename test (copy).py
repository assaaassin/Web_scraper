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


f = open("sample.txt").read();
# print f
list_of_reviews = [];
review_map = {};
# data = f.split("\n");
f = f.replace("\n\n", "\n");
f = f.replace('Was the above review useful to you?', '');
f = f.replace("useful:", "useful.\n\n");
# print f
list = f.split("\n\n\n");
for x in list[:-7]:
	print x
# print "\n"
# print "\n"
# for x in range(len(data)):
# 	try:
# 		# print data[x]
# 		review_map[data[x]] = {
# 			data[x+1]: data[x+2]
# 		}
# 	except IndexError:
# 		pass
# print review_map


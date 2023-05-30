# List to 3 Columns
# Takes a list of items and produces a 3 column csv
# e.g.
# Input:
# dog
# cat
# monkey
# rat 
# bat
# horse
# 
# Output:
# dog,cat,monkey,
# rat,bat,horse,
#
#
 

file = "../data/BIS_Dictionary.txt"

output = "../data/BIS_Dictionary_3col.csv"

counter = 0 

with open(output, 'a') as out:
	with open(file) as dict:
		data = []
		for line in dict:
			counter = counter + 1
			if counter < 3:
				data.append(line)
			if counter == 3:
				data.append(line)
				commacount = 0
				for x in data:
					commacount = commacount + 1
					if commacount < 3:
						out.write(x[0:-1] + ',')
					if commacount == 3:
						out.write(x[0:-1])	
				out.write('\n')
				data = []
				counter = 0


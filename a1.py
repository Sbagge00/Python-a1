import csv
import json

row_count = 0
ufo_data = []

# import the csv file: each row is a list
with open('complete.csv', 'r') as csvfile:
	complete_stream = csv.DictReader(csvfile, delimiter=',', quotechar='"')
	
	# This moves over the data file by row
	for table in complete_stream:
	
		row_count += 1
		print(table)
		
		if row_count > 10: 
			break 
		
		# This finds and replaces texts
		# table_row_dict['duration (hours/min)'] = table_row_dict['duration (hours/min)'].replace('sec.','seconds')
		
		#filter 
		#if ufo_row_dict['state'] == '':
		#	print(row_count, ufo_row_dict['city'], ufo_row_dict['state'], ufo_row_dict['country'])
		#else:
		#	continue
			
		#ufo_data.append(ufo_row_dict)

print('I found this many rows in the csv', row_count)
with open('result.json', 'w') as fp:
	print(json.dumps(complete_data, fp, sort_keys=True, indent=4, separators=(',', ': ')))
	
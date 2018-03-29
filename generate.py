import random

filename = open("/Users/sarthakbhagat/Desktop/aarogya_heatmap/data.txt","w")

for i in range (100):
	longi = random.uniform(76.83, 77.33)
	lat = random.uniform(28, 29)
	diseaseno = random.randint(0,3)
	if (diseaseno == 0):
		disease = 'dengue'
	elif (diseaseno == 1):
		disease = 'malaria'
	elif (diseaseno == 2):
		disease = 'swineflu'
	elif (diseaseno == 3):
		disease = 'cancer'
	filename.write(str(longi) + " " + str(lat) + " " + disease + "\n")
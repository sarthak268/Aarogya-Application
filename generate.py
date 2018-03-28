import random

filename = open("/Users/sarthakbhagat/Desktop/data.txt","w")

for i in range (100):
	longi = random.uniform(76.83, 77.33)
	lat = random.uniform(28, 29)
	filename.write(str(longi) + " " + str(lat) + "\n")
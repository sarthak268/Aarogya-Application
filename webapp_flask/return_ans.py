import math
import time, random
from googlesearch import search
import webbrowser



def deg2rad(deg):
	return (deg*math.pi / 180)

def distance (lat1, long1, lat2, long2):
	r = 6371
	dlat = deg2rad(lat2 - lat1)
	dlong = deg2rad(long2 - long1)
	a = math.sin(dlat/2)*math.sin(dlat/2) + math.cos(deg2rad(lat1))*math.cos(deg2rad(lat2))*math.sin(dlong/2)*math.sin(dlong/2)
	c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = r*c
	return d #in km

file = open("/Users/sarthakbhagat/Desktop/aarogya_heatmap/data.txt","r")
files = file.readlines()

for i in range (len(files)):
	files[i] = files[i].rstrip().split(' ')


def make_separate_arrays(array):
	centers = []
	
	for i in range(len(array)):
		if (array[i][2] == 'dengue'):
			numb = 0
			for j in range(len(array)):
				if (distance( float(array[i][0]), float(array[i][1]), float(array[j][0]), float(array[j][1]) ) < 50):
					numb = numb + 1
			if (numb > 101):
				centers.append(['dengue', array[i][0], array[i][1]])
		elif (array[i][2] == 'malaria'):
			numb = 0
			for j in range(len(array)):
				if (distance( float(array[i][0]), float(array[i][1]), float(array[j][0]), float(array[j][1]) ) < 50):
					numb = numb + 1
			if (numb > 11):
				centers.append(['malaria', array[i][0], array[i][1]])
		elif (array[i][2] == 'swineflu'):
					numb = 0
					for j in range(len(array)):
						if (distance( float(array[i][0]), float(array[i][1]), float(array[j][0]), float(array[j][1]) ) < 50):
							numb = numb + 1
					if (numb > 101):
						centers.append(['swineflu', array[i][0], array[i][1]])
		elif (array[i][2] == 'cancer'):
					numb = 0
					for j in range(len(array)):
						if (distance( float(array[i][0]), float(array[i][1]), float(array[j][0]), float(array[j][1]) ) < 50):
							numb = numb + 1
					if (numb > 101):
						centers.append(['cancer', array[i][0], array[i][1]])
	return (centers)

centers_for_diseases = make_separate_arrays(files)

from geopy.geocoders import Nominatim

def getplace(lon, lat):
	# give lat and lon in string
    geolocator = Nominatim()
    location = geolocator.reverse(str(lon) + ', ' + str(lat))
    return location.address

def find_nearest_doctors(lon, lat):	
	area = getplace(lon, lat)
	L = list()
	print ("These are some useful links according to your requirements : \n")
	for url in search('Doctors in ' + area, tld='es', lang='es', stop=20):
		L.append(url)
	return L

def prevention_methods(disease, methods=['GET','POST']):
	links = []
	for url in search('Prevention methods of ' + disease, tld = 'es', lang = 'es', stop = 20):
		links.append(url)
	ind = random.randint(0,len(links) - 1)	
	webbrowser.open_new_tab(links[ind])

def doctor_speciality(speciality):
	for url in search('Doctors for ' + speciality, tld='es', lang='es', stop=20):
		print(url)


a=find_nearest_doctors(76.89556727129242, 28.72403411836996)
print(a)


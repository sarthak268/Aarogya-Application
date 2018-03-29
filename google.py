

from googlesearch import search
for url in search('Doctors in ashok vihar', tld='es', lang='es', stop=20):
    print(url)
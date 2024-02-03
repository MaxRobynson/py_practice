from socket import *

adresse = 'time.nist.gov'
port = 13
localisation = (adresse, port)

service = socket(AF_INET, SOCK_STREAM)
service.connect(localisation)
octets = service.recv(100)
reponse = octets.decode('utf8')

print('chaine retourne par le service date : ', reponse)
date = reponse.split(' ')
print('date = {}, heure = {} TU', format(date[1], date[2]))
service.close()
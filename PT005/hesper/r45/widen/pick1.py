import sys,json
from pick import pick
p=int(sys.argv[1]); n=int(sys.argv[2])
rows,tries=pick(p,20261016,n)
json.dump({'seed':20261016,'rows':rows,'tries':tries},open(f'pick_{p}.json','w')); print(p,tries)

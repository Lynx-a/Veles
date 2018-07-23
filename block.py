import json
import os

def write_block (name, amount, to_whom, prev_hash = ' '):
        blockchain_dir = os.curdir + '/blockchain/'

        files = os.listdir(blockchain_dir)
        files = sorted([int(i) for i in files])

        last_file = files[-1]

        filename = str(last_file + 1)
        	    
        data = {'name' : name, 
	   'amount' : amount, 
	   'to_whom' : to_whom, 
	   'prev_hash' : prev_hash}
       
        with open(blockchain_dir + filename, 'w', encoding='Latin-1') as file:
                 json.dump(data, file, indent=4, ensure_ascii=False)


write_block(name='ivan', amount=2, to_whom='katja')





    

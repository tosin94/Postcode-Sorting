import re #regular expressions

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "tosinomotayo"
    
postCodes = []
code = []
final = []
string =''
i =0

with open('TO_CLEAN.txt','r') as f:
        
    for line in f.readlines():
        
        #todo use string methods to search for two quotes
        # each pair denotes a new line. secondly, a blank line also denotes an empty field and a new line as well
        if line.isspace():
            postCodes.append(line)
            code.append(line)
        
        if line.startswith('"'):
            string += line.replace('"','')
            string = string.replace('\n',' ')
            check = True
            
        if line.endswith('"',0,len(line) -1):
                string += line.replace('"','')
                string = string.replace('\n',' ')
                
                
                tmp = line.replace('"','') #just taking the last line
                tmp = tmp.replace('\n','')
                code.append(tmp)
                
                postCodes.append(string)
                string =''
                check = True
                test = True
            
        if not check:
            string += line.replace('\n',' ')
            check = False
        
        check = False
        
f.close()
string = "^([A-Za-z][A-Ha-hK-Yk-y]?[0-9][A-Za-z0-9]? [0-9][A-Za-z]{2}|[Gg][Ii][Rr] 0[Aa]{2})$" #may need to be re-written
#string ="^([A-Za-z][A-Ha-hK-Yk-y]?[0-9][A-Za-z0-9]? ?[0-9][A-Za-z]{2}|[Gg][Ii][Rr] ?0[Aa]{2})$"

#empty the file contents 
open('new.txt','w').close() 

with open('new.txt','w') as f:
    
    for x in code:
        #print ('testing ..... {} ++ {} ....'.format(x.isspace(),x))
        if x.isspace():
            final.append('null')
            continue
        x = x.replace('.','')
        x = x.replace('  ',' ')
        #print(x)
        if len(x) > 7:
            offset = len(x) - 7
            var = x[(offset-1):]
            if var.startswith(' '):
                var = var.replace(' ','',1)
            tmp = var
            var = re.findall(string, var)
            if len(var) == 0:
                value = (var,x,tmp)
                var = 'null'
                
                
        else:
            var = re.findall(string, x)
            if len(var) == 0: #if re.findall did not find a match. either postcode wrong or its a blank line
                value = (var,x)
                var = 'null'
                #print(value)
                
        #print('var is =>',str(var),' x is =>',x)
        final.append(var)
    
    for x in final:
        x = str(x)
        x = x.replace('[','')
        x = x.replace(']','')
        x = x.replace("'",'')
        
        #print(x)
        f.write(x)
        f.write('\n')
f.close()


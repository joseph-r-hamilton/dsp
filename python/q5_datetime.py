# Hint:  use Google to find python function

import dateutil.parser
from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
delta = dateutil.parser.parse(date_stop) - dateutil.parser.parse(date_start)
print(delta.days)

####b)  
date_start = '12312013'  
date_stop = '05282015'  
delta = datetime.strptime(date_stop,'%m%d%Y') - datetime.strptime(date_start,'%m%d%Y')
print (delta.days)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
delta = dateutil.parser.parse(date_stop) - dateutil.parser.parse(date_start)
print (delta.days)


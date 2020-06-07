from datetime import datetime
date_string = 'May 25, 2020 04AM'

date_object = datetime.strptime(date_string, '%B %d, %Y %I%p')
print(date_object)
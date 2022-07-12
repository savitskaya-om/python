import csv
import sys
from collections import defaultdict
from collections import Counter

csv.field_size_limit(sys.maxsize)
csv.field_size_limit(100000000)

vacs = list(csv.DictReader(open('C:\\py\\vacancy.csv', encoding="utf-8")))
vacs_keys = vacs[0].keys()
vacs_keys

c = Counter (row['vactitle'] for row in vacs)
c.most_common(10)

vactitles = [row['vactitle'] for row in vacs]

# Сколько вакансий, которые вам нравятся?
ilike = [row for row in vactitles if ("data scientist" in row.lower() or "analyst" in row.lower() ) and "казна" in row.lower()]
print("вакансии, которые мне нравятся ",len(ilike), ": ", [el for el in ilike] )
# За какие периоды эти вакансии?
period = set (row['created_at'][0:7] for row in vacs if row['vactitle'] in ilike)
print("эти вакансии за период: ", [el for el in period])
# Сколько вакансий с такими позициями, на которых вы работаете?
my_prof = [row for row in vactitles if "казначейств" in row.lower() or "risk" in row.lower() or "риск" in row.lower() and "юриск" not in row.lower()]
print("количество вакансий с такими позициями, на которых я работаю: ", len(my_prof))
# Сколько вакансий для аналитика данных?
analyst =[row for row in vactitles if ("аналитик данных" in row.lower() or "data analyst" in row.lower())]
print("количество вакансий для аналитика данных: ", len(analyst))
# Сколько вакансий для аналитика данных с использованием Python?
analyst_py  = [row['vactitle'] for row in vacs if (row['vactitle'] in analyst and "python" in row['vacdescription'].lower())]
print("количество вакансий для аналитика данных с использованием Python: ", len(analyst_py))
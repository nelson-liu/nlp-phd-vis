'''
Makes the graphs for the "when did you start your PhD" graph
Author : John Hewitt
'''


from functools import reduce
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(font_scale=2)

responses = {
    "Sebastian": (4,),
    "Roma": (3,),  # Late August, early September.
    "Nicholas": (2,3,4),  # Late August, early September.
    "Nelson": (1,3,2,3),
    "Michi": (2,3,2),
    "Lucy": (3,),
    "Kevin": (3,),
    "Kalpesh": (3,3,3),
    #"Eric": (),
    "Akari": (3,3),
    "Aishwarya": (4,)
}
start_date_counts = Counter(reduce(lambda x, y: x + y , responses.values()))
integer_year_map = ['1st year', '2nd year', '3rd year', '4th year']
integer_count_map = [start_date_counts[x] for x in sorted(start_date_counts.keys())]
print(integer_year_map)
print(integer_count_map)

plt.figure(figsize=(10, 10))
plt.bar(integer_year_map, integer_count_map, align='center')
plt.title("When did you start working with your LoR writers?")
plt.xlabel("Year Started Working")
plt.ylabel("Number of LoR Writers")

plt.savefig("lor_writers_start_date.png", bbox_inches="tight", pad_inches=0.1)

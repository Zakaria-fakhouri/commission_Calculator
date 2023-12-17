# commission_Calculator



INPUTS: Sum_of_Customer, Limit[i], Provision[i], Maximum
OUTPUT: commission

Explanation:
for each Limit that fits in the Sum_of_Customer: Limit[i]*Provision[i] until the Limit[i]>Sum_of_Customer

-The User Can enters a Maximum Commession-

Example:
Enter Sum of Customer: 100 
Enter limit: 50
Enter Provision: 1
----------------------------
Enter limit: 2
Worng arrangement
Enter limit: 75
Enter Provision: 2
----------------------------
Enter limit: 100
Enter Provision: 3
----------------------------
Enter a Maximum Provision(If you dont want one press 'N'): N
End Provision: 175
----------------------------


What Happens?

50*1
+(75-50)*2
+(100-75)*3
=175



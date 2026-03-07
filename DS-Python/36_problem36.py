'''Sets (great for unique values, membership, intersections in DS)

You have two lists of customer IDs:
campaign1 = [1001, 1002, 1003, 1005, 1007]campaign2 = [1002, 1004, 1005, 1006, 1008]
Find:
a) Customers in both campaigns (intersection)
b) Customers only in one campaign (symmetric difference)
c) All unique customers (union)
Do it using set operations (convert lists to sets first).'''

campaign1 = [1001, 1002, 1003, 1005, 1007]
campaign2 = [1002, 1004, 1005, 1006, 1008]

set1 = set(campaign1)
set2 = set(campaign2)

# customers in both campaigns
both_campaign = set1 & set2

# customer only in one camapaign
one_campaign = set1 ^ set2

# all uniwue customers
unique = set1 | set2

print ("a) Customers in both campaigns",both_campaign)
print ("b) Customers only in one campaign",one_campaign)
print ("c) All unique customers",unique)
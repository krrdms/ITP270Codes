from typing import List

httperrorset = { 401,403,404,500, 501, 502, 503 }


#make a copy
httperrorset_ = httperrorset.copy()

httperrorset.add(503)
httperrorset.add(504)


unofficialcodelist = [218,509]
# note update takes an iterable - list, tuple, etc
httperrorset.update(unofficialcodelist)

print("new ",httperrorset)
print("old ", httperrorset_)
#for item in httperrorset:
#    if item in httperrorset_:
#        print("found in copy:", item)
#   else:
#        print("not found in copy:", item)

diffset = httperrorset.difference(httperrorset_)
interset = httperrorset.intersection(httperrorset_)
union = httperrorset.union(httperrorset_)

print(diffset)

print(interset)

print(union)
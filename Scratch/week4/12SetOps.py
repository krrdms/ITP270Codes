#Set assignment syntax:
nvcc_campuses = {'AN', 'WO', 'AL', 'LO'}
gmu_campuses = {'ARL', 'FFX', 'PW', 'KOR'}
vt_campuses = {'BBG','NVC'}

#Set union syntax: (all unique items)
campuses = nvcc_campuses  | gmu_campuses
print(campuses)

#Set interection syntax: (items in both)
share_campuses = nvcc_campuses & gmu_campuses
print(share_campuses)

#Set difference syntax: (items in left, not in right)
diff_campuses = nvcc_campuses - gmu_campuses
print(diff_campuses)

#Check Superset:
issuperset = campuses >= nvcc_campuses
print(issuperset)

#Check Subset:
issubset = nvcc_campuses < campuses
print(issubset)

#Set update
campuses |= vt_campuses
print(campuses)


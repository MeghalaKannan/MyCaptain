nums1=[12,-7,5,64,-14]
nums2=[12,14,-95,3]
print("list1 :",nums1,"list2 :",nums2)
new_nums=list(filter(lambda x:x>0,nums1))
new_nums=list(filter(lambda x:x>0,nums2))
print("Positive nums in list1 :",new_nums,"Positive nums in list2 :",new_nums)

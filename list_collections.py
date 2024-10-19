collection_list = ['saeed','ali','vali']
print(collection_list,type(collection_list))

collection_list.pop()
print(collection_list)
collection_list[1]='ahmad'
print(collection_list)
collection_tuple= ('saeed','ali','vahid')
print(collection_tuple,type(collection_tuple))
#collection_tuple[0]='amir'
coll_range=range(6)
print(coll_range)

list_a=list(coll_range)
print(list_a)

set_val=set((1,2,(("one","two"),'a','b')))
#set_val=set((0, "one", (2, 3, 4)))
print(set_val,type(set_val))
set_val2=set('saeed')
print(set_val2,type(set_val2))

# Linear Search
# In this type of search, a sequential search is made over all items one by one. Every item is checked and if a match is found then that particular item is returned, otherwise the search continues till the end of the data structure.

# Example

def linear_search(values, search_for):
   search_at = 0
   search_res = False
# Match the value with each data element	
   while search_at < len(values) and search_res is False:
      if values[search_at] == search_for:
         search_res = True
      else:
         search_at = search_at + 1
   return search_res
l = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(l, 12))
print(linear_search(l, 91))

# Output
# When the above code is executed, it produces the following result −

# True
# False
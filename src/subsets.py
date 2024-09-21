paths = []
res = []
def potenzialsumme(arr, path, cur_sub, i):
    if i == len(arr):
        paths.append(path)    
        res.append(cur_sub)
        return 
    if path == 1:
        cur_sub.append(arr[i])

    potenzialsumme(arr, 1, cur_sub[:], i+1)
    potenzialsumme(arr, 0, cur_sub[:], i+1)

    # return [left_path, right_path]

inp = [1,2, 3]
potenzialsumme(inp, 0, [], -1)
subsets = []
print(paths)
print('res')
print(res)
print(len(res))
# for sub in paths:
#     tmp = []
#     for i, is_in in enumerate(sub):
#         if is_in:
#             tmp.append(inp[i])
#     subsets.append(tmp)
# print(subsets)

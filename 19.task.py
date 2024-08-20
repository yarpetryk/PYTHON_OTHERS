# # Create function that takes a list as a argument and returnes new list with all elements '0' moved to the end of the list.
# # e.g.
# list1 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
#
# def list_handler(input: list) -> list:
#     for el in input:
#         if el == 0:
#            input.remove(el)
#            input.append(el)
#
#     return input
#
# print(list_handler(list1))
#
# def list_handler_2(input: list) -> list:
#     new_list = [el for el in input if el!=0] + [el for el in input if el==0]
#     return new_list
#
# print(list_handler_2(list1))

sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

for key, value in sampleDict.items():
        if value == min(sampleDict.values()):
            print(key, value)


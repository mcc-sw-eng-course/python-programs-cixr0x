
alist=[]
input_file_path_name = ""
output_file_path_name = ""
def set_input_data(file_path_name):
    global input_file_path_name
    input_file_path_name = file_path_name

def set_output_data(file_path_name):
    global output_file_path_name
    output_file_path_name = file_path_name

def file_to_list():
    try:
        with open(input_file_path_name, 'r') as f:
            pList = list(map(lambda x: float(x), f.read().split(",")))
            return pList
    except ValueError:
        raise ValueError("List only supports numbers, one of the values of the file is not a number")

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

set_input_data(input("SetInputData"))
set_output_data(input("SetOutputData"))
print (input_file_path_name)
print (output_file_path_name)
print (file_to_list())



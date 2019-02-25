
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
    except FileNotFoundError:
        raise FileNotFoundError("Could not find file in path "+input_file_path_name)

def list_to_file(p_list):
    try:
        with open(output_file_path_name, 'w') as f:
            list_string = ','.join(str(e) for e in p_list)
            f.write(list_string)
    except FileNotFoundError:
        raise FileNotFoundError("Could not write file in path "+input_file_path_name)

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

def execute_merge_sort():
    alist = file_to_list()
    mergeSort(alist)
    list_to_file(alist)

inputFile = input("Input name of the file to sort")
set_input_data(inputFile)
outputFile = input("Set file name to store sorted output")
set_output_data(outputFile)

execute_merge_sort()



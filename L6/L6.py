import csv

class DataSorter(object):
    def __init__(self):
        self.lst=[]
        self.input_file_path_name =""
        self.output_file_path_name = ""
    
    def set_input_data(self, file_path_name):
        self.input_file_path_name = file_path_name     
        self.file_to_list()

    def set_output_data(self, file_path_name):
        self.output_file_path_name = file_path_name

    def file_to_list(self):
        try:
            self.lst=[]
            with open(self.input_file_path_name, 'r') as f:
                reader=csv.reader(f)
                for row in reader:
                    for item in row:
                        item=float(item)
                        self.lst.append(item)
        except ValueError:
            raise ValueError("List only supports numbers, one of the values of the file is not a number")
        except FileNotFoundError:
            raise FileNotFoundError("Could not find file in path "+self.input_file_path_name)
        return self.lst

    def list_to_file(self, p_list):
        with open(self.output_file_path_name, 'w') as f:
            writer=csv.writer(f)
            writer.writerow(self.lst)

    
    def mergeSort(self,lista):
        alist=lista
        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
    
            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)
    
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

    def execute_merge_sort(self):
        alist = self.file_to_list()
        self.mergeSort(alist)
        self.list_to_file(alist)
    

#srtDt=sortingData()
#lista=srtDt.setInputData("Book1")
#srtDt.mergeSort(lista)
#srtDt.set_output_data("SortedBook1")
#print(srtDt.lst)
'''sorter = DataSorter()
inputFile = input("Input name of the file to sort")
sorter.set_input_data(inputFile)
outputFile = input("Set file name to store sorted output")
sorter.set_output_data(outputFile)

sorter.execute_merge_sort()'''
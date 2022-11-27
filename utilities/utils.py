import csv


class utils:
    def assertloop(self, list, value):
        for i in list:
            assert i.text == value
    def read_csv_file(filename):
        datalist=[]
        csvdata=open(filename,"r")
        reader=csv.reader(csvdata)
        next(reader)
        for row in reader:
            datalist.append(row)
        return datalist



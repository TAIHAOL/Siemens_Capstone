import xlsxwriter
import xlrd

class Excel_Io(object):
    def __init__(self, Main):                          #read the excel, initialize the buttun
        self.__address = 'data.xlsx'
        self.__list = self.__import_excel()
        for x,y in self.__list:
            Main.createNewButton(x,y)

    def add(self, height, radius):                     #call when add new buttun
        self.__list.append((height, radius))
        self.save()

    def delete(self, index):                          #call when delete a buttun
        self.__list.pop(index)
        self.save()

    def save(self):
        workbook = xlsxwriter.Workbook(self.__address)
        worksheet = workbook.add_worksheet()
        lens = len(self.__list)
        for i in range(lens):
            worksheet.write('A' + str(i + 1), self.__list[i][0])
            worksheet.write('B' + str(i + 1), self.__list[i][1])
        workbook.close()

    def __import_excel(self):                         #private function
        wb = xlrd.open_workbook(self.__address)
        sheet = wb.sheet_by_index(0)
        i = 0
        list = []
        while True:
            try:
                tuple = (sheet.cell_value(i, 0), sheet.cell_value(i, 1))
                list.append(tuple)
                i+=1
            except:
                return list
        pass


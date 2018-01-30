import xlrd
import xlwt

EXCEL_NAME = 'prize.xls'

g_sheet = None
g_table = None
g_current_count = 0


def get_data(file_name=EXCEL_NAME, col=0):
    '''
    从Excel中获取相应列的所有数据
    :return: 返回Excel中的数据
    '''
    global g_sheet
    global g_table
    global g_current_count

    g_sheet = xlrd.open_workbook(file_name)
    g_table = g_sheet.sheets()[0]

    data = []
    if col < g_table.ncols:
        # 去掉空白数据
        data = [x for x in g_table.col_values(col) if x != '']
    g_current_count = len(data)
    return data


def save_data(arr):
    '''

    :param arr:
    :return:
    '''
    if not arr or len(arr) < 2:
        return

    f = xlwt.Workbook()  # 创建工作簿

    '''
    创建第一个sheet:
      sheet1
    '''
    sheet1 = f.add_sheet(u'sheet1')  # 创建sheet

    people_source = arr[0]
    people_prize = arr[1]

    for i in range(0, len(people_source)):
        sheet1.write(i, 0, people_source[i])

    for i in range(0, len(people_prize)):
        sheet1.write(i, 1, people_prize[i])

    f.save(EXCEL_NAME)  # 保存文件


if __name__ == '__main__':
    my_list = [["a", "b", "c"], ["d", "e", "f"]]
    save_data(my_list)

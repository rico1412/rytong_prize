from tkinter import *
import threading
import prize
import tkinter.messagebox as msgBox
import img
from prize_btns import *

START_PRIZE = '开始抽奖\n'
STOP_PRIZE = '停止抽奖\n\n'


def log(log_str):
    g_log_text.insert(END, log_str)
    # 显示最后一行日志
    g_log_text.see(END)


# 显示中奖人员
def show_prize(prize_people):
    people_count = len(prize_people)
    if 0 < people_count <= 8:
        luck_label(root, ftext=prize_people[-1], index=people_count - 1)
    elif 8 < people_count <= 12:
        third_label(root, ftext=prize_people[-1], index=people_count - 1)
    elif 12 < people_count <= 14:
        second_label(root, ftext=prize_people[-1], index=people_count - 1)
    elif people_count == 15:
        first_label(root, ftext=prize_people[-1], index=people_count - 1)


# 抽奖线程
class PrizeThread(threading.Thread):
    """docstring for PrizeThread"""

    def __init__(self, count, type, prize_app, f_show_btn, *args, **kwargs):
        super(PrizeThread, self).__init__(*args, **kwargs)
        self.prize_app = prize_app
        # 总共需要抽取的次数
        self.count = count
        # 当前以及抽取的次数
        self.current_count = 0
        self.type = type
        self.f_show_btn = f_show_btn
        self.__running = threading.Event()
        self.__running.set()

    def run(self):
        while self.__running.isSet():

            self.start_prize()

            self.__running.clear()

    def start_prize(self):
        self.current_count += 1

        # 递归结束
        if self.current_count > self.count:
            # 显示下一个按钮
            self.f_show_btn(self.type)
            return

        log(START_PRIZE)

        self.prize_app.start()

        self.show_options(self.prize_app.stop())

    def show_options(self, prize_item):
        prize_str = '恭喜【 ' + prize_item + ' 】获得 ' + self.get_prize_type() + '！！！\n'
        log(prize_str)
        flag = msgBox.askokcancel(
            title='提示', message=prize_str)
        if flag:
            self.stop_prize()
            self.start_prize()
        else:
            is_again = msgBox.askokcancel(title='提示', message='确定重新抽取吗？')
            if is_again:
                self.prize_app.source_arr.append(prize_item)
                self.current_count -= 1
                self.start_prize()
            else:
                self.show_options(prize_item)

    def get_prize_type(self):
        if self.type == 0 or self.type == 1:
            return "幸运奖"
        elif self.type == 2 or self.type == 3:
            return "三等奖"
        elif self.type == 4 or self.type == 5:
            return "二等奖"
        elif self.type == 6:
            return "一等奖"

    def stop_prize(self):
        log(STOP_PRIZE)
        self.prize_app.save()
        show_prize(self.prize_app.prize_people)


# 抽奖主流程
class Main(object):
    """docstring for Main"""

    def __init__(self):
        super(Main, self).__init__()
        self.click_count = -1
        self.prize_app = prize.Prize(log)

    def init_view(self):
        prize_len = len(self.prize_app.prize_people)

        # 显示中奖人员名单
        if self.prize_app.prize_people:
            for i in range(0, prize_len):
                show_prize(self.prize_app.prize_people[:i + 1])

        self.init_btn_type()
        self.click_count = self.type - 1

        # 显示抽奖按钮
        for i in range(0, self.type):
            self.show_btn(i)

    def init_btn_type(self):
        prize_len = len(self.prize_app.prize_people)

        if 0 <= prize_len < 4:
            self.type = 0
        elif 4 <= prize_len < 8:
            self.type = 1
        elif 8 <= prize_len < 10:
            self.type = 2
        elif 10 <= prize_len < 12:
            self.type = 3
        elif prize_len == 12:
            self.type = 4
        elif prize_len == 13:
            self.type = 5
        elif prize_len == 14:
            self.type = 6

    def init_prize_count(self):
        prize_len = len(self.prize_app.prize_people)

        self.count = 0
        if self.type == 0 or self.type == 1:
            self.count = 4 - prize_len % 4
        elif self.type == 2 or self.type == 3:
            self.count = 2 - prize_len % 2
        elif self.type > 3:
            self.count = 1
        print('count=' + str(self.count))
        print('type=' + str(self.type))
        print('len=' + str(prize_len))

    def start_prize_thread(self):
        PrizeThread(
            self.count,
            self.type,
            self.prize_app,
            self.show_btn
        ).start()

    def btn_click(self, type):
        self.type = type
        if self.type <= self.click_count:
            msgBox.showerror(title='提示', message='这个奖已经抽过啦！！！', icon='error')
            return

        is_start = msgBox.askokcancel(title='提示', message='确定开始抽奖吗？')
        if not is_start:
            return

        self.init_prize_count()

        try:
            self.start_prize_thread()
        except IndexError as e:
            msgBox.showerror(title='提示', message='数据错误！！！', icon='error')

        self.click_count = self.type

    def show_btn(self, click_count):
        if click_count == 0:
            # 幸运奖2 按钮
            new_prize_btn(
                root,
                frelx=31,
                frely=23,
                cmd=lambda: self.btn_click(click_count + 1),
                bg=btn_bg
            )
        elif click_count == 1:
            # 三等奖1 按钮
            new_prize_btn(
                root,
                frelx=13,
                frely=23,
                cmd=lambda: self.btn_click(click_count + 1),
                bg=btn_bg
            )
        elif click_count == 2:
            # 三等奖2 按钮
            new_prize_btn(
                root,
                frelx=18,
                frely=23,
                cmd=lambda: self.btn_click(click_count + 1),
                bg=btn_bg
            )
        elif click_count == 3:
            # 二等奖1 按钮
            new_prize_btn(
                root,
                frelx=20,
                frely=9,
                cmd=lambda: self.btn_click(click_count + 1),
                bg=btn_bg
            )
        elif click_count == 4:
            # 二等奖2 按钮
            new_prize_btn(
                root,
                frelx=32,
                frely=9,
                cmd=lambda: self.btn_click(click_count + 1),
                bg=btn_bg
            )
        elif click_count == 5:
            # 一等奖 按钮
            new_prize_btn(
                root,
                frelx=5,
                frely=23,
                cmd=lambda: self.btn_click(click_count + 1),
                bg=btn_bg
            )


main_app = Main()

root = Tk()
root.title("---融易通 2018年会 抽奖系统---")
root.resizable(width=False, height=False)  # 固定宽高

background_img = img.get_img('img/bg.png')
w = background_img.width()
h = background_img.height()
root.geometry('%dx%d+0+0' % (w, h))

# 背景图
Label(root, image=background_img).place(
    relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

btn_bg = img.get_img('img/prize_btn.png')

# 初始化界面
main_app.init_view()

# 幸运奖1 按钮
new_prize_btn(root, frelx=26, frely=23,
              cmd=lambda: main_app.btn_click(0), bg=btn_bg)

# 日志框
g_log_text = Text(root, font=("楷体", 20))
g_log_text.place(
    relx=39 / 44,
    rely=15.5 / 26,
    relwidth=6 / 44,
    relheight=17 / 26,
    anchor=CENTER
)

root.mainloop()

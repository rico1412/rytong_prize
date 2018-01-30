from tkinter import *


def new_prize_btn(root, cmd=None, frelx=0, frely=0, bg=None):
    btn = Button(
        root,
        image=bg,
        bd=0,
        command=cmd
    )

    btn.place(
        relx=frelx / 44,
        rely=frely / 26,
        relwidth=2 / 44,
        relheight=2 / 26,
        anchor=CENTER
    )

    return btn


def base_label(root, ftext, frelx=0, frely=0, frelw=1, frelh=1, ffont=('楷体', 20)):
    label = Label(
        root,
        text=ftext,
        font=ffont
    )

    label.place(
        relx=frelx / 44,
        rely=frely / 26,
        relwidth=frelw / 44,
        relheight=frelh / 26,
        anchor=S
    )

    return label


# 幸运奖Label
def luck_label(root, ftext, index):
    if index < 0 or index >= 8:
        return None

    frelx = 26 + index // 4 * 5
    frely = 15 + index % 4 * 2
    return base_label(
        root,
        ftext,
        frelx,
        frely,
        frelw=4,
        frelh=1,
        ffont=('楷体', 22)
    )


# 三等奖Label
def third_label(root, ftext, index):
    if index < 8 or index >= 12:
        return None

    frelx = 13 + (index - 8) // 2 * 5
    frely = 17 + index % 2 * 4

    return base_label(
        root,
        ftext,
        frelx,
        frely,
        frelw=4,
        frelh=3,
        ffont=('楷体', 28)
    )


# 二等奖Label
def second_label(root, ftext, index):
    if index < 12 or index >= 14:
        return None

    frelx = 14.5 + (index - 12) * 12
    frely = 11

    return base_label(
        root,
        ftext,
        frelx,
        frely,
        frelw=7,
        frelh=4,
        ffont=('楷体', 50)
    )


# 一等奖Label
def first_label(root, ftext, index):
    if index is not 14:
        return None

    count = len(ftext)

    relh = 14 / count

    labels = []
    for i in range(0, count):
        if count == 2:
            frely = 14 + i * relh
        elif count == 3:
            frely = 11.5 + i * relh
        elif count == 4:
            frely = 10.5 + i * relh

        labels.append(
            base_label(
                root,
                ftext[i],
                5,
                frely,
                frelw=6,
                frelh=relh,
                ffont=('楷体', 60)
            )
        )

    return labels

# author: Sona Nair
# date: 03/17/23

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen


def clickButton(name):
    if name == "shuffle":
        tiles.shuffle()
        buttons()
    if tiles.is_valid_move(name):
        tiles.update(name)
        buttons()


def buttons():
    # button 1
    text1 = StringVar()
    name1 = tiles.tiles[0]
    if name1 == 0:
        text1.set('')
    else:
        text1.set(str(tiles.tiles[0]))
    button1 = Button(gui, textvariable=text1, name=str(name1), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name1))
    button1.configure(bg='coral')
    gui.nametowidget(name1).configure(bg='white')

    # button2
    text2 = StringVar()
    name2 = tiles.tiles[1]
    if name2 == 0:
        text2.set('')
    else:
        text2.set(str(tiles.tiles[1]))
    button2 = Button(gui, textvariable=text2, name=str(name2), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name2))
    button2.configure(bg='coral')
    gui.nametowidget(name2).configure(bg='white')

    # button 3
    text3 = StringVar()
    name3 = tiles.tiles[2]
    if name3 == 0:
        text3.set('')
    else:
        text3.set(str(tiles.tiles[2]))
    button3 = Button(gui, textvariable=text3, name=str(name3), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name3))
    button3.configure(bg='coral')
    gui.nametowidget(name3).configure(bg='white')

    # button4
    text4 = StringVar()
    name4 = tiles.tiles[3]
    if name4 == 0:
        text4.set('')
    else:
        text4.set(str(tiles.tiles[3]))
    button4 = Button(gui, textvariable=text4, name=str(name4), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name4))
    button4.configure(bg='coral')
    gui.nametowidget(name4).configure(bg='white')

    # button 5
    text5 = StringVar()
    name5 = tiles.tiles[4]
    if name5 == 0:
        text5.set('')
    else:
        text5.set(str(tiles.tiles[4]))
    button5 = Button(gui, textvariable=text5, name=str(name5), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name5))
    button5.configure(bg='coral')
    gui.nametowidget(name5).configure(bg='white')

    # buton 6
    text6 = StringVar()
    name6 = tiles.tiles[5]
    if name6 == 0:
        text6.set('')
    else:
        text6.set(str(tiles.tiles[5]))
    button6 = Button(gui, textvariable=text6, name=str(name6), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name6))
    button6.configure(bg='coral')
    gui.nametowidget(name6).configure(bg='white')

    # button 7
    text7 = StringVar()
    name7 = tiles.tiles[6]
    if name7 == 0:
        text7.set('')
    else:
        text7.set(str(tiles.tiles[6]))
    button7 = Button(gui, textvariable=text7, name=str(name7), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name7))
    button7.configure(bg='coral')
    gui.nametowidget(name7).configure(bg='white')

    # button 8
    text8 = StringVar()
    name8 = tiles.tiles[7]
    if name8 == 0:
        text8.set('')
    else:
        text8.set(str(tiles.tiles[7]))
    button8 = Button(gui, textvariable=text8, name=str(name8),bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name8))
    button8.configure(bg='coral')
    gui.nametowidget(name8).configure(bg='white')

    # button 9
    text9 = StringVar()
    name9 = tiles.tiles[8]
    if name9 == 0:
        text9.set('')
    else:
        text9.set(str(tiles.tiles[8]))
    button9 = Button(gui, textvariable=text9, name=str(name9), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name9))
    button9.configure(bg='coral')
    gui.nametowidget(name9).configure(bg='white')

    # button 10
    text10 = StringVar()
    name10 = tiles.tiles[9]
    if name10 == 0:
        text10.set('')
    else:
        text10.set(str(tiles.tiles[9]))
    button10 = Button(gui, textvariable=text10, name=str(name10), bg='white', fg='black', font=font, height=2, width=5,command=lambda: clickButton(name10))
    button10.configure(bg='coral')
    gui.nametowidget(name10).configure(bg='white')

    # button  11
    text11 = StringVar()
    name11 = tiles.tiles[10]
    if name11 == 0:
        text11.set('')
    else:
        text11.set(str(tiles.tiles[10]))
    button11 = Button(gui, textvariable=text11, name=str(name11), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name11))
    button11.configure(bg='coral')
    gui.nametowidget(name11).configure(bg='white')

    # button 12
    text12 = StringVar()
    name12 = tiles.tiles[11]
    if name12 == 0:
        text12.set('')
    else:
        text12.set(str(tiles.tiles[11]))
    button12 = Button(gui, textvariable=text12, name=str(name12), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name12))
    button12.configure(bg='coral')
    gui.nametowidget(name12).configure(bg='white')

    # button 13
    text13 = StringVar()
    name13 = tiles.tiles[12]
    if name13 == 0:
        text13.set('')
    else:
        text13.set(str(tiles.tiles[12]))
    button13 = Button(gui, textvariable=text13, name=str(name13), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name13))
    button13.configure(bg='coral')
    gui.nametowidget(name13).configure(bg='white')

    # button 14
    text14 = StringVar()
    name14 = tiles.tiles[13]
    if name14 == 0:
        text14.set('')
    else:
        text14.set(str(tiles.tiles[13]))
    button14 = Button(gui, textvariable=text14, name=str(name14), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name14))
    button14.configure(bg='coral')
    gui.nametowidget(name14).configure(bg='white')

    # button 15
    text15 = StringVar()
    name15 = tiles.tiles[14]
    if name15 == 0:
        text15.set('')
    else:
        text15.set(str(tiles.tiles[14]))
    button15 = Button(gui, textvariable=text15, name=str(name15), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name15))
    button15.configure(bg='coral')
    gui.nametowidget(name15).configure(bg='white')

    # button 16
    text16 = StringVar()
    name16 = tiles.tiles[15]
    if name16 == 0:
        text16.set('')
    else:
        text16.set(str(tiles.tiles[15]))
    button16 = Button(gui, textvariable=text16, name=str(name16), bg='white', fg='black', font=font, height=2, width=5, command=lambda: clickButton(name16))
    button16.configure(bg='coral')
    gui.nametowidget(name16).configure(bg='white')

    # shuffle button
    textshuffle = StringVar()
    textshuffle.set('shuffle')
    nameshuffle = 'shuffle'
    buttonshuffle = Button(gui, textvariable=textshuffle, name=str(nameshuffle), bg='white', fg='black', font=font, height=1, width=5, command=lambda: clickButton(nameshuffle))
    buttonshuffle.configure(bg='coral')
    gui.nametowidget(nameshuffle).configure(bg="coral")

    button1.grid(row=1, column=1)
    button2.grid(row=1, column=2)
    button3.grid(row=1, column=3)
    button4.grid(row=1, column=4)

    button5.grid(row=2, column=1)
    button6.grid(row=2, column=2)
    button7.grid(row=2, column=3)
    button8.grid(row=2, column=4)

    button9.grid(row=3, column=1)
    button10.grid(row=3, column=2)
    button11.grid(row=3, column=3)
    button12.grid(row=3, column=4)

    button13.grid(row=4, column=1)
    button14.grid(row=4, column=2)
    button15.grid(row=4, column=3)
    button16.grid(row=4, column=4)

    buttonshuffle.grid(row=5, column=1)


if __name__ == '__main__':
    # make tiles
    tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')

    # update the window
    buttons()
    gui.mainloop()

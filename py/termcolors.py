#!/usr/bin/python
#------------------------------------------------------------------------------
#
#    Copyright 2011-2013 Andrew Lamoureux
#
#    This file is a part of alib.
#
#    alib is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#------------------------------------------------------------------------------

#experiment with: echo -e "\033[31m ROUGE \033[0m"
FOREGROUND_BLACK = '\033[30m'
FOREGROUND_RED = '\033[31m'
FOREGROUND_GREEN = '\033[32m'
FOREGROUND_YELLOW = '\033[33m'
FOREGROUND_BLUE = '\033[34m'
FOREGROUND_MAGENTA = '\033[35m'
FOREGROUND_CYAN = '\033[36m'
FOREGROUND_WHITE = '\033[37m'
FOREGROUND_GREY = '\033[39m'
FOREGROUND_ORIG = '\033[0m'

original_color_saved = 0
original_color = 0
color_stack = [FOREGROUND_ORIG]

def ColorPush(color):
    color_stack.append(color)
    print color_stack[-1]

def ColorPop():
    color_stack.pop()
    print color_stack[-1]

# only change color if its not already changed
def ColorNudge(color):
    if len(color_stack) > 1:
        ColorPush(color)

def ColorReset():
    color_stack = [FOREGROUND_ORIG]
    print color_stack[-1]

def ColorMagenta():
    ColorPush(FOREGROUND_MAGENTA)
def ColorYellow():
    ColorPush(FOREGROUND_YELLOW)
def ColorRed():
    ColorPush(FOREGROUND_RED)
def ColorGrey():
    ColorPush(FOREGROUND_GREY)
def ColorBlue():
    ColorPush(FOREGROUND_BLUE)
def ColorNormal():
    ColorPush(FOREGROUND_ORIG)

# client probably wants something like this:
# 
# import termcolors
# 
# def ColorDebug():
#     termcolors.ColorOrange()
# def ColorWarn():
#     termcolors.ColorYellow()
# def ColorError():
#     termcolors.ColorRed()
# def ColorInfo():
#     termcolors.ColorGrey()
# def ColorData():
#     termcolors.ColorBlue()
# def ColorNormal():
#     termcolors.ColorNormal()
# 
# def printInfo(msg):
#     ColorInfo()
#     print msg
#     termcolors.ColorPop()
# 
# def printError(msg):
#     ColorError()
#     print msg
#     termcolors.ColorPop()
# 
# def printWarn(msg):
#     ColorWarn()
#     print msg
#     termcolors.ColorPop()
# 
# def printDebug(msg):
#     ColorDebug()
#     print msg
#     termcolors.ColorPop()


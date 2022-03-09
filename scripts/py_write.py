

                        #********************************************************************************#
                        #                                                                                #
                        #                                  нεℓℓσ,вαтεs!                                  #
                        #                                                                                #
                        #   filename: py_writer.py                                                       #
                        #   created: 2022-03-08                                                          #
                        #   system: Windows                                                              #
                        #   version: 64bit                                                               #
                        #                                       by: Bates <https://github.com/batestin1> #
                        #********************************************************************************#
                        #                           import your librarys below                           #
                        #********************************************************************************#

import os
import sys
from printW import *


def py_write(file = sys.argv[1], hd = 'D:'):
    with open(f"../folders/{file}.txt", "a", encoding='UTF-8') as output:
        for dir, subfile, files in os.walk(hd):
            for file in files:
                output.write(f"{os.path.join(dir,file)}\n")
    printW(f"files update on {os.path.abspath(os.getcwd())}/folders/{file}.txt")


if __name__ == "__main__":
   py_write()
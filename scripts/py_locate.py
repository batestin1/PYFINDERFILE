

                        #********************************************************************************#
                        #                                                                                #
                        #                                  нεℓℓσ,вαтεs!                                  #
                        #                                                                                #
                        #   filename: py_locate.py                                                       #
                        #   created: 2022-03-08                                                          #
                        #   system: Windows                                                              #
                        #   version: 64bit                                                               #
                        #                                       by: Bates <https://github.com/batestin1> #
                        #********************************************************************************#
                        #                           import your librarys below                           #
                        #********************************************************************************#

import sys

def py_locate(search = sys.argv[2],filename = sys.argv[1]):
    with open(f"../results/query.txt", "a", encoding='UTF-8') as output:
        #variables
        hd=open(f"../folders/{filename}.txt", "r",  encoding='UTF-8')
        name = ""
        count = 0
        listFile = []
        ast = '#'
        spac = ' '

        for i in hd:
            if name == "":
                if search.lower() in i.lower():
                    count = count + 1
                    listFile.append(i)


        output.write(f"""{ast.ljust(80,ast)}
{spac.ljust(80,spac)}
search: {search}
total files found: {count}
{ast.ljust(80,ast)}
{spac.ljust(80,spac)}
files:
{"".join(listFile)}
{ast.ljust(80,ast)}
{spac.ljust(80,spac)}
""")  

if __name__ == "__main__":
   py_locate()

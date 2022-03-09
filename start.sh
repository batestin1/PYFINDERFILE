

                        #********************************************************************************#
                        #                                                                                #
                        #                                  нεℓℓσ,вαтεs!                                  #
                        #                                                                                #
                        #   filename: start.sh                                                           #
                        #   created: 2022-03-08                                                          #
                        #   system: Windows                                                              #
                        #   version: 64bit                                                               #
                        #                                       by: Bates <https://github.com/batestin1> #
                        #********************************************************************************#
rm -r folders
mkdir folders
rm -r results
mkdir results

echo "Welcome to PyFindeFile"
sleep 2
echo "First let's do an iteration on your hd, listing all the files you have"

sleep 2
echo "Enter the name for your txt file:"
read filename

sleep 2
cd scripts
python py_write.py $filename
cd ..
sleep 2

echo "Do you want to do any particular file searches? [1] - Yes | [2] - No"
read choice

if [ $choice -eq 1 ]
then
    echo "What is the file you want to fetch? "
    read search
    cd scripts
    python py_locate.py $filename $search
    sleep 2
    cd ..
    cd results
    echo """You can find your query in:"
    echo "##############################################"
    ls -l
     echo "##############################################"
    
    
    echo 
else
    cd folders
    echo """Well! Your reference file can be found here:"""
    echo "##############################################"
    ls -l
    echo "##############################################"

fi



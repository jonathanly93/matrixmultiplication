Project 2 Information
============================================================
The program is in MIPS using Mars as an emulator.

The program contains 4 buffers that will store contents 
from binary file in memory.

The program will take in files "A.bin", "B.bin", "C.bin"
which is an array of numberes in binary.

A.bin contains (1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9.1)
B.bin contains (1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2)
C.bin contains (1.3, 2.3, 3.3, 4.4, 5.3, 6.3, 7.3, 8.3, 9.3)

The output file D.bin will contain
(33.759995, 41.059998, 48.359997, 74.56, 90.86, 107.16,
115.36001, 140.66, 165.96)

The program initializes by opening and reading the contents
of A.bin, B.bin and C.bin and storing the content in 
bufferA, bufferB, and bufferC respectively.

The program then multiplies the contents in bufferA with
bufferB and outputs the file in bufferD.

The program then adds the content of bufferD and bufferC
and updates the contents back to bufferD.

The program then opens up D.bin and writes the content of
bufferD into D.bin and outputs the file back to the
current directory.



How to start the program
============================================================
1. Execute Mars4_5.jar file
2. Go File -> Open and select "Project 2"
3. Go Run -> Aseemble
4. Press the green "Go" button
5. "D.bin" should be created/updated


Extra Notes
============================================================
1. Please refer to the result.jpeg to compare the expected
   results with the results found
2. Mars should be able to run without any installation.
   Just execute the file and the program should run.
3. You can use open the readBinaryFile file in Mars
   and run the file to see the results of D.bin.
   The results however do not include any empty space,
   so you have to manually add them in.
4. The loops used to multiply the matrix in the first
   step are hard encoded according to a 3x3 matrix.
   These calculations will need to be changed slightly
   to fit a nxn matrix.
5. I added a python script that allows you to read the
   d.bin binary file. Please use the python script
   readBinaryArray. You may modifiy it if needed.



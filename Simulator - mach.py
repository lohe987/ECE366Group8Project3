# Group 8: Francis, Jonathan, Jessica
# This program is a simulator packed with both assembler and disassembler.
# Simulator has 2 modes:
#            Debug mode:  Execute program every # steps and
#                         output the state of each reg, and PC
#            Normal mode: Execute program all at once

def findParity(line):
    curRes = 0
    max = 7
    for i in range(max):
        if(line[i] == "1"):
            curRes += 1 
    curRes = curRes % 2
    if(curRes == 0):
        line = str("0" + line)
    else:
        line = str("1" + line)
    print(line) # Print the result of the given instruction
                
def fromMem(line):
    if(line > 32768):
        return line - 65536
    else:
        return line

def toMem(regVal):
    if(regVal < 0):
        return 65536  + regVal
    else:
        return regVal

def disassemble(I, Nlines):     # Check imm
    print("ECE366 Fall 2018 \nFJsquared: Disassembler")
    print("-----------------")
    # print(I)

    for i in range(Nlines):
        line = I[i]
        #print(line) # comment out when done

        if (line[1:3] == "10"): # DONE # init: 10 
            # Disassembling it to: init imm
            op = "init "
            R = "$r" + line[5] + ", "
            imm = line[3] + line[4] + line[6] + line[7]
            imm = format(int(imm, 2))
            if (line[3] == '1'): # imm = 1110 = -2; 16 - 14 = 2
                imm = 16 - int(imm)
                imm = "-" + str(imm)
            else:
                imm = str(imm)
            print(op + R + imm)

        elif (line[1:3] == '11'):   # DONE # bez: 11
            # Disassembling it to: bez imm
            op = "bez "
            R = "$r" + line[5]
            print(op + R)

        elif (line[1:5] == '0000'):  # DONE # add: 0000
            # Disassembling it to: add rx, ry
            op = "add "
            rx = "$r" + line[5] + ", "
            ry = "$r" + str(format(int(line[6] + line[7], 2)))
            print(op + rx + ry)

        elif (line[1:5] == '0001'):  # DONE # slt: 0001
            # Disassembling it to: slt rx, ry
            op = "slt "
            rx = "$r" + line[5] + ", "
            ry = "$r" + str(format(int(line[6] + line[7], 2)))
            print(op + rx + ry)

        elif (line[1:5] == '0011'):  # DONE # lw: 0011
            # Disassembling it to: lw imm (unsigned)
            op = "lw "
            rx = "$r" + line[5] + ", "
            ry = "$r" + str(format(int(line[6] + line[7], 2)))
            print(op + rx + ry)

        elif(line[1:5] == '0010'):  # DONE # sw: 0010
            # Disassembling it to: sw imm (unsigned)
            op = "sw "
            rx = "$r" + line[5] + ", "
            ry = "$r" + str(format(int(line[6] + line[7], 2)))
            print(op + rx + ry)

        elif (line[1:5] == '0100'):  # DONE # xor: 0100
            # Disassembling it to: xor rx, ry
            op = "xor "
            rx = "$r" + line[5] + ", "
            ry = "$r" + str(format(int(line[6] + line[7], 2)))
            print(op + rx + ry)

        elif (line[1:5] == '0101'):  # DONE # and: 0101
            # Disassembling it to: and rx, ry
            op = "and "
            rx = "$r" + line[5] + ", "
            ry = "$r" + str(format(int(line[6] + line[7], 2)))
            print(op + rx + ry)

        elif (line[1:5] == '0111'):  # DONE # srl: 0111
            # Disassembling it to: srl rx
            op = "srl "
            rx = "$r" + line[5] + ", "
            ry = "$r" + str(format(int(line[6] + line[7], 2)))
            print(op + rx + ry)

        elif (line[1:5] == '0110'):  # DONE # sub: 0110
            # Disassembling it to: sub rx, ry, rz
            op = "sub "
            rx = "$r" + str(line[5]) + ", "
            ry = "$r" + str(line[6]) + ", "
            rz = "$r" + str(line[7])
            print(op + rx + ry + rz)
    print("******** COMPLETE OPERATION *********")


def assemble(I, Nlines):    # Check imm
    print("ECE366 Fall 2018 FJsquared: Assembler")
    print("")

    for i in range(Nlines):
        line = I[i]
        #print() # comment out when done
        #print(line)
        line = line.replace("$", "")
        line = line.replace("r", "")
        line = line.replace("\n", "")
        line = line.replace("\t", "")

        splitLine = line.split("#")
        if (len(splitLine) == 2):
            line = splitLine[0].replace(" ", "")  # remove comments
        else:
            line = splitLine[0].replace(" ", "")

        if (line[0:4] == "init"):   # DONE init Rx, Imm P 10 00 00
            line = line.replace("init", "")
            line = line.split(",")
            R = format(int(line[0]), "01b")
            if(int(line[1]) < 0):
                line[1] = 16 + int(line[1]) #line[1] = -1 => 15 = 1111
            imm = str(format(int(line[1]), "04b"))
            op = "10"
            lineEdit = str(op + imm[0:2] + R + imm[2:4])
            findParity(lineEdit)

        elif (line[0:3] == "bez"):  # DONE
            line = line.replace("bez", "")
            R = format(int(line), "01b")
            op = "11"
            lineEdit = (op + "00" + R + "00")  # The zeros are don't cares but in for convertions use sake will be zero
            findParity(lineEdit)
            
        elif (line[0:3] == "add"):  # DONE
            line = line.replace("add", "")
            line = line.split(",")
            Rx = format(int(line[0]), "01b")
            Ry = format(int(line[1]), "02b")
            op = "0000"
            lineEdit = (op + Rx + Ry)
            findParity(lineEdit)

        elif (line[0:3] == "slt"):  # DONE
            line = line.replace("slt", "")
            line = line.split(",")
            Rx = format(int(line[0]), "01b")
            Ry = format(int(line[1]), "02b")
            op = "0001"
            lineEdit = (op + Rx + Ry)
            findParity(lineEdit)

        elif (line[0:2] == "lw"):   # DONE
            line = line.replace("lw", "")
            line = line.split(",")
            Ry = format(int(line[1]), "02b")
            Rx = format(int(line[0]), "01b")
            op = "0011"
            lineEdit = (op + Rx + Ry)
            findParity(lineEdit)

        elif (line[0:2] == "sw"):   # DONE
            line = line.replace("sw", "")
            line = line.split(",")
            Ry = format(int(line[1]), "02b")
            Rx = format(int(line[0]), "01b")
            op = "0010"
            lineEdit = (op + Rx + Ry)
            findParity(lineEdit)

        elif (line[0:3] == "xor"):  # DONE 
            line = line.replace("xor", "")
            line = line.split(",")
            Rx = format(int(line[0]), "01b")
            Ry = format(int(line[1]), "02b")
            op = "0100"
            lineEdit = (op + Rx + Ry)
            findParity(lineEdit)

        elif (line[0:3] == "and"):  # DONE
            line = line.replace("and", "")
            line = line.split(",")
            Rx = format(int(line[0]), "01b")
            Ry = format(int(line[1]), "02b")
            op = "0101"
            lineEdit = (op + Rx + Ry)
            findParity(lineEdit)

        elif (line[0:3] == "srl"):
            line = line.replace("srl", "")
            Rx = format(int(line[0]), "02b")
            op = "0111"
            lineEdit = (op + "0" + Rx)  # The zero is a don't care
            findParity(lineEdit)

        elif (line[0:3] == "sub"):  # DONE
            line = line.replace("sub", "")
            line = line.split(",")
            Rx = format(int(line[0]), "01b")
            Ry = format(int(line[1]), "01b")
            Rz = format(int(line[2]), "01b")
            op = "0110"
            lineEdit = (op + Rx + Ry + Rz)
            findParity(lineEdit)

        else:
            print("INSTRUCTION DOES NOT EXIST, SKIPED")
    print("******** COMPLETE OPERATION *********")



def simulate(I, Nsteps, debug_mode, Memory):
    print("ECE366 Fall 2018 ISA Design: Simulator")
    print()
    PC = 0  # Program-counter
    DIC = 0
    Reg = [0, 0, 0, 0]  # 4 registers, init to all 0
    print("******** Simulation starts *********")
    finished = False
    while (not (finished)):
        fetch = I[PC]
        DIC += 1

        #if (debug_mode):
        #    print("\n***!!!!! NEXT INSTRUCTION !!!!!***")
        #   print(fetch)
        
        if (fetch[1:3] == "10"): # DONE # init: 10 
            R = int(fetch[5])
            imm = fetch[3] + fetch[4] + fetch[6] + fetch[7]
            imm = int(format(int(imm,2)))

            if (fetch[3] == '1'):
                imm = -16 + imm
            Reg[R] = int(imm)
            PC += 1
            
        elif (fetch[1:3] == '11'):   # DONE # bez: 11
            R = int(fetch[5])
            if (Reg[0] == 0):
                PC = PC + Reg[R]
                if (Reg[R] == 0):   # Dead loop
                    finished = True
            else:
                PC += 1
                
        elif (fetch[1:5] == '0000'):  # DONE # add: 0000
            Rx = int(fetch[5])
            Ry = int(fetch[6] + fetch[7], 2)
            Reg[Ry] = Reg[Rx] + Reg[Ry]
            PC += 1
            
        elif (fetch[1:5] == '0001'):  # DONE # slt: 0001
            Rx = int(fetch[5])
            Ry = int(fetch[6] + fetch[7], 2)
            compVal = Reg[Ry] - Reg[Rx]
            if (compVal > 0):
                Reg[Rx] = 1
            else:
                Reg[Rx] = 0
            PC += 1
            
        elif (fetch[1:5] == '0100'):  # DONE # xor: 0100
            Rx = int(fetch[5])
            Ry = int(fetch[6] + fetch[7], 2)
            Reg[Rx] = Reg[Rx] ^ Reg[Ry]
            PC += 1
            
        elif (fetch[1:5] == '0011'):  # DONE # lw: 0011
            Rx = int(fetch[5])
            Ry = int(fetch[6] + fetch[7], 2)
            Reg[Ry] = fromMem(Memory[Reg[Rx]])
            PC += 1
            
        elif(fetch[1:5] == '0010'):  # DONE # sw: 0010
            Rx = int(fetch[5])
            Ry = int(format(int(fetch[6] + fetch[7], 2)))
            Memory[int(Reg[Ry])] = toMem(Reg[Rx])
            PC += 1
            
        elif (fetch[1:5] == '0101'):  # DONE # and: 0101
            Rx = int(fetch[5])
            Ry = int(fetch[6] + fetch[7], 2)
            Reg[Rx] = Reg[Rx] and Reg[Ry]
            PC += 1
            
        elif (fetch[1:5] == '0111'):  # DONE # srl: 0111
            Rx = int(fetch[5])
            Ry = int(fetch[6] + fetch[7], 2)
            Reg[Rx] = Reg[Rx] >> 1
            PC += 1
            
        elif (fetch[1:5] == '0110'):  # DONE # sub: 0110
            Rx = int(fetch[5])
            Ry = int(fetch[6])
            Rz = int(fetch[7])
            Reg[Rz] = int(Reg[Rx]) - int(Reg[Ry])
            PC += 1
            
        if (debug_mode):
            if ((DIC % Nsteps) == 0):  # print stats every Nsteps
                print("Registers R0-R3: ", Reg)
                print("Program Counter : ", PC)
                # print("Memory: ",Memory)   # Dont print memory atm.
                # Too much cluster
                input("Press any enter to continue")
                print()
        elif (finished) :
            print("Program success")
        else:
            continue
        if(not debug_mode):
            print("******** Simulation finished *********")
            print("Dynamic Instr Count: ", DIC)
            print("Registers R0-R3: ", Reg)
            print("Memory :[", end = '')
            for i in range(len(Memory)):
                print(fromMem(Memory[i]), end='')
                if(i != len(Memory) - 1):
                    print(", ", end='')
            print("]")
            print("PC: ", PC)
        else:
            if ((DIC % Nsteps) == 0):  # print stats every Nsteps
                print("******** Simulation finished *********")
                print("Dynamic Instr Count: ", DIC)
                print("Registers R0-R3: ", Reg)
                print("Memory :[", end='')
                for i in range(len(Memory)):
                    print(fromMem(Memory[i]), end='')
                    if (i != len(Memory) - 1):
                        print(", ", end='')
                print("]")
                print("PC: ", PC)
        data = open("d_mem.txt", "w")  # Write data back into d_mem.txt
        for i in range(len(Memory)):
            data.write(format(Memory[i], "016b"))
            data.write("\n")
        data.close()
    while(True):
        print("\nDo you want to go back to the menu? (Y/N)")
        prompt = input(">>")
        if(prompt == 'y'):
            return True
        elif(prompt == 'n'):
            print("\nGoodbye!\n")
            return False
        else:
            print("Unknown selection. Please pick Y or N.\n")


def main():
    Memory = []
    debug_mode = False  # is machine in debug mode?
    Nsteps = 3  # How many cycle to run before output statistics
    Nlines = 0  # How many instrs total in input.txt
    Instruction = []  # all instructions will be stored here
    askAgain = True
    while(askAgain):
        print("\nWelcome to FJsquared's ISA Menu")
        print(" 1 = simulator")
        print(" 2 = disassembler")
        print(" 3 = assembler")
        mode = int(input("Please enter the mode of program: "))
        print("\nMode selected: ", end="")
        if (mode == 1):
            print("Simulator")
            print("\nSimulator has 2 modes: ")
            print(" 1] Normal execution")
            print(" 2] Debug mode")
            simMode = int(input("Please select simulator's mode: "))
            if (simMode == 1):
                debug_mode = False
            elif (simMode == 2):
                debug_mode = True
                Nsteps = int(input("Debug Mode selected. Please enter # of debugging steps: "))
            else:
                print("Error, unrecognized input. Try again.\n")
                askAgain = True
                mode = 4
        elif (mode == 2):
            print("Disassembler")
        elif (mode == 3):
            print("Assembler")
        else:
            print("\nError. Unrecognized mode. Try Again\n")
            askAgain = True
        # mode = 1            # 1 = Simulation
        # 2 = disassembler
        # 3 = assembler
        # Which files are we looking at?
        askProgram = True
        program = 0
        while(askProgram):
            print("\nPlease input which program we are using: (1 or 2)")
            program = input(">>")
            if(program == '1'):
                file1 = "p3_group_8_p1_imem.txt"
                askProgram = False
            elif(program == '2'):
                file1 = "p3_group_8_p2_imem.txt"
                askProgram = False
            else:
                print("\nError. Unrecognized program. Try again")
        program = 'A'
        askProgram = True
        while (askProgram):
            print("\nPlease input which data memory we are using: (A or B or C or D)")
            program == input(">>")
            if (program == 'A'):
                file2 = "p3_group_8_dmem_A.txt"
                askProgram = False
            elif (program == 'B'):
                file2 = "p3_group_8_dmem_B.txt"
                askProgram = False
            elif (program == 'C'):
                file2 = "p3_group_8_dmem_C.txt"
                askProgram = False
            elif (program == 'D'):
                file2 = "p3_group_8_dmem_D.txt"
                askProgram = False
            else:
                print("\nError. Unrecognized data memory. Try again")

        instr_file = open(file1, "r")
        data_file = open(file2, "r")

        for line in instr_file:  # Read in instr
            if (line == "\n" or line[0] == '#'):  # empty lines,comments ignored
                continue
            line = line.replace("\n", "")
            Instruction.append(line)  # Copy all instruction into a list
            Nlines += 1

        for line in data_file:  # Read in data memory
            if (line == "\n" or line[0] == '#'):  # empty lines,comments ignored
                continue
            Memory.append(int(line, 2))

        if (mode == 1):  # Check wether to use disasembler or assembler or simulation
            askAgain = simulate(Instruction, Nsteps, debug_mode, Memory)
        elif (mode == 2):
            askAgain = disassemble(Instruction, Nlines)
        elif (mode == 3):
            askAgain = assemble(Instruction, Nlines)

    instr_file.close()
    data_file.close()
    exit()


if __name__ == "__main__":
    main()


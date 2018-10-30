# Group 8: Francis, Jonathan, Jessica
# This program is a simulator packed with both assembler and disassembler.
# Simulator has 2 modes:
#            Debug mode:  Execute program every # steps and
#                         output the state of each reg, and PC
#            Normal mode: Execute program all at once

def disassemble(I, Nlines):
    print("ECE366 Fall 2018 \nFJsquared: Disassembler")
    print("-----------------")
    # print(I)

    for i in range(Nlines):
        line = I[i]
        print(line)

        if (line[1:3] == "10"):  # init: 10
            # Splitting the line to: P|1 0|I I|Rx| I I
            binaryInput = [line[0], line[1:3], line[3:5], line[5], line[6:8]]

            # Disassembling it to: init imm
            disassembled[0] = "init "
            disassembled[1] = "$r" + str(int(binaryInput[3])) + ", "
            immediate = str(binaryInput[2]) + str(binaryInput[4])
            if (immediate[0] == '1'):
                imm = -16 + int(format(int(immediate, 2)))
                imm = str(int(imm))
            else:
                imm = str(int(format(int(immediate, 2))))
            disassembled[2] = imm

            print(disassembled[0] + disassembled[1] + disassembled[2])

        elif (line[1:3] == '11'):  # bez: 11
            # Splitting the line to: P|1 0|X X|Rx|X X
            binaryInput = [line[0], line[1:3], line[3:5], line[5], line[6:8]]

            # Disassembling it to: bez imm
            disassembled[0] = "bez "
            disassembled[1] = "$r" + binaryInput[3]

            print(disassembled[0] + disassembled[1])

        elif (line[1:5] == '0000'):  # add: 0000
            # Splitting the line to: P|0 0 0 0|Rx|Ry Ry
            binaryInput = [line[0], line[1:5], line[5], line[6:8]]

            # Disassembling it to: add rx, ry
            disassembled[0] = "add "
            rx = str(int(format(int(binaryInput[2], 2))))
            ry = str(int(format(int(binaryInput[3], 2))))
            disassembled[1] = "$r" + rx + ", "
            disassembled[2] = "$r" + ry + "\t"

            print(disassembled[0] + disassembled[1] + disassembled[2])

        elif (line[1:5] == '0001'):  # slt: 0001
            # Splitting the line to: P|0 0 0 1|Rx|Ry Ry
            binaryInput = [line[0], line[1:5], line[5], line[6:8]]

            # Disassembling it to: slt rx, ry
            disassembled[0] = "slt "
            rx = str(int(format(int(binaryInput[1], 2))))
            ry = str(int(format(int(binaryInput[2], 2))))
            disassembled[1] = "$r" + rx + ", "
            disassembled[2] = "$r" + ry

            print(disassembled[0] + disassembled[1] + disassembled[2])

        elif (line[1:5] == '0011'):  # lw: 0011
            # Splitting the line to: P|0 0 1 1|Rx|Ry Ry
            binaryInput = [line[0], line[1:5], line[5], line[6:8]]

            # Disassembling it to: lw imm (unsigned)
            disassembled[0] = "lw "
            disassembled[2] = "$r" + str(int(format(int(binaryInput[2], 2))))
            disassembled[1] = "$r" + str(int(format(int(binaryInput[3], 2)))) + ", "

            print(disassembled[0] + disassembled[1] + disassembled[2])

        elif(line[1:5] == '0010'):  # sw: 0010
                # Splitting the line to: P|0 0 1 0|Rx|Ry Ry
                binaryInput = [line[0], line[1:5], line[5], line[6:8]]

                # Disassembling it to: sw imm (unsigned)
                disassembled[0] = "sw "
                disassembled[2] = "$r" + str(int(format(int(binaryInput[2], 2))))
                disassembled[1] = "$r" + str(int(format(int(binaryInput[3], 2)))) + ", "

                print(disassembled[0] + disassembled[1] + disassembled[2])

        elif (line[1:5] == '0100'):  # xor: 0100
            # Splitting the line to: P|0 1 0 0|Rx|Ry Ry
            binaryInput = [line[0], line[1:5], line[5], line[6:8]]

            # Disassembling it to: xor rx, ry
            disassembled[0] = "xor "
            rx = str(int(format(int(binaryInput[2], 2))))
            ry = str(int(format(int(binaryInput[3], 2))))
            disassembled[1] = "$r" + rx + ", "
            disassembled[2] = "$r" + ry

            print(disassembled[0] + disassembled[1] + disassembled[2])

        elif (line[1:5] == '0101'):  # and: 0101
            # Splitting the line to: P|0 1 0 1|Rx|Ry Ry
            binaryInput = [line[0], line[1:5], line[5], line[6:8], line[8:]]

            # Disassembling it to: and rx, ry
            disassembled[0] = "and "
            rx = str(int(format(int(binaryInput[2], 2))))
            ry = str(int(format(int(binaryInput[3], 2))))
            disassembled[1] = "$r" + rx + ", "
            disassembled[2] = "$r" + ry

            print(disassembled[0] + disassembled[1] + disassembled[2])

        elif (line[1:5] == '0111'):  # srl: 0111
            # Splitting the line to: P|0 1 1 1|X| Rx Rx
            binaryInput = [line[0:0], line[1:5], line[5], line[6:7]]

            # Disassembling it to: srl rx
            disassembled[0] = "srl "
            disassembled[1] = "$r" + str(int(format(int(binaryInput[3], 2))))

            print(disassembled[0] + disassembled[1])

        elif (line[1:5] == '0110'):  # sub: 0110
            # Splitting the line to: P|0 1 1 1|Rx|Ry|Rz
            binaryInput = [line[0], line[1:5], line[5], line[6], line[7]]

            # Disassembling it to: sub rx, ry, rz
            disassembled[0] = "sub "
            disassembled[1] = "$r" + str(binaryInput[2]) + ","
            disassembled[2] = "$r" + str(binaryInput[3]) + ","
            disassembled[3] = "$" + str(binaryInput[4])

            print(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])


def assemble(I, Nlines):
    print("ECE366 Fall 2018 FJsquared: Assembler")
    print("")

    for i in range(Nlines):
        line = I[i]
        print()
        print(line)
        line = line.replace("$", "")
        line = line.replace("r", "")
        line = line.replace("\n", "")
        line = line.replace("\t", "")

        splitLine = line.split("#")
        if (len(splitLine) == 2):
            line = splitLine[0].replace(" ", "")  # remove comments
        else:
            line = splitLine[0].replace(" ", "")

        if (line[0:4] == "init"):
            line = line.replace("init", "")
            line = line.split(",")
            R = format(int(line[0]), "02b")
            imm = str(format(int(line[1]), "04b"))
            op = "10"
            print("P " + op + " " + imm[0:3] + " " + R + " " + imm[2:4])

        elif (line[0:3] == "bez"):
            line = line.replace("bez", "")
            R = format(int(line), "01b")
            op = "11"
            print("P " + op + " XX " + R + " XX ")

        elif (line[0:3] == "add"):
            line = line.replace("add", "")
            line = line.split(",")
            Rx = format(int(line[0]), "01b")
            Ry = format(int(line[1]), "02b")
            op = "0000"
            print("P " + op + " " + Rx + " " + Ry)

        elif (line[0:3] == "slt"):
            line = line.replace("slt", "")
            line = line.split(",")
            Ry = format(int(line[0]), "01b")
            Rx = format(int(line[1]), "02b")
            op = "0001"
            print("P " + op + " " + Rx + " " + Ry)

        elif (line[0:2] == "lw"):
            line = line.replace("lw", "")
            line = line.split(",")
            Ry = format(int(line[0]), "02b")
            Rx = format(int(line[1]), "01b")
            op = "0011"
            print("P " + op + " " + Rx + " " + Ry)

        elif (line[0:2] == "sw"):
            line = line.replace("sw", "")
            line = line.split(",")
            Ry = format(int(line[0]), "02b")
            Rx = format(int(line[1]), "01b")
            op = "0010"
            print("P " + op + " " + Rx + " " + Ry)

        elif (line[0:3] == "XOR"):
            line = line.replace("XOR", "")
            line = line.split(",")
            Rx = format(int(line[0]), "01b")
            Ry = format(int(line[1]), "02b")
            op = "0100"
            print("P " + op + " " + Rx + " " + Ry)

        elif (line[0:3] == "AND"):  # why "slt0" instead of "sltR0" ?
            line = line.replace("AND", "")
            line = line.split(",")
            Rx = format(int(line[0]), "01b")
            Ry = format(int(line[1]), "02b")
            op = "0101"
            print("P " + op + " " + Rx + " " + Ry)

        elif (line[0:3] == "srl"):
            line = line.replace("srl", "")
            line = line.split(",")
            Rx = format(int(line[0]), "02b")

            op = "0111"
            print("P " + op + " X " + Rx)

        elif (line[0:3] == "sub"):
            line = line.replace("sub", "")
            line = line.split(",")
            Rx = str(int(line[0]))
            Ry = str(int(line[1]))
            Rz = str(int(line[2]))

            op = "0110"
            print("P " + op + " " + Rx + " " + Ry + " " + Rz)

        else:
            print("PLEASE FIX")


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

        if (debug_mode):
            print(fetch)
        fetch = fetch.replace("$", "")  # Delete all the '$' to make things simpler
        fetch = fetch.replace("r", "")  # Delete all the 'r' to make things simpler
        fetch = fetch.replace(" ", "")  # Delete all the ' ' to make things simpler
        fetch = fetch.replace("\t", "")  # Delete all the '\t' to make things simpler

        splitLine = fetch.split("#")
        if (len(splitLine) == 2):
            fetch = splitLine[0].replace(" ", "")  # remove comments
        else:
            fetch = splitLine[0].replace(" ", "")

        if (fetch[0:4] == "init"):  # DONE

            # Extracting data values
            fetch = fetch.replace("init", "")
            fetch = fetch.split(",")
            R = int(fetch[0])
            imm = int(fetch[1])
            Reg[R] = imm
            PC += 1
        elif (fetch[0:3] == "bez"):  # DONE
            fetch = fetch.replace("bez", "")
            R = int(fetch)
            if (Reg[0] == 0):
                PC = PC + R
            else:
                PC += 1
        elif (fetch[0:3] == "add"):  # DONE
            fetch = fetch.replace("add", "")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Ry] = Reg[Rx] + Reg[Ry]
            PC += 1
        elif (fetch[0:3] == "slt"):  # DONE
            fetch = fetch.replace("slt", "")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            compVal = Reg[Ry] - Reg[Rx]


            if (compVal > 0):
                Reg[Rx] = 1

            else:
                Reg[Rx] = 0

                PC += 1
        elif (fetch[0:3] == "XOR"):  # DONE
            fetch = fetch.replace("XOR", "")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] ^ Reg[Ry]
            PC += 1
        elif (fetch[0:2] == "lw"):  # DONE
            fetch = fetch.replace("lw", "")
            fetch = fetch.split(",")
            Ry = int(fetch[0])
            Rx = int(fetch[1])
            Reg[Rx] = Memory[Ry]
            PC += 1
        elif (fetch[0:2] == "sw"):  # DONE
            fetch = fetch.replace("sw", "")
            fetch = fetch.split(",")
            Ry = int(fetch[0])
            Rx = int(fetch[1])
            Memory[Reg[Ry]] = Reg[Rx]
            PC += 1
        elif (fetch[0:4] == "slt0"):  # why "slt0" instead of "sltR0" ?
            # --> because all the 'R' is deleted at fetch to make things simplier.
            fetch = fetch.replace("slt0 ", "")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            if (Reg[Rx] < Reg[Ry]):
                Reg[0] = 1
            else:
                Reg[0] = 0
            PC += 1
        elif (fetch[0:4] == "bez0"):
            fetch = fetch.replace("bez0 ", "")
            fetch = fetch.split(",")
            imm = int(fetch[0])
            if (Reg[0] == 0):
                PC = PC + imm
            else:
                PC += 1
        elif (fetch[0:4] == "jump"):
            fetch = fetch.replace("jump ", "")
            fetch = fetch.split(",")
            imm = int(fetch[0])
            if (imm == 0):
                finished = True
            else:
                PC = PC + imm

        elif (fetch[0:6] == "finish"):
            finished = True

        if (debug_mode):
            if ((DIC % Nsteps) == 0):  # print stats every Nsteps
                print("Registers R0-R3: ", Reg)
                print("Program Counter : ", PC)
                # print("Memory: ",Memory)   # Dont print memory atm.
                # Too much cluster
                input("Press any key to continue")
                print()
        else:
            continue

        print("******** Simulation finished *********")
        print("Dynamic Instr Count: ", DIC)
        print("Registers R0-R3: ", Reg)
        # print("Memory :",Memory)

        data = open("d_mem.txt", "w")  # Write data back into d_mem.txt
        for i in range(len(Memory)):
            data.write(format(Memory[i], "016b"))
            data.write("\n")
        data.close()


def main():
    instr_file = open("i_mem.txt", "r")
    data_file = open("d_mem.txt", "r")
    Memory = []
    debug_mode = False  # is machine in debug mode?
    Nsteps = 3  # How many cycle to run before output statistics
    Nlines = 0  # How many instrs total in input.txt
    Instruction = []  # all instructions will be stored here
    print("Welcome to ECE366 ISA sample programs")
    print(" 1 = simulator")
    print(" 2 = disassembler")
    print(" 3 = assembler")
    mode = int(input("Please enter the mode of program: "))
    print("Mode selected: ", end="")
    if (mode == 1):
        print("Simulator")
        print("Simulator has 2 modes: ")
        print(" 1] Normal execution")
        print(" 2] Debug mode")
        simMode = int(input("Please select simulator's mode: "))
        if (simMode == 1):
            debug_mode = False
        elif (simMode == 2):
            debug_mode = True
            Nsteps = int(input("Debug Mode selected. Please enter # of debugging steps: "))
        else:
            print("Error, unrecognized input. Exiting")
            exit()
    elif (mode == 2):
        print("Disassembler")
    elif (mode == 3):
        print("Assembler")
    else:
        print("Error. Unrecognized mode. Exiting")
        exit()
    # mode = 1            # 1 = Simulation
    # 2 = disassembler
    # 3 = assembler
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
        simulate(Instruction, Nsteps, debug_mode, Memory)
    elif (mode == 2):
        disassemble(Instruction, Nlines)
    else:
        assemble(Instruction, Nlines)

    instr_file.close()
    data_file.close()


if __name__ == "__main__":
    main()


import os

opdict ={
    "lw": "100011",
    "sw": "101011",
    "j":  "000010",
    "beq": "000100",
    "jal":"000011",
    "addi":"001000",
    "ori" : "001101"
}

regdict =	{
  "$s0": "10000",
  "$s1": "10001",
  "$s2": "10010",
  "$s3": "10011",
  "$s4": "10100",
  "$s5": "10101",
  "$t2": "01010",
  "$t0": "01000",
  "$t1": "01001",
  "$t3": "01011",
  "$t4": "01100",
  "$t5": "01101",
  "$t6" : "01110",
  "$ra": "11111"
}

functdict = {
    "add": "100000",
    "and": "100100",
    "or": "100101",
    "sll": "000000",
    "slt": "101010",
    "jr": "001000"
}

def get_opcode (inst):
    for j in opdict:
        if j== inst:
            op=opdict[j]
    return op

def funct (inst):
    for j in functdict:
        if j== inst:
            fun=functdict[j]
    return fun

def registers (rx):
    for j in regdict:
        if j == rx:
            rx=regdict[j]
    return rx


def dec_to_bin(n,bits):
    n= int(n)
    s= bin(n & int("1"*bits,2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

def open_file(file):
    
    print(file)
    with open('inst_mem.txt','w') as f:
        address=0
        line=0
        labeldict={}
        #i=get_labels(file)
        for i in file.readlines():
                    line=line+1
                    x=i.find(':')
                    print(x)
                    if x!= -1:
                        labeldict[i[:x]]=line-1
                        print(labeldict)
                        #i=i[x+2:]
                        #print(i)
                        #print (line)
        file.seek(0)

        for i in file:
                line = line+1
                x=i.find(':')
                if x != -1:
                    i=i[x+2:]
                """for i in file:
                    
                    print(i)
                    line=line+1
                    print("loop")
                    x=i.find(':')
                    print(x)
                    if x!= -1:
                        labeldict[i[:x]]=line-1
                        print(labeldict)
                        i=i[x+2:]
                        print(x)
                        print (line)"""
                
            
                address=address+1
                print (i)
                statement = i.split()
                """if statement[0] != "add" and statement[0] != "lw" and statement [0] != "and" and statement [0] != "addi" and statement [0] != "j" and statement [0] != "sw" and statement [0] != "beq" and statement [0] != "sll" and statement [0] != "slt" and statement [0] != "or" and statement [0] != "jr" and statement [0] != "jal" and statement [0] != "ori":
                    print("l1")
                else:
                    print("inst")"""
                
                if i == "":
                    break
                else:
                    instr = statement[0]

                    #R-FORMAT
                    if instr == "add" or instr =="and" or instr =="or" or instr =="sll" or instr =="slt" or instr =="jr":
                        opcode="000000"
                        print("R-form")
                        stat2 = statement[1].split(',')

                        if instr == "sll":
                                shamt1=dec_to_bin(int(stat2[2]),5)
                                shamt=str(shamt1) 
                                rs="00000"
                                rt=stat2[1]
                                rd=stat2[0]
                                rt=registers(rt)
                                rd=registers(rd)
                                func=funct(instr)

                        elif instr == "add" or instr =="and" or instr =="or" or instr =="slt":
                                func=funct(instr)
                                shamt="00000"
                                rs=stat2[1]
                                rt=stat2[2]
                                rd=stat2[0]
                                rs=registers(rs)
                                rt=registers(rt)
                                rd=registers(rd)
                            
                        elif instr == "jr":
                                func=funct(instr)
                                rs=statement[1]
                                rs=registers(rs)
                                rt="00000"
                                rd="00000"
                                shamt="00000"

                        #List has all the instruction joined together
                        instList =[opcode,rs,rt,rd,shamt,func]
                        for x in instList:
                                print(x)
                        seperator = ''
                        f.write(seperator.join(instList))
                        f.write("\n")
                        print(seperator.join(instList))

                    #I-FORMAT
                    elif instr == "lw" or instr == "sw" or instr =="beq" or instr == "addi" or instr =="ori":
                            """if instr =="beq":
                                print("I-form")
                                stat2=statement[1].split(',') 
                                rs=stat2[0]
                                rt=stat2[1]
                                immediate=stat2[2]
                                instList =[opcode,rs,rt,immediate]
                                print(immediate)
                                print (stat2[1])
                                print("****")"""
                            if instr == "addi" or instr == "ori":
                                stat2=statement[1].split(',')
                                rt=stat2[0]
                                rt=registers(rt)
                                rs=stat2[1]
                                rs=registers(rs)
                                opcode = get_opcode(instr)
                                immediate=stat2[2]
                                immediate=dec_to_bin(str(immediate),16)
                                instList =[opcode,rs,rt,immediate]
                                seperator = ''
                                print(seperator.join(instList))
                                f.write(seperator.join(instList))
                                f.write("\n")
                                print(immediate)

                            elif instr == "beq":
                                stat2=statement[1].split(',')
                                rs=stat2[0]
                                rs=registers(rs)
                                rt=stat2[1]
                                rt=registers(rt)
                                opcode=get_opcode(instr)
                                label=stat2[2]
                                addressnew=0
                                for j in labeldict:
                                    if label ==j:
                                        addressnew=labeldict[j]
                                        print(addressnew)
                                        print(address)
                                        print(addressnew-line-1)
                                        immediate=str(dec_to_bin(addressnew-address,16)) 
                                        print(immediate)
                                instList =[opcode,rs,rt,immediate]
                                seperator = ''
                                print(seperator.join(instList))
                                f.write(seperator.join(instList))
                                f.write("\n")
                            else:
                                print("I-lw or sw")
                                stat2=statement[1].split(',') 

                                rt=stat2[0]
                                rt=registers(rt)

                                stat3=stat2[1].split('(')

                                immediate1=dec_to_bin(int(stat3[0]),16)
                                immediate=str(immediate1) 

                                stat4=stat3[1].split(')') #3shan ntal3 el reg lwa7do mn gher ) fel akher

                                rs=stat4[0]
                                rs=registers(rs)
                        
                                if instr == "lw":
                                    opcode = get_opcode(instr)
                                elif instr == "sw":
                                    opcode = get_opcode(instr)
                                instList =[opcode,rs,rt,immediate]
                                seperator = ''
                                print(seperator.join(instList))
                                f.write(seperator.join(instList))
                                f.write("\n")
                                

                    #J-FORMAT
                    elif instr == "j" or instr == "jal":
                            print("J-form")
                            if instr =="j":
                                opcode = get_opcode(instr)
                            elif instr == "jal":
                                opcode = get_opcode(instr)
                            
                            label=statement[1]
                            addressnew=0
                            flag=0

                            for j in labeldict:
                                if label == j:
                                    print(j)
                                    addressnew=labeldict[j]
                                    flag=1
                            if flag ==0:
                                print("no label")
                            """for i in file:
                                x=i.find(':')
                                if x!= -1:
                                    i=i[x+2:]
                                    print(x)
                                statement = i.split()
                                if statement[0]==label:
                                    print("yarab")
                                    addressnew=flag+address
                                    break
                                flag=flag+1"""
                            addressnew=str(dec_to_bin(addressnew,26))
                            instList =[opcode,addressnew]
                            print(seperator.join(instList))
                            print(address)
                            print(addressnew)
                            f.write(seperator.join(instList))
                            f.write("\n")
                
    os.system('cmd/c "cd D:\College projects\processor\mips files& vsim -c -do sim.do work.mips_collec"')
    #os.system('cmd/c "cd D:\backend"')
    #os.system("vsim -c -do sim.do test_bench_add" )
    #os.system('vsim -c -do sim.do test_bench_add '\
       # 'D:\College projects\processor/test_bench_add')
    #os.system('cmd/c "cd D:\backend\examples& vsim -c -do "run -all" work.test_bench_add" ')


 #'vsim -c -do "run -all" '\
                          #'F:/3rd-CSE/1stTerm/COII/COIIProjects/Modeltech_pe_edu_10.4a/examples/work.MIPS_cpu'
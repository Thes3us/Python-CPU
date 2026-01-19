# Python-CPU
A CPU with ALU, CU, counter, 8 bytes of registers. Interprets instruction in a binary stream
## ISA
### INSTRUCTION SET
format: 00 000 000
- 00 XXX XXX : stores any value from 0 to 63 integers to reg 0
- 01 XXX YYY : moves value of reg0,reg1,reg2,reg3,reg4,reg5,reg6,out to reg0,reg1,reg2,reg3,reg4,reg5,reg6,out
  - 000 - reg0
  - 001 - reg1
  - 010 - reg2
  - 011 - reg3
  - 100 - reg4
  - 101 - reg5
  - 110 - reg6
  - 111 - output 
- 10 000 XXX : calculate reg1 and reg2 and store result to reg 3
  - 000 - add
  - 001 - sub
  - 010 - and
  - 011 - nand
  - 100 - or
  - 101 - nor
- 11 000 XXX : compares reg 3 and updates counter to reg0
  - 000 - never
  - 001 - >0
  - 010 - >=0
  - 011 - =0
  - 100 - <=0
  - 101 - <0
  - 110 - !=0
  - 111 - always

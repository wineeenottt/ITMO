
.data
buffer: .byte 0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F
cur_letter: .word 0x00 
i: .word 0
len: .word 0x20
different: .word 0x20 
const_1: .word 0x01
a: .word 0x61 
z: .word 0x7A 
newline: .word 0x0A  
input_addr: .word 0x80 
output_addr: .word 0x84 
error_msg:      .word 0xCCCC_CCCC
mask:           .word 0xFF

.text
.org 0x88
_start:
	load_imm buffer
	store i  

read_loop:
    load len
    beqz error

    load_addr input_addr   
    load_acc       
    and mask       

	sub newline
	beqz read_end

    add newline
    store cur_letter

    load cur_letter
    sub a
    ble write_let

    load cur_letter
    sub z
    bgt write_let

    load cur_letter
	sub different
	store cur_letter

write_let:
    load cur_letter
    store_ind i
    load i
    add const_1
    store i
    load len
    sub const_1
    store len
    jmp read_loop

read_end:
    load_imm    0x5F5F5F00
    store_ind   i
    
    load_imm    buffer
    store       i
    
print_loop:
    load        i
    load_acc
    and         mask
    beqz        end
    store_ind   output_addr
    load        i
    add         const_1
    store       i
    jmp         print_loop
    
end:
    halt

error:
    load        error_msg
    store_ind   output_addr
    jmp         end

.data
buffer: .byte 0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F,0x5F
padding:     .byte 0x5F,0x5F
input_addr:  .word 0x80
output_addr: .word 0x84
i:           .word 0
newline:     .word '\n'
const_1:     .word 0x01
mask:        .word 0xFF
a_lower:     .word 'a'
z_lower:     .word 'z'
different:   .word 0x20
error_msg:   .word 0xCCCC_CCCC

.text
.org 0x88
_start:
    load_imm buffer
    store i

read_loop:
    load_imm padding
    sub i
    beqz end_error

    load_addr input_addr
    load_acc
    and mask

    sub newline
    beqz read_end
    add newline

    sub a_lower
    ble write_letter_a
    add a_lower
    sub z_lower
    bgt write_letter_z
    add z_lower

    sub different
    jmp save_letter

write_letter_a:
    add a_lower
    jmp save_letter

write_letter_z:
    add z_lower

save_letter:
    store_ind i
    load i
    add const_1
    store i
    jmp read_loop

read_end:
    load_imm 0x5f5f5f00
    store_ind i

    load_imm buffer
    store i

print_loop:
    load_addr i
    load_acc
    and mask
    beqz end
    store_ind output_addr
    load i
    add const_1
    store i
    jmp print_loop

end:
    halt

end_error:
    load        error_msg
    store_ind   output_addr
    jmp end

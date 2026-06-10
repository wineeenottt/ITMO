    .data
input_addr:      .word  0x80
output_addr:     .word  0x84

    .text
    .org     0x88

_start:
    jal      ra, init_stack
    jal      ra, do_task
    halt

init_stack:
    addi     sp, zero, 0x300
    jr       ra

do_task:
    addi     sp, sp, -4
    sw       ra, 4(sp)

    lui      t0, %hi(input_addr)
    addi     t0, t0, %lo(input_addr)
    lw       a2, 0(t0)
    lw       a3, 4(t0)

    lw       a0, 0(a2)

    bgt      a0, zero, call_sum
    sub      a0, zero, a0

call_sum:
    jal      ra, sum_of_digits

    sw       a0, 0(a3)

    lw       ra, 4(sp)
    addi     sp, sp, 4
    jr       ra

sum_of_digits:
    addi     sp, sp, -12
    sw       ra, 8(sp)
    sw       t1, 4(sp)

    beqz     a0, base_case

    addi     a1, zero, 10
    rem      t1, a0, a1
    div      a0, a0, a1

    jal      ra, sum_of_digits

    add      a0, a0, t1

base_case:
    lw       t1, 4(sp)
    lw       ra, 8(sp)
    addi     sp, sp, 12
    jr       ra
    .data

input_addr:      .word  0x80
output_addr:     .word  0x84
mask:            .word  0x1

    .text
    .org 0x88

_start:
    read_input
    check_zero
    if call_write_answer32
    counting_zeros

call_write_answer32:
    write_output
    end

read_input:
    @p input_addr a! @ /
    ;

check_zero:
    dup
    if answer32
    lit -1
    ;

answer32:
    drop
    lit 32
    lit 0
    ;

counting_zeros:
    lit 32 >r
    lit 0
    over

loop:
    dup
    @p mask
    and
    if main
    exit ;

main:
    2/
    over
    lit 1
    +
    over
    next loop

exit:
    drop
    r> drop
    ;

write_output:
    @p output_addr a! !
    ;

end:
    r> drop
    halt

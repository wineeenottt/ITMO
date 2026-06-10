.text
    .org     0x88
_start:
    movea.l  0x70, A7          
    movea.l  0x80, A1          
    movea.l  0x84, A2  
    move.l 0, D6        
    move.l   0, D7             
    movea.l  0, A3             
    movea.l  0, A4             

read_first:
    move.b   (A1), D0          
    cmp.b    0xA, D0           
    beq      end
    add.l    1, D6
    cmp.l    0x40, D6
    beq      overflow_instant
    move.l   1, D1             

count_loop:
    move.b   (A1), D2          
    cmp.b    0xA, D2           
    beq      write_last
    add.l    1, D6
    cmp.l    0x40, D6
    beq      overflow_instant
    cmp.b    D0, D2            
    bne      write_pair        
    cmp.l    9, D1             
    beq      write_pair        
    add.l    1, D1             
    jmp      count_loop

write_pair:
    jsr      write_count_and_char   
    move.b   D2, D0            
    move.l   1, D1             
    jmp      count_loop

write_last:
    jsr      write_count_and_char   

end:
    move.b   0, (A3)           

read_loop:
    move.b   (A4)+, D0         
    beq      hlt               
    move.b   D0, (A2)          
    jmp      read_loop

hlt:
    halt

write_count_and_char:
    add.l    2, D7             
    cmp.l    0x40, D7
    beq      overflow_instant
    bgt      overflow_instant

    move.l   D1, D3
    add.b    0x30, D3         
    move.b   D3, (A3)+         
    move.b   D0, (A3)+         
    rts

overflow_instant:
    move.l   -858993460, D0
    move.l   D0, (A2)
    jmp      hlt
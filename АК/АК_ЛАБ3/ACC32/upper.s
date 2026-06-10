.data
    .org 0x00
; Резервируем место под буфер (адреса 0, 4, 8, 12... до 32)
buffer:      .word 0, 0, 0, 0, 0, 0, 0, 0

    .org 0x40
; Переменные и константы
c_step:      .word 4         ; Шаг 4 байта (размер слова в Acc32)
c_upper:     .word 32        ; Разница ASCII
c_a:         .word 97        ; 'a'
c_z:         .word 122       ; 'z'
c_nl:        .word 10        ; '\n'
ptr_in:      .word 0
ptr_out:     .word 0
tmp:         .word 0

    .text
    .org 0x100
_start:
    ; Инициализация указателей
    load_addr 0x80          ; Читаем адрес начала входных данных из порта
    store ptr_in
    load_imm 0              ; Начинаем запись с адреса 0x00
    store ptr_out

read_loop:
    ; Проверка на конец буфера (чтобы не выйти за 32 байта)
    load_imm 32
    sub ptr_out
    ble overflow            ; Если ptr_out >= 32, выходим

    ; Читаем символ
    load ptr_in
    load_acc                ; Acc = mem[ptr_in]
    store tmp

    ; Проверка на '\n' (конец строки)
    sub c_nl
    beqz finish

    ; Логика перевода в верхний регистр
    load tmp
    sub c_a
    ble store_char          ; Если символ < 'a'
    load tmp
    sub c_z
    bgt store_char          ; Если символ > 'z'

    load tmp
    sub c_upper             ; Вычитаем 32
    store tmp

store_char:
    load tmp
    store_ind ptr_out       ; mem[ptr_out] = заглавная буква

    ; Сдвигаем указатели на 4 байта (1 слово)
    load ptr_in
    add c_step
    store ptr_in
    load ptr_out
    add c_step
    store ptr_out
    jmp read_loop

overflow:
    load_imm 0xCCCCCCCC     ; Код ошибки, если строка слишком длинная
    store_addr 0x84
    halt

finish:
    load_imm 0              ; Ставим терминатор \0 в буфер
    store_ind ptr_out
    
    load_imm 0              ; Возвращаем адрес начала буфера (0)
    store_addr 0x84         ; Записываем результат в порт 0x84
    halt
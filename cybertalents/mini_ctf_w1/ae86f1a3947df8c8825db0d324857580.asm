.READ_FLAG:
        .string "Enter the flag:"
.LC1:
        .string "%25s"
.NO_FLAG:
        .string "Wrong Flag :("
.YES_FLAG:
        .string "Correct Flag : %s"
main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 160
        mov     DWORD PTR [rbp-160], 150
        mov     DWORD PTR [rbp-156], 204
        mov     DWORD PTR [rbp-152], 233
        mov     DWORD PTR [rbp-148], 31
        mov     DWORD PTR [rbp-144], 211
        mov     DWORD PTR [rbp-140], 75
        mov     DWORD PTR [rbp-136], 212
        mov     DWORD PTR [rbp-132], 74
        mov     DWORD PTR [rbp-128], 193
        mov     DWORD PTR [rbp-124], 215
        mov     DWORD PTR [rbp-120], 85
        mov     DWORD PTR [rbp-116], 176
        mov     DWORD PTR [rbp-112], 132
        mov     DWORD PTR [rbp-108], 215
        mov     DWORD PTR [rbp-104], 57
        mov     DWORD PTR [rbp-100], 222
        mov     DWORD PTR [rbp-96], 38
        mov     DWORD PTR [rbp-92], 75
        mov     DWORD PTR [rbp-88], 2
        mov     DWORD PTR [rbp-84], 139
        mov     DWORD PTR [rbp-80], 75
        mov     DWORD PTR [rbp-76], 21
        mov     DWORD PTR [rbp-72], 215
        mov     DWORD PTR [rbp-68], 21
        mov     DWORD PTR [rbp-64], 229
        mov     edi, OFFSET FLAT:.READ_FLAG
        call    puts
        lea     rax, [rbp-48]
        mov     rsi, rax
        mov     edi, OFFSET FLAT:.LC1
        mov     eax, 0
        call    __isoc99_scanf
        mov     DWORD PTR [rbp-4], 0
        jmp     .L2
.L5:
        mov     eax, DWORD PTR [rbp-4]
        cdqe
        movzx   eax, BYTE PTR [rbp-48+rax]
        movsx   eax, al
        imul    eax, eax, 137
        cdq
        shr     edx, 24
        add     eax, edx
        movzx   eax, al
        sub     eax, edx
        mov     DWORD PTR [rbp-8], eax
        mov     eax, DWORD PTR [rbp-4]
        cdqe
        mov     eax, DWORD PTR [rbp-160+rax*4]
        cmp     DWORD PTR [rbp-8], eax
        je      .INCREMENT_rbp
        mov     edi, OFFSET FLAT:.NO_FLAG
        call    puts
        mov     eax, 0
        jmp     .EXIT
.INCREMENT_rbp:
        add     DWORD PTR [rbp-4], 1
.L2:
        cmp     DWORD PTR [rbp-4], 24
        jle     .L5
        lea     rax, [rbp-48]
        mov     rsi, rax
        mov     edi, OFFSET FLAT:.YES_FLAG
        mov     eax, 0
        call    printf
        mov     eax, 0
.EXIT:
        leave
        ret
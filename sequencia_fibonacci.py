def em_fibonacci(num):
    # primeiros dois numeros da sequencia de fibonacci
    a = 0
    b = 1
    
    seq = [0, 1]
    
    if num < 0:
        return []

    for i in range(num):
        c = a + b
        a = b
        b = c
        
        seq.append(c)
        
        if (c >= num):
            return seq
        
    return seq


num = int(input("Digite um número: "))
seq_fibonacci = em_fibonacci(num)

if num in seq_fibonacci:
    print(f'{num} está na sequência de fibonacci')
else:
    print(f'{num} não pertence a sequência de fibonacci')

if (seq_fibonacci):
    print(f'Os {len(seq_fibonacci)} primeiros termos da sequência de fibonacci são: ')
    print(*seq_fibonacci, sep=' ')
    
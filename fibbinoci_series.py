def fibbinoci_number_generator(n):
    sequence=[]
    first_no,second_no=0,1
    for _ in range(n):
        sequence.append(first_no)
        first_no,second_no=second_no,first_no+second_no
    return sequence

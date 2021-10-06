#Tower-of-Hanoi

NUMBER = int(input("How many disks:\n"))

def hanoi( p_from, p_tmp, p_to, number ):
    if number == 1:
        print( "Disk 1 from", p_from, "to", p_to )
        return 1
    steps = hanoi( p_from, p_to, p_tmp, number-1 )
    print( "Disk", number, "from", p_from, "to", p_to )
    steps += 1+hanoi( p_tmp, p_from, p_to, number-1 )
    return steps

steps = hanoi( 'A', 'B', 'C', NUMBER )
print( steps, "steps done" )
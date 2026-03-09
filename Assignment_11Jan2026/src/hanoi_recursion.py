def solve_hanoi(n, source='A', auxiliary='B', target='C'):
    if n == 1:
        print(f"Moving disk 1 from {source} to {target}")
        return 1

    moves = 0
    moves += solve_hanoi(n-1, source, target, auxiliary)
    print(f"Moving disk {n} from {source} to {target}")
    moves += 1
    moves += solve_hanoi(n-1, auxiliary, source, target)

    return moves

    
    
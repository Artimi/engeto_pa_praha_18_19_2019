
def vertical_histogram(sequence, bar_width=1):
    max_row = max(sequence)
    max_row_length = len(str(max_row))
    for level in range(max_row, 0, -1):
        row = f'{level:>{max_row_length}}|'
        for item in sequence:
            fill_symbol = '*' if item >= level else ' '
            row += f' {fill_symbol * bar_width}'
        print(row)


vertical_histogram([4, 5, 7, 10, 6, 3, 2], bar_width=5)



def print_table(*rows, **formatting):
    separator = formatting.get('separator', "|")
    padding = " " * formatting.get('padding', 2)
    header = formatting.get('header', False)
    align = formatting.get('align', "left")
    
    for row_index, row in enumerate(rows):
        formatted_cells = []

        for value in row:
            value = str(value)
        
            if align == 'right':
                formatted_cells.append(value.rjust(10))
            else:
                formatted_cells.append(value.ljust(10))


        print(separator + padding + 
            f"{padding}{separator}{padding}".join(formatted_cells) +
            padding + separator
            )
        
        if row_index == 0 and header:
            print(separator + 
                separator.join('-' * 12 for _ in row) +
                separator
                )


def main():
    print_table(('Name', 'Age', 'City'), ('Alice', 30, 'NYC'), ('Bob', 25, 'LA'), separator='|', padding=1, header=True, align='left')


main()
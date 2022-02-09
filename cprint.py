def cprint(items, columns=4, padding='   ', format_spec='{:<w}'):
    n_items = len(items)
    n_cols = columns
    n_rows = -(n_items // -n_cols)

    by_col = [items[col_i*n_rows:(col_i+1)*n_rows] for col_i in range(n_cols)]
    col_widths = [max(len(item) for item in col) for col in by_col]
    by_row = [items[row_i::n_rows] for row_i in range(n_rows)]

    format_spec = format_spec.replace('w', '{w}')
    format_spec = format_spec.replace('{:', '{item:')

    for row in by_row:
        item_strings = []
        for item, width in zip(row, col_widths):
            item_string = format_spec.format(w=width, item=item)
            item_strings.append(item_string)
        line = padding.join(item_strings)
        print(line)

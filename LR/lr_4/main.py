def process_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0]) if m > 0 else 0

    # Найти сумму в каждой строке
    row_sums = [sum(row) for row in matrix]
    print("Суммы строк:", row_sums)

    # Количество столбцов, в которых сумма больше 0
    positive_columns = sum(1 for col in zip(*matrix) if sum(col) > 0)
    print("Кол-во столбцов с суммой > 0:", positive_columns)

    # Номера строк, в которых элементы упорядочены по убыванию
    decreasing_rows = [
        i for i, row in enumerate(matrix)
        if all(row[j] > row[j + 1] for j in range(len(row) - 1))
    ]
    print("Номера строк с убывающими элементами:", decreasing_rows)


matrix = [
    [5, 3, 1],
    [2, 4, 6],
    [9, 7, 5]
]
process_matrix(matrix)
def format_table(benchmarks, algos, results):
    benchmarks = list(map(str, benchmarks))
    algos = list(map(str, algos))
    results = [list(map(str, l)) for l in results]
    width_max = [max(len('Benchmark'), max(map(len, benchmarks)))]\
    + [max(max(map(len, [results[i][j] for i in range(len(results))])), len(algos[j])) for j in range(len(algos))]
    table = '| ' + 'Benchmark'.ljust(width_max[0]) + ' | '
    for i in range(len(algos)):
        table += ' ' + algos[i].ljust(width_max[i + 1]) + ' |'
    table += '\n|' + '-' * (len(table) - 2) + '|\n'
    for i in range(len(benchmarks)):
        table += '| ' + benchmarks[i].ljust(width_max[0]) + ' | '
        for j in range(len(algos)):
            table += ' ' + results[i][j].ljust(width_max[j + 1]) + ' |'
        table += '\n'
    print(table)


if __name__ == "__main__":
    format_table(["best case", "worst case"],\
    ["quick sort", "merge sort", "bubble sort"],\
    [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])

    format_table(["best case", "the worst case"],\
    ["quick", "merge", "bubble"],\
    [[1.2323548890, 1.56785239, 2.0455646], [3.334343, 2.9434234, 3.9344342]])




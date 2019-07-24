import csv
with open('people Chadwick.csv', 'rt') as master:
    master_indices = dict((r[0], i) for i, r in enumerate(csv.reader(master)))

    with open('query bbref.csv', 'rt') as hosts:
        with open('results.csv', 'w') as results:
            reader = csv.reader(hosts)
            writer = csv.writer(results)

            writer.writerow(next(reader, []) + ['RESULTS'])

            for row in reader:
                index = master_indices.get(row[0])
                if index is not None:
                    message = 'FOUND in Chadwick list (row {})'.format(index)
                    writer.writerow(row + [message])

                else:
                     message = 'NOT FOUND in Chadwick list'
                     writer.writerow(row + [message])

        results.close()
import csv


def read(filename, delimiter=';', quotechar='"', fieldnames=None):
    rows = []
    with open(filename, newline='') as csvfile:
        for r in csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar, fieldnames=fieldnames):
            rows.append(dict(r))
    return rows


def write(rows, filename, delimiter=';', fieldnames=None):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=delimiter, fieldnames=fieldnames)

        writer.writeheader()
        for row in rows:
            writer.writerow(dict(row))

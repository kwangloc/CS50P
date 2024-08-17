import csv

def main():
    # test_reader()
    # test_writer()
    # test_dict_reader()
    test_dict_writer()

def test_reader():
    with open("csv_library.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print("|".join(row))

def test_writer():
    tmp_li = ["abc", "qwe"]
    with open("csv_library.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # writer.writerow(["France", "Park"])
        writer.writerow(tmp_li)

def test_dict_reader():
    with open("csv_library.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"{row['name']} {row['coach']}")

def test_dict_writer():
    with open("csv_library.csv", "a", newline='') as csvfile:
        fieldnames = ["name", "coach"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        # writer.writeheader()
        writer.writerow({'name': 'Baked', 'coach': 'Beans'})
        writer.writerow({'name': 'Lovely', 'coach': 'Spam'})
        writer.writerow({'name': 'Wonderful', 'coach': 'Spam'})

if __name__ == "__main__":
    main()
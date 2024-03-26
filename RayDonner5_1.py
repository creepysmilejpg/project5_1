def main():
    import os.path
    import re
    import csv

    name = 'files/' + input('Enter input file name: ').strip()
    while name != 'files/input.txt':
        try:
            file = open(f'{name}', 'r')

        except:
            name = 'files/' + input('Enter correct file name: ').strip()

    file = open(f'{name}', 'r')
    file.seek(0)
    name2 = input('What would you like to name this file? ').strip()

    if os.path.isfile(f'files/{name2}'):
        print(f'{name2} exists')
        answer = input('Would you like to overwrite this file?(y/n) ').lower()
        while answer != 'y' and answer != 'n':
            print('output.csv exists')
            answer = input('Overwrite?(y/n) ').lower()

        if answer == 'n':
            name2 = input('What would you like to name the new file?').strip()

            if os.path.isfile(f'files/{name2}'):
                hold = name2
                while name2 == hold:
                    name2 = input('Please enter a new file name: ').strip()

    else:
        name2 = input('What would you like to name this file?').strip()

    filesopen = 'files/' + name2
    csvfile = open(f'{filesopen}', 'w', newline='')

    csvheader = ['Email ', 'Subject ', 'Confidence']
    csv_writer = csv.writer(csvfile)

    csvfile.seek(0)

    line1 = []
    line2 = []
    line3 = []

    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(csvheader)

    for line in file:
        line = line.rstrip()
        if re.findall('^From: (\S*@\S*)', line):
            line = line.replace('From: ', '')
            line1 = line

        if re.findall('^Subject: ', line):
            line = line.replace('Subject: [sakai] svn commit: ', '')
            colon = line.find(':')
            head, sep, tail = line.partition(' - ')
            line2 = head

        if re.findall('^X-DSPAM-Confidence:', line):
            line = line.replace('X-DSPAM-Confidence: ', '')
            l = len(line)
            middle = (l // 2) + 7
            first, second = line[:middle], line[middle:]
            line3 = line

            csv_writer.writerow([line1, line2, line3])

    print('Data stored!')
    file.close()
    csvfile.close()


if __name__ == '__main__':
    main()

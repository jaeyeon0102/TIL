import csv

# with open('data.csv','w',newline='',encoding='utf-8') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['이름','나이','직업'])
#     csv_writer.writerow(['이름','나이','직업'])



with open('data.csv','w',newline='',encoding='utf-8') as file:
    fieldnames = ['이름','나이','직업']
    csv_writer = csv.DictWriter(file, fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow(['이름','나이','직업'])
    csv_writer.writerow(['이름','나이','직업'])


    
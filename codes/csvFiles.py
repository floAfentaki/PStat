import csv


def write(c):
    c.execute("select * from month;")
    with open("../csv files/month3.csv","w",newline='') as f:
        writer=csv.writer(f)
        writer.writerow([i[0] for i in c.description])
        writer.writerows(c)

    c.execute("select * from year;")
    with open("../csv files/yearly.csv","w",newline='') as f:
        writer=csv.writer(f)
        writer.writerow([i[0] for i in c.description])
        writer.writerows(c)

    c.execute("select * from top;")
    with open("../csv files/top5.csv","w",newline='') as f:
        writer=csv.writer(f)
        writer.writerow([i[0] for i in c.description])
        writer.writerows(c)

    c.execute("select * from trans;")
    with open("../csv files/transportation.csv","w",newline='') as f:
        writer=csv.writer(f)
        writer.writerow([i[0] for i in c.description])
        writer.writerows(c)

import csv

datas = "rollcall_data.txt"
file_csv = datas.replace("txt", "csv")

with open("rollcall_data.txt",encoding="utf_8_sig") as rf:
    with open("rollcall.csv", "w",encoding="utf_8_sig")as wf:
        readfile = rf.readlines()
        
        for read_text in readfile:
            # listに分割
            read_text = read_text.split()
            # csvに書き込む
            writer = csv.writer(wf, delimiter=',')
            writer.writerow(read_text)


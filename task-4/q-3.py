#Question-5
mark_list = [ [1,"A.Yashaswini",100],
             [2,"B.Keerthana",99],
              [3,"C.Siddharth",98],
              [4,"D.Akash",97],
              [5,"E.Vishnu",96]]

print("|  Roll Number  |  Student Name  |  Marks Obtained  |")

for item in mark_list:
    print("|",item[0]," "*(12-len(str(item[0]))),"|",
    item[1]," "*(13-len(item[1])),"|",
    item[2]," "*(15-len(str(item[2]))),"|")


print()
print("|  Roll Number  |  Student Name  |  Marks Obtained  |")
for i in range(len(mark_list)):
    if i==1:
        print("|",mark_list[i][0]," "*(12-len(str(mark_list[i][0]))),"|",
        mark_list[i][1]," "*(13-len(mark_list[i][1])),"|",
        mark_list[i][2]," "*(15-len(str(mark_list[i][2]))),"|")
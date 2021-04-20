data = int(input())

data_str = str(data)

if data < 10:
    data_str = "0"+data_str

count = 0
new_num = "-1"

while data != int(new_num):
    s_last = str(sum(list(map(int,data_str))))[-1]
    
    new_num = data_str[-1] + s_last
    
    data_str = new_num
    count+=1
    
print(count)

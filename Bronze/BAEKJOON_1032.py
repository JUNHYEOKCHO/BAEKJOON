n = int(input())


files = []

for _ in range(n):
    files.append(input())
    
command = list(files[0])
file_len = len(command)

for i in range(1, len(files)):
    for j in range(file_len):
        if command[j] != files[i][j]:
            command[j] = "?"
print("".join(command))

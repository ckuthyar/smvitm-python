def readlines_and_compare(file1_path, file2_path):
    
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        sentences_file1 = file1.read().splitlines()
        sentences_file2 = file2.read().splitlines()

    
    fault_lines = []

    
    for i, (line1, line2) in enumerate(zip(sentences_file1, sentences_file2), start=1):
        if line1 != line2:
            fault_lines.append(i)
            print(line1, ": is different from :" ,line2)
    
    return fault_lines


file1_path = r'D:\file1.txt'
file2_path = r'D:\file2.txt'

result = readlines_and_compare(file1_path, file2_path)
print("Differences found at lines:", result)

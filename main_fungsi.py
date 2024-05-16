import itertools
import re

# membuka & membaca file
with open('data_inputan.txt', 'r') as file:
    # Membaca dua baris pertama dan membaginya menjadi dua angka terpisah
    dimensions = file.readline().strip().split()
    n = int(dimensions[0])
    m = int(dimensions[1])
    
    matrix = []
    
    # Membaca matriks
    for _ in range(n):
        matrix_item = file.readline().strip()
        matrix.append(matrix_item)
    
   
    encoded_string = "".join(char for group in itertools.zip_longest(*matrix, fillvalue='') for char in group)
    
    #fungsi regex
    pat = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
    decoded_string = re.sub(pat, ' ', encoded_string)
    
    with open("output.txt", "w") as output_file:
        output_file.write(decoded_string)
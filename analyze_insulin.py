def analyze_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Первая строка - это заголовок (header), остальное - ДНК
    header = lines[0].strip()
    # Склеиваем все остальные строки в одну длинную цепочку
    sequence = "".join(line.strip() for line in lines[1:])
    
    length = len(sequence)
    g_count = sequence.upper().count('G')
    c_count = sequence.upper().count('C')
    gc_content = (g_count + c_count) / length * 100
    
    print(f"Анализ файла: {file_path}")
    print(f"Описание: {header}")
    print(f"Длина гена: {length} пар нуклеотидов")
    print(f"GC-состав: {gc_content:.2f}%")

# Запускаем анализ нашего скачанного файла
analyze_fasta("insulin.fasta")
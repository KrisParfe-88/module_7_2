def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    string_position = {}
    n = 0
    for i in strings:
        n += 1
        string_position[(n, file.tell())] = i
        file.write(i + '\n')
    file.close()
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

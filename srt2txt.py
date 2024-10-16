import pyperclip
import re

file_name = input("Write file name: ")
if not file_name.lower().endswith('.srt'):
    file_name += ".srt"

def srt2txt(srt):
    lines = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n', '', srt)
    lines = lines.strip().split('\n')
    #return lines
    return '\n'.join(line for line in lines if line.strip())

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        srt_content = file.read()
    plain_text = srt2txt(srt_content)

    pyperclip.copy(plain_text)

    output_file_name = file_name.replace('.srt','.txt')
    with open(output_file_name, 'w', encoding='utf-8') as file:
        file.write(plain_text)
    print("Success!!!")
except:
    print("not working")
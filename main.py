import re

def clean_mnemonic(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        cleaned_lines = []

        for line in lines:
            cleaned_line = re.sub(r'[0-9\.\(\)]', '', line).split()
            cleaned_lines.append(' '.join(cleaned_line))
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(cleaned_lines))

        print("Готово! Результат збережено у result.txt")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == '__main__':
    clean_mnemonic('mnemonic.txt', 'result.txt')
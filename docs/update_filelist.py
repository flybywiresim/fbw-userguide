import os

# Global variables for the starting folder path and the output file
STARTING_FOLDER = '.'
OUTPUT_FILE = 'FILE_LIST.md'

def extract_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# '):
                return line[2:].strip()
    return None

def traverse_directory(directory):
    pages = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                title = extract_title(file_path)
                if title:
                    pages.append((file_path, title))
    return pages

def format_output(pages, base_directory):
    output = []
    previous_first_level_folder = None
    for file_path, title in pages:
        relative_path = os.path.relpath(file_path, base_directory)
        indent_level = relative_path.count(os.sep)
        indent = ' ' * 4 * indent_level
        first_level_folder = relative_path.split(os.sep)[0] if indent_level > 0 else None
        if first_level_folder and first_level_folder != previous_first_level_folder:
            # if previous_first_level_folder is not None:
            # output.append('\n')  # Add an empty line after each first-level folder
            previous_first_level_folder = first_level_folder
        output.append(f"{indent}- [X] [{title}]({relative_path.replace(os.sep, '/')})")
    return '\n'.join(output)

def update_existing_output(existing_content, new_content):
    existing_lines = existing_content.split('\n')
    new_lines = new_content.split('\n')

    updated_lines = []
    new_lines_dict = {line.strip(): line for line in new_lines}

    for line in existing_lines:
        stripped_line = line.strip()
        if stripped_line.startswith('- [X]') and stripped_line in new_lines_dict:
            updated_lines.append(new_lines_dict.pop(stripped_line))
        else:
            updated_lines.append(line)

    for new_line in new_lines_dict.values():
        updated_lines.append(new_line)

    return '\n'.join(updated_lines)

if __name__ == "__main__":
    docs_directory = STARTING_FOLDER
    pages = traverse_directory(docs_directory)
    formatted_output = format_output(pages, docs_directory)

    output_file_path = os.path.join(docs_directory, OUTPUT_FILE)

    if os.path.exists(output_file_path):
        with open(output_file_path, 'r', encoding='utf-8') as output_file:
            existing_content = output_file.read()
        updated_content = update_existing_output(existing_content, formatted_output)
    else:
        updated_content = formatted_output

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(updated_content)

    print(f"Output updated in {output_file_path}")
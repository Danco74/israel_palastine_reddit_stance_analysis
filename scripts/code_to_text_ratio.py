import json
from pathlib import Path

nb_path = Path('data_science_project/notebook.ipynb')

with nb_path.open('r', encoding='utf-8') as f:
    nb = json.load(f)

md_chars = 0
code_chars = 0
md_cells = 0
code_cells = 0

for cell in nb.get('cells', []):
    src = ''.join(cell.get('source', []))
    if cell.get('cell_type') == 'markdown':
        md_cells += 1
        md_chars += len(src)
    elif cell.get('cell_type') == 'code':
        code_cells += 1
        code_chars += len(src)

total_chars = md_chars + code_chars
ratio = (md_chars / code_chars) if code_chars else float('inf')
cell_ratio = (md_cells / code_cells) if code_cells else float('inf')

print("NOTEBOOK TEXT-TO-CODE (characters)")
print("-" * 40)
print(f"Markdown cells: {md_cells}")
print(f"Code cells: {code_cells}")
print(f"Markdown chars: {md_chars:,}")
print(f"Code chars: {code_chars:,}")
print(f"Total chars: {total_chars:,}")
print(f"Text-to-code ratio: {ratio:.2f}:1")
print(f"Markdown-to-code ratio (cells): {cell_ratio:.2f}:1")
print(f"Text share: {md_chars/total_chars*100:.1f}% | Code share: {code_chars/total_chars*100:.1f}%")
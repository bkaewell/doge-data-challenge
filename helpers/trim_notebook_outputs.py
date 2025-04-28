import nbformat
import sys

# Configuration
MAX_LINES = 20
MAX_CHARS = 5000

def truncate_output_text(output_text):
    if not output_text:
        return output_text
    lines = output_text.splitlines()
    if len(lines) > MAX_LINES or len(output_text) > MAX_CHARS:
        truncated = "\n".join(lines[:MAX_LINES])
        truncated = truncated[:MAX_CHARS]  # Truncate to char limit
        return truncated + "\n\n\n... [truncated for Git preview] ...\n\n\n"
    return output_text

def trim_notebook_outputs(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    modified = False
    for cell in nb.cells:
        if cell.cell_type == 'code' and 'outputs' in cell:
            for output in cell.outputs:
                if 'text' in output:
                    new_text = truncate_output_text(output['text'])
                    if new_text != output['text']:
                        output['text'] = new_text
                        modified = True

    if modified:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"✅ Trimmed outputs in: {notebook_path}")
    else:
        print(f"ℹ️  No trimming needed: {notebook_path}")

# Run script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python trim_outputs.py your_notebook.ipynb")
        sys.exit(1)
    trim_notebook_outputs(sys.argv[1])


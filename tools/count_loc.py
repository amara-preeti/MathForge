import os

def count_loc(directory, extensions):
    total_loc = 0
    for root, _, files in os.walk(directory):
        if 'node_modules' in root or '.git' in root or '__pycache__' in root or 'venv' in root:
            continue
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        total_loc += len(lines)
                except Exception:
                    pass
    return total_loc

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    python_loc = count_loc(base_dir, ['.py'])
    ts_loc = count_loc(base_dir, ['.ts', '.tsx'])
    js_loc = count_loc(base_dir, ['.js', '.jsx'])
    css_loc = count_loc(base_dir, ['.css', '.scss'])
    test_loc = count_loc(os.path.join(base_dir, 'tests'), ['.py', '.ts', '.tsx']) + count_loc(os.path.join(base_dir, 'frontend', 'src'), ['.test.ts', '.test.tsx'])
    md_loc = count_loc(base_dir, ['.md'])
    
    total = python_loc + ts_loc + js_loc + css_loc + md_loc
    
    print("=== MathForge LOC Count ===")
    print(f"Python:       {python_loc}")
    print(f"TypeScript:   {ts_loc}")
    print(f"JavaScript:   {js_loc}")
    print(f"CSS:          {css_loc}")
    print(f"Tests:        {test_loc} (included in above)")
    print(f"Markdown:     {md_loc}")
    print("---------------------------")
    print(f"Total Source: {total}")
    print("===========================")

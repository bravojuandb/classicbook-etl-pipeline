
# 🧾 `pathlib` Cheat Sheet (Python 3.6+)

## 📦 Importing
```python
from pathlib import Path
```

---

## 📁 Creating Path Objects

| Task | Code |
|------|------|
| Current working directory | `Path.cwd()` |
| Script directory (current file) | `Path(__file__).resolve().parent` |
| Home directory | `Path.home()` |
| Relative path | `Path("data") / "file.txt"` |
| Absolute path | `Path("/usr/local/bin")` |

---

## 📄 Reading & Writing Files

```python
path = Path("example.txt")

# Write text
path.write_text("Hello, world!", encoding="utf-8")

# Read text
content = path.read_text(encoding="utf-8")

# Write binary
path.write_bytes(b"binary content")

# Read binary
data = path.read_bytes()
```

---

## 📚 File and Directory Info

| Task | Code |
|------|------|
| Check if file exists | `path.exists()` |
| Is it a file? | `path.is_file()` |
| Is it a directory? | `path.is_dir()` |
| Get file name | `path.name` |
| Get file stem (no extension) | `path.stem` |
| Get file suffix | `path.suffix` |
| Get parent directory | `path.parent` |
| Get all parts | `path.parts` |
| Convert to string | `str(path)` |

---

## 🗂️ Creating and Deleting

```python
# Create a directory (and parents if needed)
path.mkdir(parents=True, exist_ok=True)

# Remove file
path.unlink()

# Remove empty directory
path.rmdir()
```

---

## 🔁 Iterating Over Files

```python
# All .txt files in folder
for file in Path("folder").glob("*.txt"):
    print(file.name)

# All .txt files recursively
for file in Path("folder").rglob("*.txt"):
    print(file)
```

---

## 🔄 Path Operations

| Task | Code |
|------|------|
| Join paths | `base / "subdir" / "file.txt"` |
| Resolve absolute path | `path.resolve()` |
| Relative path from another | `path.relative_to(base_path)` |
| Change file extension | `path.with_suffix('.md')` |
| Rename file | `path.rename("newname.txt")` |
| Copy file | `shutil.copy2(src, dst)` *(via `import shutil`)* |

---

## 🧪 Example

```python
from pathlib import Path

base = Path(__file__).resolve().parent
data_file = base / "extract_phase" / "raw_data" / "latin" / "book1.txt"

if data_file.exists():
    content = data_file.read_text(encoding="utf-8")
    print(content[:100])  # Preview first 100 characters
```

---

## ✅ Best Practices

- Always use `.resolve()` for safe absolute paths
- Use `Path(...).mkdir(parents=True, exist_ok=True)` to ensure dirs exist
- Avoid hardcoding paths with slashes (`"folder/file.txt"`)

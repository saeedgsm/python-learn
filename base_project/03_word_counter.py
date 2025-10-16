# شمارشگر کلمات/حروف/خطوط یک فایل متنی
# مباحث: فایل، رشته‌ها، split، حلقه

from pathlib import Path

def count_file(path: str):
    p = Path(path)
    if not p.exists():
        return {"lines": 0, "words": 0, "chars": 0}
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()
    words = text.split()
    return {"lines": len(lines), "words": len(words), "chars": len(text)}

def main():
    target = input("file path: ").strip()
    stats = count_file(target)
    print(stats)

if __name__ == "__main__":
    main()


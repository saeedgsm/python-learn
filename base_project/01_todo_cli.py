# TODO CLI ساده: افزودن، لیست، تکمیل/حذف، ذخیره‌سازی فایل متنی
# مباحث: رشته‌ها، لیست‌ها، فایل، شرط‌ها، حلقه

from pathlib import Path

DATA_FILE = Path("todo.txt")

def load_items():
    if not DATA_FILE.exists():
        return []
    return [line.strip() for line in DATA_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]

def save_items(items):
    DATA_FILE.write_text("\n".join(items) + ("\n" if items else ""), encoding="utf-8")

def add_item(items, text):
    items.append(text)
    return items

def remove_item(items, index):
    if 0 <= index < len(items):
        items.pop(index)
    return items

def list_items(items):
    if not items:
        print("empty")
        return
    for i, it in enumerate(items):
        print(f"{i}. {it}")

def main():
    items = load_items()
    while True:
        cmd = input("[a]dd [l]ist [r]emove [q]uit: ").strip().lower()
        if cmd == "a":
            text = input("new item: ").strip()
            if text:
                add_item(items, text)
                save_items(items)
        elif cmd == "l":
            list_items(items)
        elif cmd == "r":
            idx = input("index: ")
            if idx.isdigit():
                remove_item(items, int(idx))
                save_items(items)
        elif cmd == "q":
            break
        else:
            print("unknown")

if __name__ == "__main__":
    main()


# کار با JSON و مسیرها با pathlib
import json
from pathlib import Path

data = {"name": "Ali", "scores": [18, 19, 17]}

# ذخیره JSON در فایل
path = Path("data.json")
path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

# خواندن JSON از فایل
loaded = json.loads(path.read_text(encoding="utf-8"))
print(loaded["name"], sum(loaded["scores"]))

# ساخت و اطمینان از وجود دایرکتوری
out_dir = Path("outputs")
out_dir.mkdir(exist_ok=True)
(out_dir / "result.txt").write_text("ok", encoding="utf-8")
print((out_dir / "result.txt").exists())


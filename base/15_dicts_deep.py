# دیکشنری‌ها در پایتون: ساختار داده کلیدی-مقداری
# کلیدها باید قابل هش باشند (مانند str, int, tupleهای فقط-قابل-هش)

# ساخت دیکشنری
user = {"name": "Sara", "age": 28}
print(user)

# دسترسی به مقدار با کلید
print(user["name"])  # خطا اگر کلید وجود نداشته باشد
print(user.get("job"))  # برنمی‌گرداند خطا؛ None برمی‌گرداند
print(user.get("job", "unknown"))  # مقدار پیش‌فرض

# افزودن/ویرایش مقدار
user["city"] = "Tehran"
user.update({"age": 29})
print(user)

# setdefault: اگر کلید نبود مقدار پیش‌فرض تنظیم می‌کند و مقدار را برمی‌گرداند
prefs = {}
p = prefs.setdefault("theme", "light")
print(p, prefs)

# حذف مقدار
removed = user.pop("city", None)
print(removed)
del user["age"]
print(user)

# مشاهده کلیدها/مقدارها/آیتم‌ها
print(list(user.keys()))
print(list(user.values()))
print(list(user.items()))

# پیمایش دیکشنری
for key, value in {"a": 1, "b": 2}.items():
    print(key, value)

# دیکشنری تو در تو
people = {
    "u1": {"name": "Ali", "scores": [18, 19]},
    "u2": {"name": "Reza", "scores": [15, 17]},
}
print(people["u1"]["scores"][0])

# درک دیکشنری (dict comprehension)
names = ["ali", "sara", "reza"]
caps = {n: n.capitalize() for n in names}
print(caps)

# ادغام دیکشنری‌ها (Python 3.9+)
a = {"x": 1, "y": 2}
b = {"y": 20, "z": 3}
merged = a | b  # کلیدهای تکراری از سمت راست جایگزین می‌شوند
print(merged)

# کپی سطحی و عمیق
import copy
original = {"name": "A", "tags": [1, 2]}
shallow = original.copy()
deep = copy.deepcopy(original)
original["tags"][0] = 99
print(shallow["tags"])  # تحت تأثیر قرار می‌گیرد
print(deep["tags"])     # مستقل باقی می‌ماند


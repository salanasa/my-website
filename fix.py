import os

# هذا الكود سيصلح الـ 2000 سطر تلقائياً
path = 'templates/index.html'

if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()

    # إضافة كلمة static قبل المجلدات ليفهمها Flask
    data = data.replace('gallery/', 'static/gallery/')
    data = data.replace('fonts/', 'static/fonts/')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)
    print("Success: Done!")
else:
    print("Error: File not found")
    
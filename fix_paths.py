import os

# 1. حدد اسم ملف الـ HTML الخاص بك
file_path = 'templates/index.html'

if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 2. استبدال المسارات القديمة بالمسارات المتوافقة مع Flask
    # سيبحث عن gallery/ ويحولها إلى /static/gallery/
    new_content = content.replace('src="gallery/', 'src="/static/gallery/')
    new_content = new_content.replace("src='gallery/", "src='/static/gallery/")
    
    # وأيضاً للخطوط إذا كانت موجودة
    new_content = new_content.replace('url("fonts/', 'url("/static/fonts/')
    new_content = new_content.replace("url('fonts/", "url('/static/fonts/")

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print("✅ تم تحديث جميع المسارات بنجاح! الآن جرب تشغيل الموقع.")
else:
    print("❌ خطأ: لم يتم العثور على ملف index.html داخل مجلد templates")
    
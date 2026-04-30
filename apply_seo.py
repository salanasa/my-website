import os
import re

# مسار الملف
file_path = 'templates/index.html'

if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. إعداد الـ Meta Tags
    seo_tags = """
    <!-- SEO Excellence Tags -->
    <meta name="description" content="اكتشف التميز التعليمي في أرقى صرح تربوي؛ حيث ندمج الابتكار بالقيم لبناء جيل مبدع ومستقبل واعد. بيئة تعليمية تلهم العقول وتصقل المواهب بأحدث المعايير العالمية.">
    <meta name="keywords" content="مدرسة، تعليم متميز، تطوير مهارات، جودة التعليم، تربية، مدرسة نموذجية، مستقبل الطلاب، تفوق أكاديمي">
    """

    # إضافة التاجز داخل الـ <head>
    if '<head>' in content:
        content = content.replace('<head>', f'<head>{seo_tags}', 1)

    # 2. تحديث الروابط الخارجية لتفتح في نافذة جديدة
    # التعبير النمطي يبحث عن الروابط التي تبدأ بـ http ولا تملك target="_blank"
    def update_external_links(match):
        tag = match.group(0)
        if 'target=' not in tag:
            # إضافة target="_blank" و rel للسكورتي
            return tag.replace('<a ', '<a target="_blank" rel="noopener noreferrer" ')
        return tag

    # استهداف الروابط الخارجية فقط (التي تبدأ بـ http)
    content = re.sub(r'<a\s+[^>]*href=["\']http[s]?://[^"\']*[ " \'>]', update_external_links, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ تم تطبيق بروتوكول SEO Excellence بنجاح!")
    print("✅ تم تحديث الوصف والكلمات المفتاحية.")
    print("✅ تم ضبط جميع الروابط الخارجية لتفتح في نافذة جديدة.")
else:
    print("❌ خطأ: لم يتم العثور على ملف index.html")
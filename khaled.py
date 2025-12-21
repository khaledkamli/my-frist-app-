
import pandas as pd
import flask

print("تم تثبيت الإضافات والمكتبات بنجاح!")
print(f"نسخة Flask المثبتة هي: {flask.__version__}")
import pandas as pd

def analyze_url(url):
    # سمات الأمان التي سنبحث عنها
    score = 0
    reasons = []

    # 1. التحقق من البروتوكول
    if not url.startswith("https"):
        score += 30
        reasons.append("لا يستخدم بروتوكول HTTPS المشفر")

    # 2. التحقق من طول الرابط (الروابط الطويلة جداً مشبوهة غالباً)
    if len(url) > 50:
        score += 20
        reasons.append("طول الرابط مبالغ فيه (قد يخفي إعادة توجيه)")

    # 3. البحث عن كلمات تدل على الاحتيال
    phishing_keywords = ['login', 'verify', 'update-password', 'bank', 'free-gift', 'win']
    for word in phishing_keywords:
        if word in url.lower():
            score += 40
            reasons.append(f"يحتوي على كلمة مشبوهة: ({word})")

    # النتيجة النهائية
    print(f"\n--- نتائج فحص الرابط: {url} ---")
    if score >= 70:
        print("❌ النتيجة: رابط عالي الخطورة (High Risk)!")
    elif score >= 30:
        print("⚠️ النتيجة: رابط متوسط الخطورة (Warning).")
    else:
        print("✅ النتيجة: الرابط يبدو آمناً.")
    
    for reason in reasons:
        print(f" - {reason}")

# تجربة البرنامج
my_url = input("أدخل الرابط الذي تريد فحصه: ")
analyze_url(my_url)


import pandas as pd

def analyze_url(url):
    # سمات الأمان التي سنبحث عنها
    score = 0
    reasons = []

    # 1. التحقق من البروتوكول
    if not url.startswith("https"):
        score += 30
        reasons.append("لا يستخدم بروتوكول HTTPS المشفر")

    # 2. التحقق من طول الرابط (الروابط الطويلة جداً مشبوهة غالباً)
    if len(url) > 50:
        score += 20
        reasons.append("طول الرابط مبالغ فيه (قد يخفي إعادة توجيه)")

    # 3. البحث عن كلمات تدل على الاحتيال
    phishing_keywords = ['login', 'verify', 'update-password', 'bank', 'free-gift', 'win']
    for word in phishing_keywords:
        if word in url.lower():
            score += 40
            reasons.append(f"يحتوي على كلمة مشبوهة: ({word})")

    # النتيجة النهائية
    print(f"\n--- نتائج فحص الرابط: {url} ---")
    if score >= 70:
        print("❌ النتيجة: رابط عالي الخطورة (High Risk)!")
    elif score >= 30:
        print("⚠️ النتيجة: رابط متوسط الخطورة (Warning).")
    else:
        print("✅ النتيجة: الرابط يبدو آمناً.")
    
    for reason in reasons:
        print(f" - {reason}")

# تجربة البرنامج
my_url = input("أدخل الرابط الذي تريد فحصه: ")
analyze_url(my_url)

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer

# مثال لبيانات تدريب (بسيطة للهاكاثون)
urls = ['google.com', 'bank-verify-login.it', 'facebook.com', 'win-free-money.xyz']
labels = [0, 1, 0, 1]  # 0 آمن، 1 خبيث

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(urls)

model = RandomForestClassifier()
model.fit(X, labels)

def predict_threat(new_url):
    query = vectorizer.transform([new_url])
    result = model.predict(query)
    return "🚨 تهديد سيبراني" if result[0] == 1 else "✅ آمن"

print(predict_threat("bank-login-update.com"))
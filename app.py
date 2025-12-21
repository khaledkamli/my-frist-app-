
from flask import Flask, render_template_string, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# --- 1. جزء الذكاء الاصطناعي (تجهيز سريع للهكاثون) ---
urls = ['google.com', 'bank-login-update.com', 'github.com', 'verify-free-money.xyz']
labels = [0, 1, 0, 1] 
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(urls)
model = RandomForestClassifier()
model.fit(X, labels)

# --- 2. تصميم الصفحة المطور (CSS + HTML) ---
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>رادار الأمن السيبراني</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; background: #0f172a; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background: #1e293b; padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); text-align: center; width: 450px; border: 1px solid #334155; }
        h1 { color: #3b82f6; margin-bottom: 25px; }
        input { width: 100%; padding: 14px; margin: 15px 0; border-radius: 10px; border: 1px solid #334155; background: #0f172a; color: white; box-sizing: border-box; outline: none; }
        button { background: #3b82f6; color: white; border: none; padding: 14px; border-radius: 10px; cursor: pointer; font-weight: bold; width: 100%; font-size: 16px; transition: 0.3s; }
        button:hover { background: #2563eb; transform: translateY(-2px); }
        .result { margin-top: 25px; padding: 15px; border-radius: 10px; font-weight: bold; font-size: 18px; }
        .safe { background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid #22c55e; }
        .danger { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid #ef4444; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ رادار الأمن الذكي</h1>
        <form method="POST">
            <input type="text" name="url" placeholder="أدخل الرابط للفحص هنا..." required>
            <button type="submit">فحص الرابط الآن</button>
        </form>
        {% if result %}
        <div class="result {% if 'آمن' in result %}safe{% else %}danger{% endif %}">
            {{ result }}
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

# --- 3. الأوامر البرمجية (Logic) ---
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        user_url = request.form.get('url')
        query = vectorizer.transform([user_url])
        prediction = model.predict(query)
        result = "النتيجة: 🚨 رابط خبيث (تهديد!)" if prediction[0] == 1 else "النتيجة: ✅ رابط آمن"
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
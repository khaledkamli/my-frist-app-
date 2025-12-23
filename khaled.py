import os
from flask import Flask, render_template_string, request
from urllib.parse import urlparse

app = Flask(__name__)

# دالة تحليل الروابط المحدثة
def analyze_url(url):
    score = 0
    reasons = []
    if not url: return "آمن ✅", [], 0
    
    if not url.startswith("https"):
        score += 30
        reasons.append("لا يستخدم تشفير HTTPS")
    if len(url) > 50:
        score += 20
        reasons.append("الرابط طويل بشكل مريب")
    if "@" in url:
        score += 40
        reasons.append("يحتوي على رمز '@' المخادع")
        
    status = "خطير جداً ❌" if score >= 70 else "متوسط الخطورة ⚠️" if score >= 30 else "آمن ✅"
    return status, reasons, score

# الواجهة المنسقة
HTML_PAGE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <style>
        body { font-family: sans-serif; background: #f4f4f9; text-align: center; padding: 50px; }
        .card { background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); display: inline-block; width: 400px; }
        input { width: 80%; padding: 10px; margin: 10px; border: 1px solid #ddd; border-radius: 5px; }
        button { background: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
        .result { margin-top: 20px; padding: 15px; border-radius: 10px; font-weight: bold; }
        .danger { background: #ffe6e6; color: #d9534f; }
        .safe { background: #e6ffed; color: #28a745; }
    </style>
</head>
<body>
    <div class="card">
        <h2>🔍 فاحص الروابط الذكي</h2>
        <form action="/check">
            <input type="text" name="url" placeholder="ضع الرابط هنا..." required>
            <button type="submit">فحص الآن</button>
        </form>
        {% if status %}
        <div class="result {% if 'خطير' in status %}danger{% else %}safe{% endif %}">
            <p>الحالة: {{ status }}</p>
            <ul> {% for r in reasons %} <li>{{ r }}</li> {% endfor %} </ul>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/check')
def check():
    url = request.args.get('url', '')
    status, reasons, score = analyze_url(url)
    return render_template_string(HTML_PAGE, status=status, reasons=reasons)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

# دالة تحليل الرابط (نفس منطقك البرمجي)
def analyze_url(url):
    score = 0
    reasons = []
    if not url.startswith("https"):
        score += 30
        reasons.append("الرابط لا يستخدم تشفير HTTPS")
    if len(url) > 50:
        score += 40
        reasons.append("الرابط طويل بشكل مريب")
    
    status = "آمن ✅"
    if score >= 70: status = "خطير جداً ❌"
    elif score >= 30: status = "متوسط الخطورة ⚠️"
    return status, reasons

# تصميم واجهة الموقع البسيطة
HTML_PAGE = '''
<!DOCTYPE html>
<html dir="rtl">
<head><meta charset="UTF-8"><title>رادار الأمن</title></head>
<body style="text-align:center; padding-top:50px; font-family:Arial;">
    <h1>🛡️ رادار الأمن الذكي</h1>
    <form action="/check">
        <input type="text" name="url" placeholder="ضع الرابط هنا..." style="width:300px; padding:10px;">
        <button type="submit" style="padding:10px;">افحص الآن</button>
    </form>
    {% if status %}
        <h2>النتيجة: {{ status }}</h2>
        <ul>{% for r in reasons %} <li>{{ r }}</li> {% endfor %} </ul>
    {% endif %}
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/check')
def check():
    url = request.args.get('url', '')
    status, reasons = analyze_url(url)
    return render_template_string(HTML_PAGE, status=status, reasons=reasons)

if __name__ == "__main__":
    # السطر الأهم لربط الكود بـ Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

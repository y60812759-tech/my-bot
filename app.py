from flask import Flask, render_template_string

app = Flask(__name__)

# منيو كشري التحرير - عربي
MENU = [
    {"id": 1, "name": "كشري ملك", "price": 45, "desc": "أرز ومكرونة وعدس وحمص وصوص طماطم"},
    {"id": 2, "name": "كشري إكسترا", "price": 60, "desc": "كشري ملك + كبده + ورد إضافي"},
    {"id": 3, "name": "طاجن لحمة", "price": 85, "desc": "طاجن لحمة بلدي مع أرز"},
    {"id": 4, "name": "رز بلبن", "price": 25, "desc": "رز بلبن بالمكسرات"},
    {"id": 5, "name": "حاجة ساقعة", "price": 15, "desc": "بيبسي / ميرندا / سفن"}
]

WHATSAPP_NUMBER = "201000000000"  # هتغيريه برقم العميل بعدين

HTML = """
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>كشري التحرير - منيو QR</title>
<style>
body { font-family: 'Cairo', sans-serif; background:#FFF8E7; margin:0; padding:15px; }
.header { background:#D32F2F; color:white; padding:20px; text-align:center; border-radius:15px; }
.card { background:white; border-radius:12px; padding:15px; margin:12px 0; box-shadow:0 2px 8px #0001; display:flex; justify-content:space-between; align-items:center; }
.price { color:#D32F2F; font-weight:bold; font-size:18px; }
.btn { background:#25D366; color:white; padding:12px; border:none; border-radius:8px; width:100%; font-size:16px; cursor:pointer; margin-top:5px; }
h2 { color:#D32F2F; }
</style>
</head>
<body>
<div class="header">
<h1>🍛 كشري التحرير</h1>
<p>أصل الكشري المصري - اطلب الآن على واتساب</p>
</div>
<h2>المنيو</h2>
<div id="menu">
{% for item in menu %}
<div class="card">
<div>
<b>{{ item.name }}</b><br>
<small>{{ item.desc }}</small>
</div>
<div style="text-align:left">
<div class="price">{{ item.price }} ج</div>
<button class="btn" onclick="order('{{ item.name }}','{{ item.price }}')">اطلب</button>
</div>
</div>
{% endfor %}
</div>
<script>
function order(name, price){
let text = `السلام عليكم، عايز أطلب: ${name} - السعر ${price} جنيه`;
let url = `https://wa.me/{{ whatsapp }}?text=${encodeURIComponent(text)}`;
window.open(url, '_blank');
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, menu=MENU, whatsapp=WHATSAPP_NUMBER)

if __name__ == '__main__':
    app.run()
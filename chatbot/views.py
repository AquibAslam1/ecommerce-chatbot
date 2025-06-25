from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from products.models import Product
from .models import ChatLog
import json
import re

# 🧠 Chatbot UI
@login_required
def chatbot_ui(request):
    return render(request, 'chatbot/chatbot.html')

# 🤖 Handle Chatbot Query
from django.db.models import Q
from django.http import JsonResponse
from .models import ChatLog
from products.models import Product
import json
import re

def query_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query', '').lower().strip()

        print("Query received:", query)  # 👈 Debug: log the query in terminal

        # 🔍 Search across name, description, and category
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )

        # 💰 Handle "under 5000" type price query
        price_match = re.search(r'under\s+(\d+)', query)
        if price_match:
            price_limit = int(price_match.group(1))
            products = products.filter(price__lt=price_limit)

        if products.exists():
            response = ", ".join([
                f"<a href='/chatbot/product/{p.id}/' target='_blank'>{p.name}</a>"
                for p in products[:10]
            ])
        else:
            response = "❌ No matching products found. Try different keywords."

        ChatLog.objects.create(
            user=request.user if request.user.is_authenticated else None,
            user_query=query,
            bot_response=response
        )

        return JsonResponse({'response': response})



# 🛍️ Product Detail View
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'chatbot/product_detail.html', {'product': product})

# 📜 View Chat History
@login_required
def chat_history(request):
    logs = ChatLog.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'chatbot/chat_history.html', {'logs': logs})


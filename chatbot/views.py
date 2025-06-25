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

from django.db.models import Q

from django.db.models import Q
import json
import re

# Stopwords list (you can expand this)
STOPWORDS = ['i', 'want', 'show', 'me', 'the', 'a', 'an', 'to', 'get', 'find']

def query_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query', '').lower()

        # Start with all products
        products = Product.objects.all()

        # Filter by price (under/below X)
        price_match = re.search(r'(under|below)\s*(\d+)', query)
        if price_match:
            price_limit = int(price_match.group(2))
            products = products.filter(price__lt=price_limit)

        # Filter by product name or category keywords
        keywords = ['iphone', 'apple', 'redmi', 'oneplus', 'phone', 'mobile',
                    'laptop', 'dell', 'hp', 'lenovo', 'asus',
                    'book', 'books', 'headphone', 'earbuds', 'earphone', 'boat', 'sony',
                    'watch']

        filtered = Product.objects.none()

        for word in keywords:
            if word in query:
                filtered |= Product.objects.filter(name__icontains=word) | Product.objects.filter(category__icontains=word)

        # If both filters applied
        if price_match and filtered.exists():
            products = products & filtered
        elif filtered.exists():
            products = filtered

        # Return response
        if products.exists():
            response = ", ".join([f"<a href='/chatbot/product/{p.id}/' target='_blank'>{p.name}</a>" for p in products])
        else:
            response = "❌ No matching products found. Try different keywords."

        # Save ChatLog
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


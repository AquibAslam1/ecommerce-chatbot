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
        query = data.get('query', '').lower().strip()

        # Remove punctuation for better match
        query_cleaned = re.sub(r'[^\w\s]', '', query)

        # First attempt: Full query match
        products = Product.objects.filter(
            Q(name__icontains=query_cleaned) |
            Q(category__icontains=query_cleaned) |
            Q(description__icontains=query_cleaned)
        )

        # Fallback: Tokenized smart search without stopwords
        if not products.exists():
            words = [word for word in query_cleaned.split() if word not in STOPWORDS]
            q_object = Q()
            for word in words:
                q_object |= Q(name__icontains=word)
                q_object |= Q(category__icontains=word)
                q_object |= Q(description__icontains=word)
            if words:
                products = Product.objects.filter(q_object)

        # Build bot response
        if products.exists():
            response = ", ".join(
                [f"<a href='/chatbot/product/{p.id}/' target='_blank'>{p.name}</a>" for p in products]
            )
        else:
            response = "❌ No matching products found. Try different keywords."

        # Save chat
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


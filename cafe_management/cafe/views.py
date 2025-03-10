from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Order
from .forms import OrderForm

# Отображение всех заказов
def orders_list(request):
    selected_status = request.GET.get('status')
    if selected_status:
        orders = Order.objects.filter(status=selected_status)
    else:
        orders = Order.objects.all()
    context = {
        'orders': orders,
        'statuses': Order.ORDER_STATUS,
        'selected_status': selected_status
    }
    return render(request, 'cafe/orders_list.html', context)

# Добавление заказа
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('orders_list')
    else:
        form = OrderForm()
    return render(request, 'cafe/add_order.html', {'form': form})

# Удаление заказа
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('cafe/orders_list')

# Изменение статуса заказа
def update_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in dict(Order.ORDER_STATUS):
            order.status = status
            order.save()
            return redirect('orders_list')
    return render(request, 'cafe/update_status.html', {'order': order})

# Изменение позиций в заказе
def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders_list')
    else:
        form = OrderForm(instance=order, initial={
            'items': order.items.all()
        })
    
    return render(request, 'cafe/edit_order.html', {'form': form, 'order': order})

# Расчет выручки за смену
def calculate_revenue(request):
    paid_orders = Order.objects.filter(status='paid')
    total_revenue = sum(order.total_price for order in paid_orders)
    return render(request, 'cafe/revenue.html', {'total_revenue': total_revenue})

# API: Получение списка заказов
def api_orders_list(request):
    orders = Order.objects.all()
    data = [{'id': o.id, 'table_number': o.table_number, 'total_price': str(o.total_price), 'status': o.status} for o in orders]
    return JsonResponse(data, safe=False)
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, DetailView, ListView
from .models import Item, OrderItem, Order, UserProfile, CostumerUserProfile
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import RegisterationForm


class HomeView(ListView):
    model = Item
    paginate_by = 3
    template_name = "home.html"

class ItemDetailView(DetailView):

    model = Item
    template_name = "item_detail.html"

class OrderSummaryView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(costumer__user=self.request.user, ordered=False)
            context = {
                'object': order,
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "شما سفارشی ندارید")
            return redirect("/")



def add_to_order(request, slug):
    item = get_object_or_404(Item, slug=slug)
    try:
        cos_user = CostumerUserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        cos_user = CostumerUserProfile.objects.create(user=request.user)

    order_item = OrderItem.objects.create(
        item=item,
        costumer=cos_user,
        user_profile=item.user)
    order_qs = Order.objects.filter(costumer__user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            messages.warning(request, "این آیتم قبلا در سفارش شما بوده است. ")
    else:
        order = Order.objects.create(costumer=cos_user)
        order.items.add()
    return redirect(reverse("merchant:item-detail", kwargs={
        'slug': item.slug,
    }))


class FinalizingView(View):
    pass


def remove_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user_profile__user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user_profile__user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "این محصول از سفارش شما حذف شد")
            return redirect("merchant:order-summary")
        else:
            messages.info(request, "این محصول در سفارش شما نیست")
            return redirect(reverse("merchant:item-detail", kwargs={
                'slug': item.slug,
            }))
    else:
        messages.info(request, "شما سفارشی ندارید")
        return redirect(reverse("merchant:item-detail", kwargs={
            'slug': item.slug,
        }))

class RegisterationFormView(View):
    def get(self, *args, **kwargs):
        form = RegisterationForm()
        context = {
            'form': form,

        }
        return render(self.request, "registeration.html", context)
    def post(self, *args, **kwargs):
        form = RegisterationForm(self.request.POST or None)
        if form.is_valid():
            form.save()
            print("The Form is Valid")
        return redirect("/")


class OrderConfirmView(View):

    def get(self, *args, **kwargs):
        try:
            order = Order.objects.filter(items__user_profile__user=self.request.user)
            context = {
                "objects": order,
            }
            return render(self.request, 'order_confirm.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "شما سفارشی ندارید")
            return redirect("/")

# def confirm_costumer(request):


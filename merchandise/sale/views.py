from django.shortcuts import render, redirect
from django.views.generic import FormView
from sale.forms import BarcodeForm
from sale.utils import Cart


class SaleView(FormView):
    """View for a new sale."""

    form_class = BarcodeForm
    template_name = "sale/sale.html"
    success_url = "/sale/"
    params = {
        'page_header': "New Sale"
    }

    def get_context_data(self, **kwargs):
        context = super(SaleView, self).get_context_data(**kwargs)

        # If create a new cart if it does not exist
        if not 'cart_items' in self.request.session:
            self.request.session['cart_items'] = {}
        
        # Set parameters for the template
        cart = Cart(self.request.session['cart_items'])
        self.params['total'] = cart.get_total_display()
        self.params['object_list'] = cart.get_items()
        context.update(self.params)

        return context

    def form_valid(self, form):
        # Get the cart from the session
        cart_items = self.request.session['cart_items']
        cart = Cart(cart_items)

        # Add the item to the cart
        cart.add_item(form.cleaned_data['item'])

        # Store the cart in the session
        self.request.session['cart_items'] = cart.cart_items

        return super(SaleView, self).form_valid(form)


def clear_cart(request):
    """View to clear the current cart and redirect to new sale."""

    del request.session['cart_items']

    return redirect("sale:sale")

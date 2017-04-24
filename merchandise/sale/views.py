from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import FormView, DetailView, ListView, UpdateView
from sale.models import Transaction, Sale
from sale.forms import BarcodeForm, TransactionForm, SaleReturnForm
from sale.utils import Cart
from crispy_forms.helper import FormHelper


class TransactionListView(ListView):
    """List View for Transaction."""

    model = Transaction
    params = {
        'page_header': "Sales"
    }

    def get_context_data(self, **kwargs):
        context = super(TransactionListView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context
    
    def get_queryset(self):
        return super(TransactionListView, self).get_queryset().order_by('-timestamp')


class CartView(FormView):
    """View for a new sale."""

    form_class = BarcodeForm
    template_name = "sale/cart.html"
    success_url = "/sale/cart/"
    params = {
        'page_header': "New Sale"
    }

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)

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

        return super(CartView, self).form_valid(form)


def clear_cart(request):
    """View to clear the current cart and redirect to new sale."""

    del request.session['cart_items']

    return redirect("sale:cart")


class TransactionCreateView(FormView):
    """View for a new Transaction."""

    form_class = TransactionForm
    template_name = "sale/transaction.html"
    params = {
        'page_header': "Complete Transaction"
    }

    def get(self, request, *args, **kwargs):
        # Redirect user if there aren't any items in the cart
        if not 'cart_items' in self.request.session or not self.request.session['cart_items']:
            return redirect("sale:cart")
            
        return super(TransactionCreateView, self).get(self, request, args, kwargs)


    def get_context_data(self, **kwargs):
        context = super(TransactionCreateView, self).get_context_data(**kwargs)

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
        cart = Cart(self.request.session['cart_items'])

        # Create a new transaction with these items for this customer
        self.object = Transaction.new_transaction(
            items=cart.get_items_list(), 
            transaction_type=form.cleaned_data['transaction_type'], 
            customer=form.cleaned_data['customer'], 
            user=self.request.user, 
            location=form.cleaned_data['location']
        )

        # Remove the items from the cart
        del self.request.session['cart_items']

        return super(TransactionCreateView, self).form_valid(form)

    
    def get_success_url(self):
        return reverse('sale:transaction_detail', kwargs={'pk':self.object.id})


class TransactionDetailView(DetailView):
    """Detail View for ItemDetails."""

    model = Transaction
    params = {
        'page_header': "Transaction"
    }

    def get_context_data(self, **kwargs):
        context = super(TransactionDetailView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context


class SaleDetailView(DetailView):    
    """Detail View for ItemDetails."""

    model = Sale
    params = {}

    def get_context_data(self, **kwargs):
        self.params['page_header'] = self.object.item
        context = super(SaleDetailView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context


class SaleReturnView(FormView):
    """Update View for Sale for a return."""

    form_class = SaleReturnForm
    template_name = "sale/sale_form.html"
    params = {
        'page_header': "Return Item"
    }

    def get_context_data(self, **kwargs):
        context = super(SaleReturnView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

    def get_initial(self):
        sale = get_object_or_404(Sale, pk=self.kwargs['pk'])
        return {'sale': sale}
    
    def form_valid(self, form):
        self.object = form.cleaned_data['sale']
        location = form.cleaned_data['location']
        user = self.request.user

        self.object.return_sale(location, user)

        return super(SaleReturnView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('sale:sale_detail', kwargs={'pk':self.object.id})

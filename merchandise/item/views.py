from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse
from item.forms import ItemForm
from item.models import ItemDetails, Item
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ItemDetailsListView(ListView):
    """List View for ItemDetails."""

    model = ItemDetails
    params = {
        'page_header': "Items"
    }

    def get_context_data(self, **kwargs):
        context = super(ItemDetailsListView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context


class ItemDetailsDetailView(DetailView):
    """Detail View for ItemDetails."""

    model = ItemDetails
    params = {}

    def get_context_data(self, **kwargs):
        self.params['page_header'] = self.object.name
        context = super(ItemDetailsDetailView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context


class ItemDetailsCreateView(CreateView):
    """Create View for ItemDetails."""

    model = ItemDetails
    fields = ['name', 'description', 'category', 'is_active']
    params = {
        'page_header': "New Item"
    }

    def get_context_data(self, **kwargs):
        context = super(ItemDetailsCreateView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        return form
    
    def get_success_url(self):
        return reverse('item:item_details_detail', kwargs={'pk':self.object.id})


class ItemDetailsUpdateView(UpdateView):
    """Update View for ItemDetails."""

    model = ItemDetails
    fields = ['name', 'description', 'category', 'is_active']
    params = {}

    def get_context_data(self, **kwargs):
        self.params['page_header'] = self.object.name
        context = super(ItemDetailsUpdateView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        return form
    
    def get_success_url(self):
        return reverse('item:item_details_detail', kwargs={'pk':self.object.id})


class ItemCreateView(CreateView):
    """Create View for Item."""

    model = Item
    form_class = ItemForm
    params = {}

    def get_context_data(self, **kwargs):
        self.params['page_header'] = "Add Size for {}".format(
                                        get_object_or_404(
                                            ItemDetails, 
                                            pk=self.kwargs.get('pk')
                                        ).name)
        context = super(ItemCreateView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context
    
    def get_success_url(self):
        return reverse('item:item_details_detail', kwargs={'pk':self.object.details.id})

    def get_initial(self):
        details = get_object_or_404(ItemDetails, pk=self.kwargs.get('pk'))
        return {
            'details':details
        }

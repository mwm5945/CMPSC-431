var Item = Backbone.Model.extend({
    urlRoot: '/api/items'
});

var ItemCollection = Backbone.Collection.extend({
    model: Item,
    url: '/api/items',
    comparator: function(object) {
        return object.get('name');
    }
});



var Size = Backbone.Model.extend({
    urlRoot: '/api/sizes'
});

var SizeCollection = Backbone.Collection.extend({
    model: Size,
    url: '/api/sizes',
    comparator: function(object) {
        return object.get('id');
    }
});




var Category = Backbone.Model.extend({
    urlRoot: '/api/categories'
});

var CategoryCollection = Backbone.Collection.extend({
    model: Category,
    url: '/api/categories'
});

var Page = Backbone.View.extend({
	render: function() {  
        var data = this.model.toJSON();
        this.$el.html(this.template(data));
        sizeContainer = new SizePage({model: this.model});
        sizeContainer.render();
        $(this.el.firstElementChild).modal('show'); 
	}
});

var ItemPage = Page.extend({   
    el: '#container',
    template: Handlebars.compile($("#item-details-template").html())
});

var SizePage = Backbone.View.extend({
    render: function() {
        if(this.model.get("sizes").length != 0){
            var sizes = new SizeCollection(this.model.get("sizes"));
            var scolumns = [{
                name: "size",
                label: "Size",
                cell: Backgrid.StringCell.extend({
                    render: function() {
                        sz = this.model.get("size");
                        if(sz) {
                            this.$el.text(sz);
                        }
                        else {
                            this.$el.text("None");
                        }
                        return this;
                    }
                }),
                editable: false
            },{
                name: "price",
                label: "Price",
                cell: "string",
                editable: false
            },{
                name: "sku",
                label: "SKU",
                cell: "integer",
                editable: false
            }];
            var sgrid = new Backgrid.Grid({
                columns: scolumns,
                collection: sizes
            });
            $("#size-container").append(sgrid.render().el);
        }
        else{
            $("#size-container").append("No Sizes Found");
        }
    }
});

var items = new ItemCollection();
items.fetch();

var columns = [{
    name: "name",
    label: "Name",
    // The cell type can be a reference of a Backgrid.Cell subclass, any Backgrid.Cell subclass instances like *id* above, or a string
    cell: Backgrid.Cell.extend({
        className: "col-md-6",
        render: function(){

            // You have access to the whole model - get values like normal in Backbone
            var name = this.model.get("name");
            var id = this.model.get("id");

            // Put what you want inside the cell (Can use .html if HTML formatting is needed)
            //this.$el.html("<a href='#view/"+id+"'>"+name+"</a>");
            this.$el.html("<a href='#'>"+ name +"</a>");

            // MUST do this for the grid to not error out
            return this;

        },
        events: {
            'click': function() {  
                var page = new ItemPage({model: this.model, modal: '#myModal'});            
                page.render();
            }
        }
    }),
    editable: false
  },{
      name: "category",
      label: "Category",
      editable: false,
      cell: Backgrid.StringCell.extend({
          className: "col-md-3"
      })
    },{
      name: "is_active",
      label: "Active",
      editable: false,
      cell: Backgrid.BooleanCell.extend({
          className: "col-md-3",
          render: function(){
              if(this.model.get("is_active")){
                  this.$el.html('<div class="text-left"><i class="fa fa-check text-success"></i></div>');
              }
              else {
                  this.$el.html('<div class="text-left"><i class="fa fa-times text-danger"></i></div>');
              }
              return this;
          }
      })
}];

// Initialize a new Grid instance
var grid = new Backgrid.Grid({
  columns: columns,
  collection: items
});

// Render the grid and attach the root to your HTML document
$("#item-container").append(grid.render().el);


// ClientSideFilter performs a case-insensitive regular
// expression search on the client side by OR-ing the keywords in
// the search box together.
var clientSideFilter = new Backgrid.Extension.ClientSideFilter({
  collection: items,
  placeholder: "Name",
  // The model fields to search for matches
  fields: ['name'],
  // How long to wait after typing has stopped before searching can start
  wait: 150,
  className: "input-field"
});

$("#search-form").append(clientSideFilter.render().el);

var categories = new CategoryCollection();
categories.fetch().done(function() {
    var temp = _.map(categories.models, function(o) {return {label: o.get('name'), value: o.get('name')};});
    

    var clientSideFilter2 = new Backgrid.Extension.SelectFilter({
        collection: items,
        field: "category",
        selectOptions: _.union([{label: "All", value: null}], temp)
    });

    $("#search-form").append(clientSideFilter2.render().el);
    $('select').material_select();
});

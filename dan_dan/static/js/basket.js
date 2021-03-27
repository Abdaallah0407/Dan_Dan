$(document).ready(function(){
    var form = $('#form-product');
    console.log(form);
    form.on('submit', function(e) {
        e.preventDefault();
        console.log('123');
        var nmb = $ ('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("title");
        var product_price = submit_btn.data("price");
        console.log(product_id);
        console.log(product_name);

        

        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
         var csrf_token = $('#form-product [name="csrfmiddlewaretoken"]').val();
         data["csrfmiddlewaretoken"] = csrf_token;
         var url = form.attr("action");
        console.log(data)
         $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");
                 console.log(data.products_total_nmb);
                 if (data.products_total_nmb){
                    $('#basket_total_nmb').text("("+data.products_total_nmb+")");
                    console.log(data.products)
                    $('.basket-items ul').html("");
                    $.each(data.products, function(k, v){
                        $('.basket-items ul').append('<li>'+ v.name+', ' + v.nmb + 'шт. ' + 'по ' + v.price_per_item + 'Сом  ' +
                            // '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
                            '</li>');
                     });
                 }

             },
             error: function(){
                 console.log("error")
             }
         })

   



    });

    $('.basket-container').on('click', function(){
       e.preventDefault();
       $('.basket-items').removeClass('invisible');
    });

    $('.basket-container').mouseover(function(){
        $('.basket-items').removeClass('invisible');
    });

    $('.basket-container').mouseout(function(){
        $('.basket-items').addClass('invisible');
    });

    $(document).on('click', '.delete-food', function(e){
        e.preventDefault();
        $(this).closest('li').remove();
    });
});
const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


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

        // var data = {};
        // data.product_id = product_id;
        // data.nmb = nmb;
        //     var csrf_token = $('#form-product [name="csrfmiddlevaretoken"]').val();
        //     data("csrfmiddlevaretoken") = csrf_token;
        //     var url = form.attr("action");
        //     $.ajax({
        //         url: url,
        //         type: POST,
        //         data: data,
        //         cache: true,
        //         success: function (data) {
        //             console.log("OK");
        //         },
        //         error: function(){
        //             console.log("error")
        //         }

        //     })


        $('.basket-item ul').append('<li>'+product_name+', ' + nmb + 'шт. ' + 'по ' + product_price + 'С  ' +
        '<a class="delete-food" href="">X</a>'+
        '</li>');
    });

    function foodsbasket() {
        $('.basket-item').removeClass('invisible');
        
    }

    $('.basket-container').on( function(){
        foodsbasket()
    });

    $('.basket-container').mouseover(function(){
        foodsbasket()
    });

    $('.basket-container').mouseout(function(){
        $('.basket-item').addClass('invisible');
    });

    $(document).on('click', '.delete-food', function(e){
        e.preventDefault();
        $(this).closest('li').remove();
    });
});
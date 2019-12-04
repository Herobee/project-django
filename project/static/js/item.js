$(function() {
    var order_list = [];
    $('#item-check:checked').each(function(i) {
        order_list[i] = $(this).val();
    });
    $('#total-price').val(order_list);
    $('.item-add-btn').click(function() {
        alert('Yout need to login!');
    });
    $('#order-btn').click(function() {
        var order_list = [];
        $('#item-check:checked').each(function(i) {
            order_list[i] = $(this).val();
        });
        alert(order_list);
        $('#total-price').val(order_list);
    });
    $('#item-check').change(function() {
        var order_list = [];
        $('#item-check:checked').each(function(i) {
            order_list[i] = $(this).val();
        });
        $('#total-price').val(order_list);
    });
    $('#add-tag').keypress(function(e) {
        if (e.which == 13) {
            alert('!!!!!');
        }
    });
    $('#add_cart_btn').click(function() {
        var result = confirm('Move to Your Cart?');
        if (result) {} else {
            return false;
        }
    });

    $('#item_count').change(function() {
        var price = $('#item_count').val();
        var p = $('#item_price').val();
        $('#total_price').val(price * p);
    });
});
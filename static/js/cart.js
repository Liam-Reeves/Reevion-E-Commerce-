document.addEventListener("DOMContentLoaded", function(){

    const addtoCartButtons = document.querySelectorAll('.add_to_cart');

    addtoCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            const productId = this.dataset.productId;
            const quantity = this.dataset.quantity || 1;
            
            addToCart(productId, quantity);
        });  



        
 
    });


});
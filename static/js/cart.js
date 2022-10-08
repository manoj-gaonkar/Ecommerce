var addButton = document.getElementsByClassName('update-cart')

for (var i = 0; i < addButton.length; i++){
    addButton[i].addEventListener('click', function() {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log(user);
        
        console.log("product id", productId, "action", action);
    })
}

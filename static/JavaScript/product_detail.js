document.addEventListener("DOMContentLoaded", function(event) {
    const btnPlus = document.getElementById("btnPlus");
    const btnMinus = document.getElementById("btnMinus");
    const txtQty = document.getElementById("txtQty");
    const pid = document.getElementById("pid");
    const btnCart = document.getElementById("btnCart");
    const btnFav = document.getElementById("btnFav");

    btnPlus.addEventListener("click", function() {
        let qty=parseInt(txtQty.value,10);
        qty=isNaN(qty)?0:qty;
        
        if(qty<10){
            qty++;
            txtQty.value=qty;
        }
    });

    btnMinus.addEventListener("click", function() {
        let qty=parseInt(txtQty.value,10);
        qty=isNaN(qty)?0:qty;

        if(qty>1){
            qty--;
            txtQty.value=qty;
        }
    });

    btnCart.addEventListener("click", function() {
        let qty=parseInt(txtQty.value,10);
        qty=isNaN(qty)?0:qty;
        
        if(qty>0){
            let postObj = { 
                'product_qty': qty, 
                'pid': pid.value
            }
            
            fetch("/addtocart",{
            method: 'POST',
            credentials: 'same-origin',
            headers:{
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': '{{ csrf_token }}',
            },
            body: JSON.stringify(postObj)
            }).then(response => {
                return response.json();
            }).then(data => {
                alert(data['status']);
            });

        }else{
            alert("Please Enter The Quantity");
        }
        
    });


    btnFav.addEventListener("click", function() {
        
        let postObj = { 
            'pid': pid.value
        }
        console.log(postObj);
        fetch("/favorite",{
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': '{{ csrf_token }}',
        },
        body: JSON.stringify(postObj)
        }).then(response => {
            return response.json();
        }).then(data => {
            alert(data['status']);
        });
        
    });


});

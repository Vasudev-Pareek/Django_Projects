var updateBtns = document.getElementsByClassName("update-cart")
for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        // console.log("productId",productId);
        // console.log("action",action);

        // console.log("user",user);
        if(user == 'AnonymousUser'){
            addCookieItem(productId, action)
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function addCookieItem(productId, action){
    console.log("Not logged - in");

    if (action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'quantity':1}
        }else{
            cart[productId]['quantity'] += 1
        }
    }

    if (action == 'remove'){
        cart[productId]['quantity'] -= 1

        if(cart[productId]['quantity'] <= 0){
            console.log("Remove item...");
            delete cart[productId]
            
        }
    }
    console.log('cart:', cart);
    document.cookie = 'cart='+ JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}


// function updateUserOrder(productId, action){
//     // console.log("user logged - in, sending the data");

//     let url = "/update_item/"

//     fetch(url, {
//         method:'POST',
//         headers:{
//             'Content-Type':'application/json',
//             'X-CSRFToken':csrftoken
//         },
//         body:JSON.stringify({'productId':productId, 'action':action})
//     })
//     .then((response)=>{
//         return response.json()
//     })
//     .then((data)=>{
//         // console.log("data:", data);
//         location.reload()
        
//     })
// }  

function updateUserOrder(productId, action) {
    console.log("user logged - in, sending the data");

    let url = "/update_item/"

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Server Error: " + response.status);
        }
        return response.json(); // Parsing the JSON response
    })
    .then(data => {
        // console.log(data);
        location.reload(); // Reload page after updating
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred: " + error.message);
    });
}























// modren javascript converted code ------------->

// let updateBtns = document.querySelectorAll(".update-cart")
// updateBtns.forEach(element => {
//     element.addEventListener("click", (e)=>{
//         let productId = e.target.dataset.product
//         let action = e.target.dataset.action
//         console.log("productId",productId);
//         console.log("action",action);
//     })
// });



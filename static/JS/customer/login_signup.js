ScrollReveal({ 
     reset: true ,
     distance:'100px',
     duration:1500,
     delay:400

});
ScrollReveal().reveal('.sign_in', { delay: 100 ,origin:'top'});
ScrollReveal().reveal('.in', { delay: 100 ,origin:'left'});
ScrollReveal().reveal('input', { delay: 100 ,origin:'bottom'});
ScrollReveal().reveal('.login_but', { delay: 100 ,origin:'right'});

function gotoRegister(){
     document.getElementById("fullForm").style.transform = "translateX(400px)";
}
function gotoForgotPassword(){
     document.getElementById("fullForm").style.transform = "translateX(-400px)";
}
function gotoLogin(){
     document.getElementById("fullForm").style.transform = "translateX(0px)";
}

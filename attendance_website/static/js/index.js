
var vid = document.getElementById("vid");
vid.play();
// vid.muted = false;
vid.addEventListener("ended",myhandler,false);
function myhandler(){
    document.getElementById("vid").remove();
}
const t1 = gsap.timeline({ defaults: { ease: "power1.out" }});
t1.to(".logo", {opacity:1, duration: 1, delay: 2.89});
t1.to(".banner", {opacity:1, duration: 1, /*onComplete:function(){
        document.getElementById("banner").style.opacity=0;}*/
});
// t1.to("header.scrolled img.banner",{opacity:0});

// const tl = gsap.timeline({ defaults: { ease: "power1.out" }, delay:10 });
// tl.fromTo("#vid", { opacity: 1 }, { opacity: 0, duration: 10 },);
// t1.delay(5);
// tl.fromTo(".logo", { opacity: 0 }, { opacity: 1, duration: 1 } );

$(document).ready(function(e){
    $('.btn').on('mouseenter',function(e){
        x = e.pageX -$(this).offset().left;
        y = e.pageY -$(this).offset().top;
        $(this).find('span').css({top:y,left:x})
    })
    $('.btn').on('mouseout',function(e){
        x = e.pageX -$(this).offset().left;
        y = e.pageY -$(this).offset().top;
        $(this).find('span').css({top:y,left:x})
    })
})





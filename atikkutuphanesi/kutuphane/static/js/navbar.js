/* const drop = document.querySelector(".atik"); */
/* const navDrop = document.querySelector(".navDrop"); */
/* const li1 = document.querySelector(".li1"); */
var atikList = ["Atık pil ve akü" , "Atık yağ",  "Ambalaj atıkları", "Atık lastik" , "Tehlikeli atık" , "Biyobozunur atık" , "Bitkisel atık yağ" , "Atık elektrikli elektronik aletler" , "Tıbbi atık"];
var atikhref = ["/atiklist#atikpil","/atiklist#atikyag","/sectionpart/atiklist.html#ambalajatik","/sectionpart/atiklist.html#yağatik","/sectionpart/atiklist.html#pilatik","/sectionpart/atiklist.html#elektronikatik","/sectionpart/atiklist.html#bitkiselatik","/sectionpart/atiklist.html#biyobozunuratik","http://127.0.0.1:8000/atiklist/tibbiatik"]
const ul = document.querySelector(".navDropUl");
const a1 = document.querySelectorAll(".a1");

const ul2 = document.querySelector(".ul");

// atık listesi
function atikAdd(){
    atikList.forEach(function(item, index){
        const newLi = document.createElement("li");
        const a = document.createElement("a");
        a.setAttribute("href",atikhref[index]);
        a.setAttribute("class","atiklist");
        a.innerText=item;
        newLi.appendChild(a);
        ul.appendChild(newLi);
        

    })
}

// burger butonu 
const burger = document.querySelector(".burger");
const navDrop = document.querySelector(".navDrop");
burger.addEventListener("click", function(){
    console.log("burger worked");
    navDrop.classList.toggle("toggle");


})
navSlide = () =>{
    
    

};




//responsive taşıma 
/* const navSlide = () =>{
    const burger = document.querySelector(".burger");
    const nav = document.querySelector(".ul");
    const navLinks = document.querySelectorAll(".ul li");
    
    burger.addEventListener("click",()=>{
      nav.classList.toggle("nav-activate");
      navLinks.forEach((link,index)=>{
      
        link.style.animation=`navLinkFade 0.5s ease forwards`;
     // console.log(index/7);
    });
      
    });
    
     
    
      
  };
  */
 /*  console.log(drop.style)
  
  
  // about hove
 
function hoverFunc(drom){
    drop.addEventListener("click",function(){
        navDrop.classList.toggle("toggle");
        li1.classList.toggle("liHoverBack");

        
  
    })
   
    
} */

/* function textDecoration(item){
    item.addEventListener("click",function(e){
        a1.forEach(function(remove){
            remove.classList.remove("liHoverBack");
            console.log(e.target);

            
        })
        
       
        
        e.target.classList.toggle("liHoverBack");

        


    });
} */
navSlide();
atikAdd();
/* navSlide(); */
/* hoverFunc();
textDecoration(ul2) */
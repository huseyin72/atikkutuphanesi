const drop = document.querySelector(".atik");
const navDrop = document.querySelector(".navDrop");
const li1 = document.querySelector(".li1");
var atikList = ["Tehlikeli atık" , "Tıbbi atık",  "Ambalaj atıkları", "Atık yağ" , "Atık pil ve akü" , "Atık elektrikli elektronik ekipmanlar" , "Bitkisel atık yağ" , "Biyobozunur atık" , "Atık lastik"];
const ul = document.querySelector(".navDropUl");
const a1 = document.querySelectorAll(".a1");

const ul2 = document.querySelector(".ul");

// atık listesi
function atikAdd(){
    atikList.forEach(function(item){
        const newLi = document.createElement("li");
        const a = document.createElement("a");
        a.setAttribute("href","#")
        a.innerText=item;
        a.classList="a";
        newLi.appendChild(a);
        ul.appendChild(newLi);
        

    })
}



//responsive taşıma 
const navSlide = () =>{
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
 
  console.log(drop.style)
  
  
  // about hove
 
function hoverFunc(drom){
    drop.addEventListener("click",function(){
        navDrop.classList.toggle("toggle");
        li1.classList.toggle("liHoverBack");

        
  
    })
   
    
}
function textDecoration(item){
    item.addEventListener("click",function(e){
        a1.forEach(function(remove){
            remove.classList.remove("liHoverBack");
            console.log(e.target);

            
        })
        
       
        
        e.target.classList.toggle("liHoverBack");

        


    });
}

atikAdd();
navSlide();
hoverFunc();
textDecoration(ul2)
// for particles
// import {particle} from '../../../node_modules'

// console.log(typeof particle)


// for navbar toggle
var mobile= document.querySelector('.for-mobile')
var mobileNav= document.querySelector('.nav-m')
const clickDiv= ()=>{
    mobile.classList.toggle('mobile')
    mobileNav.classList.toggle('mobile-nav')
}



// animation

var y= 0
var x= 0

var textContainer= document.querySelector('.bio-writing')
var mobileCont= document.querySelector('.details-for-mobile')
var mobileTxt= 'I am Zechariah Adebayo'
var myText= 'am Zechariah, a passionate software developer who\'s concerned with solving real-world problems with my software development skills. Being an intuitive type, I like burrowing into the core of any concepts and problems, so as to gain the overall knowledge of it, and to come up with a better approach for a solution. My Strength, however, is more on the backend side of software development.'

// for large screen 
function animate1(){
    if(y < myText.length){
        textContainer.innerHTML += myText.charAt(y)
        y++
        setTimeout(animate1, 80)
    }
}

// for mobile
function animate2(){
    if(x < mobileTxt.length){
        mobileCont.innerHTML += mobileTxt.charAt(x)
        x++
        setTimeout(animate2, 150)
    }
}

// writing the above functions separately is redundant, because they pretty much do the same thing.
// A better approach would have being: giving my function 2 parameters-- 1 for the the actual text, the other for the container to insert the text during iteration.
// I didn't do it that way cuz javascript could not let me use the "length" attribute on a function parameter-- it raised TypeError
animate1()
animate2()


// Love Calculator App
 function loveCalculator(){
    
    var myName = prompt("Enter your name: ");
    var partnerName = prompt("Enter your partner's name: ");

    var r = Math.random(),
        r = Math.floor(r * 100) + 1;

    return myName + " ❤ " + partnerName + " at " + r + " %.";
    
 }

 loveCalculator();

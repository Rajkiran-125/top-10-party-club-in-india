function getBotResponse(input) {
    //rock paper scissors
    if (input == "rock") {
        return "paper";
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    let newstring = "Top 10 Indian Club: <br>1. Clube Cubana <br>2. Kitty Su Mumbai <br>3. Venom Bar<br>4. SinQ Night Club<br>5. Hammerzz Nightclub<br>6. Sin City<br>7. Pink Fly Lounge<br>8. Club Tito's<br>9. Owl-The Premium Night Club<br>10. The Brown Room";
    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else if (input == "clubs") {
        return(newstring)+"<br><br>from above which one club you are looking?";  
    } else if (input == "1"){
        return "Location: Club Cubana, Arpora Hill, Anjuna, North Goa. <br> Club Timings: Open from 9:30 PM to 4:00 AM.";
    } else if (input == "2"){
        return "Ground Floor The LaLit Mumbai, Airport Rd, Navpada, Marol, Andheri East, Mumbai, Maharashtra 400059";
    } else if (input == "3"){
        return "Ground Floor The LaLit Mumbai, Airport Rd, Navpada, Marol, Andheri East, Mumbai, Maharashtra 400059";
    }

    else {  
        return "Try asking something else!";
    }
    

    

}
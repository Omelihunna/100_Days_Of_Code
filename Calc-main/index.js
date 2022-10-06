const buttons = document.querySelectorAll("button")
const display = document.querySelector("#display")

buttons.forEach((button) => {
    button.onclick = () => {
        if (button.id == "clear") {;
            display.innerHTML = "";
        } else if (button.id == "backspace") {
            let displayText = display.innerHTML.toString();
            display.innerHTML = displayText.slice(0, displayText.length - 1);
        } else if (display.innerHTML != "" && button.id == "equal") {
            display.innerHTML = eval(display.innerHTML)
        } else if (display.innerHTML == "" && button.id == "equal") {
            display.innerHTML = "Empty!";
            setTimeout(() => (display.innerHTML = ""), 2000);
        } else {
            display.innerHTML += button.id
        }
    }    
});

// $("button").click((event) => {
//     let idx = event.target.id;
//     let displayText = $("#display").text();
//     if (idx == "clear") {
//         $("#display").text("");
//     } else if (idx == "backspace") {
//         let newDisplay = displayText.slice(0, displayText.length - 1);
//         $("#display").text(newDisplay);
//     } else if (displayText != "" && idx == "equal") {
//         $("#display").text(`${eval(displayText)}`);
//     } else {

//     }
// });

const themeToggler = document.querySelector(".theme-toggler");
const calculator = document.querySelector(".calculator");
const toggleIcon = document.querySelector("toggler-icon");
let isDark = true;
themeToggler.onclick = () => {
    calculator.classList.toggle("dark");
    themeToggler.classList.toggle("active");
    isDark = !true;
}
const getURL = document.querySelector(".getURL");
const showURL = document.querySelector(".showURL");
const url = "http://localhost:5000/tweet";
var oReq = new XMLHttpRequest();

const urlGet = () => {
    oReq.open("GET", url);
    oReq.setRequestHeader("Content-Type", "text/plain")
    oReq.send();
}

const reqTest = () => {
    console.log(oReq.responseText);
    console.log(oReq.responseURL);
}

getURL.addEventListener("click", urlGet);
showURL.addEventListener("click", reqTest);
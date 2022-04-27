const getURL = document.querySelector(".getURL");
const showURL = document.querySelector(".showURL");
const url = "http://localhost:5000/get";
var oReq = new XMLHttpRequest();

const urlGet = () => {
    oReq.addEventListener("load", () => console.log("OK"));
    oReq.open("GET", url);
    //oReq.responseType = "json";
    oReq.send();
}

const reqTest = () => {
    console.log(oReq.responseText);
    console.log(oReq.responseType);
    console.log(oReq.responseURL);
}

getURL.addEventListener("click", urlGet);
showURL.addEventListener("click", reqTest);
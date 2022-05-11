const getButton = document.querySelector(".get");
const outputButton = document.querySelector(".output");
const clickImage = document.getElementById("images");
const reqURL = "http://localhost:5000/tweet";
var oReq = new XMLHttpRequest();

const getURL = () => {
    oReq.open("GET", reqURL);
    oReq.setRequestHeader("Content-Type", "text/plain");
    oReq.send();
}

const refreshImages = () => {
    if (!oReq.responseURL) {
        alert("1.get\n2.output");
        return;
    }
    // console.log(oReq.responseText);
    // console.log(oReq.responseURL);
    let arr = [];
    for (let i = 0; i < JSON.parse(oReq.responseText).includes["media"].length; i++) {
        if (JSON.parse(oReq.responseText).includes["media"][i]["type"] == "photo") {
            arr.push(JSON.parse(oReq.responseText).includes["media"][i]["url"]);
        }
    }
    arr.forEach((e) => {
        let imgElement = document.createElement("img");
        let urlElement = document.createElement("p");
        let imgArea = document.getElementById("images");
        let urlArea = document.getElementById("url");
        imgElement.src = e;
        imgElement.height = 240;
        urlElement.textContent = e;
        imgArea.appendChild(imgElement);
        urlArea.appendChild(urlElement);
    });
}

getButton.addEventListener("click", getURL);
outputButton.addEventListener("click", refreshImages);
clickImage.addEventListener("click", e => {
    if(e.target.src) window.open(e.target.src);
});
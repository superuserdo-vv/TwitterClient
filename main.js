const myUserId = '1511703981655212035';
const getUrl = `https://api.twitter.com/2/users/${myUserId}/tweets`;
const getTweet = document.querySelector('.getTweet');

const getUserTweets = () => {
    let oReq = new XMLHttpRequest();

    if (!oReq) {
        console.log('HMLHttpRequest error');
        return false;
    }
    oReq.onreadystatechange = getContents;
    oReq.open('GET', getUrl + '&max_results=5');
    oReq.send();
}

const getContents = (req) => {
    try {
        if (req.readyState === XMLHttpRequest.DONE) {
            if (req.status === 200) {
                console.log(req.body);
            }
        }
    }
    catch (e) {
        console.log(e.description);
    }

}

getTweet.addEventListener('click', getUserTweets);
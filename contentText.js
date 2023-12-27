const subreddit = 'ask';
const postId = '18s04ay';


const getData = (subreddit, postId) => {
    fetch(`https://www.reddit.com/r/${subreddit}/comments/${postId}.json`)
    .then(response => response.json())
    .then(data => {
        // Process the JSON data here

        const resData = data[0].data.children[0].data;
        const title  = resData.title;
        const content = resData.selftext;

        const fs = require('fs');
        fs.writeFile('./Assets/content.txt', content, (err) => {
            if (err) {
                console.error(err);
                return;
            }
        });

        fs.writeFile('./Assets/title.txt', title, (err) => {
            if (err) {
                console.error(err);
                return;
            }
        });

    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}

getData(subreddit, postId);
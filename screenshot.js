const puppeteer = require('puppeteer');

async function takeElementScreenshot(url, elementSelector, outputFileName) {
    const browser = await puppeteer.launch({ headless: 'new' });
    const page = await browser.newPage();

    try {
        await page.goto(url, { waitUntil: 'domcontentloaded' });

        await page.waitForSelector(elementSelector);

        const boundingBox = await page.$eval(elementSelector, (element) => {
            const rect = element.getBoundingClientRect();
            return {
                x: rect.x,
                y: rect.y,
                width: rect.width,
                height: rect.height,
            };
        });
        await page.screenshot({ path: 'screenshot.png' });

        await page.screenshot({
            path: outputFileName,
            clip: {
                x: boundingBox.x - 10,
                y: boundingBox.y - 45,
                width: boundingBox.width + 15,
                height: boundingBox.height + 55,
            },
        });
    } finally {
        await browser.close();
    }

    const fs = require('fs')
    fs.unlink('screenshot.png', (err) => {
        if (err) {
            console.error(err)
            return
        }
    })
}

// Example usage
const webpageUrl = 'https://www.reddit.com/r/ask/comments/18ramj4/straight_men_can_you_tell_if_anpther_guy_is/';
const targetElementSelector = 'h1';
const outputFilename = './Assets/element_screenshot.png';

takeElementScreenshot(webpageUrl, targetElementSelector, outputFilename).catch((error) => {
    console.error(error);
    process.exit(1); // Exit with an error code
});

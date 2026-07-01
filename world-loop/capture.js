const { chromium } = require('/Users/david/Documents/GitHub/fm-jun26/node_modules/playwright-chromium');
const path = require('path');

const W = 1920, H = 812;
const args = process.argv.slice(2);
const N = parseInt(args[0] || '300', 10);
const testT = args[1] !== undefined ? parseFloat(args[1]) : null;
const htmlFile = process.env.HTML || 'anim.html';
const outDir = process.env.OUT || 'frames';

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, htmlFile));
  await page.waitForFunction('window.__ready === true');

  if (testT !== null) {
    await page.evaluate((t) => window.render(t), testT);
    await page.screenshot({ path: path.join(__dirname, `test_${Math.round(testT*1000)}.png`) });
    console.log('test frame at t=' + testT + ' (' + htmlFile + ')');
  } else {
    const pad = (n) => String(n).padStart(4, '0');
    for (let f = 0; f < N; f++) {
      await page.evaluate((tt) => window.render(tt), f / N);
      await page.screenshot({ path: path.join(__dirname, outDir, `${pad(f)}.png`) });
    }
    console.log('captured ' + N + ' frames -> ' + outDir);
  }
  await browser.close();
})();

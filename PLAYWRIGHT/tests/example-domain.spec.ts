import { test, expect, chromium } from '@playwright/test';

test('test con slowMo', async () => {
  const browser = await chromium.launch({ headless: false, slowMo: 1000 });
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('https://example.com/');
  await page.getByRole('link', { name: 'Learn more' }).click();

  await browser.close();
});

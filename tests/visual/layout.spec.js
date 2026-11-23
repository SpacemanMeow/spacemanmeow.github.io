// @ts-check
const { test, expect } = require('@playwright/test');

// Representative page types from D21, one per layout family. Paths are relative
// to _site/ and must exist in the 5-language combined build.
const PAGES = [
  ['home', '/'],
  ['app', '/apps/meow-money-manager/'],
  ['article', '/posts/alternatives-to-assistive-touch/'],
  ['faq-hub', '/faq/'],
  ['tag-hub', '/tags/'],
  ['glossary-hub', '/glossary/'],
  ['docs', '/docs/'],
];

for (const [name, path] of PAGES) {
  test(`${name} — 无横向溢出且关键元素可见`, async ({ page }) => {
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));

    // Wait for CSS/fonts: measuring at domcontentloaded catches the unstyled
    // state where overflow-x:auto is not yet applied (false-positive overflow).
    const response = await page.goto(path, { waitUntil: 'load' });
    expect(response?.status(), `HTTP status for ${path}`).toBe(200);
    await page.evaluate(() => document.fonts.ready);

    // D21 core: rendered width must not exceed viewport width.
    const widths = await page.evaluate(() => ({
      scroll: document.documentElement.scrollWidth,
      client: document.documentElement.clientWidth,
      bodyScroll: document.body.scrollWidth,
    }));
    expect(widths.scroll, `horizontal overflow on ${path}`).toBeLessThanOrEqual(widths.client + 1);
    expect(widths.bodyScroll, `body overflow on ${path}`).toBeLessThanOrEqual(widths.client + 1);

    // Structural smoke checks that previously relied on manual eyeballing.
    await expect(page.locator('h1')).toHaveCount(1);
    await expect(page.locator('main')).toBeVisible();
    await expect(page.locator('.site-header')).toBeVisible();
    await expect(page.locator('.site-footer')).toBeVisible();

    // Nav must be reachable at every viewport (hamburger toggle below 768px).
    const navToggle = page.locator('[data-nav-toggle]');
    const navLinks = page.locator('.site-nav a');
    const navReachable = await navToggle.isVisible() || await navLinks.first().isVisible();
    expect(navReachable, 'navigation unreachable').toBeTruthy();

    expect(errors, `page errors on ${path}`).toEqual([]);
  });
}

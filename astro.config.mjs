// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Apex custom domain, so `base` stays '/'. If this ever moves to
// adilsoncarvalho.github.io/<repo>, `base` must become '/<repo>' or every
// internal link breaks.
export default defineConfig({
  site: 'https://zettelkasten.adilsoncarvalho.com',
  base: '/',
  // Directory format emits dist/outline/index.html, which GitHub Pages serves at
  // both /outline and /outline/. The 'file' format emits outline.html, which
  // 404s on the trailing-slash form — bad for inbound links we do not control.
  build: { format: 'directory' },
  trailingSlash: 'ignore',
  integrations: [sitemap()],
});

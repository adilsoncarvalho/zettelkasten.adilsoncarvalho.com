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
  // /divisions was the canonical table before it split into core and personal
  // tiers. Static output emits a meta-refresh page, so old links still land.
  redirects: { '/divisions': '/core' },
  // Compression drops a whitespace run entirely when the run contains a newline,
  // so `word\n<em>next</em>` renders as "wordnext". Prose here wraps at the print
  // margin, which puts a newline before most inline tags, so any sentence that
  // changes style mid-way loses the space. Keep this off: the alternative is
  // hand-placing {' '} at every wrap, and the next reflow undoes it. The cost is
  // uncompressed bytes only — /outline grows about half again in raw size, and
  // only a few percent over the gzip that Pages actually serves.
  compressHTML: false,
  integrations: [sitemap()],
});

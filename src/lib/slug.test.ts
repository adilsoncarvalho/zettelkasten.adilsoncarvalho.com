import { test } from 'node:test';
import assert from 'node:assert/strict';
import { slug, text } from './slug.ts';

test('markup around the words does not reach the fragment', () => {
  assert.equal(slug('<span class="ad">1000</span> Thought and expression'), '1000-thought-and-expression');
  assert.equal(slug('How <em>each</em> address was derived'), 'how-each-address-was-derived');
});

test('the escaped entities the renderer emits resolve before slugifying', () => {
  // Astro escapes & as &#38;, so a raw pass would cut "-38-" into the fragment.
  assert.equal(slug('Cards &#38; drawers'), 'cards-drawers');
  assert.equal(slug('Cards &amp; drawers'), 'cards-drawers');
  assert.equal(text('&#x2014; dash'), '— dash');
});

test('apostrophes close up rather than splitting the word', () => {
  assert.equal(slug('One filer&#39;s tier'), 'one-filers-tier');
  assert.equal(slug('One filer’s tier'), 'one-filers-tier');
});

test('punctuation and em dashes collapse to single hyphens', () => {
  assert.equal(slug('The four digits — meaning'), 'the-four-digits-meaning');
  assert.equal(slug('1. A sub-discipline under an existing discipline'), '1-a-sub-discipline-under-an-existing-discipline');
  assert.equal(slug('  Spaced  out  '), 'spaced-out');
});

test('a heading with no slugifiable content fails the build rather than sharing an empty id', () => {
  assert.throws(() => slug('— —'), /No fragment/);
  assert.throws(() => slug('<span class="ad"></span>'), /No fragment/);
});

test('an out-of-range character reference is left as written instead of throwing', () => {
  assert.equal(slug('a&#1114112;b'), 'a-1114112-b');
});

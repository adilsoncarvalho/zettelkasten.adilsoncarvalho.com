/**
 * Heading fragments — cut a stable URL fragment from rendered heading markup.
 *
 * Headings on this site are authored as inline HTML rather than Markdown, so
 * there is no Markdown pipeline to slugify them. `Heading.astro` renders its
 * slot to a string and hands that string here, which means the input arrives
 * carrying tags and the escaped entities the renderer emits. Both are resolved
 * before the fragment is cut.
 *
 * Kept free of imports so it can be unit-tested with plain `node --test`.
 */

const NAMED: Record<string, string> = {
  amp: '&',
  lt: '<',
  gt: '>',
  quot: '"',
  apos: "'",
  nbsp: ' ',
};

const decode = (ref: string, whole: string): string => {
  if (ref[0] !== '#') return NAMED[ref.toLowerCase()] ?? whole;
  const hex = ref[1] === 'x' || ref[1] === 'X';
  const code = Number.parseInt(hex ? ref.slice(2) : ref.slice(1), hex ? 16 : 10);
  // A code point outside Unicode would throw in fromCodePoint. Leave the
  // reference as written instead: it slugifies to nothing, which is wrong but
  // not fatal, where a throw takes the whole build down.
  return Number.isInteger(code) && code >= 0 && code <= 0x10ffff
    ? String.fromCodePoint(code)
    : whole;
};

/** Rendered heading markup → its plain text, tags dropped and entities resolved. */
export function text(html: string): string {
  return html
    .replace(/<[^>]*>/g, '')
    .replace(/&(#[Xx]?[0-9A-Fa-f]+|[A-Za-z]+);/g, (whole, ref: string) => decode(ref, whole))
    .replace(/\s+/g, ' ')
    .trim();
}

/**
 * Heading text → the fragment that addresses it.
 *
 * ASCII letters and digits survive; every other run collapses to a single
 * hyphen. Apostrophes close up first, so "one filer's tier" reads as
 * `filers` rather than splitting the word in two.
 *
 * Throws when nothing survives: a heading made entirely of punctuation or
 * non-Latin script has no fragment to derive, and failing the build is better
 * than shipping an empty `id` that every such heading would share.
 */
export function slug(html: string): string {
  const out = text(html)
    .toLowerCase()
    .replace(/['‘’]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
  if (!out) throw new Error(`No fragment can be derived from heading: ${text(html) || html}`);
  return out;
}

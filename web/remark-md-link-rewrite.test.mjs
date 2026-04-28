// web/remark-md-link-rewrite.test.mjs
//
// Phase 9 / C-P6-6 — fixture test for the lang-neutral throw guard and the
// drop-<a>-wrapper-for-out-of-collection branch added in Phase 6.4. Runs
// against the plugin without bringing in remark-parse: build minimal mdast
// trees inline. The plugin uses unist-util-visit which only requires the
// `type` + `children` shape we hand-build here.
import { describe, it, expect } from 'vitest';
import remarkMdLinkRewrite from './remark-md-link-rewrite.mjs';

function tree(linkUrl, children = [{ type: 'text', value: 'X' }]) {
  return {
    type: 'root',
    children: [
      { type: 'paragraph', children: [{ type: 'link', url: linkUrl, children }] },
    ],
  };
}

const transform = remarkMdLinkRewrite();

describe('remark-md-link-rewrite', () => {
  it('throws when entry lacks frontmatter.lang and has known .md cross-ref', () => {
    const t = tree('USER_GUIDE.md');
    const file = { data: {} };
    expect(() => transform(t, file)).toThrow(/Lang-neutral/);
  });

  it('rewrites .md cross-ref to /<lang>/guide/<slug>', () => {
    const t = tree('USER_GUIDE.md');
    const file = { data: { astro: { frontmatter: { lang: 'zh' } } } };
    transform(t, file);
    expect(t.children[0].children[0].url).toBe('/zh/guide/user-guide');
  });

  it('routes CHANGELOG.md to /<lang>/changelog (dedicated route)', () => {
    const t = tree('CHANGELOG.md');
    const file = { data: { astro: { frontmatter: { lang: 'en' } } } };
    transform(t, file);
    expect(t.children[0].children[0].url).toBe('/en/changelog');
  });

  it('preserves anchor on cross-ref', () => {
    const t = tree('USER_GUIDE.md#install');
    const file = { data: { astro: { frontmatter: { lang: 'ja' } } } };
    transform(t, file);
    expect(t.children[0].children[0].url).toBe('/ja/guide/user-guide#install');
  });

  it('drops <a> wrapper for out-of-collection ./self_deploy/', () => {
    const t = tree('./self_deploy/', [{ type: 'text', value: 'sd' }]);
    const file = { data: { astro: { frontmatter: { lang: 'zh' } } } };
    transform(t, file);
    // The link node was replaced by its text child.
    expect(t.children[0].children[0].type).toBe('text');
    expect(t.children[0].children[0].value).toBe('sd');
  });

  it('skips absolute URL (http://) untouched', () => {
    const t = tree('https://example.com/foo');
    const file = { data: { astro: { frontmatter: { lang: 'zh' } } } };
    transform(t, file);
    expect(t.children[0].children[0].url).toBe('https://example.com/foo');
    expect(t.children[0].children[0].type).toBe('link');
  });
});

// web/remark-md-link-rewrite.mjs
import { visit, SKIP } from 'unist-util-visit';

// Top-level guide-collection slugs (post 6.0 rename). Maps source filename
// stem (UPPER_SNAKE) → web slug (lowercase-hyphenated).
const SLUG_MAP = new Map([
  ['README', 'readme'],
  ['USER_GUIDE', 'user-guide'],
  ['GLOSSARY', 'glossary'],
  ['PLATFORM_COMPARISON', 'platform-comparison'],
  ['KNOWN_LIMITATIONS', 'known-limitations'],
  ['DEMO_QUESTIONS', 'demo-questions'],
  ['CHANGELOG', 'changelog'],
]);

// Strict shape: optional ./ prefix + UPPER_SNAKE name + optional .lang suffix
// + .md + optional #hash. Anything with a / inside the path component (e.g.
// self_deploy/X.md) or .. parent-crawl is out-of-collection.
const SHAPE = /^(?:\.\/)?([A-Z_]+)(?:\.(zh|en|ja))?\.md(#.*)?$/;

export default function remarkMdLinkRewrite() {
  return (tree, file) => {
    const lang = file?.data?.astro?.frontmatter?.lang;

    visit(tree, 'link', (node, index, parent) => {
      const url = node.url;
      if (!url || !/\.md(?:#|$)/.test(url)) return;

      const m = url.match(SHAPE);
      const knownSlug = m && SLUG_MAP.get(m[1]);

      if (!knownSlug) {
        // Out-of-collection (self_deploy/, ../../, unknown stem). Drop the
        // <a> wrapper, keep the inline text children in place.
        if (parent && typeof index === 'number') {
          parent.children.splice(index, 1, ...node.children);
          return [SKIP, index];
        }
        return;
      }

      if (!lang) {
        throw new Error(
          `remark-md-link-rewrite: entry without frontmatter.lang has .md cross-ref to ${url}. ` +
          `Lang-neutral entries cannot rewrite per-lang. Either add lang: to the entry frontmatter ` +
          `or remove the cross-ref.`
        );
      }

      const hash = m[3] || '';
      // CHANGELOG has a dedicated /[lang]/changelog route (D-P5-1); everything
      // else lives under /[lang]/guide/.
      node.url = knownSlug === 'changelog'
        ? `/${lang}/changelog${hash}`
        : `/${lang}/guide/${knownSlug}${hash}`;
    });
  };
}

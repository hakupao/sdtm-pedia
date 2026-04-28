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
      if (!url) return;
      // Skip absolute URLs (http:, https:, mailto:, tel:, etc.), anchor-only,
      // and absolute paths. Process every remaining (relative) ref so
      // out-of-collection ones — including non-.md directory refs like
      // ./self_deploy/ — get their <a> wrapper dropped, not just .md
      // cross-refs.
      if (/^(?:[a-z][a-z0-9+.-]*:|#|\/)/i.test(url)) return;

      const m = url.match(SHAPE);
      const knownSlug = m && SLUG_MAP.get(m[1]);

      if (!knownSlug) {
        // Out-of-collection (self_deploy/, ./self_deploy/X.md, ../../X.md,
        // unknown stem). Drop the <a> wrapper, keep the inline text children
        // in place.
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

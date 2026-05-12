import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
import path from 'node:path';

const RELEASE_DIR = path.resolve('../release/v1.0');

const guide = defineCollection({
  loader: glob({
    // Only top-level docs (README/USER_GUIDE/GLOSSARY/PLATFORM_COMPARISON/
    // KNOWN_LIMITATIONS/DEMO_QUESTIONS/CHANGELOG). Excludes self_deploy/**
    // tutorial markdown which lacks the slug frontmatter contract.
    pattern: '*.md',
    base: RELEASE_DIR,
    // Multiple files share the same `slug` frontmatter (e.g. compare.zh/en/ja).
    // Default generateId keys off `data.slug` and would collide. Compose a
    // unique id from `${lang}-${slug}` for langed entries, leaving lang-neutral
    // entries (DEMO_QUESTIONS) as bare `${slug}`.
    generateId: ({ data }) => {
      const slug = data.slug as string | undefined;
      const lang = data.lang as string | undefined;
      if (!slug) throw new Error('guide collection: missing slug frontmatter');
      return lang ? `${lang}-${slug}` : slug;
    },
  }),
  schema: z.object({
    lang: z.enum(['zh', 'en', 'ja']).optional(),
    // slug is required: it composes the unique id (with lang) and is the URL
    // segment for every guide route. Schema validation gives a clearer error
    // than the generateId throw if any future doc is added without it.
    slug: z.string(),
    order: z.number().optional(),
    title: z.string().optional(),
  }),
});

// Per-platform deployment tutorials, sourced from
// release/v1.0/self_deploy/<platform>/tutorial.<lang>.md. These markdown files
// ship verbatim inside the user-facing release zip and intentionally carry no
// frontmatter — platform/lang are derived from the file path instead.
const deploy = defineCollection({
  loader: glob({
    pattern: '{chatgpt,claude,gemini,notebooklm}/tutorial.{zh,en,ja}.md',
    base: path.join(RELEASE_DIR, 'self_deploy'),
    // Compose id as `${lang}-${platform}` so the page route can look up an
    // entry by composing the same key from URL params.
    generateId: ({ entry }) => {
      const m = entry.match(/^(chatgpt|claude|gemini|notebooklm)\/tutorial\.(zh|en|ja)\.md$/);
      if (!m) throw new Error(`deploy collection: unexpected entry path "${entry}"`);
      return `${m[2]}-${m[1]}`;
    },
  }),
  // Tutorials have no frontmatter; passthrough keeps the validator happy.
  schema: z.object({}).passthrough(),
});

export const collections = { guide, deploy };

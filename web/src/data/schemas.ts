// web/src/data/schemas.ts
//
// Phase 9 / C-P6-7 — runtime validation schemas for the JSON data files
// consumed by Astro components (downloads.json, compare-dimensions.json).
// Used by `web/src/data/schemas.test.ts` as a regression guard against silent
// data drift (e.g. a future bump to v1.1 that forgets to update the tag
// regex, or a new compare dimension missing one of the 3 langs).
//
// Existing consumers (DownloadsSection.astro, ComparePreviewSection.astro,
// [lang]/compare.astro) keep importing the JSON directly — this file is
// purely a parallel validator. Migration to schema.parse() at import sites
// is left as a deliberate v1.1+ move when the JSON drift surface widens.
import { z } from 'zod';

export const DownloadsSchema = z.object({
  tag: z.string().regex(/^v\d+\.\d+(\.\d+)?$/, 'tag must be vX.Y or vX.Y.Z'),
  bundles: z.array(z.object({
    platform: z.enum(['claude', 'chatgpt', 'gemini', 'notebooklm']),
    filename: z.string().regex(/_bundle_v\d+\.\d+(\.\d+)?\.zip$/, 'filename must end with _bundle_vX.Y(.Z).zip'),
    files: z.number().int().nonnegative(),
    sizeMB: z.number().nonnegative(),
  })).length(4, 'must contain exactly 4 platform bundles'),
});

// 9.14 / F-4 fix: tighten values keys to the same platform enum DownloadsSchema
// uses. Catches typos like "cladue" that would otherwise render a blank cell.
const platformKeys = z.enum(['claude', 'chatgpt', 'gemini', 'notebooklm']);
const localizedString = z.object({
  zh: z.string().min(1),
  en: z.string().min(1),
  ja: z.string().min(1),
});

export const DimensionsSchema = z.array(z.object({
  key: z.string().regex(/^[a-z][a-z0-9-]*$/, 'key must be lowercase-hyphenated'),
  label: localizedString,
  values: z.record(platformKeys, localizedString),
  winners: z.array(z.string()),
}));

export type Downloads = z.infer<typeof DownloadsSchema>;
export type Dimensions = z.infer<typeof DimensionsSchema>;

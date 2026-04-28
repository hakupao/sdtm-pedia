// web/src/data/schemas.test.ts
//
// Phase 9 / C-P6-7 — regression guard that the canonical JSON data files
// validate against the published schemas. If a schema change lands without
// the JSON being updated (or vice versa), this test fails loud at CI time
// rather than silently rendering broken data on the live site.
import { describe, it, expect } from 'vitest';
import downloadsRaw from './downloads.json';
import dimsRaw from './compare-dimensions.json';
import { DownloadsSchema, DimensionsSchema } from './schemas';

describe('data schemas', () => {
  it('downloads.json parses', () => {
    expect(() => DownloadsSchema.parse(downloadsRaw)).not.toThrow();
  });

  it('downloads.json has exactly 4 bundles (one per supported platform)', () => {
    const d = DownloadsSchema.parse(downloadsRaw);
    expect(d.bundles.length).toBe(4);
    const platforms = d.bundles.map((b) => b.platform).sort();
    expect(platforms).toEqual(['chatgpt', 'claude', 'gemini', 'notebooklm']);
  });

  it('compare-dimensions.json parses', () => {
    expect(() => DimensionsSchema.parse(dimsRaw)).not.toThrow();
  });

  it('compare-dimensions.json: every dimension has all 3 lang labels', () => {
    const dims = DimensionsSchema.parse(dimsRaw);
    expect(dims.length).toBeGreaterThan(0);
    for (const d of dims) {
      expect(d.label.zh).toBeTruthy();
      expect(d.label.en).toBeTruthy();
      expect(d.label.ja).toBeTruthy();
    }
  });
});

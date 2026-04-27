import { describe, it, expect } from 'vitest';
import { buildReleaseAssetURL, REPO } from './downloads';

describe('downloads', () => {
  it('REPO matches actual repo', () => {
    expect(REPO).toBe('hakupao/sdtm-pedia');
  });
  it('buildReleaseAssetURL builds canonical GH URL', () => {
    expect(buildReleaseAssetURL('v1.0', 'claude_bundle_v1.0.zip'))
      .toBe('https://github.com/hakupao/sdtm-pedia/releases/download/v1.0/claude_bundle_v1.0.zip');
  });
});

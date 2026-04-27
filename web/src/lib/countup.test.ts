import { describe, it, expect } from 'vitest';
import { easeOutQuad, frameValue } from './countup';

describe('easeOutQuad', () => {
  it('0 → 0', () => expect(easeOutQuad(0)).toBe(0));
  it('1 → 1', () => expect(easeOutQuad(1)).toBe(1));
  it('0.5 → 0.75', () => expect(easeOutQuad(0.5)).toBe(0.75));
});

describe('frameValue', () => {
  it('elapsed >= duration returns end', () => {
    expect(frameValue(0, 17, 1000, 600)).toBe(17);
  });
  it('elapsed 0 returns start', () => {
    expect(frameValue(0, 17, 0, 600)).toBe(0);
  });
  it('mid duration eases', () => {
    expect(frameValue(0, 17, 300, 600)).toBeCloseTo(12.75, 2);
  });
});

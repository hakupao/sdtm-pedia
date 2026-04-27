export function easeOutQuad(t: number): number { return t * (2 - t); }

export function frameValue(start: number, end: number, elapsed: number, duration: number): number {
  if (elapsed >= duration) return end;
  const t = elapsed / duration;
  return start + (end - start) * easeOutQuad(t);
}

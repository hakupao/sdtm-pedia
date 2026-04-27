import { useEffect, useRef, useState } from 'react';
import { frameValue } from '../../lib/countup';

interface Props { end: number; duration?: number; decimals?: number; }

export function CountUp({ end, duration = 600, decimals = 0 }: Props) {
  const [value, setValue] = useState(0);
  const ref = useRef<HTMLSpanElement>(null);

  useEffect(() => {
    if (typeof window === 'undefined') return;
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) {
      setValue(end);
      return;
    }
    const node = ref.current;
    if (!node) return;
    const observer = new IntersectionObserver((entries) => {
      if (!entries[0].isIntersecting) return;
      observer.disconnect();
      const startTime = performance.now();
      let raf = 0;
      const tick = (t: number) => {
        const elapsed = t - startTime;
        setValue(frameValue(0, end, elapsed, duration));
        if (elapsed < duration) raf = requestAnimationFrame(tick);
      };
      raf = requestAnimationFrame(tick);
      return () => cancelAnimationFrame(raf);
    });
    observer.observe(node);
    return () => observer.disconnect();
  }, [end, duration]);

  return <span ref={ref}>{value.toFixed(decimals)}</span>;
}

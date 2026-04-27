// Fix for Node 25+ where native localStorage stub lacks .clear()/.getItem()/.setItem().
// vitest's populateGlobal skips localStorage when it already exists in the global
// (Node 25 injects a broken stub). Replace it with a spec-compliant in-memory impl.

class InMemoryStorage implements Storage {
  private store: Record<string, string> = {};

  get length(): number {
    return Object.keys(this.store).length;
  }

  clear(): void {
    this.store = {};
  }

  getItem(key: string): string | null {
    return Object.prototype.hasOwnProperty.call(this.store, key)
      ? this.store[key]
      : null;
  }

  setItem(key: string, value: string): void {
    this.store[key] = String(value);
  }

  removeItem(key: string): void {
    delete this.store[key];
  }

  key(index: number): string | null {
    return Object.keys(this.store)[index] ?? null;
  }
}

if (typeof globalThis.localStorage === 'undefined' || typeof globalThis.localStorage.clear !== 'function') {
  Object.defineProperty(globalThis, 'localStorage', {
    value: new InMemoryStorage(),
    writable: true,
    configurable: true,
  });
}

if (typeof globalThis.sessionStorage === 'undefined' || typeof globalThis.sessionStorage.clear !== 'function') {
  Object.defineProperty(globalThis, 'sessionStorage', {
    value: new InMemoryStorage(),
    writable: true,
    configurable: true,
  });
}

// jsdom does not implement matchMedia; provide a stub so vi.spyOn can wrap it.
if (typeof globalThis.matchMedia !== 'function') {
  Object.defineProperty(globalThis, 'matchMedia', {
    writable: true,
    configurable: true,
    value: (_query: string): MediaQueryList => ({
      matches: false,
      media: _query,
      onchange: null,
      addListener: () => {},
      removeListener: () => {},
      addEventListener: () => {},
      removeEventListener: () => {},
      dispatchEvent: () => false,
    }),
  });
}

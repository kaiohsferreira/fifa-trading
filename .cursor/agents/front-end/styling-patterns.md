---
description: Padrões de estilização no IFinc (SCSS Modules, Tailwind, Tema)
globs: "**/*.{scss,tsx,css}"
alwaysApply: false
---

# Padrões de Estilização

## SCSS Modules

Cada componente usa seu próprio módulo SCSS:

```tsx
// ComponentName.tsx
import styles from "./ComponentName.module.scss";

export function ComponentName() {
  return <div className={styles.container}>...</div>;
}
```

```scss
// ComponentName.module.scss
.container {
  padding: 16px;
  border-radius: 8px;
}
```

## Tema Dark/Light

```tsx
import { useTheme } from "~/hooks/useTheme";

function MyComponent() {
  const { theme } = useTheme(); // "dark" | "light"
  return <div className={theme === "dark" ? styles.dark : styles.light}>...</div>;
}
```

## Tailwind CSS

Usar para utilitários rápidos, não para estilização principal do componente:

```tsx
<div className="flex items-center gap-4 p-2">
  <span className="text-sm text-gray-500">Texto</span>
</div>
```

## Responsividade

```tsx
import { useWindowDimensions } from "~/context/global/useWindowDimensions";

function MyComponent() {
  const { isDesktop, isMobile, screenWidth } = useWindowDimensions();

  return isDesktop ? <DesktopView /> : <MobileView />;
}
```

Breakpoints comuns: `480px`, `768px`, `920px`, `1024px`, `1440px`

## Cores do Projeto

- Primária: `#204887` (azul escuro)
- Secundária: `#62B9B7` (verde-azulado)
- Scrollbar customizada com essas cores

## Font

- **DM Sans** (Google Fonts) — configurada globalmente em `globals.css` e `tailwind.config.js`

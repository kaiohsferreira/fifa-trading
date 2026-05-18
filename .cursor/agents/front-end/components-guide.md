---
description: Guia de uso dos componentes UI e Structure do IFinc
globs: src/components/**/*.tsx
alwaysApply: false
---

# Guia de Componentes

## Componentes de Estrutura (structure/)

| Componente | Quando Usar |
|---|---|
| `ListPageStructure` | Qualquer listagem com tabela (com ou sem abas) |
| `GenericCrudPage` | CRUD simples com formulário modal dinâmico |
| `FormPageStructure` | Página de formulário com build/prepare/submit |
| `TableCollapsedTree` | Tabela com linhas expansíveis e abas externas/internas |
| `KanbanBoard` | Visualização Kanban com drag-and-drop |
| `WorkingHoursListPage` | Lista com filtros de data no header |
| `PrivatePageStructure` | Wrapper de página autenticada (título, padding) |
| `ProfileEntitySidebar` | Sidebar de perfil de entidade |
| `CardStructure*` | Cards de telefone, email, endereço, conta bancária |

## Componentes de UI (ui/)

| Componente | Props Principais |
|---|---|
| `Button` | `text`, `icon`, `color`, `onClick`, `loading`, `disabled`, `href` |
| `Modal` | `title`, `maxWidth`, `openButton`, `openExternal`, `onClose`, `children(closeModal)` |
| `Grid` | `container`, `xs/sm/md/lg/xl` (colunas), `spacing` |
| `Flexbox` | `flexDirection`, `align`, `justify`, `spacing`, `wrap` |
| `Typography` | `component` (h1-h8, p, span), `color`, `align` |
| `Card` | `padding`, `backgroundColor`, `removeBoxShadow` |
| `Tabs` | `tabsData`, `active`, `setActive`, `styleType` ("1"-"5") |
| `Icon` | `type` (IconTypes/HeroIconTypes), `size`, `src` |
| `Label` | `text`, `required`, `loading`, `labelFor` |
| `PopupLoading` | `visible` — loading fullscreen |

## FormInputs (integrados com react-hook-form)

| Componente | Props Essenciais |
|---|---|
| `TextInputForm` | `name`, `label`, `required`, `disabled`, `onValueChange` |
| `SelectForm` | `name`, `label`, `options`, `listenId`, `listenGet`, `isSearchable` |
| `DateInputForm` | `name`, `label`, `type` ("date"/"datetime-local"), `required` |
| `CheckboxForm` | `name`, `label` |
| `FileInputForm` | `name`, `label` |
| `TextAreaForm` | `name`, `label` |
| `InputMaskForm` | `name`, `label`, `mask` |
| `RadioGroupForm` | `name`, `label`, `options` |

## SelectForm com Opções Dinâmicas

```tsx
// Opções carregadas quando o campo "categoria" muda
<SelectForm
  name="subcategoria"
  label="Subcategoria"
  listenId="categoria"
  listenGet={API_SUBCATEGORY.GETBYCAT}
  required
/>
```

## Espaçamento (SpacingPatternType)

Valores: `"pp"` (4px), `"p"` (8px), `"m"` (16px), `"g"` (24px), `"xg"` (32px), `"xxg"` (48px)

Usado em: `Grid spacing`, `Flexbox spacing`, `Card padding`, `Button padding`, `Typography margin`

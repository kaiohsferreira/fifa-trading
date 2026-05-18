---
description: Padrões de chamadas de API, serviços e tratamento de erros no IFinc
globs: "**/*.{ts,tsx}"
alwaysApply: false
---

# Padrões de API e Serviços

## Fazendo Requisições

```tsx
import { GetRequest, PostRequest } from "~/utils/Requests/Requests";
import Toast from "~/utils/Toast/Toast";
import { CONSTANTS_MESSAGES_APIERROR } from "~/config/messages";

// GET
const response = await GetRequest<MeuTipo[]>(API_ENTIDADE.GETALL());
if (response.success) {
  setData(response.object);
} else {
  Toast.error(response.message || CONSTANTS_MESSAGES_APIERROR);
}

// POST
const response = await PostRequest<void>(API_ENTIDADE.SAVE(), payload);
if (!response.success) {
  Toast.error(response.message || CONSTANTS_MESSAGES_APIERROR);
}
```

## Rotas de API

Definidas em `src/config/apiRoutes/` como objetos com funções:

```typescript
export const API_ENTIDADE = {
  GETALL: () => "entidade/getall",
  SAVE: () => "entidade/save",
  PREPARE: (token: string) => `entidade/prepare/${token}`,
  DELETE: (id: number) => `entidade/delete/${id}`,
  BUILD: () => "entidade/build",
};
```

## Validação Antes de Enviar

```tsx
// ❌ ERRADO: enviar sem validar
await PostRequest(API_LEAD.SAVE(), { nome, cpf });

// ✅ CORRETO: validar primeiro
if (!nome?.trim()) {
  Toast.error("Por favor, preencha o nome.");
  return;
}
if (!cpf?.trim()) {
  Toast.error("Por favor, preencha o CPF.");
  return;
}
await PostRequest(API_LEAD.SAVE(), { nome, cpf });
```

## Tratamento de Erros do Backend

```tsx
// ❌ ERRADO: exibir mensagem crua do backend
Toast.error(response.message); // pode ser "JSON parse error"

// ✅ CORRETO: mensagem amigável
const isGenericError = response.message?.includes("JSON") ||
                       response.message?.includes(".error") ||
                       !response.message;
Toast.error(isGenericError ? CONSTANTS_MESSAGES_APIERROR : response.message);
```

## Serviços Disponíveis

- `list.service` → `getList()`, `getListPost()`, `itemDelete()` (usado pelo DataTableRender)
- `form.service` → `build()`, `prepare()`, `submit()`, `getSelectOptions()` (usado pelo FormPageStructure)
- `auth.service` → `signIn()` (autenticação)
- `export.service` → `exportListPDFExcel()` (exportação)
- `chart.service` → `getChart()`, `getList()` (gráficos)

## Autenticação

- Token em cookies via `nookies`
- `GetAuthToken(ctx?)` — obtém token
- Auto-refresh em 401 via `RefreshToken()`
- `privateroute()` HOC protege páginas

---
description: Padrões de criação de páginas Next.js no IFinc (listas, formulários, CRUD)
globs: src/pages/**/*.tsx
alwaysApply: false
---

# Padrões de Páginas

## Página de Lista

```tsx
import { privateroute } from "~/routes/private.route";
import PrivatePageStructure from "~/components/structure/PrivatePageStructure/PrivatePageStructure";
import ListPageStructure from "~/components/structure/ListPageStructure";
import { API_ENTITY } from "~/config/apiRoutes/entity";

function EntityListPage() {
  return (
    <PrivatePageStructure title="Entidades" noPadding>
      <ListPageStructure
        getListPath={API_ENTITY.GETALL()}
        createPath="/adm/entidade/adicionar"
        editPath="/adm/entidade/editar"
        removeAPIPath={API_ENTITY.DELETE}
        details={true}
        customizedBodyColumns={<EntityCustomizedBodyColumns />}
      />
    </PrivatePageStructure>
  );
}
export default privateroute(EntityListPage);
```

## Página de Formulário (Criar)

```tsx
function EntityAddPage() {
  return (
    <PrivatePageStructure title="Nova Entidade">
      <FormPageStructure
        buildPath={API_ENTITY.BUILD()}
        submitPath={API_ENTITY.SAVE()}
        buttonSubmitText="Salvar"
        returnPath="/adm/entidade/lista"
      />
    </PrivatePageStructure>
  );
}
export default privateroute(EntityAddPage);
```

## Página de Edição (Rota Dinâmica `[token].tsx`)

```tsx
function EntityEditPage() {
  const { token } = useRouter().query;
  return (
    <PrivatePageStructure title="Editar Entidade">
      <FormPageStructure
        buildPath={API_ENTITY.BUILD()}
        submitPath={API_ENTITY.SAVE()}
        preparePath={API_ENTITY.PREPARE(token as string)}
        buttonSubmitText="Salvar"
        returnPath="/adm/entidade/lista"
      />
    </PrivatePageStructure>
  );
}
export default privateroute(EntityEditPage);
```

## Checklist de Nova Página

- [ ] Envolver com `PrivatePageStructure` (ou `LoginPageStructure` para login)
- [ ] Exportar com `privateroute()` HOC (ou `loginroute`/`comumroute`)
- [ ] Definir `title` na PrivatePageStructure
- [ ] Para listas: usar `ListPageStructure` com rotas de API corretas
- [ ] Para formulários: usar `FormPageStructure` com `buildPath`, `submitPath`
- [ ] Criar `CustomizedBodyColumns` se precisar de colunas customizadas

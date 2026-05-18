---
description: Padrões de formulários e validação no IFinc
globs: "**/*.tsx"
alwaysApply: false
---

# Formulários e Validação

## Estrutura de Formulário com FormPageStructure

O `FormPageStructure` gerencia o ciclo completo: build → prepare (edição) → submit.

```tsx
<FormPageStructure
  buildPath={API_ENTITY.BUILD()}        // Monta campos do formulário
  submitPath={API_ENTITY.SAVE()}        // Endpoint de envio
  preparePath={API_ENTITY.PREPARE(id)}  // Carrega dados (edição)
  buttonSubmitText="Salvar"
  returnPath="/adm/entidade/lista"
  onSuccess={(event, handleClose) => { Toast.success("Salvo!"); }}
  onFailure={(response) => { Toast.error(response.message); }}
/>
```

## Formulário Manual (sem FormPageStructure)

```tsx
import Toast from "~/utils/Toast/Toast";
import { PostRequest } from "~/utils/Requests/Requests";

interface FormData {
  nome: string;
  email: string;
  tipo: number;
}

function MyForm() {
  const [formData, setFormData] = useState<FormData>({ nome: "", email: "", tipo: 0 });
  const [loading, setLoading] = useState(false);

  async function handleSubmit() {
    // 1. Validar campos obrigatórios
    if (!formData.nome.trim()) {
      Toast.error("Por favor, preencha o nome.");
      return;
    }
    if (!formData.email.trim()) {
      Toast.error("Por favor, preencha o e-mail.");
      return;
    }

    // 2. Chamar API
    setLoading(true);
    const response = await PostRequest(API_ENTITY.SAVE(), formData);
    setLoading(false);

    // 3. Tratar resposta
    if (response.success) {
      Toast.success("Salvo com sucesso!");
    } else {
      Toast.error(response.message || CONSTANTS_MESSAGES_APIERROR);
    }
  }

  return (
    <Grid container spacing="m">
      <Grid xs={12} md={6}>
        <Label text="Nome" required />
        <TextInput value={formData.nome} onChange={(e) => setFormData({...formData, nome: e.target.value})} required />
      </Grid>
      <Grid xs={12} md={6}>
        <Label text="E-mail" required />
        <TextInput value={formData.email} onChange={(e) => setFormData({...formData, email: e.target.value})} required />
      </Grid>
      <Grid xs={12}>
        <Button text="Salvar" onClick={handleSubmit} loading={loading} />
      </Grid>
    </Grid>
  );
}
```

## Validação com Yup (FormValidation)

```typescript
import { formValidation } from "~/utils/FormValidation/FormValidation";

// O FormPageStructure usa internamente; para uso manual:
const isValid = await formValidation(schema, data);
```

## Padrão de Campos Required

```tsx
// ✅ CORRETO: required no Label E no Input
<Label text="Nome" required={true} />
<TextInput required={true} value={nome} onChange={handleChange} />

// ✅ Com FormInputs (integrado)
<TextInputForm name="nome" label="Nome" required />
<SelectForm name="tipo" label="Tipo" options={options} required />
```

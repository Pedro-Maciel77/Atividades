# Como adicionar conteúdo novo

Siga estes passos para qualquer atividade nova (de UC ou do PI). Assim o repositório continua organizado e os índices se atualizam sozinhos.

## 1. Escolha onde o arquivo vai ficar

| É... | Pasta |
|------|-------|
| Atividade individual de uma UC | `ucs/<nome-da-uc>/` |
| Documento do Projeto Integrador | `pi-altura/<fase>/` |

UC nova? Crie `ucs/<nome-da-uc>/README.md` a partir de [templates/readme-nova-uc.md](templates/readme-nova-uc.md), acrescente a UC em [taxonomia.yml](taxonomia.yml) e na tabela de [ucs/README.md](ucs/README.md).

## 2. Crie o arquivo a partir do modelo

Copie [templates/documento.md](templates/documento.md) e dê um nome no padrão `NN-slug.md`:

- `NN` é o próximo número da pasta (01, 02, 03...).
- `slug` é um nome curto, em minúsculas, sem acento e com hífens.
- Exemplo: `ucs/gestao-da-informacao/01-api-de-tarefas.md`

Se tiver o arquivo original (PDF, imagem), coloque na mesma pasta com o mesmo nome: `01-api-de-tarefas.pdf`.

## 3. Preencha o cabeçalho (front matter)

Use **somente** termos de [taxonomia.yml](taxonomia.yml). Veja os campos em [docs/metadados.md](docs/metadados.md).

Precisa de um termo que não existe? Acrescente em `taxonomia.yml` primeiro, com uma definição curta.

## 4. Escreva o documento

Mantenha as seções do modelo: Resumo, Conteúdo e Relações. Para trabalhos de grupo, escreva `escopo: grupo` e identifique o grupo como autoria.

## 5. Ajuste a navegação

- No fim do novo documento, preencha `← Anterior | ↑ Índice | Próximo →`.
- No documento anterior, troque o link "Próximo" para apontar para o novo.
- Acrescente o documento na tabela do README da UC ou de [pi-altura/README.md](pi-altura/README.md).
- Acrescente o documento em [SUMARIO.md](SUMARIO.md).

## 6. Ligue com outros documentos (se houver relação)

Acrescente o `id` do outro documento em `relacionados` nos dois lados e crie um item na seção "Relações". Para o mapa visual, veja [docs/relacoes.md](docs/relacoes.md).

## 7. Atualize os índices e valide

```bash
python scripts/atualizar.py
```

O script regenera `INDEX.md`, `catalogo.yml` e `docs/taxonomia.md`, e mostra erros como termos fora da taxonomia, links quebrados e relações sem volta.

## 8. Envie para o GitHub

```bash
git add .
git commit -m "Adiciona <nome da atividade>"
git push
```

## Cuidados

- Não suba dados pessoais de entrevistados (nomes, e-mails, telefones, gravações).
- Não escreva resultados, notas ou datas que você não tenha. Use `[PREENCHER]` e complete depois.

---

[← Voltar ao README](README.md) | [Sumário geral](SUMARIO.md) | [Glossário](GLOSSARIO.md)

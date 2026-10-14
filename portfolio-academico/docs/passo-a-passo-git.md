---
id: doc-passo-a-passo-git
titulo: "Passo a passo: criar o repositório no GitHub com git"
descricao: "Comandos para criar o repositório, subir os arquivos e configurar descrição e topics no GitHub."
tipo: documentacao
fase_pi: nenhuma
ucs: []
escopo: individual
autores: [pedro-henrique-maciel]
data: 2026-10-13
status: em-andamento
tags: [git, github]
relacionados: [doc-encontrabilidade]
---

# Passo a passo: criar o repositório no GitHub com git

Rode os comandos no terminal, **dentro da pasta `portfolio-academico`**.

## 0. Antes de começar

- Tenha o `git` instalado (`git --version`) e uma conta no GitHub (usuário `Pedro-Maciel77`).
- Opcional, mas facilita: o [GitHub CLI](https://cli.github.com/) (`gh --version`).
- Para rodar o script de índices: Python 3 e `pip install pyyaml`.
- Complete os `[PREENCHER]` que conseguir (veja [pendências](pendencias.md)).
- **Cuidado com dados pessoais:** não suba nomes, e-mails, telefones ou gravações de entrevistados. O Altura pretende seguir a LGPD, e o portfólio também deve.
- **Combine com o grupo** antes de deixar documentos do PI em um repositório público.

## 1. Configurar o git (só na primeira vez)

```bash
git config --global user.name "Pedro Henrique Maciel"
git config --global user.email "seu-email@exemplo.com"
```

## 2. Gerar os índices e validar

```bash
pip install pyyaml
python scripts/atualizar.py
```

O script deve terminar com "Tudo certo". Os `[PREENCHER]` restantes aparecem na lista, mas não impedem o envio.

## 3. Criar o repositório local e o primeiro commit

```bash
git init -b main
git add .
git commit -m "Cria estrutura do portfólio acadêmico"
```

Se o seu git for antigo e `-b main` der erro: `git init` e depois `git branch -M main`.

## 4. Criar o repositório no GitHub e enviar

### Opção A: com o GitHub CLI (um comando só)

```bash
gh auth login
gh repo create Pedro-Maciel77/portfolio-academico --public \
  --description "Portfólio acadêmico de Pedro Henrique Maciel (ADS, Senac): atividades das UCs e do Projeto Integrador Altura, organizadas com Arquitetura da Informação." \
  --source=. --remote=origin --push
```

Troque `--public` por `--private` se preferir deixar privado por enquanto.

### Opção B: pelo site

1. Em github.com, clique em **New repository**.
2. Nome: `portfolio-academico`. **Não** marque README, .gitignore nem licença (já existem aqui).
3. Clique em **Create repository** e rode:

```bash
git remote add origin https://github.com/Pedro-Maciel77/portfolio-academico.git
git push -u origin main
```

## 5. Configurar descrição e topics

### Com o GitHub CLI

```bash
gh repo edit Pedro-Maciel77/portfolio-academico \
  --description "Portfólio acadêmico de Pedro Henrique Maciel (ADS, Senac): atividades das UCs e do Projeto Integrador Altura, organizadas com Arquitetura da Informação." \
  --add-topic portfolio,portfolio-academico,senac,projeto-integrador,analise-e-desenvolvimento-de-sistemas,arquitetura-da-informacao,startups,investidores,matchmaking,react,typescript
```

### Pelo site

1. Na página do repositório, clique na engrenagem ao lado de **About**.
2. Cole a descrição no campo **Description**.
3. Em **Topics**, digite cada topic e pressione Enter.
4. Clique em **Save changes**.

## 6. Dia a dia: adicionar uma atividade nova

```bash
# 1. crie o arquivo seguindo o CONTRIBUINDO.md
python scripts/atualizar.py
git add .
git commit -m "Adiciona atividade 01 da UC FullStack"
git push
```

## 7. Opcional: renomear o repositório NEXO para Altura

O código do MVP ainda está em `github.com/Pedro-Maciel77/nexo`. Se o grupo renomear o repositório (Settings → General → Repository name), o GitHub redireciona o endereço antigo, mas vale atualizar os links:

1. Troque `nexo` pelo novo nome em [10-codigo-do-mvp.md](../pi-altura/04-mvp/10-codigo-do-mvp.md) (campo `arquivo_original` e texto) e em [pi-altura/README.md](../pi-altura/README.md).
2. Rode `python scripts/atualizar.py` e faça um novo commit.

---

[← Anterior: Relações](relacoes.md) | [↑ README](../README.md) | [Próximo: Pendências →](pendencias.md)

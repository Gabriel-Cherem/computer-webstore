# 🔄 Guia: Fazer Merge de Branch no Git

## ✅ Resumo Rápido dos Comandos

Execute esses comandos no PowerShell (um de cada vez):

### 1. Verificar status da branch atual
```powershell
git status
```

### 2. Fazer commit das mudanças (se houver)
```powershell
git add .
git commit -m "refactor: Separar templates home em index (base) e content"
```

### 3. Fazer push da branch atual para o GitHub
```powershell
git push origin refatorar-html
```

### 4. Trocar para a branch main
```powershell
git checkout main
```

### 5. Atualizar a branch main com as mudanças do GitHub (se necessário)
```powershell
git pull origin main
```

### 6. Fazer o merge da branch refatorar-html
```powershell
git merge refatorar-html
```

### 7. Enviar as mudanças para o GitHub
```powershell
git push origin main
```

### 8. (Opcional) Deletar a branch refatorar-html localmente
```powershell
git branch -d refatorar-html
```

### 9. (Opcional) Deletar a branch refatorar-html no GitHub
```powershell
git push origin --delete refatorar-html
```

---

## 📊 Visualizar o Histórico

Após o merge, você pode ver:

```powershell
# Ver todas as branches
git branch -a

# Ver histórico de commits
git log --oneline

# Ver o diagrama de branches
git log --graph --oneline --all
```

---

## 🆘 Se houver Conflito

Se o merge gerar conflitos:

1. **Abra os arquivos** que tem conflito (VS Code mostrará automaticamente)
2. **Resolva os conflitos** - escolha qual versão manter
3. **Faça o commit**:
   ```powershell
   git add .
   git commit -m "Resolver conflitos de merge"
   git push origin main
   ```

Se quiser **desfazer o merge**:
```powershell
git merge --abort
```

---

## ✨ Resultado Final

Sua branch `main` terá todas as mudanças da `refatorar-html`! 🎉

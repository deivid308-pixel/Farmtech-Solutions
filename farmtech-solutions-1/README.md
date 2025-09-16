# FarmTech Solutions — Agricultura Digital (Python + R)

## Como rodar
1. **Python**
   ```bash
   cd python
   python3 main.py
   ```
   Use o menu para cadastrar áreas e manejos; ao sair (opção 0) ou escolher a opção 9, os CSVs são exportados em `../dados/`.

2. **R (estatísticas)**
   ```bash
   cd R
   Rscript stats.R
   ```

3. **R (meteorologia - Ir além)**
   ```bash
   cd R
   Rscript meteo.R
   ```
   *Dica:* Se necessário, instale pacotes: `install.packages(c("httr","jsonlite"))`.

## Estrutura
```
farmtech-solutions/
├─ python/main.py
├─ R/stats.R
├─ R/meteo.R
├─ dados/
├─ docs/resumo_embrapa.txt
├─ ENTREGA/video_link.txt
└─ README.md
```

## Entrega
- Grave vídeo (≤ 5 min), marque como **Não listado** no YouTube e cole o link em `ENTREGA/video_link.txt`.
- Compacte tudo em um `.zip` e envie pela plataforma.

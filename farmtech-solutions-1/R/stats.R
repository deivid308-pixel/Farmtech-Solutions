# -*- coding: utf-8 -*-

areas_path  <- file.path("..", "dados", "areas.csv")
insumos_path <- file.path("..", "dados", "insumos.csv")

message("=== Estatísticas - Áreas ===")
if (file.exists(areas_path)) {
  areas <- read.csv(areas_path, sep = ";", header = TRUE, stringsAsFactors = FALSE)
  # converter para numérico (caso venha com vírgula)
  areas$area_m2 <- as.numeric(gsub(",", ".", areas$area_m2))
  culturas <- unique(areas$cultura)
  for (c in culturas) {
    sub <- areas[areas$cultura == c, ]
    if (nrow(sub) > 0) {
      m <- mean(sub$area_m2, na.rm = TRUE)
      s <- sd(sub$area_m2, na.rm = TRUE)
      cat(sprintf("Cultura: %-8s | n=%d | média=%.2f m² | desvio=%.2f m²\n",
                  c, nrow(sub), m, s))
    }
  }
} else {
  message("Arquivo de áreas não encontrado. Gere via Python (opção 9).")
}

message("\n=== Estatísticas - Insumos (total de litros) ===")
if (file.exists(insumos_path)) {
  ins <- read.csv(insumos_path, sep = ";", header = TRUE, stringsAsFactors = FALSE)
  ins$total_litros <- as.numeric(gsub(",", ".", ins$total_litros))
  # Por cultura
  culturas <- unique(ins$cultura)
  for (c in culturas) {
    sub <- ins[ins$cultura == c, ]
    if (nrow(sub) > 0) {
      m <- mean(sub$total_litros, na.rm = TRUE)
      s <- sd(sub$total_litros, na.rm = TRUE)
      cat(sprintf("Cultura: %-8s | n=%d | média=%.2f L | desvio=%.2f L\n",
                  c, nrow(sub), m, s))
    }
  }
  cat("\n-- Por produto --\n")
  prods <- unique(ins$produto)
  for (p in prods) {
    sub <- ins[ins$produto == p, ]
    if (nrow(sub) > 0) {
      m <- mean(sub$total_litros, na.rm = TRUE)
      s <- sd(sub$total_litros, na.rm = TRUE)
      cat(sprintf("Produto: %-12s | n=%d | média=%.2f L | desvio=%.2f L\n",
                  p, nrow(sub), m, s))
    }
  }
} else {
  message("Arquivo de insumos não encontrado. Gere via Python (opção 9).")
}

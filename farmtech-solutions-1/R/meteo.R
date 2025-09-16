# -*- coding: utf-8 -*-
# Requer: install.packages(c("httr","jsonlite"))
suppressWarnings({
  library(httr)
  library(jsonlite)
})

# Função para buscar previsão por coordenadas (ex.: São Paulo)
fetch_weather <- function(lat=-23.55, lon=-46.64,
                          hourly=c("temperature_2m","relativehumidity_2m","precipitation","windspeed_10m"),
                          timezone="America/Sao_Paulo") {

  base <- "https://api.open-meteo.com/v1/forecast"
  query <- list(
    latitude = lat,
    longitude = lon,
    hourly = paste(hourly, collapse=","),
    timezone = timezone
  )
  resp <- GET(base, query=query)
  stop_for_status(resp)
  fromJSON(content(resp, "text", encoding="UTF-8"), flatten=TRUE)
}

# Mostrar resumo textual das próximas horas
print_weather <- function(dat, horas=12) {
  cat("=== Tempo (Open-Meteo) ===\n")
  if (is.null(dat$hourly$time)) {
    cat("Sem dados horários.\n"); return(invisible())
  }
  n <- min(length(dat$hourly$time), horas)
  for (i in seq_len(n)) {
    t  <- dat$hourly$time[i]
    tt <- dat$hourly$temperature_2m[i]
    rh <- if (!is.null(dat$hourly$relativehumidity_2m)) dat$hourly$relativehumidity_2m[i] else NA
    pr <- if (!is.null(dat$hourly$precipitation)) dat$hourly$precipitation[i] else NA
    ws <- if (!is.null(dat$hourly$windspeed_10m)) dat$hourly$windspeed_10m[i] else NA
    cat(sprintf("%s | T=%.1f°C | UR=%.0f%% | Prec=%.2f mm | Vento=%.1f km/h\n",
                t, tt, rh, pr, ws))
  }
}

# Execução
dat <- fetch_weather()
print_weather(dat, horas=12)

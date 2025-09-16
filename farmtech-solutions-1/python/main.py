#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import csv
import os

# ===============================
# Estruturas de dados (vetores)
# ===============================
areas = []   # cada item: {id, cultura, forma, params, area_m2}
insumos = [] # cada item: {id, cultura, produto, dose_tipo, dose_valor, qtd_ruas, comp_m_por_rua, total_litros}

# id sequencial simples
_next_area_id = 1
_next_insumo_id = 1

# ===============================
# Funções de Cálculo
# ===============================
def calc_area_cafe_retangulo(comprimento_m, largura_m):
    # Área para café (retângulo)
    return float(comprimento_m) * float(largura_m)

def calc_area_laranja_circulo(raio_m):
    # Área para laranja (círculo)
    return math.pi * float(raio_m) ** 2

def calc_insumo_ml_por_m(dose_ml_por_m, qtd_ruas, comp_m_por_rua):
    total_metros = float(qtd_ruas) * float(comp_m_por_rua)
    total_litros = (float(dose_ml_por_m) * total_metros) / 1000.0
    return total_litros

# ===============================
# Funções de CRUD
# ===============================

def adicionar_area():
    global _next_area_id

    print("\n=== Adicionar Área Plantada ===")
    print("Culturas disponíveis: 1) Café (retângulo)  2) Laranja (círculo)")
    op = input("Escolha a cultura [1-2]: ").strip()

    if op == "1":
        cultura = "Cafe"
        forma = "retangulo"
        try:
            comp = float(input("Comprimento do talhão (m): "))
            larg = float(input("Largura do talhão (m): "))
            area_m2 = calc_area_cafe_retangulo(comp, larg)
            item = {
                "id": _next_area_id,
                "cultura": cultura,
                "forma": forma,
                "params": {"comprimento_m": comp, "largura_m": larg},
                "area_m2": area_m2
            }
            areas.append(item)
            print(f"[OK] Área cadastrada: ID {item['id']} | {cultura} | {area_m2:.2f} m²")
            _next_area_id += 1
        except ValueError:
            print("[ERRO] Valores inválidos.")
    elif op == "2":
        cultura = "Laranja"
        forma = "circulo"
        try:
            raio = float(input("Raio do talhão (m): "))
            area_m2 = calc_area_laranja_circulo(raio)
            item = {
                "id": _next_area_id,
                "cultura": cultura,
                "forma": forma,
                "params": {"raio_m": raio},
                "area_m2": area_m2
            }
            areas.append(item)
            print(f"[OK] Área cadastrada: ID {item['id']} | {cultura} | {area_m2:.2f} m²")
            _next_area_id += 1
        except ValueError:
            print("[ERRO] Valores inválidos.")
    else:
        print("[ERRO] Opção inválida.")

def listar_areas():
    print("\n=== Áreas Cadastradas ===")
    if not areas:
        print("(vazio)")
        return
    for a in areas:
        if a["forma"] == "retangulo":
            p = a["params"]
            extra = f"comp={p['comprimento_m']}m, larg={p['largura_m']}m"
        else:
            p = a["params"]
            extra = f"raio={p['raio_m']}m"
        print(f"ID {a['id']:>3} | {a['cultura']:<7} | {a['forma']:<9} | {extra:<30} | área={a['area_m2']:.2f} m²")

def atualizar_area():
    print("\n=== Atualizar Área ===")
    try:
        id_alvo = int(input("Informe o ID da área: "))
    except ValueError:
        print("[ERRO] ID inválido.")
        return

    alvo = next((x for x in areas if x["id"] == id_alvo), None)
    if not alvo:
        print("[ERRO] ID não encontrado.")
        return

    if alvo["cultura"] == "Cafe":
        try:
            comp = float(input("Novo comprimento (m): "))
            larg = float(input("Nova largura (m): "))
            alvo["params"]["comprimento_m"] = comp
            alvo["params"]["largura_m"] = larg
            alvo["area_m2"] = calc_area_cafe_retangulo(comp, larg)
            print("[OK] Área atualizada.")
        except ValueError:
            print("[ERRO] Valores inválidos.")
    elif alvo["cultura"] == "Laranja":
        try:
            raio = float(input("Novo raio (m): "))
            alvo["params"]["raio_m"] = raio
            alvo["area_m2"] = calc_area_laranja_circulo(raio)
            print("[OK] Área atualizada.")
        except ValueError:
            print("[ERRO] Valores inválidos.")

def deletar_area():
    print("\n=== Deletar Área ===")
    try:
        id_alvo = int(input("Informe o ID da área: "))
    except ValueError:
        print("[ERRO] ID inválido.")
        return

    idx = next((i for i,x in enumerate(areas) if x["id"] == id_alvo), None)
    if idx is None:
        print("[ERRO] ID não encontrado.")
        return

    removido = areas.pop(idx)
    print(f"[OK] Removido ID {removido['id']} ({removido['cultura']}).")

def adicionar_insumo():
    global _next_insumo_id

    print("\n=== Cálculo de Manejo de Insumos ===")
    print("Culturas disponíveis: 1) Café  2) Laranja")
    op = input("Escolha a cultura [1-2]: ").strip()
    cultura = "Cafe" if op == "1" else "Laranja" if op == "2" else None
    if cultura is None:
        print("[ERRO] Opção inválida.")
        return

    produto = input("Produto (ex.: Fosfato, Fungicida, etc.): ").strip()
    print("Tipo de dose: 1) mL/metro (por rua)")
    dose_tipo = "ml_m"
    try:
        dose_valor = float(input("Dose (mL por metro): "))
        qtd_ruas = int(input("Quantidade de ruas: "))
        comp_m_por_rua = float(input("Comprimento por rua (m): "))
        total_litros = calc_insumo_ml_por_m(dose_valor, qtd_ruas, comp_m_por_rua)
        item = {
            "id": _next_insumo_id,
            "cultura": cultura,
            "produto": produto,
            "dose_tipo": dose_tipo,
            "dose_valor": dose_valor,
            "qtd_ruas": qtd_ruas,
            "comp_m_por_rua": comp_m_por_rua,
            "total_litros": total_litros
        }
        insumos.append(item)
        print(f"[OK] Insumo cadastrado: ID {item['id']} | {cultura} | total={total_litros:.2f} L")
        _next_insumo_id += 1
    except ValueError:
        print("[ERRO] Valores inválidos.")

def listar_insumos():
    print("\n=== Manejos de Insumos ===")
    if not insumos:
        print("(vazio)")
        return
    for it in insumos:
        print(f"ID {it['id']:>3} | {it['cultura']:<7} | {it['produto']:<12} | dose={it['dose_valor']} mL/m | "
              f"ruas={it['qtd_ruas']} | comp={it['comp_m_por_rua']} m | total={it['total_litros']:.2f} L")

def atualizar_insumo():
    print("\n=== Atualizar Insumo ===")
    try:
        id_alvo = int(input("Informe o ID do insumo: "))
    except ValueError:
        print("[ERRO] ID inválido.")
        return

    alvo = next((x for x in insumos if x["id"] == id_alvo), None)
    if not alvo:
        print("[ERRO] ID não encontrado.")
        return

    try:
        novo_prod = input(f"Produto [{alvo['produto']}]: ").strip() or alvo["produto"]
        nova_dose = input(f"Dose mL/m [{alvo['dose_valor']}]: ").strip()
        nova_dose = float(nova_dose) if nova_dose else alvo["dose_valor"]
        novas_ruas = input(f"Qtd ruas [{alvo['qtd_ruas']}]: ").strip()
        novas_ruas = int(novas_ruas) if novas_ruas else alvo["qtd_ruas"]
        novo_comp = input(f"Comp por rua (m) [{alvo['comp_m_por_rua']}]: ").strip()
        novo_comp = float(novo_comp) if novo_comp else alvo["comp_m_por_rua"]

        alvo["produto"] = novo_prod
        alvo["dose_valor"] = nova_dose
        alvo["qtd_ruas"] = novas_ruas
        alvo["comp_m_por_rua"] = novo_comp
        alvo["total_litros"] = calc_insumo_ml_por_m(nova_dose, novas_ruas, novo_comp)

        print("[OK] Insumo atualizado.")
    except ValueError:
        print("[ERRO] Valores inválidos.")

def deletar_insumo():
    print("\n=== Deletar Insumo ===")
    try:
        id_alvo = int(input("Informe o ID do insumo: "))
    except ValueError:
        print("[ERRO] ID inválido.")
        return

    idx = next((i for i,x in enumerate(insumos) if x["id"] == id_alvo), None)
    if idx is None:
        print("[ERRO] ID não encontrado.")
        return

    removido = insumos.pop(idx)
    print(f"[OK] Removido ID {removido['id']} ({removido['produto']}).")

# ===============================
# Exportação para CSV (para o R)
# ===============================

def exportar_csvs():
    os.makedirs(os.path.join("..", "dados"), exist_ok=True)
    path_areas = os.path.join("..", "dados", "areas.csv")
    path_insumos = os.path.join("..", "dados", "insumos.csv")

    with open(path_areas, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["id", "cultura", "forma", "comprimento_m", "largura_m", "raio_m", "area_m2"])
        for a in areas:
            comp = a["params"].get("comprimento_m", "")
            larg = a["params"].get("largura_m", "")
            raio = a["params"].get("raio_m", "")
            w.writerow([a["id"], a["cultura"], a["forma"], comp, larg, raio, f"{a['area_m2']:.4f}"])

    with open(path_insumos, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["id", "cultura", "produto", "dose_tipo", "dose_valor_ml_m", "qtd_ruas", "comp_m_por_rua", "total_litros"])
        for it in insumos:
            w.writerow([
                it["id"], it["cultura"], it["produto"], it["dose_tipo"], it["dose_valor"],
                it["qtd_ruas"], it["comp_m_por_rua"], f"{it['total_litros']:.4f}"
            ])
    print(f"[OK] CSVs exportados para a pasta 'dados/'.")

# ===============================
# Menu
# ===============================

def menu():
    while True:
        print("\n================== FarmTech Solutions - Menu ==================")
        print("1) Entrada de dados - Áreas")
        print("2) Saída de dados - Áreas")
        print("3) Atualizar dados - Áreas")
        print("4) Deletar dados - Áreas")
        print("5) Entrada de dados - Manejo de Insumos")
        print("6) Saída de dados - Manejo de Insumos")
        print("7) Atualizar dados - Manejo de Insumos")
        print("8) Deletar dados - Manejo de Insumos")
        print("9) Exportar CSVs (para R)")
        print("0) Sair do programa")
        print("===============================================================")

        op = input("Escolha uma opção: ").strip()
        if op == "1":
            adicionar_area()
        elif op == "2":
            listar_areas()
        elif op == "3":
            atualizar_area()
        elif op == "4":
            deletar_area()
        elif op == "5":
            adicionar_insumo()
        elif op == "6":
            listar_insumos()
        elif op == "7":
            atualizar_insumo()
        elif op == "8":
            deletar_insumo()
        elif op == "9":
            exportar_csvs()
        elif op == "0":
            # Exportar automaticamente ao sair
            exportar_csvs()
            print("Saindo... Até logo!")
            break
        else:
            print("[ERRO] Opção inválida.")

if __name__ == "__main__":
    menu()

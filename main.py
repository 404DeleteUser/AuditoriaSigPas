from AuditoriaProcesso.consolidated import fluxo_auditoria
from AuditoriaProcesso.styles import styles


def main():
    print("Iniciando Auditoria de faltas")
    fluxo_auditoria()

    print("Estilizando Auditoria")
    styles()


if __name__ == "__main__":
    main()

def organograma():

    hierarquia = {
        "GABINETE DO SECRETARIO DE ESTADO DE EDUCACAO": {
            "COLEGIO DIRETIVO ESTRATEGICO": {},
            "COLEGIO DE AVALIACAO DAS ESTRATEGIAS": {},
            "COMITES SETORIAIS": {},
            "CONSELHO ESTADUAL DE ALIMENTACAO ESCOLAR": {},
            "CONSELHO ESTADUAL DE EDUCACAO INDIGENA": {},
            "NUCLEO DE GESTAO ESTRATEGICA PARA RESULTADOS": {},
            "UNIDADE DE COMUNICACAO DA EDUCACAO": {},
            "OUVIDORIA SETORIAL": {},
            "UNIDADE SETORIAL DE CORREICAO": {},
            "GABINETE DE DIRECAO": {},
            "UNIDADE DE DESENVOLVIMENTO ORGANIZACIONAL": {},
            "UNIDADE ESPECIAL DE ARTICULACAO INSTITUCIONAL": {},
            "UNIDADE SETORIAL": {},
            "COMISSAO DE ETICA": {},
            "UNIDADE SETORIAL DE CONTROLE INTERNO": {},
            "UNIDADE DE APOIO ESTRATEGICO": {},
            "UNIDADE DE ASSESSORIA": {},
            "CONSELHO ESTADUAL DE EDUCACAO": {
                "SECRETARIA DO CONSELHO": {},
                "COORDENADORIA DE APOIO AS CAMARAS": {
                    "CAMARA DE EDUCACAO BASICA": {},
                    "CAMARA DE EDUCACAO PROFISSIONAL E ENSINO SUPERIOR": {},
                },
                "COORDENADORIA DE SUPORTE OPERACIONAL": {},
            },
        },
        "GABINETE DO SECRETARIO ADJUNTO EXECUTIVO ": {
            "UNIDADE DE CERIMONIAL": {},
            "UNIDADE EXECUTIVA E DE NEGOCIO DA SECRETARIA ADJUNTA EXECUTIVA": {},
            "UNIDADE DE COORDENACAO DO PROGRAMA": {},
            "UNIDADE DE MICROPLANEJAMENTO": {},
            "NUCLEO DE APOIO E MONITORAMENTO ESCOLAR": {},
            "UNIDADE DE NORMAS DA SECRETARIA ADJUNTA EXECUTIVA": {},
            "SUPERINTENDENCIA": {
                "COORDENADORIA DE DESENVOLVIMENTO DE SOLUCOES DE TI": {
                    "NUCLEO DE ANALISE E DESENVOLVIMENTO DE SOLUCOES DE TI": {},
                    "NUCLEO DE INTELIGENCIA DE NEGOCIOS": {},
                    "NUCLEO DE TECNOLOGIAS EDUCACIONAIS": {},
                },
                "COORDENADORIA DE INFRAESTRUTURA E SEGURANCA DA INFORMACAO": {
                    "NUCLEO DE INFRAESTRUTURA DE TI": {},
                    "NUCLEO DE SUPORTE TECNICO DE TI": {},
                    "NUCLEO DE SERVICOS DE TI": {},
                    "NUCLEO DE SEGURANCA DA INFORMACAO E PROTECAO DE DADOS": {},
                },
            },
            "SUPERINTENDENCIA DE ESCOLAS ESTADUAIS MILITARES E CIVICO MILITARES": {
                "NUCLEO DE ESCOLAS ESTADUAIS MILITARES": {},
                "NUCLEO DE ESCOLAS ESTADUAIS CIVICO-MILITARES": {},
            },
        },
        "GABINETE DO SECRETARIO ADJUNTO DE GESTAO DE PESSOAS": {
            "UNIDADE EXECUTIVA E DE NEGOCIO DA GESTAO DE PESSOAS": {},
            "UNIDADE POLITICAS DE FORMACAO CONTINUADA": {},
            "UNIDADE DE NORMAS DA GESTAO DE PESSOAS": {},
            "SUPERINTENDENCIA DE DESENVOLVIMENTO, APLICACAO, SAUDE E SEGURANCA": {
                "COORDENADORIA DE APLICACAO E VIDA FUNCIONAL": {
                    "NUCLEO DE PROGRESSAO E ENQUADRAMENTO FUNCIONAL": {},
                    "NUCLEO DE INFORMACAO DA VIDA FUNCIONAL": {},
                },
                "COORDENADORIA DE DESENVOLVIMENTO": {
                    "NUCLEO DE E-FORMACAO E MIDIA": {},
                    "NUCLEO DE E FORMACAO E MIDIA": {},
                    "NUCLEO DE MONITORAMENTO DA QUALIFICACAO PROFISSIONAL": {},
                    "NUCLEO DE LOGISTICA DE FORMACAO": {},
                },
                "COORDENADORIA DE SAUDE E SEGURANCA": {},
            },
            "SUPERINTENDENCIA DE PROVIMENTO E MOVIMENTACAO": {
                "COORDENADORIA DE PROVIMENTO": {
                    "GERENCIA DE QUADRO DE PESSOAL": {},
                    "NUCLEO DE RECRUTAMENTO E SELECAO": {},
                    "NUCLEO DE PROVIMENTO DA EDUCACAO ESPECIAL": {},
                    "NUCLEO DE PROVIMENTO DA EDUCACAO ESPECIAL": {},
                    "NUCLEO DE ESTAGIO": {},
                    "NUCLEO DE SELETIVOS INTERNOS E EXTERNOS": {},
                },
                "COORDENADORIA DE MOVIMENTACAO": {},
            },
            "SUPERINTENDENCIA DE MONITORAMENTO E FOLHA DE PAGAMENTO": {
                "COORDENADORIA DE CONTROLE DE DESPESA E CONFORMIDADE DA FOLHA": {
                    "NUCLEO DE CONFORMIDADE DA FOLHA": {},
                    "NUCLEO DE CONTROLE DE DESPESAS DE PESSOAL": {},
                },
                "COORDENADORIA DE MONITORAMENTO DE PESSOAL": {
                    "NUCLEO DE GESTAO DE ASSIDUIDADE": {},
                    "NUCLEO DE MONITORAMENTO E IMPACTO DE PESSOAL": {},
                },
            },
        },
        "GABINETE DO SECRETARIO ADJUNTO DE INFRAESTRUTURA E PATRIMONIO": {
            "UNIDADE EXECUTIVA E DE NEGOCIO DA INFRAESTRUTURA E PATRIMONIO": {},
            "UNIDADE DE NORMAS DA INFRAESTRUTURA E PATRIMONIO": {},
            "SUPERINTENDENCIA DE PATRIMONIO": {
                "COORDENADORIA DE PATRIMONIO MOBILIARIO": {},
                "COORDENADORIA DE PATRIMONIO IMOBILIARIO": {
                    "NUCLEO DE PATRIMONIO IMOBILIARIO": {},
                    "NUCLEO DE PATRIMONIO MOBILIARIO": {},
                },
            },
            "SUPERINTENDENCIA DE OBRAS": {
                "COORDENADORIA DE PROJETOS E MANUTENCAO": {
                    "NUCLEO DE DESENVOLVIMENTO DE PROJETOS": {},
                    "NUCLEO DE MANUTENCAO": {},
                    "NUCLEO DE INFRAESTRUTURA": {},
                    "NUCLEO DE ANALISE DE PROJETOS DE DESCENTRALIZACAO": {},
                },
                "COORDENADORIA DE EXECUCAO DE OBRAS": {
                    "NUCLEO DE FISCALIZACAO DE OBRAS": {},
                },
            },
        },
        "GABINETE DO SECRETARIO ADJUNTO DE ADMINISTRACAO SISTEMICA": {
            "UNIDADE EXECUTIVA E DE NEGOCIO DA ADMINISTRACAO SISTEMICA": {},
            "UNIDADE DE NORMAS DA ADMINISTRACAO SISTEMICA": {},
            "SUPERINTENDENCIA DE AQUISICOES E CONTRATOS": {
                "COORDENADORIA DE GESTAO DE AQUISICOES": {},
                "COORDENADORIA DE GESTAO DE CONTRATO": {},
            },
            "SUPERINTENDENCIA DE FINANCAS": {
                "COORDENADORIA DE ORCAMENTO": {},
                "COORDENADORIA FINANCEIRA": {
                    "NUCLEO DE CONFORMIDADE": {},
                    "NUCLEO DE PESTACAO DE CONTAS DE DIARIAS": {},
                },
                "NUCLEO DE RECEITA": {},
            },
            "SUPERINTENDENCIA CONTABIL": {
                "GERENCIA DE INFORMACOES CONTABEIS": {},
                "GERENCIA DE PRESTACAO E CONFORMIDADE": {},
                "GERENCIA DE SISTEMA DE INFORMACAO ORCAMENTARIO PUBLICO DE EDUCACAO": {},
            },
            "SUPERINTENDENCIA DE ADMINISTRATIVA": {},
            "SUPERINTENDENCIA ADMINISTRATIVA": {
                "COORDENADORIA ADMINISTRATIVA": {
                    "GERENCIA DE PROTOCOLO": {},
                    "GERENCIA DE ARQUIVO CENTRAL": {},
                    "NUCLEO DE FROTAS": {},
                    "NUCLEO DE SERVICOS GERAIS": {},
                },
            },
            "SUPERINTENDENCIA DE CONVENIOS E PRESTACAO DE CONTAS": {
                "COORDENADORIA DE CONVENIOS E PRESTACAO DE CONTAS": {
                    "NUCLEO DE CONVENIOS DE INGRESSO": {},
                    "NUCLEO DE CONVENIOS DE DESCENTRALIZACAO": {},
                    "NUCLEO DE PRESTACAO DE CONTAS": {},
                }
            },
        },
        "GABINETE DO SECRETARIO ADJUNTO DE GESTAO EDUCACIONAL": {
            "UNIDADE EXECUTIVA E DE NEGOCIO DA GESTAO EDUCACIONAL": {},
            "UNIDADE DE NORMAS DA GESTAO EDUCACIONAL": {},
            "SUPERINTENDENCIA DE DESENVOLVIMENTO CURRICULAR E GESTAO PARA APRENDIZAGEM": {
                "COORDENADORIA DE ENSINO FUNDAMENTAL": {},
                "COORDENADORIA DE ENSINO MEDIO": {},
                "COORDENADORIA DE EDUCACAO EM TEMPO INTEGRAL": {},
                "COORDENADORIA DE EDUCACAO INTEGRADA E INOVACAO": {
                    "NUCLEO DE CURRICULO": {}
                },
            },
            "SUPERINTENDENCIA DE EQUIDADE E INCLUSAO": {
                "COORDENADORIA DE EDUCACAO INCLUSIVA": {
                    "CENTRO DE APOIO E SUPORTE A INCLUSAO DA EDUCACAO ESPECIAL": {}
                },
                "COORDENADORIA DE EDUCACAO ESCOLAR INDIGENA": {},
                "COORDENADORIA DE EDUCACAO ETNICO-RACIAL E AMBIENTAL": {},
                "COORDENADORIA DE EDUCACAO ETNICO RACIAL E AMBIENTAL": {},
                "COORDENADORIA DE EDUCACAO DE JOVENS E ADULTOS": {},
            },
            "SUPERINTENDENCIA DE AVALIACAO DE EDUCACAO BASICA": {
                "COORDENADORIA DE AVALIACAO E MONITORAMENTO EDUCACIONAL": {}
            },
        },
        "GABINETE DO SECRETARIO ADJUNTO DE GESTAO REGIONAL": {
            "UNIDADE EXECUTIVA E DE NEGOCIO DA GESTAO REGIONAL": {},
            "UNIDADE DE CENARIOS DA GESTAO REGIONAL": {},
            "UNIDADE DE NORMAS DA GESTAO REGIONAL": {},
            "SUPERINTENDENCIA DE GESTAO REGIONAL": {
                "NUCLEO DE GESTAO DE REPASSES": {},
                "NUCLEO DE MONITORAMENTO DAS DREs": {},
                "NUCLEO DE MONITORAMENTO DAS DRES": {},
                "NUCLEO DE INFORMACOES ESTATISTICAS": {},
                "COORDENADORIA DE ALIMENTACAO ESCOLAR": {
                    "NUCLEO DE NUTRICAO E MONITORAMENTO": {},
                    "NUCLEO DE GESTAO DAS AQUISICOES DA ALIMENTACAO ESCOLAR": {},
                },
            },
            "SUPERINTENDENCIA DE GESTAO ESCOLAR": {
                "COORDENADORIA DE GESTAO DE REDE": {
                    "NUCLEO DE ESTRUTURA E FUNCIONAMENTO DE GESTAO ESCOLAR": {},
                    "NUCLEO DE MEDIACAO ESCOLAR": {},
                    "NUCLEO DE ESCRITURACAO": {},
                    "NUCLEO DE MATRICULAS": {},
                    "NUCLEO DE BEM-ESTAR": {},
                    "NUCLEO DE BUSCA ATIVA ESCOLAR": {},
                }
            },
        },
        "GABINETE DO SECRETARIO ADJUNTO DE REGIME DE COLABORACAO": {
            "NUCLEO EDUCA-MT": {},
            "NUCLEO DE ANALISE E MONITORAMENTO DE INDICADORES": {},
            "UNIDADE EXECUTIVA E DE NEGOCIO DE REGIME DE COLABORACAO": {},
            "UNIDADE DE NORMAS DO REGIME DE COLABORACAO": {},
            "SUPERINTENDENCIA DE POLITICAS EM REGIME DE COLABORACAO": {
                "COORDENADORIA DE IMPACTO EDUCACIONAL": {
                    "NUCLEO DE APOIO E DESENVOLVIMENTO DA EDUCACAO INFANTIL": {},
                    "NUCLEO DE APOIO E DESENVOLVIMENTO DA ALFABETIZACAO E ANOS INICIAIS": {},
                    "NUCLEO DE APOIO E DESENVOLVIMENTO A GESTAO MUNICIPAL": {},
                },
                "COORDENADORIA DE TRANSPORTE ESCOLAR": {},
            },
        },
        "NAO SEI CLASSIFICAR": {
            "C A P D V DE MATO GROSSO CAP MT": {},
        },
    }

    return hierarquia


def busca_organograma(hierarquia, setor, super_atual=None):
    for chave, valor in hierarquia.items():
        if "GABINETE" in chave:
            super_atual = chave

        if chave == setor:
            return super_atual

        if isinstance(valor, dict):
            resultado = busca_organograma(valor, setor, super_atual)

            if resultado is not None:
                return resultado

    return None

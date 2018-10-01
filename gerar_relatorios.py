import csv_file
import os

# NR_CANDIDATO
# NM_URNA_CANDIDATO

# NR_CPF_CANDIDATO
# NM_EMAIL_CANDIDATO
# NM_SOCIAL_CANDIDATO
# NM_CANDIDATO
# CD_SITUACAO_CANDIDATURA
# DS_SITUACAO_CANDIDATURA
# DS_DETALHE_SITUACAO_CAND

# CD_CARGO
# DS_CARGO

# NM_COLIGACAO
# TP_AGREMIACAO
# NM_PARTIDO
# SQ_COLIGACAO
# DS_COMPOSICAO_COLIGACAO

# -----
# ORIGEM
# =====
# CD_NACIONALIDADE
# SG_UF_NASCIMENTO
# NM_MUNICIPIO_NASCIMENTO

# -----
# IDADE
# =====
# DT_NASCIMENTO
# NR_IDADE_DATA_POSSE

# -----
# GENERO
# =====
# CD_GENERO
# DS_GENERO

# -----
# GRAU DE INSTRU
# =====
# CD_GRAU_INSTRUCAO
# DS_GRAU_INSTRUCAO

# -----
# ESTADO CIVIL
# =====
# CD_ESTADO_CIVIL
# DS_ESTADO_CIVIL

# -----
# RACA
# =====
# CD_COR_RACA
# DS_COR_RACA

# -----
# OCUPACAO
# =====
# CD_OCUPACAO
# DS_OCUPACAO

# -----
# DESPESA_CAMPANHA
# =====
# VR_MAX_DESPESA_CAMPANHA

# https://www.google.com/search?q=


"""
CAMPOS = [
    'NR_CANDIDATO',
    'link',
    'NM_URNA_CANDIDATO',
    'NR_CPF_CANDIDATO',
    'NM_EMAIL_CANDIDATO',
    'NM_SOCIAL_CANDIDATO',
    'NM_CANDIDATO',
    'CD_SITUACAO_CANDIDATURA',
    'DS_SITUACAO_CANDIDATURA',
    'DS_DETALHE_SITUACAO_CAND',
    'CD_CARGO',
    'DS_CARGO',
    'NM_COLIGACAO',
    'TP_AGREMIACAO',
    'NM_PARTIDO',
    'DS_COMPOSICAO_COLIGACAO',
    'CD_NACIONALIDADE',
    'DS_NACIONALIDADE',
    'SG_UF_NASCIMENTO',
    'NM_MUNICIPIO_NASCIMENTO',
    'DT_NASCIMENTO',
    'NR_IDADE_DATA_POSSE',
    'CD_GENERO',
    'DS_GENERO',
    'CD_GRAU_INSTRUCAO',
    'DS_GRAU_INSTRUCAO',
    'CD_ESTADO_CIVIL',
    'DS_ESTADO_CIVIL',
    'CD_COR_RACA',
    'DS_COR_RACA',
    'CD_OCUPACAO',
    'DS_OCUPACAO',
    'VR_MAX_DESPESA_CAMPANHA']
"""

CAMPOS_GOVERNADOR = [
    'NR_CANDIDATO',
    'link',
    'NM_URNA_CANDIDATO',
    'NR_CPF_CANDIDATO',
    'NM_EMAIL_CANDIDATO',
    'NM_SOCIAL_CANDIDATO',
    'NM_CANDIDATO',
    'NM_COLIGACAO',
    'TP_AGREMIACAO',
    'NM_PARTIDO',
    'DS_COMPOSICAO_COLIGACAO',
    'DS_NACIONALIDADE',
    'SG_UF_NASCIMENTO',
    'NM_MUNICIPIO_NASCIMENTO',
    'DT_NASCIMENTO',
    'NR_IDADE_DATA_POSSE',
    'DS_GENERO',
    'DS_GRAU_INSTRUCAO',
    'DS_ESTADO_CIVIL',
    'DS_COR_RACA',
    'DS_OCUPACAO',
    'VR_MAX_DESPESA_CAMPANHA']

CAMPOS = [
    'NR_CANDIDATO',
    'link',
    'NM_URNA_CANDIDATO',
    'NR_CPF_CANDIDATO',
    'NM_EMAIL_CANDIDATO',
    'NM_SOCIAL_CANDIDATO',
    'NM_CANDIDATO',
    'NM_COLIGACAO',
    'TP_AGREMIACAO',
    'NM_PARTIDO',
    'DS_NACIONALIDADE',
    'SG_UF_NASCIMENTO',
    'NM_MUNICIPIO_NASCIMENTO',
    'DT_NASCIMENTO',
    'NR_IDADE_DATA_POSSE',
    'DS_GENERO',
    'DS_GRAU_INSTRUCAO',
    'DS_ESTADO_CIVIL',
    'DS_COR_RACA',
    'DS_OCUPACAO',
    'VR_MAX_DESPESA_CAMPANHA']

GRUPOS = (
    ('DS_NACIONALIDADE', 'SG_UF_NASCIMENTO', 'NM_MUNICIPIO_NASCIMENTO'),
    ('NR_IDADE_DATA_POSSE', ),
    ('DS_GENERO', ),
    ('DS_GRAU_INSTRUCAO', ),
    ('DS_ESTADO_CIVIL', ),
    ('DS_COR_RACA', ),
    ('DS_OCUPACAO', ),
    ('VR_MAX_DESPESA_CAMPANHA', ),
)

ROW0 = '"DT_GERACAO";"HH_GERACAO";"ANO_ELEICAO";"CD_TIPO_ELEICAO";"NM_TIPO_ELEICAO";"NR_TURNO";"CD_ELEICAO";"DS_ELEICAO";"DT_ELEICAO";"TP_ABRANGENCIA";"SG_UF";"SG_UE";"NM_UE";"CD_CARGO";"DS_CARGO";"SQ_CANDIDATO";"NR_CANDIDATO";"NM_CANDIDATO";"NM_URNA_CANDIDATO";"NM_SOCIAL_CANDIDATO";"NR_CPF_CANDIDATO";"NM_EMAIL";"CD_SITUACAO_CANDIDATURA";"DS_SITUACAO_CANDIDATURA";"CD_DETALHE_SITUACAO_CAND";"DS_DETALHE_SITUACAO_CAND";"TP_AGREMIACAO";"NR_PARTIDO";"SG_PARTIDO";"NM_PARTIDO";"SQ_COLIGACAO";"NM_COLIGACAO";"DS_COMPOSICAO_COLIGACAO";"CD_NACIONALIDADE";"DS_NACIONALIDADE";"SG_UF_NASCIMENTO";"CD_MUNICIPIO_NASCIMENTO";"NM_MUNICIPIO_NASCIMENTO";"DT_NASCIMENTO";"NR_IDADE_DATA_POSSE";"NR_TITULO_ELEITORAL_CANDIDATO";"CD_GENERO";"DS_GENERO";"CD_GRAU_INSTRUCAO";"DS_GRAU_INSTRUCAO";"CD_ESTADO_CIVIL";"DS_ESTADO_CIVIL";"CD_COR_RACA";"DS_COR_RACA";"CD_OCUPACAO";"DS_OCUPACAO";"NR_DESPESA_MAX_CAMPANHA";"CD_SIT_TOT_TURNO";"DS_SIT_TOT_TURNO";"ST_REELEICAO";"ST_DECLARAR_BENS";"NR_PROTOCOLO_CANDIDATURA";"NR_PROCESSO"'
COLUMNS = [row[1:-1] for row in ROW0.split(';')]


def get_candidatos_por_numero(rows):
    _rows = {}
    for index, data in enumerate(rows):
        link = '`Google <https://www.google.com/search?q={}>`_'.format(data.get('NM_CANDIDATO').replace(' ', '+'))
        data.update({'link': link, 'index': index})
        _rows[index] = data
    return _rows


def agrupar_por(items, index, row, colunas):
    valores = []
    for coluna in colunas:
        valor = str(row.get(coluna))
        valores.append(valor)
    k = '-'.join(valores)
    if items.get(k) is None:
        items[k] = []
    items[k].append(index)


def agrupar(candidatos, grupos):
    _rows = {}
    governador_rows = {}
    for index, data in candidatos.items():
        index = data.get('index')
        status = (str(data.get('DS_SITUACAO_CANDIDATURA')), str(data.get('DS_DETALHE_SITUACAO_CAND')))
        cd_cargo = str(data.get('DS_CARGO'))
        sq_coligacao = str(data.get('DS_COMPOSICAO_COLIGACAO'))

        if 'GOVERNADOR' in cd_cargo:
            if governador_rows.get(status) is None:
                governador_rows[status] = {}
            if governador_rows[status].get(cd_cargo) is None:
                governador_rows[status][cd_cargo] = {}
            for colunas in grupos:
                rotulo = '|'.join(colunas)
                if governador_rows[status][cd_cargo].get(rotulo) is None:
                    governador_rows[status][cd_cargo][rotulo] = {}
                agrupar_por(governador_rows[status][cd_cargo][rotulo], index, data, colunas)
        else:
            if _rows.get(status) is None:
                _rows[status] = {}
            if _rows[status].get(cd_cargo) is None:
                _rows[status][cd_cargo] = {}
            if _rows[status][cd_cargo].get(sq_coligacao) is None:
                _rows[status][cd_cargo][sq_coligacao] = {}

            for colunas in grupos:
                rotulo = '|'.join(colunas)
                if _rows[status][cd_cargo][sq_coligacao].get(rotulo) is None:
                    _rows[status][cd_cargo][sq_coligacao][rotulo] = {}
                agrupar_por(_rows[status][cd_cargo][sq_coligacao][rotulo], index, data, colunas)
    return _rows, governador_rows


def gerar_relatorios_governadores(candidatos_por_n, governadores, campos, path):
    for status, candidatos_por_status in governadores.items():
        for cargo, candidatos_por_cargo in candidatos_por_status.items():
            for grupo, candidatos_por_grupo in candidatos_por_cargo.items():
                save_governador_rst(path, status, cargo, grupo, candidatos_por_grupo, candidatos_por_numero, campos)


def gerar_relatorios(candidatos_por_n, agrupados, campos, path):
    for status, candidatos_por_status in agrupados.items():
        for cargo, candidatos_por_cargo in candidatos_por_status.items():
            for coligacao, candidatos_por_coligacao in candidatos_por_cargo.items():
                for grupo, candidatos_por_grupo in candidatos_por_coligacao.items():
                    save_rst(path, status, cargo, coligacao, grupo, candidatos_por_grupo, candidatos_por_numero, campos)


def nome_de_dir(s):
    return ''.join([c if c.isalnum() else '-' for c in s])


def save_governador_rst(_path, status, cargo, grupo, candidatos_por_grupo, candidatos_por_numero, campos):
    paths = [nome_de_dir(item) for item in (status[0], status[1], cargo)]
    path = os.path.join(_path, paths[0], paths[1], paths[2])
    if not os.path.isdir(path):
        os.makedirs(path)

    nome = nome_de_dir(grupo).lower()

    content = []
    content += [cargo + '\n' + '='*len(cargo) + '\n']

    t = 0
    for nome_do_grupo in sorted(list(candidatos_por_grupo.keys())):

        title = '{} ({})'.format(nome_do_grupo, len(candidatos_por_grupo[nome_do_grupo]))
        content += [title + '\n' + '.'*len(title) + '\n']
        for nr in sorted(candidatos_por_grupo[nome_do_grupo]):
            candidato = candidatos_por_numero.get(nr)
            t += 1
            content += ['**{}**'.format(candidato.get('NM_CANDIDATO')) + '\n']
            for campo in campos:
                content += ['- {}: {}'.format(campo, candidato.get(campo, '?'))]
            content += ['\n']

    filename = os.path.join(path, '{}_{}.rst'.format(nome, t))
    with open(filename, 'w') as f:
        f.write('Total: {}'.format(t)+'\n\n')
        f.write('\n'.join(content).replace('None', 'Nenhum valor'))
    print(filename)


def save_rst(_path, status, cargo, coligacao, grupo, candidatos_por_grupo, candidatos_por_numero, campos):
    paths = [nome_de_dir(item) for item in (status[0], status[1], cargo, coligacao)]
    path = os.path.join(_path, paths[0], paths[1], paths[2], paths[3])
    if not os.path.isdir(path):
        os.makedirs(path)

    nome = nome_de_dir(grupo).lower()

    content = []
    content += [cargo + '\n' + '='*len(cargo) + '\n']
    content += [coligacao + '\n' + '-'*len(coligacao) + '\n']

    t = 0
    for nome_do_grupo in sorted(list(candidatos_por_grupo.keys())):

        title = '{} ({})'.format(nome_do_grupo, len(candidatos_por_grupo[nome_do_grupo]))
        content += [title + '\n' + '.'*len(title) + '\n']
        for nr in sorted(candidatos_por_grupo[nome_do_grupo]):
            candidato = candidatos_por_numero.get(nr)
            t += 1
            content += ['**{}**'.format(candidato.get('NM_CANDIDATO')) + '\n']
            for campo in campos:
                content += ['- {}: {}'.format(campo, candidato.get(campo, '?'))]
            content += ['\n']

    filename = os.path.join(path, '{}_{}.rst'.format(nome, t))
    with open(filename, 'w') as f:
        f.write('Total: {}'.format(t)+'\n\n')
        f.write('\n'.join(content).replace('None', 'Nenhum valor'))
    print(filename)


ROWS = csv_file.read('consulta_cand_2018_SP.csv', fieldnames=COLUMNS)[1:]

# print(ROWS)
print(len(ROWS))
candidatos_por_numero = get_candidatos_por_numero(ROWS)
print(len(candidatos_por_numero))
agrupados, governadores = agrupar(candidatos_por_numero, GRUPOS)
gerar_relatorios_governadores(candidatos_por_numero, governadores, CAMPOS, 'relatorios')
gerar_relatorios(candidatos_por_numero, agrupados, CAMPOS, 'relatorios')


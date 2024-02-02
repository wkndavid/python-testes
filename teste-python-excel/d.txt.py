lista_palavras = [
    'SAIN', 'SH', 'BOA VISTA - IMPÉRIO DOS NOBRES', 'SMAS', 'SHIS', 'SDN', 'SAM', 'SMHS', 'SEN', 
    'Q CENTRAL SETOR RESIDENCIAL', 'ARIE SANTUARIO DE VIDA SILVESTREDO RIACHO FUNDO', 'SHCNW', 
    'SETOR DE HOTEIS E DIVERSOES', 'SETOR DE OFICINAS E INDUSTRIAS DE PEQUENO PORTE', 'SCN B', 
    'AEMN', 'ADE', 'SCN 2', 'RUA 5', 'SHCGN', 'SBN', 'SETOR ITAMARACA', 'SCEN', 'SETOR E NORTE', 
    'SAI/SO', 'MUDB', 'EMI', 'SEPS', 'SGAS', 'PQEB', 'VILA SAO JOSE', 'SHS', 'SHLSW', 'SETOR A SUL', 
    'SETOR B NORTE', 'SETOR COMERCIAL CENTRAL', 'SPO', 'SETOR ADMINISTRATIVO', 'SCN 1', 'SGCV', 'SMU', 
    'SETOR DE POSTOS E MOTEIS', 'SH BOA VISTA - LOTEAMENTO BIANCA', 'SETOR N NORTE', 'SETOR C NORTE', 
    'SHLS', 'SBS', 'SRTVN', 'SETOR G NORTE', 'SIG', 'SDC', 'SAUN', 'SETOR RECREATIVO CULTURAL', 'SDS', 
    'RIACHO FUNDO II', 'SETOR DE OFICINAS E AREAS ESPECIAIS NORTE', 'BAIRRO CRIXÁ', 'SETOR HOSPITALAR', 
    'SAUS', 'SAI', 'QELC VILA TECNOLOGICA', 'SETOR JUSCELINO KUBITSCHEK', 'STN', 'SIN', 'PTS', 'SRTVS', 
    'SAIS', 'SCTS', 'STS', 'SPMS', 'SCLN', 'SRPS', 'SH OURO VERMELHO II - FASE I E II', 
    'SH GRANDE COLORADO/PARCELAMENTO MANSOES COLORADO', 'PFR', 'SCS B', 'SH TORORÓ JARDIM ATLÂNTICO SUL', 
    'SH TORORO - SANTA BARBARA', 'SETOR DE GARAGENS E CONCESSIONARIAS DE VEICULOS', 
    'SH TORORO / PARQUE DO MIRANTE', 'EMO', 'SETOR R NORTE', 'CENTRO METROPOLITANO', 'SETOR NORTE', 
    'SH ESTRADA DO SOL/RESIDENCIAL QUINTAS INTERLAGOS', 'VILA NOVA DIVINEIA', 'SETOR DE OFICINAS E PEQUENAS INDUSTRIAS', 
    'SAI/SE', 'SHVP - ETAPA 3 - CA. SAMAMBAIA', 'SETOR DE AREAS COMPLEMENTARES', 
    'SETOR HABITACIONAL VICENTE PIRES/GLEBA 1/2/3', 'SETOR DE AREAS ESPECIAIS NORTE', 'ZOOLOGICO', 'SCEE SUL', 
    'SOF SUL', 'SPP', 'SETOR DE AREAS ISOLADAS', 'SETOR DE POSTOS E MOTEIS SUL', 'SMI', 'SAI/O', 'SETOR DE INDUSTRIA', 
    'SCES', 'SEDB', 'SETOR DE EDUCACAO', 'Q CENTRAL SETOR HOTELEIRO', 'SETOR CENTRAL', 'SETOR F SUL', 
    'SETOR DE INDUSTRIAS GRAFICAS', 'Q CENTRAL SETOR ADMINISTRATIVO E CULTURAL', 'SETOR A NORTE', 
    'SETOR INDUSTRIAL', 'SETOR DE MÚTIPLAS ATIVIDADES', 'ADE OESTE', 'PTP', 'SETOR DE DESENVOLVIMENTO ECONOMICO', 
    'VILA DVO', 'SAFN', 'SETOR H NORTE', 'SHCES', 'SH SAO BARTOLOMEU TRECHO 1', 'SH TORORO - ESTÂNCIA DEL REY', 
    'SHIN', 'SETOR DE AREAS ESPECIAIS NORTE 1 BURITIS II', 'RUA 3', 'VILA DNOCS', 'SETOR DE EXPANSAO ECONOMICA', 
    'SMHN', 'SCIA', 'SMDB', 'SPMN', 'SAI NORDESTE', 'SETOR RESIDENCIAL NORTE A', 'SETOR G SUL', 'SETOR F NORTE', 
    'SETOR Q NORTE', 'SETOR M NORTE', 'EXPANSAO DO SETOR O', 'SDMC', 'SRIA I', 'QELC', 'SETOR O NORTE', 'NUCLEO RURAL NB 1', 
    'SML', 'SCLRN', 'SETOR P NORTE', 'SAI/L', 'SEPN', 'SETOR HABITACIONAL SOL NASCENTE', 'ADE POLO JK', 
    'SH SAO BARTOLOMEU/ QUINTAS DA ALVORADA', 'VPLA', 'SIA', 'SETOR SUL', 'SETOR B SUL', 'SRES', 'STRC', 
    'SETOR DE MANSOES SUDESTE', 'SETOR D NORTE', 'SITIO DO GAMA', 'VILA VICENTINA', 'SRIA II', 'ADE SUL', 'SHTQ', 
    'CENTRO URBANO', 'BAIRRO VEREDAS', 'SETOR HABITACIONAL ALTO DA BOA VISTA', 'SETOR L NORTE', 'SETOR E SUL', 
    'SETOR OESTE', 'SETOR HOTELEIRO', 'SHLN', 'SETOR C SUL', 'SETOR RESIDENCIAL OESTE VILA NOSSA SENHORA DE FATI', 
    'SETOR LESTE', 'SETOR D SUL', 'SETOR QI', 'SGO', 'SPVP', 'EMO/O', 'SETOR J NORTE', 'SETOR DE MANSOES LESTE', 
    'SES', 'SGAN', 'SETOR TRADICIONAL', 'SAI/NO', 'SHN', 'ERN', 'UNB', 'Q CENTRAL SETOR COMERCIAL', 
    'Q CENTRAL SETOR ADMINISTRATIVO', 'SGMN', 'VILA METROPOLITANA', 'EXPANSAO URBANA SETOR OESTE', 'SCTN', 
    'ERS', 'SETOR RESIDENCIAL LESTE', 'SETOR PLACA DA MERCEDES', 'SETOR INDUSTRIAL BERNARDO SAYAO', 'SHCAO', 
    'ALDEIAS DO CERRADO', 'SHIGS', 'SH JARDIM BOTÂNICO - ETAPA 2', 'SHTN', 'SCRN', 'SHCSW', 'SCS', 'PMU', 'SCRS', 
    'SCLS', 'SHPB', 'SH BONSUCESSO', 'SH CONTAGEM/LOTEAMENTO RESIDENCIAL IPÊS', 
    'SH GRANDE COLORADO/VIVENDAS LAGO AZUL', 'SH ARAPOANGA ETAPA 3', 'SHBJ - ETAPA 4', 'SH BOA VISTA - SÍTIO VILA CÉLIA', 
    'SETOR MEIRELES', 'SH ESTRADA DO SOL - COND. BELVEDERE GREEN', 'SH CONTAGEM / JARDIM VITÓRIA', 
    'SH TORORÓ/ MANSÔES FLAMBOYANT', 'SAFS', 'MSPW', 'SHA', 'SH ARAPOANGA - ETAPA 3', 'SH CONTAGEM/MARINA', 
    'SETOR HABITACIONAL ARAPOANGA', 'SH CONTAGEM / RESIDENCIAL SOL NASCENTE', 'EXPANSÃO DA VILA SÃO JOSÉ', 
    'SH CONTAGEM/PARCELAMENTO CARAVELO', 'SH JARDIM BOTÂNICO', 'SH ESTRADA DO SOL CONDOMÍNIO VERDE', 
    'SH GRANDE COLORADO PARCELAMENTO SOLAR DE ATHENAS', 'SHJK', 'SH CONTAGEM/RESIDENCIAL SOBRADINHO', 
    'SH CONTAGEM - PARCELAMENTO RESIDENCIAL PLANALTO', 'URBITA', 'SH BOA VISTA - RESIDENCIAL CALLIANDRA', 
    'SETOR AVENIDA CONTORNO', 'SETOR HABITACIONAL DO TORORÓ', 'SH BOA VISTA', 
    'SH MEIRELES - RESIDENCIAL FAZENDA SANTA MARIA','SH CONTAGEM/RECANTO DOS NOBRES','SH CONTANGEM/SÃO JORGE','SH CONTAGEM/PARAÍSO','SCIA','SHCNW','SHIN','EXPANSAO URBANA SETOR OESTE','SHCES','SHVP - ETAPA 3 - CA. SAMAMBAIA','SHIS','BAIRRO CRIXÁ','SRIA II','SETOR CENTRAL','SHCSW','ALDEIAS DO CERRADO','SH OURO VERMELHO II - FASE I E II','SITIO DO GAMA','SETOR RESIDENCIAL NORTE A','SETOR RESIDENCIAL LESTE','SETOR A SUL','SETOR DE EXPANSAO ECONOMICA','SETOR P NORTE','SETOR B NORTE','SETOR DE INDUSTRIA','SETOR HABITACIONAL VICENTE PIRES/GLEBA 1/2/3','SETOR N NORTE','SETOR O NORTE','SETOR B SUL','SETOR G NORTE','SMAS','SETOR RESIDENCIAL OESTE VILA NOSSA SENHORA DE FATI','SH TORORO / PARQUE DO MIRANTE','SH TORORO - ESTÂNCIA DEL REY','SRIA I','SAI/O',
    'QELC','RIACHO FUNDO II','SETOR M NORTE','SHTQ','SH ESTRADA DO SOL/RESIDENCIAL QUINTAS INTERLAGOS','SETOR LESTE','SETOR G SUL','SETOR C SUL','SETOR INDUSTRIAL BERNARDO SAYAO','SETOR H NORTE','SETOR J NORTE','SHIGS','SETOR D NORTE','SETOR INDUSTRIAL','SEPS','SCRS',    'VILA VICENTINA',    'SETOR TRADICIONAL',    'SIG',    'SETOR NORTE',    'SCLS',    'VILA METROPOLITANA',    'EXPANSAO DO SETOR O',    'SGAS',    'SH GRANDE COLORADO/VIVENDAS LAGO AZUL',    'SCRN',    'SETOR OESTE',    'SH BOA VISTA - IMPÉRIO DOS NOBRES',    'ADE OESTE',    'SH TORORÓ JARDIM ATLÂNTICO SUL',    'SETOR F SUL',    'SETOR HABITACIONAL ALTO DA BOA VISTA',    'SETOR QI',    'SOF SUL',    'SML',    'SETOR A NORTE',    'SETOR HABITACIONAL SOL NASCENTE',    'SDMC',    'SGAN',    'SCLN',    'SEPN',    'SETOR C NORTE',    'SHN',   'SETOR COMERCIAL CENTRAL',    'ADE POLO JK',    'SH JARDIM OTÂNICO - ETAPA 2',    'SETOR DE AREAS ESPECIAIS NORTE 1 BURITIS II',    'SH SAO BARTOLOMEU/ QUINTAS DA ALVORADA',   'ADE',    'SIA',
    'SETOR SUL',    'SETOR E SUL',    'SETOR D SUL',    'SETOR F NORTE',    'SETOR E NORTE',    'CENTRO METROPOLITANO',    'SRES',
    'SHTN',    'SHCAO',    'VILA DNOCS',    'SHPB',    'SETOR R NORTE',    'SH BONSUCESSO',    'SCLRN',    'SHS',    'SH SAO ARTOLOMEU TRECHO 1',    'VILA SAO JOSE',    'VPLA',    'SETOR DE AREAS ISOLADAS',    'SAUS',    'BAIRRO VEREDAS',    'SETOR Q NORTE',    'SETOR L NORTE',    'Q CENTRAL SETOR HOTELEIRO',    'Q CENTRAL SETOR RESIDENCIAL',    'SETOR DE DESENVOLVIMENTO ECONOMICO',    'STRC',    'QELC VILA TECNOLOGICA',    'MSPW',    'CENTRO URBANO',    'SETOR ITAMARACA',    'Q CENTRAL SETOR ADMINISTRATIVO',    'Q CENTRAL SETOR ADMINISTRATIVO E CULTURAL',    'Q CENTRAL SETOR COMERCIAL',    'SHLS',
    'SAFS',    'SGO',    'SETOR DE OFICINAS E PEQUENAS INDUSTRIAS',    'SMHN',    'SCES',    'SCEN',    'SRTVN',    'SAUN',  'SHCGN',
    'SH ARAPOANGA ETAPA 3',    'SHBJ - ETAPA 4',    'SH BOA VISTA - SÍTIO VILA CÉLIA',    'SHA',    'EXPANSÃO DA VILA SÃO JOSÉ',
    'SH ARAPOANGA - ETAPA 3',    'SETOR HABITACIONAL ARAPOANGA',    'SH TORORO - SANTA BARBARA',    'SHJK',    'URBITA',    'SETOR MEIRELES',    'SH BOA VISTA',    'SH MEIRELES - RESIDENCIAL FAZENDA SANTA MARIA'
]
print(len(lista_palavras))

# -*- coding: utf-8 -*-
u"""Escreve o `_letreiro/conteudo.json` — O LETREIRO DE BLUMENAU (5º ano).

Por que o conteúdo mora num .py e não direto no .json: são 32 fases, cada uma
com andaime de três degraus, e o JSON cru não aceita comentário nenhum. Aqui dá
para explicar POR QUE cada fase existe — e a explicação é o que sobrevive à
próxima pessoa que mexer.

⚠️ O PORTÃO 0 (EDUVERSE-FILOSOFIA.md): o problema vem primeiro e o conceito por
ÚLTIMO. A criança passa a atividade inteira consertando letreiro e só na fase
30 o Pincel ouve dela, escrita como regra, a coisa que ela já vinha fazendo. Se
a regra aparecesse na fase 1, isto viraria exercício de aplicar regra — que é
exatamente o que ela já faz no caderno e que não a faz querer mais.
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# O BANCO DE PALAVRAS — e ele não é uma lista qualquer.
#
# ⚠️ A armadilha desta regra: quase toda lista de "palavras com M antes de P e
#    B" que se acha por aí é feita de palavras que a criança de 10 anos não
#    usa (âmbar, ímpar, tímpano). Ela acerta a letra e não leva nada para a
#    vida. As daqui são palavras de Blumenau e de escola: campo, bomba,
#    sempre, ombro, tambor, campeão, bombeiro, lâmpada.
# --------------------------------------------------------------------------
COM_M = [u"CAMPO", u"BOMBA", u"SEMPRE", u"TEMPO", u"TAMBÉM", u"OMBRO",
         u"SOMBRA", u"LÂMPADA", u"COMPRAR", u"TAMBOR", u"POMBA", u"LIMPO",
         u"CAMPEÃO", u"BOMBEIRO", u"SIMPLES", u"COMPRIDO"]
COM_N = [u"CANTO", u"MANGA", u"ONDA", u"PONTE", u"TINTA", u"BANCO",
         u"DENTE", u"ONTEM", u"MUNDO", u"PLANTA", u"VENTO", u"CONTA"]


def fase(fid, mec, selo, enun, dica, conceito, dados, extra=None, revela=None):
    f = {"id": fid, "mec": mec, "selo": selo, "enunciado": enun,
         "dica": dica, "conceito": conceito, "dados": dados}
    if extra:
        f["dadosExtra"] = extra
    if revela:
        f["revela"] = revela
    return f


FASES = []
A = FASES.append

# ==========================================================================
# BLOCO 0 — O PROBLEMA (o conceito NÃO aparece aqui)
# ==========================================================================

# ⚠️ A PRIMEIRA TELA É A QUE DECIDE. Ela não pergunta nada sobre ortografia:
#    mostra a placa da padaria escrita errada, na rua onde a criança passa. O
#    que ela sente primeiro é "isso está esquisito", não "vou estudar M e N".
A(fase(
    "f01", "conserte-o-erro", u"A PLACA DA PADARIA",
    u"O ajudante novo pintou as placas da Rua XV. Esta ficou estranha e a dona não sabe por quê. Ache o pedaço errado e conserte.",
    u"Leia a placa em voz alta, devagar. Onde a sua boca faz um som diferente do que está escrito?",
    "objetivo1",
    [
        {"selo": u"PADARIA DA RUA XV", "cab": u"O LETREIRO PINTADO ONTEM",
         "bal": u"A dona pediu <b>PADARIA CAMPO BOM</b>. O ajudante pintou assim. Ache o pedaço errado.",
         "pecas": ["PADARIA", "CANPO", "BOM"], "erro": 1, "certa": "CAMPO",
         "ops": ["CAMPO", "CAMPU", "CANMPO"],
         "por": u"É <b>CAMPO</b>, com M. Guarde esta placa: no fim você vai saber dizer por quê.",
         "dicas": [u"Diga a palavra em voz alta: <b>cam-po</b>. Escute o pedacinho antes do P.",
                   u"Uma letra ali está no lugar da outra. É a letra que vem <b>antes do P</b>.",
                   u"Era esta: eu marquei para você. Agora escolha o jeito certo."],
         "dicas2": [u"Duas opções mudam a última letra; uma muda a letra do meio. Ouça: <b>cam-po</b>.",
                    u"O fim da palavra é <b>-PO</b>, com O. O que muda mesmo é a letra antes do P.",
                    u"Era <b>CAMPO</b>. Troquei para você ver na placa."]},
        {"selo": u"FLORICULTURA DO GARCIA", "cab": u"A SEGUNDA PLACA",
         "bal": u"Esta é da floricultura do bairro Garcia. Ache o pedaço errado.",
         "pecas": ["FLORES", "SENPRE", "VIVAS"], "erro": 1, "certa": "SEMPRE",
         "ops": ["SEMPRE", "SENPRE", "SEMPRI"],
         "por": u"É <b>SEMPRE</b>, com M antes do P.",
         "dicas": [u"Fale devagar: <b>sem-pre</b>. Repare no som antes do P.",
                   u"O erro está na mesma família do erro da padaria.",
                   u"Marquei o pedaço: agora é só escolher o certo."],
         "dicas2": [u"Uma opção troca o fim da palavra; a outra troca a letra do meio.",
                    u"O fim é <b>-PRE</b>. Olhe a letra que vem antes do P.",
                    u"Era <b>SEMPRE</b>. Troquei para você ver."]},
    ]))

# ⚠️ CONCRETO ANTES DE FIGURAL (Bruner/CPA): antes de olhar a LETRA, a criança
#    sente a palavra no corpo — bate a sílaba e escuta o ar sair pelo nariz. É
#    o degrau que quase toda aula de ortografia pula.
A(fase(
    "f02", "bater-silabas", u"O SOM QUE VEM DO NARIZ",
    u"Bata uma vez para cada pedaço da palavra. Ponha o dedo no nariz enquanto fala: você vai sentir ele tremer.",
    u"O nariz treme no pedaço que termina com o som de M ou de N. Fale bem devagar.",
    "objetivo1",
    [
        {"pal": u"CAMPO", "sil": ["CAM", "PO"], "voz": u"cam... po", "fig": "lt_campo",
         "d": [u"Diga <b>CAM-PO</b> devagar e bata uma vez para cada pedaço.",
               u"São dois pedaços. O primeiro sai pelo nariz: <b>cam</b>.",
               u"São <b>2</b> batidas: cam... po. Elas já estão aí — toque em Pronto."]},
        {"pal": u"BOMBA", "sil": ["BOM", "BA"], "voz": u"bom... ba", "fig": "lt_bomba",
         "d": [u"Ponha a mão no nariz e diga <b>BOM-BA</b>. Sentiu o tremor?",
               u"O tremor está no primeiro pedaço, que é o que termina no som do nariz.",
               u"São <b>2</b> batidas: bom... ba."]},
        {"pal": u"TAMBOR", "sil": ["TAM", "BOR"], "voz": u"tam... bor", "fig": "lt_tambor",
         "d": [u"Diga <b>TAM-BOR</b> batendo na mesa, como se fosse o próprio tambor.",
               u"Dois pedaços, e o nariz treme no primeiro.",
               u"São <b>2</b> batidas: tam... bor."]},
    ]))

A(fase(
    "f03", "escolher", u"QUAL PLACA ESTÁ CERTA?",
    u"A gráfica mandou duas provas de cada placa. Escolha a que está escrita do jeito certo.",
    u"Fale as duas em voz alta. As duas soam igual — então a diferença está na LETRA, não no som.",
    "objetivo1",
    [
        {"p": u"A academia da esquina quer o nome dela numa placa. Qual está certa?",
         "c": u"OMBRO A OMBRO", "e": [u"ONBRO A ONBRO", u"OMBRU A OMBRU"],
         "d": [u"Diga <b>om-bro</b> e escute o pedaço antes do B.",
               u"Você já viu esse mesmo pedaço em CAMPO e em SEMPRE.",
               u"É <b>OMBRO A OMBRO</b>. Toque nela para seguir."]},
        {"p": u"A loja de instrumentos do centro. Qual placa está certa?",
         "c": u"CASA DO TAMBOR", "e": [u"CASA DO TANBOR", u"CASA DO TAMBÔR"],
         "d": [u"Fale <b>tam-bor</b> devagar, do jeito que você bateu na fase passada.",
               u"O pedaço antes do B é o mesmo de BOMBA.",
               u"É <b>CASA DO TAMBOR</b>."]},
        {"p": u"A oficina que conserta bomba d'água. Qual placa está certa?",
         "c": u"BOMBA D'ÁGUA", "e": [u"BONBA D'ÁGUA", u"BOMBA D'AGUA"],
         "d": [u"Diga <b>bom-ba</b>. Que letra fecha o primeiro pedaço?",
               u"É a mesma letra que fechava o primeiro pedaço de CAMPO.",
               u"É <b>BOMBA D'ÁGUA</b> — e o A leva acento."]},
    ],
    extra={"TITULO": u"A PROVA DA GRÁFICA",
           "FECHO": u"As três placas saíram certas da gráfica!"}))

# ==========================================================================
# BLOCO 1 — A LETRA QUE MORA ALI (objetivo2)
# ==========================================================================

# ⚠️ ESTE É O GESTO DA REGRA: a palavra vem com o buraco e a criança leva a
#    letra até ele. Nenhuma outra mecânica faz isso — escolher uma opção é
#    outro gesto, e o gesto é metade do que se aprende.
A(fase(
    "f04", "letras-escondidas", u"FALTA UMA LETRA",
    u"O ajudante deixou um buraco em cada palavra. Leve a letra certa até ele.",
    u"Toque no alto-falante e ouça a palavra inteira antes de escolher.",
    "objetivo1",
    [
        {"pal": u"CAMPO", "esc": u"CA_PO", "extra": ["N", "L"], "img": "lt_campo", "voz": u"campo",
         "d": [u"Diga a palavra devagar e escute o nariz: <b>cam-po</b>. Que letra falta antes do P?",
               u"Deixei só duas na bandeja. Escute de novo: <b>cam-po</b>.",
               u"É o <b>M</b>. Ele está aceso — toque nele para seguir."]},
        {"pal": u"BOMBA", "esc": u"BO_BA", "extra": ["N", "T"], "img": "lt_bomba", "voz": u"bomba",
         "d": [u"Ouça a palavra de novo e repare no que vem antes do <b>B</b>.",
               u"Ficaram duas na bandeja. Qual delas você ouviu?",
               u"É o <b>M</b>: ele está aceso."]},
        {"pal": u"SEMPRE", "esc": u"SE_PRE", "extra": ["N", "R"], "img": "lt_sempre", "voz": u"sempre",
         "d": [u"<b>Sem-pre</b>. Escute o fim do primeiro pedaço.",
               u"É a mesma letra de CAMPO e de BOMBA.",
               u"É o <b>M</b>."]},
        {"pal": u"OMBRO", "esc": u"O_BRO", "extra": ["N", "S"], "img": "lt_ombro", "voz": u"ombro",
         "d": [u"<b>Om-bro</b>: ponha a mão no ombro e diga.",
               u"Antes do B mora sempre a mesma letra.",
               u"É o <b>M</b>."]},
    ],
    extra={"LETXT": {"selo": u"A LETRA QUE FALTA",
                     "balao": u"Leve a <b>letra certa</b> até o buraco da palavra.",
                     "hint": u"Toque na letra, arraste, ou digite no teclado.",
                     "ouvir": u"a palavra",
                     "fecho": u"Você fechou todas as palavras da vitrine!"}}))

A(fase(
    "f05", "escolher", u"A MESMA LETRA, DE NOVO",
    u"Mais placas chegaram da gráfica. Escolha a que está certa — e repare que a letra é sempre a mesma.",
    u"Você já fez isso na prova da gráfica. Olhe a letra antes do P ou do B.",
    "objetivo2",
    [
        {"p": u"A loja de bicicletas quer TEMPO BOM na placa. Qual está certa?",
         "c": u"TEMPO BOM", "e": [u"TENPO BOM", u"TEMPU BOM"],
         "d": [u"Fale <b>tem-po</b> devagar.",
               u"É a mesma letra de CAMPO e de SEMPRE.",
               u"É <b>TEMPO BOM</b>."]},
        {"p": u"A sorveteria da praça. Qual placa está certa?",
         "c": u"SOMBRA FRESCA", "e": [u"SONBRA FRESCA", u"SOMBRAA FRESCA"],
         "d": [u"Fale <b>som-bra</b> e escute o pedaço antes do B.",
               u"Antes de B mora sempre a mesma letra.",
               u"É <b>SOMBRA FRESCA</b>."]},
        {"p": u"A loja de lâmpadas do centro. Qual está certa?",
         "c": u"LÂMPADA ACESA", "e": [u"LÂNPADA ACESA", u"LAMPADA ACESA"],
         "d": [u"Fale <b>lâm-pa-da</b>: o primeiro pedaço tem chapéu no A.",
               u"Antes do P vem a letra que você já conhece — e o A leva acento.",
               u"É <b>LÂMPADA ACESA</b>."]},
    ],
    extra={"TITULO": u"A SEGUNDA REMESSA",
           "FECHO": u"Mais três placas conferidas!"}))

A(fase(
    "f06", "digitar", u"ESCREVA O NOME DA LOJA",
    u"O Pincel vai dizer o nome. Escreva do jeito certo — pode usar o teclado da tela ou o teclado de verdade.",
    u"Fale a palavra baixinho antes de escrever. O pedaço do nariz vem antes do P ou do B.",
    "objetivo2",
    [
        {"img": "lt_campo", "palavra": u"CAMPO", "pista": u"O lugar aberto onde o time do bairro joga bola.",
         "dic": u"Diga devagar: <b>CAM-PO</b>."},
        {"img": "lt_bomba", "palavra": u"BOMBA", "pista": u"A máquina que puxa a água do poço.",
         "dic": u"<b>BOM-BA</b>: escute a letra que fecha o primeiro pedaço."},
        {"img": "lt_tambor", "palavra": u"TAMBOR", "pista": u"O instrumento que a banda bate no desfile.",
         "dic": u"<b>TAM-BOR</b>."},
    ],
    extra={"ENUN": u"Escreva o nome da loja, letra por letra.",
           "FECHO": u"Os três nomes já podem ir para a placa!"}))

A(fase(
    "f07", "completar", u"O ANÚNCIO DO JORNAL",
    u"O jornal do bairro perdeu uma palavra de cada anúncio. Escolha a que fecha a frase.",
    u"Leia a frase inteira em voz alta antes de escolher — a palavra que falta tem que soar bem ali.",
    "objetivo2",
    [
        {"ante": u"Conserto de ", "dep": u" d'água, atendo no mesmo dia.", "cer": u"bomba",
         "out": [u"bonba", u"bomma"],
         "dic": u"Diga <b>bom-ba</b> e escolha a que tem a letra do nariz antes do B."},
        {"ante": u"Flores frescas ", "dep": u" na porta do mercado.", "cer": u"sempre",
         "out": [u"senpre", u"semppre"],
         "dic": u"<b>Sem-pre</b>: uma letra só antes do P."},
        {"ante": u"Aulas de ", "dep": u" para crianças, aos sábados.", "cer": u"tambor",
         "out": [u"tanbor", u"tambour"],
         "dic": u"É o instrumento que você bateu lá atrás: <b>tam-bor</b>."},
    ],
    extra={"ENUN": u"Toque na palavra que <b>completa</b> o anúncio.",
           "DEPOIS": u"Leia o anúncio inteiro antes de escolher.",
           "FECHO": u"Os três anúncios já podem ir para o jornal!"}))

A(fase(
    "f08", "caca-palavras", u"AS PALAVRAS DA VITRINE",
    u"Cinco palavras da vitrine se esconderam no quadro. Toque na primeira e na última letra de cada uma.",
    u"Todas as cinco têm a mesma letra antes do P ou do B. Procure por ela.",
    "objetivo2",
    [u"CAMPO", u"BOMBA", u"SEMPRE", u"TAMBOR", u"OMBRO"],
    extra={"TITULO": u"A VITRINE DAS PALAVRAS",
           "PALDEF": {u"CAMPO": u"Lugar aberto onde o time do bairro joga bola.",
                      u"BOMBA": u"Máquina que puxa a água do poço.",
                      u"SEMPRE": u"O contrário de nunca.",
                      u"TAMBOR": u"Instrumento que a banda bate no desfile.",
                      u"OMBRO": u"A parte do corpo onde a mochila se apoia."},
           "MODO": u"definicoes"}))

A(fase(
    "f09", "cruzadinha", u"A CRUZADINHA DO PINCEL",
    u"Cada dica é uma palavra que ele já pintou em alguma placa da cidade.",
    u"Se travar, lembre da placa onde você viu a palavra.",
    "objetivo2",
    [
        {"p": u"CAMPO", "ac": u"CAMPO", "r": 0, "c": 0, "pLin": 0, "pCol": 1, "n": 1,
         "d": u"Lugar aberto onde o time do bairro joga bola."},
        {"p": u"BOMBA", "ac": u"BOMBA", "r": 0, "c": 4, "pLin": 1, "pCol": 0, "n": 2,
         "d": u"Máquina que puxa a água do poço."},
        {"p": u"OMBRO", "ac": u"OMBRO", "r": 4, "c": 2, "pLin": 0, "pCol": 1, "n": 3,
         "d": u"A parte do corpo onde a mochila se apoia."},
    ],
    extra={"BANCO": u"ABCMOPRSU"}))

A(fase(
    "f10", "forca", u"A PLACA COBERTA",
    u"O pano cobriu a placa nova. Descubra a palavra letra por letra.",
    u"Comece pelas vogais: elas aparecem em quase toda palavra.",
    "objetivo2",
    [
        {"p": u"TAMBEM", "ac": u"TAMBÉM", "d": u"A palavra que a gente usa para dizer 'eu faço isso também'."},
        {"p": u"CAMPEAO", "ac": u"CAMPEÃO", "d": u"Quem ganhou o campeonato de futebol do bairro."},
        {"p": u"BOMBEIRO", "ac": u"BOMBEIRO", "d": u"Quem apaga o incêndio e ajuda na enchente."},
    ]))

A(fase(
    "f11", "memoria", u"A PALAVRA E A FIGURA",
    u"Ache o par: de um lado a palavra, do outro a figura dela.",
    u"Toque no alto-falante da carta para ouvir a palavra antes de decidir.",
    "objetivo2",
    [
        {"k": "campo", "pal": u"CAMPO", "fig": "lt_campo", "sen": u"o campo de futebol do bairro", "figsen": "lt_campo"},
        {"k": "bomba", "pal": u"BOMBA", "fig": "lt_bomba", "sen": u"a bomba que puxa a água", "figsen": "lt_bomba"},
        {"k": "tambor", "pal": u"TAMBOR", "fig": "lt_tambor", "sen": u"o tambor da banda", "figsen": "lt_tambor"},
        {"k": "lampada", "pal": u"LÂMPADA", "fig": "lt_lampada", "sen": u"a lâmpada do poste", "figsen": "lt_lampada"},
        {"k": "pomba", "pal": u"POMBA", "fig": "lt_pomba", "sen": u"a pomba da praça", "figsen": "lt_pomba"},
    ]))

# ⚠️ REVISÃO ESPAÇADA (Roediger, Bjork) no MEIO, não no fim. Não é enchimento:
#    é o que faz a criança levar a coisa para a semana que vem.
A(fase(
    "aquecimento", "relampago", u"AQUECIMENTO DA OFICINA",
    u"Antes da segunda metade, o Pincel confere o que você já pegou. Nada novo aqui — é tudo o que já passou.",
    u"Vá rápido: você já respondeu coisas assim.",
    "objetivo2",
    [
        {"p": u"CA_PO — que letra entra?", "c": u"M", "e": [u"N", u"NH"]},
        {"p": u"BO_BA — que letra entra?", "c": u"M", "e": [u"N", u"MB"]},
        {"p": u"SE_PRE — que letra entra?", "c": u"M", "e": [u"N", u"MP"]},
        {"p": u"O_BRO — que letra entra?", "c": u"M", "e": [u"N", u"MB"]},
        {"p": u"TA_BOR — que letra entra?", "c": u"M", "e": [u"N", u"NB"]},
        {"p": u"CA_PEÃO — que letra entra?", "c": u"M", "e": [u"N", u"MP"]},
    ]))


# ==========================================================================
# BLOCO 2 — A OUTRA LETRA (objetivo3)
#
# ⚠️ SEM ESTE BLOCO A REGRA NÃO EXISTE. Uma regra que só tem um lado vira
#    "ponha M em tudo": a criança sai daqui escrevendo CAMTO e MAMGA. O
#    contraste é o que dá contorno — e é por isso que o N vem logo depois do
#    M, e não numa aula de outro dia.
# ==========================================================================

A(fase(
    "f11", "letras-escondidas", u"CUIDADO: NEM TODA PLACA PEDE M",
    u"Estas placas são de outras ruas. Leve a letra certa até o buraco — e desta vez olhe bem o que vem depois dele.",
    u"Fale a palavra em voz alta e escute a letra que vem DEPOIS do buraco.",
    "objetivo3",
    [
        {"pal": u"PONTE", "esc": u"PO_TE", "extra": ["M", "R"], "img": "lt_ponte", "voz": u"ponte",
         "d": [u"<b>Pon-te</b>: o nariz treme igual. Mas olhe a letra depois do buraco.",
               u"Depois do buraco vem <b>T</b>, e não P nem B.",
               u"É o <b>N</b>. Ele está aceso."]},
        {"pal": u"CANTO", "esc": u"CA_TO", "extra": ["M", "L"], "img": "lt_canto", "voz": u"canto",
         "d": [u"<b>Can-to</b>. Que letra vem logo depois do buraco?",
               u"Vem <b>T</b>. E antes de T não mora o M.",
               u"É o <b>N</b>."]},
        {"pal": u"MANGA", "esc": u"MA_GA", "extra": ["M", "S"], "img": "lt_manga", "voz": u"manga",
         "d": [u"<b>Man-ga</b>: a fruta do quintal.",
               u"Depois do buraco vem <b>G</b>.",
               u"É o <b>N</b>."]},
        {"pal": u"VENTO", "esc": u"VE_TO", "extra": ["M", "C"], "img": "lt_vento", "voz": u"vento",
         "d": [u"<b>Ven-to</b>: o que balança as folhas.",
               u"Depois do buraco vem <b>T</b>.",
               u"É o <b>N</b>."]},
    ],
    extra={"LETXT": {"selo": u"A LETRA QUE FALTA",
                     "balao": u"Leve a <b>letra certa</b> até o buraco — olhe o que vem depois dele.",
                     "hint": u"Toque na letra, arraste, ou digite no teclado.",
                     "ouvir": u"a palavra",
                     "fecho": u"Estas placas eram de outra família!"}}))

A(fase(
    "f12", "classificar", u"AS DUAS GAVETAS DA OFICINA",
    u"O Pincel guarda os moldes em duas gavetas. Ponha cada palavra na gaveta dela.",
    u"Olhe a letra que vem DEPOIS do M ou do N. É ela que decide a gaveta.",
    "objetivo3",
    [
        {"k": "eme", "n": u"COM M<br>(antes de P e de B)", "img": ""},
        {"k": "ene", "n": u"COM N<br>(antes das outras)", "img": ""},
    ],
    extra={"ENUN": u"Toque na palavra e depois na gaveta certa.",
           "FICHAS": [
               {"t": u"CA_PO", "alvo": "eme", "img": ""},
               {"t": u"BO_BA", "alvo": "eme", "img": ""},
               {"t": u"SE_PRE", "alvo": "eme", "img": ""},
               {"t": u"PO_TE", "alvo": "ene", "img": ""},
               {"t": u"CA_TO", "alvo": "ene", "img": ""},
               {"t": u"MA_GA", "alvo": "ene", "img": ""},
           ],
           "DICAS": [
               u"Olhe a letra que vem logo depois do buraco.",
               u"Se depois do buraco vier <b>P</b> ou <b>B</b>, a palavra é da primeira gaveta. Qualquer outra letra, é da segunda.",
               u"A gaveta certa está com a borda acesa."]}))

A(fase(
    "f13", "intruso", u"A PLACA QUE NÃO É DA MESMA FAMÍLIA",
    u"Três destas palavras pedem a mesma letra. Ache a que não pertence ao grupo.",
    u"Não olhe o começo da palavra: olhe a letra que vem depois do M ou do N.",
    "objetivo3",
    [
        {"selo": u"O ARMÁRIO DOS MOLDES", "tipo": "texto",
         "enun": u"Três destas pedem a MESMA letra no buraco. <b>Qual não pertence?</b>",
         "itens": [{"k": "campo", "n": u"CA_PO", "img": ""},
                   {"k": "bomba", "n": u"BO_BA", "img": ""},
                   {"k": "ponte", "n": u"PO_TE", "img": ""},
                   {"k": "ombro", "n": u"O_BRO", "img": ""}],
         "fora": "ponte", "nomeFora": u"PO_TE",
         "d1": u"Leia cada uma e veja o que vem logo depois do buraco.",
         "d2": u"Três delas têm P ou B depois do buraco. Uma tem outra letra.",
         "d3": u"É <b>PO_TE</b>: depois do buraco vem T, então ali entra N.",
         "razoes": [
             {"t": u"Nas outras três vem P ou B depois; nesta vem T.", "ok": 1},
             {"t": u"Porque PO_TE é a palavra mais curta.", "ok": 0},
             {"t": u"Porque PO_TE começa com P.", "ok": 0}],
         "p1": u"E por que ela ficou de fora?"},
        {"selo": u"A SEGUNDA PRATELEIRA", "tipo": "texto",
         "enun": u"De novo: <b>qual não é da mesma família?</b>",
         "itens": [{"k": "canto", "n": u"CA_TO", "img": ""},
                   {"k": "manga", "n": u"MA_GA", "img": ""},
                   {"k": "sempre", "n": u"SE_PRE", "img": ""},
                   {"k": "vento", "n": u"VE_TO", "img": ""}],
         "fora": "sempre", "nomeFora": u"SE_PRE",
         "d1": u"Olhe só a letra depois do buraco de cada uma.",
         "d2": u"Três têm T ou G. Uma tem P.",
         "d3": u"É <b>SE_PRE</b>: antes de P entra M.",
         "razoes": [
             {"t": u"Nas outras três vem T ou G depois; nesta vem P.", "ok": 1},
             {"t": u"Porque SE_PRE tem seis letras.", "ok": 0},
             {"t": u"Porque SE_PRE começa com S.", "ok": 0}],
         "p1": u"E por que ela ficou de fora?"},
    ]))

A(fase(
    "f14", "filtro", u"A PENEIRA DA GRÁFICA",
    u"A gráfica só imprime o que está escrito certo. Deixe passar as certas e segure as erradas.",
    u"Leia cada ficha e confira a letra antes do P ou do B.",
    "objetivo3",
    [
        {"reg": u"Só passam as palavras <b>escritas certas</b>.",
         "curta": u"escrita certa",
         "fichas": [{"t": u"CAMPO", "ok": True}, {"t": u"SEMPRE", "ok": True},
                    {"t": u"BOMBA", "ok": True}, {"t": u"CANPO", "ok": False},
                    {"t": u"SENPRE", "ok": False}, {"t": u"BONBA", "ok": False}],
         "d1": u"Fale a palavra e olhe a letra antes do P ou do B.",
         "d2": u"Olhe CAMPO: antes do P está o M. Essa passa.",
         "d3": u"As que ainda passam estão com a moldura acesa: "},
        {"reg": u"Agora só passam as que pedem <b>N</b> no lugar do buraco.",
         "curta": u"pede N",
         "fichas": [{"t": u"PO_TE", "ok": True}, {"t": u"CA_TO", "ok": True},
                    {"t": u"VE_TO", "ok": True}, {"t": u"CA_PO", "ok": False},
                    {"t": u"O_BRO", "ok": False}, {"t": u"BO_BA", "ok": False}],
         "d1": u"Olhe a letra logo depois do buraco.",
         "d2": u"Se vier P ou B, a palavra pede M — essa fica de fora.",
         "d3": u"As que ainda passam estão acesas: "},
    ]))

A(fase(
    "f15", "ligar", u"CADA PALAVRA COM O SEU MOTIVO",
    u"Ligue a palavra ao motivo de ela levar aquela letra.",
    u"O motivo está sempre na letra que vem DEPOIS.",
    "objetivo3",
    [
        {"k": "p0", "t": u"CAMPO", "s": u"leva M porque depois vem P"},
        {"k": "p1", "t": u"BOMBA", "s": u"leva M porque depois vem B"},
        {"k": "p2", "t": u"CANTO", "s": u"leva N porque depois vem T"},
        {"k": "p3", "t": u"MANGA", "s": u"leva N porque depois vem G"},
    ],
    extra={"ENUN": u"Toque na palavra e depois no motivo dela.",
           "FECHO": u"Cada palavra com o seu motivo!",
           "DICAS": [u"Leia a palavra e veja que letra vem depois do M ou do N.",
                     u"P e B pedem M. As outras letras pedem N.",
                     u"O par certo está aceso."]}))

A(fase(
    "f16", "quem-sou-eu", u"A PLACA MISTERIOSA",
    u"O Pincel guardou uma placa embrulhada. Descubra qual é — cada pista conta mais.",
    u"Quanto menos pista você usar, mais estrela ganha.",
    "objetivo3",
    [
        {"resp": u"BOMBEIRO",
         "pistas": [u"Eu tenho <b>duas letras juntas</b> no meio: uma delas é o M.",
                    u"Eu apareço na enchente e no incêndio, sempre de <b>vermelho</b>.",
                    u"O meu nome começa igual ao de <b>BOMBA</b>."],
         "outros": [u"BONBEIRO", u"PADEIRO", u"PEDREIRO"]},
        {"resp": u"CAMPEÃO",
         "pistas": [u"Eu levo <b>M antes do P</b>, como CAMPO.",
                    u"Eu ganhei o campeonato do bairro.",
                    u"O meu nome termina com <b>-ÃO</b>."],
         "outros": [u"CANPEÃO", u"CORREDOR", u"TORCEDOR"]},
    ]))

# ==========================================================================
# BLOCO 3 — CAÇAR O ERRO NO TEXTO DE VERDADE (objetivo4)
#
# ⚠️ Aqui a palavra sai da lista e entra no TEXTO. Acertar palavra solta é uma
#    coisa; achar o erro no meio de um cartaz que a criança está lendo por
#    outro motivo é outra — e é essa a que serve para a vida.
# ==========================================================================

A(fase(
    "f18", "conserte-o-erro", u"O CARDÁPIO DA LANCHONETE",
    u"O cardápio foi impresso com um erro em cada linha. Ache e conserte.",
    u"Leia a linha inteira antes de escolher o pedaço.",
    "objetivo4",
    [
        {"selo": u"LANCHONETE DA PRAÇA", "cab": u"CARDÁPIO DA SEMANA",
         "bal": u"Uma palavra desta linha está errada. Ache e conserte.",
         "pecas": [u"SUCO", u"DE", u"MANGA", u"SENPRE", u"GELADO"], "erro": 3, "certa": u"SEMPRE",
         "ops": [u"SEMPRE", u"SENPRE", u"SEMPRI"],
         "por": u"É <b>SEMPRE</b>: antes de P vem M. E repare que MANGA está certa, com N.",
         "dicas": [u"Leia a linha baixinho, palavra por palavra.",
                   u"Duas palavras têm o som do nariz. Só uma está errada.",
                   u"Era esta: eu marquei para você."],
         "dicas2": [u"Fale <b>sem-pre</b> e escute a letra antes do P.",
                    u"Antes de P e de B a letra é sempre a mesma.",
                    u"Era <b>SEMPRE</b>. Troquei para você ver."]},
        {"selo": u"LANCHONETE DA PRAÇA", "cab": u"A SEGUNDA LINHA",
         "bal": u"Nesta linha também tem uma palavra trocada.",
         "pecas": [u"PASTEL", u"DE", u"CANPO", u"COM", u"QUEIJO"], "erro": 2, "certa": u"CAMPO",
         "ops": [u"CAMPO", u"CANPO", u"CAMPU"],
         "por": u"É <b>CAMPO</b>, com M antes do P.",
         "dicas": [u"Uma palavra tem o som do nariz antes do P.",
                   u"É a terceira palavra da linha.",
                   u"Marquei para você: agora escolha a certa."],
         "dicas2": [u"O fim da palavra é <b>-PO</b>. O que muda é a letra antes do P.",
                    u"Antes de P mora o M.",
                    u"Era <b>CAMPO</b>."]},
    ]))

A(fase(
    "f17", "pintar", u"O CARTAZ DA FESTA",
    u"Este cartaz vai para o mural da escola. Pinte as palavras que estão escritas <b>erradas</b>.",
    u"Leia o cartaz inteiro em voz alta. Onde a sua boca faz o som do nariz antes de P ou B, tem que ter M.",
    "objetivo4",
    [
        {"t": u"A festa do bairro vai ter "}, {"p": u"CANPO", "alvo": 1},
        {"t": u" de futebol, banda com "}, {"p": u"TAMBOR"},
        {"t": u" e comida "}, {"p": u"SENPRE", "alvo": 1},
        {"t": u" quentinha. Traga o guarda-chuva: o "}, {"p": u"TEMPO"},
        {"t": u" pode virar. Os "}, {"p": u"BONBEIROS", "alvo": 1},
        {"t": u" vão estar na entrada, e a "}, {"p": u"PONTE"},
        {"t": u" fica aberta até tarde."},
    ],
    extra={"CATEG": u"as palavras ERRADAS"}))

A(fase(
    "f19", "juntar-silabas", u"OS PEDAÇOS NO CHÃO DA OFICINA",
    u"O molde da palavra caiu e os pedaços se espalharam. Junte na ordem certa.",
    u"Diga a palavra devagar: qual pedaço a boca fala primeiro?",
    "objetivo4",
    [
        {"pal": u"CAMPEÃO", "sil": ["CAM", "PE", u"ÃO"], "img": "lt_campeao",
         "iscas": ["CAN", "PO"], "lento": u"CAM... PE... ÃO",
         "d": [u"Fale devagar: qual pedaço vem primeiro?",
               u"O primeiro pedaço tem o som do nariz e termina em M.",
               u"É o <b>CAM</b>: ele está aceso."]},
        {"pal": u"BOMBEIRO", "sil": ["BOM", "BEI", "RO"], "img": "lt_bombeiro",
         "iscas": ["BON", "BA"], "lento": u"BOM... BEI... RO",
         "d": [u"Qual pedaço a boca fala primeiro?",
               u"Antes do B do segundo pedaço mora o M.",
               u"É o <b>BOM</b>."]},
        {"pal": u"LÂMPADA", "sil": [u"LÂM", "PA", "DA"], "img": "lt_lampada",
         "iscas": [u"LÃN", "TA"], "lento": u"LÂM... PA... DA",
         "d": [u"Diga <b>LÂM-PA-DA</b> devagar.",
               u"O primeiro pedaço leva chapéu no A e termina em M.",
               u"É o <b>LÂM</b>."]},
    ],
    extra={"SILTXT": {"selo": u"JUNTE OS PEDAÇOS",
                      "balao": u"Junte os pedaços e forme a palavra da <b>figura</b>.",
                      "hint": u"Toque no pedaço certo. Ele escorrega até a forma.",
                      "ouvir": u"a palavra",
                      "pedacos": u"em pedaços"}}))

A(fase(
    "f20", "caca-palavras", u"AS PALAVRAS DA OUTRA RUA",
    u"Cinco palavras se esconderam no quadro — e nenhuma delas leva M. Toque na primeira e na última letra de cada uma.",
    u"Todas estas pedem N: olhe a letra que vem depois.",
    "objetivo4",
    [u"PONTE", u"CANTO", u"MANGA", u"VENTO", u"BANCO"],
    extra={"TITULO": u"O QUADRO DA OUTRA RUA",
           "PALDEF": {u"PONTE": u"Passa por cima do rio e liga um lado ao outro.",
                      u"CANTO": u"O lugar onde duas paredes se encontram.",
                      u"MANGA": u"Fruta amarela e doce do quintal.",
                      u"VENTO": u"Você não vê, mas ele balança as folhas.",
                      u"BANCO": u"Onde a gente senta na praça."},
           "MODO": u"definicoes"}))

A(fase(
    "f21", "montar-frase", u"O SLOGAN DA LOJA",
    u"Monte a frase que vai embaixo do nome da loja.",
    u"Comece pela palavrinha que abre a frase.",
    "objetivo4",
    [
        {"w": [u"O", u"campo", u"sempre", u"aberto"], "c": ["art", "sub", "adv", "adj"], "apoio": True},
        {"w": [u"A", u"bomba", u"chegou", u"hoje"], "c": ["art", "sub", "ver", "adv"], "apoio": False},
        {"w": [u"O", u"tambor", u"tocou", u"ontem"], "c": ["art", "sub", "ver", "adv"], "apoio": False},
    ],
    extra={"CLA": {
        "art": {"r": u"o / a", "d": u"a palavrinha <b>o</b> ou <b>a</b>, que abre a frase"},
        "sub": {"r": u"nome", "d": u"o <b>nome</b> da coisa que está na placa"},
        "adj": {"r": u"como é", "d": u"<b>como</b> a coisa é"},
        "ver": {"r": u"ação", "d": u"o que a coisa <b>fez</b>"},
        "adv": {"r": u"quando", "d": u"<b>quando</b> aconteceu"}},
        "FORMAS": ["art", "sub", "adj", "ver", "adv"]}))

A(fase(
    "f22", "escrever-legenda", u"A FOTO DA PLACA PRONTA",
    u"O Pincel fotografou a placa consertada. Escreva a legenda da foto.",
    u"Diga o que tem na foto e como está. As palavras de apoio entram com um toque.",
    "objetivo4",
    [
        {"img": "lt_placa_pronta", "sel": u"FOTO 1 DE 2",
         "ped": u"Escreva a legenda desta foto: <b>o que</b> tem e <b>como</b> ficou.",
         "apoio": [u"a placa", u"da padaria", u"com M", u"escrita certa", u"na Rua XV", u"nova"],
         "comeco": u"A placa da padaria ficou ",
         "exemplo": u"a placa da padaria ficou escrita certa com m"},
        {"img": "lt_placa_ponte", "sel": u"FOTO 2 DE 2",
         "ped": u"E esta, da placa da ponte: <b>o que</b> tem e <b>como</b> ficou?",
         "apoio": [u"a placa", u"da ponte", u"com N", u"escrita certa", u"perto do rio", u"grande"],
         "comeco": u"A placa da ponte ficou ",
         "exemplo": u"a placa da ponte ficou escrita certa com n"},
    ]))

# ==========================================================================
# BLOCO 4 — ESCREVER SOZINHO, E SÓ ENTÃO A REGRA (objetivo5)
# ==========================================================================

A(fase(
    "f26", "digitar", u"O LETREIRO GRANDE",
    u"As últimas placas da rua. Escreva o nome de cada uma.",
    u"Fale a palavra antes de escrever e olhe a letra que vem depois do som do nariz.",
    "objetivo5",
    [
        {"img": "lt_bombeiro", "palavra": u"BOMBEIRO", "pista": u"Quem apaga o incêndio e ajuda na enchente.",
         "dic": u"<b>BOM-BEI-RO</b>: antes do segundo B vem M."},
        {"img": "lt_ponte", "palavra": u"PONTE", "pista": u"Passa por cima do rio e liga um lado ao outro.",
         "dic": u"<b>PON-TE</b>: depois vem T, então não é M."},
        {"img": "lt_lampada", "palavra": u"LAMPADA", "pista": u"Acende no poste quando escurece.",
         "dic": u"<b>LAM-PA-DA</b>: antes do P vem M."},
    ],
    extra={"ENUN": u"Escreva o nome da placa, letra por letra.",
           "FECHO": u"As três placas grandes ficaram prontas!"}))

A(fase(
    "f23", "ditado", u"O PINCEL DITA A PLACA",
    u"Ele fala, você escreve. Pode usar o teclado da tela ou o de verdade.",
    u"Repita a palavra baixinho antes de escrever.",
    "objetivo5",
    [
        {"id": "lt_dit1", "txt": u"CAMPO", "dic": u"Diga baixinho: <b>CAM-PO</b>."},
        {"id": "lt_dit2", "txt": u"PONTE", "dic": u"Diga baixinho: <b>PON-TE</b>. Olhe a letra depois do buraco."},
        {"id": "lt_dit3", "txt": u"BOMBEIRO", "dic": u"São três pedaços: <b>BOM-BEI-RO</b>."},
    ],
    extra={"SOBRA": u"HJKQWXYZ", "ESPERA": u"&#9679; &#9679; &#9679;"}))

A(fase(
    "f24", "autoexplicacao", u"POR QUE VOCÊ ESCREVEU ASSIM?",
    u"Escolha a placa certa — e depois conte por que ela é a certa.",
    u"Não é decorar: é dizer o que você olhou para decidir.",
    "objetivo5",
    [
        {"selo": u"A PLACA DA ACADEMIA",
         "tarefa": u"A academia quer a palavra OMBRO na placa. <b>Qual</b> está certa?",
         "dicas": [u"Fale a palavra e escute a letra antes do B.",
                   u"Risquei uma que não serve. Sobrou a que tem a letra certa antes do B."],
         "esc": [{"img": "lt_ombro", "r": u"OMBRO", "c": True},
                 {"img": "lt_ombro", "r": u"ONBRO", "c": False},
                 {"img": "lt_ombro", "r": u"OMBRU", "c": False}],
         "pq": u"Deu certo! Mas <b>por que</b> essa é a certa?",
         "perguntas": [u"Que letra vem depois do buraco nessa palavra?",
                       u"E quando vem P ou B, que letra entra antes?"],
         "cards": [{"t": u"Porque depois vem <b>B</b>, e antes de B entra M.", "c": True},
                   {"t": u"Porque a palavra é grande.", "c": False},
                   {"t": u"Porque eu decorei essa palavra.", "c": False}]},
    ]))

# ⭐ AQUI, E SÓ AQUI, A REGRA VIRA PALAVRA. A criança já consertou 20 placas;
#    agora ela ENSINA o Pincel, e ele age com a regra que ela deu — se ela der
#    a errada, ele pinta errado na frente dela. É o conceito por ÚLTIMO, e
#    saindo da boca dela, não da minha.
A(fase(
    "f25", "ensinar-mascote", u"ENSINE A REGRA AO PINCEL",
    u"O Pincel vai pintar sozinho a próxima placa. Ensine a ele a regra que você usou o tempo todo.",
    u"Pense no que você olhou em cada palavra antes de escolher a letra.",
    "objetivo5",
    [
        {"sel": u"A PLACA DO CAMPO",
         "prob": u"O Pincel tem que pintar <b>CA_PO</b> e não sabe que letra pôr. <b>Ensine</b> a regra a ele.",
         "se": u"SE depois do buraco vem P ou B, ENTÃO eu ponho...",
         "regras": [
             {"t": u"a letra <b>M</b>", "cai": "M", "ok": 1},
             {"t": u"a letra <b>N</b>", "cai": "N", "ok": 0, "deixa": "monte"},
             {"t": u"as duas, <b>MN</b>", "cai": "MN", "ok": 0, "deixa": "monte"},
             {"t": u"nenhuma, deixo o buraco", "cai": "", "ok": 0}],
         "bom": u"Ficou <b>CAMPO</b>! A dona da padaria já pode pendurar.",
         "porque": u"Olhe a placa: com essa letra a palavra não fica igual à que a gente fala.",
         "d": [u"Pense no que você olhou nas outras placas antes de escolher.",
               u"Depois do buraco vem <b>P</b>. Que letra você pôs nesses casos?",
               u"A regra do <b>M</b> está acesa: toque nela para ensinar o Pincel."]},
        {"sel": u"A PLACA DA PONTE",
         "prob": u"Agora ele tem que pintar <b>PO_TE</b>. <b>Ensine</b> a regra desta.",
         "se": u"SE depois do buraco vem outra letra, ENTÃO eu ponho...",
         "regras": [
             {"t": u"a letra <b>N</b>", "cai": "N", "ok": 1},
             {"t": u"a letra <b>M</b>", "cai": "M", "ok": 0, "deixa": "monte"},
             {"t": u"a letra <b>H</b>", "cai": "H", "ok": 0, "deixa": "monte"}],
         "bom": u"Ficou <b>PONTE</b>! A placa já está no lugar.",
         "porque": u"Leia o que ficou escrito: é assim que a gente fala?",
         "d": [u"Olhe a letra que vem depois do buraco desta palavra.",
               u"Vem <b>T</b> — e antes de T não mora o M.",
               u"A regra do <b>N</b> está acesa: toque nela."]},
    ]))

A(fase(
    "f27", "escolher", u"A PROVA FINAL DA GRÁFICA",
    u"Última conferência antes de imprimir tudo. Escolha a placa certa.",
    u"Agora você já sabe olhar: veja a letra que vem depois.",
    "objetivo5",
    [
        {"p": u"A placa da farmácia. Qual está certa?",
         "c": u"SEMPRE ABERTA", "e": [u"SENPRE ABERTA", u"SEMPRE ABERTHA"],
         "d": [u"Fale <b>sem-pre</b>.", u"Depois do buraco vem P.", u"É <b>SEMPRE ABERTA</b>."]},
        {"p": u"A placa do mercado da esquina. Qual está certa?",
         "c": u"MANGA DO DIA", "e": [u"MAMGA DO DIA", u"MANGUA DO DIA"],
         "d": [u"Fale <b>man-ga</b>.", u"Depois do buraco vem G, e não P nem B.", u"É <b>MANGA DO DIA</b>."]},
        {"p": u"A placa da loja de música. Qual está certa?",
         "c": u"TAMBOR E TROMBONE", "e": [u"TANBOR E TRONBONE", u"TAMBOR E TROMBÔNE"],
         "d": [u"São duas palavras com a mesma família.",
               u"Nas duas, depois do buraco vem B.",
               u"É <b>TAMBOR E TROMBONE</b>."]},
    ],
    extra={"TITULO": u"A ÚLTIMA PROVA", "FECHO": u"A gráfica pode imprimir!"}))

A(fase(
    "f28", "relampago", u"RELÂMPAGO DA OFICINA",
    u"Rápido: M ou N? Sem dica e sem pressa no fim — vá pelo que você já sabe.",
    u"Olhe a letra que vem depois do buraco.",
    "objetivo5",
    [
        {"p": u"LI_PO", "c": u"M", "e": [u"N"]},
        {"p": u"MU_DO", "c": u"N", "e": [u"M"]},
        {"p": u"SO_BRA", "c": u"M", "e": [u"N"]},
        {"p": u"DE_TE", "c": u"N", "e": [u"M"]},
        {"p": u"TE_PO", "c": u"M", "e": [u"N"]},
        {"p": u"BA_CO", "c": u"N", "e": [u"M"]},
        {"p": u"O_BRO", "c": u"M", "e": [u"N"]},
        {"p": u"O_TEM", "c": u"N", "e": [u"M"]},
    ]))

A(fase(
    "f29", "completar", u"A CARTA DA DONA DA PADARIA",
    u"Ela escreveu para agradecer, mas o papel borrou em três lugares. Complete.",
    u"Leia a frase inteira antes de escolher.",
    "objetivo5",
    [
        {"ante": u"A minha placa ficou pronta e eu ", "dep": u" vou lembrar de vocês.",
         "cer": u"sempre", "out": [u"senpre", u"sempri"],
         "dic": u"Depois do buraco vem P."},
        {"ante": u"Agora todo mundo acha a padaria, até quem vem da outra ",
         "dep": u" do rio.", "cer": u"ponte", "out": [u"pomte", u"pontte"],
         "dic": u"Depois do buraco vem T."},
        {"ante": u"O time do ", "dep": u" já veio comprar pão duas vezes.",
         "cer": u"campo", "out": [u"canpo", u"campu"],
         "dic": u"Depois do buraco vem P."},
    ],
    extra={"ENUN": u"Toque no pedaço que <b>completa</b> a frase da carta.",
           "DEPOIS": u"Leia a frase inteira antes de escolher.",
           "FECHO": u"A carta ficou inteira!"}))

A(fase(
    "f30", "memoria", u"O ARQUIVO DA OFICINA",
    u"Ache o par: de um lado a palavra, do outro o motivo da letra dela.",
    u"Toque no alto-falante da carta para ouvir a palavra.",
    "objetivo3",
    [
        {"k": "campo", "pal": u"CAMPO", "fig": "lt_campo", "sen": u"M, porque depois vem P", "figsen": "lt_campo"},
        {"k": "ombro", "pal": u"OMBRO", "fig": "lt_ombro", "sen": u"M, porque depois vem B", "figsen": "lt_ombro"},
        {"k": "ponte", "pal": u"PONTE", "fig": "lt_ponte", "sen": u"N, porque depois vem T", "figsen": "lt_ponte"},
        {"k": "manga", "pal": u"MANGA", "fig": "lt_manga", "sen": u"N, porque depois vem G", "figsen": "lt_manga"},
    ]))

A(fase(
    "f31", "ouvir-achar", u"O PEDIDO POR TELEFONE",
    u"O cliente ligou e falou o nome da loja. Ouça e toque na placa certa.",
    u"Pode apertar o botão de ouvir quantas vezes quiser.",
    "objetivo1",
    [
        {"selo": u"OUÇA E ACHE", "alvo": "campo", "opcoes": ["campo", "canto", "ponte", "bomba"],
         "rotulo": u"A PALAVRA É", "escrito": u"CAMPO", "fala": u"campo",
         "enun": u"Ouça a palavra e toque na <b>placa</b> dela.",
         "hint": u"Sem som no computador? A palavra está escrita aí em cima.",
         "msg": u"Isso! <b>CAMPO</b> leva M porque depois vem P.",
         "dicas": [u"Aperte <b>Ouvir</b> de novo e diga a palavra junto, devagar.",
                   u"A palavra começa com <b>CA</b> e tem P no meio.",
                   u"É esta: a placa do <b>CAMPO</b> de futebol."]},
        {"selo": u"OUÇA E ACHE", "alvo": "ponte", "opcoes": ["ponte", "bomba", "campo", "manga"],
         "rotulo": u"A PALAVRA É", "escrito": u"PONTE", "fala": u"ponte",
         "enun": u"Ouça a palavra e toque na <b>placa</b> dela.",
         "hint": u"Sem som no computador? A palavra está escrita aí em cima.",
         "msg": u"Isso! <b>PONTE</b> leva N porque depois vem T.",
         "dicas": [u"Aperte <b>Ouvir</b> de novo e escute o fim da palavra.",
                   u"Ela começa com <b>PO</b> e tem T no meio.",
                   u"É esta: a placa da <b>PONTE</b> sobre o rio."]},
    ],
    extra={"CATALOGO": {
        "campo": {"nome": u"CAMPO", "voz": u"campo"},
        "canto": {"nome": u"CANTO", "voz": u"canto"},
        "ponte": {"nome": u"PONTE", "voz": u"ponte"},
        "bomba": {"nome": u"BOMBA", "voz": u"bomba"},
        "manga": {"nome": u"MANGA", "voz": u"manga"}},
        "TEXTOS": {"ouvir": u"OUVIR A PALAVRA",
                   "ouvirDica": u"Pode apertar quantas vezes quiser.",
                   "ouvirLeitor": u"Ouvir a palavra de novo"}}))

# ⚠️ A ÚLTIMA FASE É A PLACA DO MORRO — a que o fecho promete. Ela existe para
#    a criança sair com a mão coçando, não com a sensação de prova terminada.
A(fase(
    "f32", "conserte-o-erro", u"A PLACA DO MORRO DO AIPIM",
    u"A maior placa da cidade, aquela que se vê de longe. Ela tem um erro só — e ele engana até adulto.",
    u"Leia devagar. Uma das palavras tem o som do nariz e não é o que parece.",
    "objetivo5",
    [
        {"selo": u"MORRO DO AIPIM", "cab": u"A PLACA DO MIRANTE",
         "bal": u"Ache o pedaço errado desta placa e conserte.",
         "pecas": [u"MIRANTE", u"SENPRE", u"ABERTO", u"AO", u"VENTO"], "erro": 1, "certa": u"SEMPRE",
         "ops": [u"SEMPRE", u"SENPRE", u"SEMPRI"],
         "por": u"É <b>SEMPRE</b>, com M. Repare que MIRANTE e VENTO estão certas com N — e agora você sabe dizer por quê.",
         "dicas": [u"Três palavras aqui têm o som do nariz. Só uma está errada.",
                   u"Olhe a letra que vem depois em cada uma delas.",
                   u"Era esta: marquei para você."],
         "dicas2": [u"Depois do buraco vem <b>P</b>.",
                    u"E antes de P mora sempre a mesma letra.",
                    u"Era <b>SEMPRE</b>."]},
    ]))



def escreve():
    c = {
        "titulo": u"O Letreiro de Blumenau",
        "sub": u"Língua Portuguesa · 5º ano · escrever certo o M antes de P e B",
        "ano": u"5º ano",
        "prefixo": "lt",
        "mascote": "pincel",
        "mascoteNome": u"Pincel",
        "voz": "masculina",
        "crachas": 6,
        "fundo": "lt_fundo.png",
        "convite": u"<b>Quem vai pintar</b> hoje?",
        # ⚠️ A ABERTURA É O PORTÃO 0. Ela não anuncia conteúdo nenhum: entrega um
        #    problema da cidade e um pedido de socorro. A regra só nasce na f30.
        "abertura": u"O ajudante novo do Pincel pintou dezoito placas da Rua XV em um dia só — e trocou uma letra em quase todas. A padaria virou PADARIA CANPO BOM, a floricultura virou FLORES SENPRE VIVAS, e a cidade inteira está lendo errado. O Pincel já tem a tinta na mão, mas ficou com uma dúvida: qual letra é a certa? Conserte as placas com ele.",
        "fim": u"Rua XV inteira consertada — e olhe o que aconteceu: você acertou a letra antes de saber a regra, só de escutar a palavra. Ficou faltando uma placa, a maior de todas, lá no alto do Morro do Aipim. O Pincel diz que essa tem uma palavra que engana até adulto. Quer ver qual é?",
        "mesa": u"PEDAGOGO (até o 5º ano quem manda na mesa é o pedagogo, ver _padrao/RECEITA.md), com o ROTEIRISTA, o GAME DESIGNER, o DIRETOR DE ARTE e o ENGENHEIRO. Habilidade extraída do _curriculo/blumenau.txt (5º ano, Língua Portuguesa, Análise linguística/semiótica — ortografização).",
        "conceitos": {
            "objetivo1": u"O som que sai pelo nariz",
            "objetivo2": u"Antes de P e de B mora o M",
            "objetivo3": u"Antes das outras letras vem o N",
            "objetivo4": u"Caçar o erro no letreiro",
            "objetivo5": u"Pintar o letreiro certo",
        },
        "curriculo": {
            "objetivo1": u"Grafar palavras utilizando regras de correspondência fonema-grafema regulares, contextuais e morfológicas",
            "objetivo2": u"Grafar palavras utilizando regras de correspondência fonema-grafema regulares, contextuais e morfológicas",
            "objetivo3": u"Grafar palavras utilizando regras de correspondência fonema-grafema regulares, contextuais e morfológicas",
            "objetivo4": u"Grafar palavras utilizando regras de correspondência fonema-grafema regulares, contextuais e morfológicas",
            "objetivo5": u"Grafar palavras utilizando regras de correspondência fonema-grafema regulares, contextuais e morfológicas",
        },
        "fases": FASES,
    }
    # ⚠️ O ID DA FASE SE NUMERA SOZINHO, POR POSICAO. Escrito a mao, ele
    #    duplicou no primeiro remanejamento (duas fases `f11`) — e id repetido
    #    faz DUAS fases dividirem a mesma gravacao de voz, que foi um defeito
    #    ja pago no Jardim do Broto. Quem manda e a ORDEM, e a ordem o
    #    computador sabe contar melhor do que eu.
    n = 0
    for f in FASES:
        if f["id"] == "aquecimento":
            continue
        n += 1
        f["id"] = "f%02d" % n

    cam = os.path.join(RAIZ, "conteudo.json")
    io.open(cam, "w", encoding="utf-8").write(
        json.dumps(c, ensure_ascii=False, indent=1))
    print(u"escrito: %s (%d fases)" % (cam, len(FASES)))


if __name__ == "__main__":
    escreve()

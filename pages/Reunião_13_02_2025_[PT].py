import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from PIL import Image

st.set_page_config(page_title="Análise da Reunião", layout="wide")

row = st.columns(1)

row = st.columns(2)
row[0].image("logo.png", width=150)

st.write("")
st.write("")
st.write("")



st.title("📊 Análise da Reunião (13-02-2025)")

st.write("")
st.write("##### Participantes: <span style='font-weight:normal;'>André Neiva, Daniel Furtado, Francisco Falcão, Rita.</span>", unsafe_allow_html=True)
st.write("##### Duração: <span style='font-weight:normal;'>11:35 - 12:57 (92 minutos)</span>", unsafe_allow_html=True)


st.write("")

st.header("🎯 Objetivos", divider="gray")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Apresentação do sistema de transcrição automática<span style='font-weight:normal;'> e a sua aplicabilidade em formações e reuniões.</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✔️ Objetivo Atingido: <span style='font-weight:normal;'>Sim, foi demonstrado como a ferramenta funciona em tempo real e como os relatórios podem ser gerados automaticamente.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Exploração da análise do engagement<span style='font-weight:normal;'> dos formandos e o impacto no processo de aprendizagem.</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✔️ Objetivo Atingido: <span style='font-weight:normal;'>Sim, foram apresentados gráficos e métricas que mostram como a participação pode ser avaliada e melhorada.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Discussão sobre privacidade e conformidade legal<span style='font-weight:normal;'> no tratamento dos dados dos participantes.</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✔️ Objetivo Atingido: <span style='font-weight:normal;'>Sim, foram discutidas formas de anonimizar os dados e garantir a conformidade com as regulamentações.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Apresentação de melhorias futuras<span style='font-weight:normal;'> para a otimização da interface e experiência do utilizador.</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✔️ Objetivo Atingido: <span style='font-weight:normal;'>Sim, foi identificado que ajustes na interface são necessários para melhor usabilidade.</span>", unsafe_allow_html=True)


st.header("📊 Avaliação", divider="gray")

st.write("#### Classificação da Eficácia da Reunião: 87/100")

st.write("###### Critérios de Avaliação:")

dados = {
    "Critério": [
        "Cumprimento dos objetivos",
        "Clareza das discussões",
        "Tomada de decisões e atribuição de tarefas",
        "Engagement e participação dos membros",
        "Eficiência no tempo"
    ],
    "Peso (%)": [30, 20, 20, 15, 15],
    "Avaliação (0-100)": [95, 85, 90, 85, 80],
    "Justificação": [
        "Os principais objetivos foram cumpridos, incluindo a demonstração das funcionalidades do sistema.",
        "Houve clareza geral, embora alguns tópicos tenham sido debatidos extensivamente.",
        "As decisões foram bem distribuídas, mas algumas tarefas não tiveram prazos definidos.",
        "A participação foi ativa, com contribuições relevantes de diversos participantes.",
        "A reunião poderia ter sido um pouco mais objetiva em certos momentos."
    ]
}
df = pd.DataFrame(dados)

st.dataframe(df)  # Usa uma tabela interativa


st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Pontos Fortes:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Demonstração prática e clara do sistema.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Discussões produtivas sobre engagement e privacidade de dados.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Novas ideias surgiram para melhorar a experiência do utilizador.")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Pontos a Melhorar:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Algumas discussões poderiam ter sido mais objetivas.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Melhor definição de prazos para tarefas atribuídas.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Refinamento necessário na interface para uma usabilidade otimizada.")



st.write("")
st.write("")
st.write("")

st.header("📅 Temas Abordados", divider="gray")

def format_time(hour, minute):
    if (minute <  60):
        return f"{hour:02d}:{minute:02d}"
    else:
        return f"{hour+1:02d}:{minute-60:02d}"


start_hour, start_minute = 11, 35

themes = [
    (0, 7, "Introdução e chegada dos participantes.", [
        "Apresentação dos participantes.",
        "Explicação do objetivo da reunião.",
        "Referência à gravação e estrutura do relatório da reunião."
    ]),
    (7, 9, "Apresentação do relatório da reunião anterior.", [
        "Análise do relatório gerado automaticamente.",
        "Objetivos da reunião anterior e a sua eficácia.",
        "Identificação de melhorias e sugestões para melhoria." 
    ]),
    (9, 10, "Definição dos próximos passos e atribuição de tarefas.", [
        "Organização das ações a serem tomadas.",
        "Distribuição de responsabilidades entre os participantes.",
        "Importância da documentação de reuniões para futuras revisões."
    ]),
    (10, 11, "Discussão sobre a eficácia da formação e metodologias de ensino.", [
        "Como avaliar a qualidade das formações através de relatórios.",
        "Utilização da tecnologia para medir a participação e compreensão dos alunos.",
        "Benefícios de feedback estruturado para formadores e formandos."
    ]),

    (11, 12, "Análise do engagement e participação ativa.", [
        "Comparação do envolvimento dos participantes com base em métricas visuais e textuais.",
        "Identificação de momentos em que houve maior ou menor envolvimento.",
        "Importância de captar o interesse dos alunos durante as formações."
    ]),
    (12, 20, "Considerações sobre o uso da tecnologia na educação.", [
        "Aplicações da ferramenta em formações empresariais e desportivas.",
        "Possibilidades de integração com plataformas de ensino e gestão de aprendizagem.",
        "Benefícios de manter um histórico acessível das formações realizadas."
    ]),
    (20, 22, "Impacto da formação financiada e desafios de motivação.", [
        "Diferença entre formações obrigatórias e opcionais.",
        "Como a tecnologia pode garantir um melhor acompanhamento do processo de aprendizagem.",
        "Dificuldades em manter a atenção e motivação dos participantes."
    ]),
    (22, 29, "Gestão de acesso a materiais e certificação de formações.", [
        "Problemas enfrentados por entidades formadoras na disponibilização de conteúdos.",
        "Importância de um sistema integrado para armazenar informações de diferentes cursos.",
        "Comparação com plataformas como Moodle e outras soluções e-learning."
    ]),
    (29, 38, "Modelo de negócio para formação digital e plataforma centralizada.", [
        "Possibilidade de criação de um marketplace de formações.",
        "Como remunerar formadores e criar um sistema sustentável.",
        "Exemplo de um \"Spotify da Formação\", onde conteúdos poderiam ser acessados."
    ]),
    (38, 46, "Legalidade e autorizações necessárias para gravações e tratamento de dados.", [
        "Questões legais associadas à gravação e uso de dados dos participantes.",
        "Métodos para garantir conformidade com regulamentos de proteção de dados.",
        "Alternativas para anonimizar informações sensíveis."
    ]),
    (46, 52, "Integração da ferramenta em contextos académicos.", [
        "Potencial uso da tecnologia em universidades.",
        "Discussão sobre a possibilidade de parceria com a Universidade X.",
        "Benefícios da ferramenta para professores e alunos no ensino superior."
    ]),
    (52, 55, "Testes e implementação em formações reais.", [
        "Proposta para testar a ferramenta em formações práticas.",
        "Abordagem para garantir adesão dos formadores e alunos.",
        "Identificação de possíveis resistências e estratégias para superá-las."
    ]),
    (55, 82, "Reflexão final e próximos passos.", [
        "Conclusões sobre a reunião e planos de ação.",
        "Preparação do envio de um e-mail para a Universidade X.",
        "Discussão sobre estratégias de comunicação e apresentação da ferramenta."
    ])
]

for start, end, title, points in themes:
    start_time = format_time(start_hour, start_minute + start)
    end_time = format_time(start_hour, start_minute + end)
    st.write(f"##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 {title} <span style='font-weight:normal;'>({start_time} - {end_time})</span>", unsafe_allow_html=True)
    formatted_points = "".join([f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- {point}<br>" for point in points])
    st.write(f"""
        {formatted_points}
    """, unsafe_allow_html=True)


st.write("")
st.write("")
st.write("")

st.header("📝 Resumo",divider="gray")

st.text = """

A reunião teve início pontualmente às 11:35 da manhã, com a presença de André Neiva, Rita, Daniel Furtado e Francisco Falcão. 
André abriu a sessão explicando os objetivos centrais do encontro, que envolviam a apresentação dos modelos desenvolvidos pela equipa, a análise do relatório da reunião anterior e a discussão de melhorias para a automatização dos processos. 
Ele também salientou a importância de capturar dados objetivos para aprimorar a qualidade das formações e reuniões futuras. 
Logo no início, houve uma breve troca de impressões entre os participantes sobre a necessidade de um sistema de relatórios eficaz, capaz de fornecer insights valiosos para formadores e organizações.

Após essa introdução, André compartilhou um relatório gerado a partir da última reunião realizada há dois dias. 
O documento detalhava os tópicos discutidos, a eficácia do encontro e a participação dos membros. 
Rita e Daniel expressaram as suas opiniões sobre o conteúdo do relatório, apontando que a estrutura era bastante útil, mas que alguns aspectos poderiam ser melhorados, como a apresentação visual dos dados e a inclusão de métricas mais detalhadas sobre o envolvimento dos participantes. 
André mencionou que futuras versões do relatório poderiam incluir gráficos mais intuitivos e informações customizáveis para atender às necessidades específicas de cada utilizador.

O próximo ponto da reunião abordou a eficácia das formações e como a tecnologia pode melhorar o processo de ensino e aprendizagem. André explicou que uma das funções-chave da ferramenta que estavam a desenvolver era a capacidade de medir o engagement dos participantes em tempo real. 
Isso permitiria que os formadores identificassem momentos de maior ou menor atenção dos alunos e ajustassem as suas metodologias para maximizar o aproveitamento. 
Rita complementou ao mencionar que, pela sua experiência, a motivação dos formandos varia bastante dependendo da natureza da formação. 
Por exemplo, formações obrigatórias tendem a gerar menos envolvimento, enquanto cursos opcionais atraem participantes mais interessados. 
A partir dessa observação, discutiu-se a possibilidade de personalizar os relatórios para diferenciar esses cenários e sugerir intervenções específicas para melhorar o envolvimento dos alunos.

Outro tema importante foi a gestão do acesso aos materiais e a certificação das formações. 
Rita destacou que muitas plataformas de ensino restringem o acesso ao conteúdo assim que o curso é concluído, o que pode ser prejudicial para os formandos que desejam revisar a matéria posteriormente. 
Francisco sugeriu a criação de uma plataforma que funcionasse como um repositório centralizado de aprendizado, onde os alunos poderiam consultar seus materiais sempre que precisassem. 
Comparações foram feitas com plataformas existentes como Moodle, mas ficou evidente que a solução proposta teria um diferencial significativo ao agregar diferentes cursos e entidades formadoras num único ambiente acessível.

A reunião então avançou para a questão legal relacionada à gravação e ao processamento de dados dos participantes. 
Francisco explicou que qualquer gravação exigiria uma autorização explícita, e que seria essencial garantir conformidade com as regulamentações de proteção de dados. 
Surgiram diferentes abordagens para contornar possíveis preocupações, como a anonimização de determinados dados ou a configuração de um sistema que processasse as informações sem armazená-las de forma permanente. 
André e Daniel refletiram sobre a viabilidade dessas soluções, destacando que a tecnologia poderia ser ajustada para atender a requisitos legais sem comprometer a funcionalidade da ferramenta.

Em seguida, discutiu-se a possibilidade de expandir o uso da ferramenta para o meio académico, particularmente na Universidade X. 
Rita comentou que a instituição tem um histórico de apoiar projetos inovadores e que poderia ser uma parceira estratégica para a implementação inicial da tecnologia. 
André mencionou que já teve uma conversa preliminar com uma psicóloga da universidade que mostrou interesse no potencial da ferramenta para melhorar a experiência de aprendizagem. 
A ideia de marcar uma reunião formal com representantes da universidade foi bem recebida, e Francisco sugeriu preparar um material de apresentação detalhado para destacar os benefícios da plataforma.

Outro ponto abordado foi a aplicação prática da tecnologia em formações corporativas. 
Rita compartilhou uma experiência recente em que houve dificuldades em avaliar a eficácia de uma formação devido à falta de dados objetivos. 
Com a ferramenta desenvolvida, seria possível gerar relatórios detalhados sobre a performance dos formandos e a dinâmica das sessões. 
Francisco reforçou que a adoção de um sistema de acompanhamento contínuo poderia beneficiar tanto formadores quanto empresas, proporcionando um panorama mais claro sobre o retorno dos investimentos em formação.

Nos momentos finais da reunião, houve uma revisão das próximas ações a serem tomadas. 
Ficou decidido que um e-mail seria enviado à Universidade X para formalizar o contacto e agendar uma reunião. 
Além disso, Francisco comprometeu-se a consultar especialistas jurídicos para garantir que todas as questões legais fossem abordadas corretamente antes da implementação em larga escala. 
André mencionou que um primeiro teste da plataforma poderia ser realizado num ambiente controlado, permitindo ajustes antes de uma aplicação mais abrangente.

A reunião foi concluída com um sentimento positivo de avanço. 
Todos os participantes concordaram que as discussões trouxeram insights valiosos para a evolução do projeto e que os próximos passos estavam bem definidos. 
Ficou claro que a tecnologia desenvolvida tem o potencial de revolucionar a forma como formações e reuniões são conduzidas, proporcionando um método inovador para análise e acompanhamento de desempenho. 
A expectativa é que as próximas etapas de implementação e teste tragam resultados concretos que confirmem os benefícios discutidos ao longo do encontro.


"""

with st.container(height=500, border=True):
    st.write(st.text)

st.write("")
st.write("")
st.write("")


import streamlit as st

st.header("✅ Destaques", divider="gray")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Objetivo principal da reunião: <span style='font-weight:normal;'>A reunião teve como foco a análise da plataforma de transcrição e resumo de reuniões, bem como sua aplicação na educação e formação profissional.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Análise do relatório da reunião anterior: <span style='font-weight:normal;'>Foi apresentado um relatório detalhado da reunião anterior, destacando os pontos fortes e melhorias necessárias para otimizar a geração de relatórios automáticos.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Medição de Engagement e Participação: <span style='font-weight:normal;'>Discutiu-se a evolução do sistema para captar expressões faciais e padrões de interação, permitindo um melhor acompanhamento do envolvimento dos participantes.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Aplicação da Tecnologia no Ensino e Formação: <span style='font-weight:normal;'>Foram exploradas possibilidades de utilização da ferramenta na educação superior e em formações empresariais, com destaque para a potencial colaboração com a Universidade X.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Questões Legais e Proteção de Dados: <span style='font-weight:normal;'>Debateu-se a necessidade de conformidade com regulamentos de proteção de dados e possíveis soluções para anonimizar informações sensíveis.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Melhoria da Interface e Apresentação dos Relatórios: <span style='font-weight:normal;'>Foi identificada a necessidade de tornar os relatórios mais visuais e intuitivos, utilizando gráficos e métricas mais claras.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Testes Piloto e Implementação Inicial: <span style='font-weight:normal;'>Discutiu-se a realização de um teste inicial da plataforma num ambiente controlado para avaliar a sua eficácia antes da implementação em larga escala.</span>", unsafe_allow_html=True)

st.write("\n\n\n")

st.header("👣 Próximos Passos", divider="gray")

st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Agendar uma reunião com representantes da Universidade X para discutir a viabilidade de uma parceria e a aplicação da ferramenta no meio académico.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Consultar especialistas jurídicos para definir a melhor abordagem em relação à proteção de dados e permissões de uso da tecnologia.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Melhorar a interface do sistema, tornando os relatórios mais intuitivos e amigáveis para os utilizadores.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Refinar o \"engagement score\" e criar indicadores mais detalhados para avaliar a participação dos formandos.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Implementar um teste inicial da plataforma num ambiente controlado para recolher feedback e ajustes antes da expansão do projeto.")

st.write("\n\n\n")


st.header("✍🏻 Tarefas Atribuídas", divider="gray")

# Dicionário de tarefas atribuídas a cada pessoa
tasks = {
    "André Neiva": [
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Enviar um e-mail para a Universidade X para formalizar o interesse na parceria e agendar uma reunião.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Trabalhar na apresentação visual dos relatórios para torná-los mais intuitivos e informativos.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Coordenar com a equipa a organização do primeiro teste controlado da plataforma."
    ],
    "Daniel Furtado": [
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Melhorar a funcionalidade de medição de engagement no sistema, incorporando análise de expressões faciais e interações.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Implementar ajustes técnicos para otimizar o processamento de transcrições e resumos em tempo real.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Desenvolver um mecanismo para personalizar relatórios conforme o tipo de formação e necessidade do utilizador."
    ],
    "Francisco Falcão": [
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Consultar advogados para garantir conformidade legal da plataforma, especialmente em relação à proteção de dados e permissões.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Trabalhar na estruturação dos relatórios para torná-los mais acessíveis aos utilizadores finais."
    ],
    "Rita": [
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Explorar contactos na Universidade X para facilitar a comunicação e viabilizar a apresentação da ferramenta.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Avaliar possíveis resistências de formadores e empresas em relação ao uso da tecnologia e sugerir estratégias para aumentar a aceitação."
    ]
}

st.write("\n\n\n")

# Criar checkboxes para cada pessoa
selected_people = []
for person in tasks.keys():
    if st.checkbox(person, value=True):  # Começa marcado por padrão
        selected_people.append(person)

# Exibir as tarefas das pessoas selecionadas
for person in selected_people:
    st.write(f"#### {person}")
    for task in tasks[person]:
        st.write(f" {task}")

st.write("\n\n\n")

st.header("❔ Questões Relevantes", divider="gray")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 A plataforma permite que os formandos acessem o conteúdo das formações após a conclusão? <span style='font-weight:normal;'>(Francisco Falcão)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Resposta: <span style='font-weight:normal;'>Atualmente, os formandos têm um período limitado de acesso devido às restrições da plataforma. A ideia futura é que cada aluno tenha um espaço próprio onde possa agregar todas as formações feitas ao longo da sua vida profissional e revisitar materiais sempre que necessário.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Como garantir que as perguntas e respostas durante a formação sejam armazenadas de forma útil para os alunos? <span style='font-weight:normal;'>(Francisco Falcão)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Resposta: <span style='font-weight:normal;'>O sistema pode registrar as perguntas feitas pelos participantes e organizá-las num relatório, que poderá ser consultado posteriormente. Esse relatório pode incluir respostas, materiais de apoio e até recomendações personalizadas de estudo, sem necessidade de identificar os autores das perguntas.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 O modelo atual permite personalizar recomendações de aprendizagem com base na interação dos formandos? <span style='font-weight:normal;'>(André Neiva)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Resposta: <span style='font-weight:normal;'>Sim, a plataforma pode analisar o nível de engagement de cada formando e gerar sugestões de materiais complementares, como vídeos, artigos ou podcasts. Se o sistema detectar que um determinado tema não foi bem compreendido, poderá sugerir reforços específicos para cada aluno.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Como garantir a conformidade legal do armazenamento de dados dos formandos? <span style='font-weight:normal;'>(André Neiva)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Resposta: <span style='font-weight:normal;'>A equipa jurídica está a rever as melhores práticas para garantir a conformidade com a legislação de proteção de dados. Alternativas incluem anonimizar os dados dos formandos, processar as informações em tempo real sem necessidade de armazenamento prolongado e garantir que os participantes tenham total transparência e controlo sobre os seus dados.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Os formandos podem optar por não participar da análise de engagement? <span style='font-weight:normal;'>(Rita)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Resposta: <span style='font-weight:normal;'>Sim, os participantes podem optar por não participar da análise facial e de engagement. Caso recusem, os seus dados não serão processados e apenas informações gerais da turma serão apresentadas.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Como evitar que a presença de câmeras influencie o comportamento dos formandos? <span style='font-weight:normal;'>(Rita)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Resposta: <span style='font-weight:normal;'>Estudos mostram que, após os primeiros minutos, os formandos deixam de se preocupar com as câmeras e agem naturalmente. Além disso, a ferramenta pode funcionar em segundo plano sem gravação permanente, apenas analisando expressões faciais e engagement no momento.</span>", unsafe_allow_html=True)

st.write("\n\n\n")


st.header("🫡 Feedback da Reunião", divider="gray")

st.write("### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;André Neiva")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Aspetos Positivos:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Explicou bem a estrutura do projeto e os objetivos da ferramenta desenvolvida.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Conseguiu manter a interação ativa com os outros participantes.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Trouxe exemplos práticos para ilustrar a funcionalidade do sistema.")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Aspetos a Melhorar:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - A comunicação poderia ser mais objetiva, evitando explicações longas e justificações desnecessárias.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Algumas piadas e comentários informais poderiam ser reduzidos para manter o foco na reunião.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Garantir que todos os participantes tenham espaço para intervir, evitando monopolizar a conversa.")

st.write("### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rita")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Aspetos Positivos:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Demonstrou interesse genuíno e trouxe perspetivas valiosas sobre a aplicação do sistema no setor da formação.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Explicou de forma clara as dificuldades e desafios da formação online e presencial.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Sugeriu contactos importantes, nomeadamente com a Universidade X.")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Aspetos a Melhorar:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Algumas ideias foram repetidas ao longo da reunião. Poderia ser mais concisa.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Poderia estruturar melhor as suas intervenções para facilitar a fluidez da conversa e evitar desvios do tema central.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Algumas explicações foram longas e detalhadas demais, dificultando a compreensão rápida dos pontos principais.")


st.write("### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Francisco Falcão")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Aspetos Positivos:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Apresentou bem os aspetos legais e técnicos da ferramenta.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Fez uma boa ligação entre a ferramenta e o impacto na formação contínua e na certificação dos formandos.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Trouxe argumentos sólidos sobre a importância do projeto e a sua aplicabilidade em diferentes setores.")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Aspetos a Melhorar:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Algumas explicações foram demasiado extensas, o que pode ter tornado certos pontos menos claros.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Poderia resumir melhor alguns conceitos para tornar a reunião mais eficiente.")

st.write("### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Daniel Furtado")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Aspetos Positivos:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Demonstrou conhecimento técnico e esteve atento à discussão.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Trouxe uma perspetiva relevante sobre a possibilidade de adaptar a plataforma com novas funcionalidades.")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Aspetos a Melhorar:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Participação foi muito reduzida. Poderia intervir mais e esclarecer dúvidas técnicas quando surgem.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Poderia ter uma abordagem mais proativa para apresentar sugestões ou melhorias ao projeto.")




topics = {
    "Global": None,
    "Introdução e chegada dos participantes": ("11:35", "11:42"),
    "Apresentação do relatório da reunião anterior": ("11:42", "11:44"),
    "Definição de próximos passos e atribuição de tarefas": ("11:44", "11:45"),
    "Discussão sobre a eficácia da formação e metodologias de ensino": ("11:45", "11:46"),
    "Análise do engagement e participação ativa": ("11:46","11:47"),
    "Considerações sobre o uso da tecnologia na educação": ("11:47","11:55"),
    "Impacto da formação financiada e desafios de motivação": ("11:55","11:57"),
    "Gestão de acesso a materiais e certificação de formações": ("11:57","12:04"),
    "Modelo de negócio para formação digital e plataforma centralizada": ("12:04","12:13"),
    "Legalidade e autorizações necessárias para gravações e tratamento de dados": ("12:13","12:21"),
    "Integração da ferramenta em contextos académicos": ("12:21","12:27"),
    "Testes e implementação em formações reais": ("12:27","12:30"),
    "Reflexão final e próximos passos": ("12:30","12:57"),
}


st.header("📈 Engagement", divider="gray")

data = pd.read_csv("pages/Reuniao_13_02_2025/Files/data_final.csv")
data["datetime"] = pd.to_datetime(data["datetime"])

time_adjust = "1min" 


plot_data = []

data_global = data.set_index('datetime').resample(time_adjust)["engagement"].mean().reset_index()
data_global['person'] = 'Média Global' 


selected_topic = st.selectbox("🔍 Filtrar Tema:", list(topics.keys(),), key="engagement")
if selected_topic != "Global":
    start_time, end_time = topics[selected_topic]
    mask_time = (data['datetime'].dt.strftime("%H:%M") >= start_time) & (data['datetime'].dt.strftime("%H:%M") <= end_time)
    mask_time1 = (data_global['datetime'].dt.strftime("%H:%M") >= start_time) & (data_global['datetime'].dt.strftime("%H:%M") <= end_time)
    data_filtered = data[mask_time]
    data_filtered_global = data_global[mask_time1]
else:
    data_filtered = data
    data_filtered_global = data_global



for person in data['person'].unique():
    data_person = data_filtered[data_filtered['person'] == person].set_index('datetime')
    grouped_data = data_person["engagement"].resample(time_adjust).mean().reset_index()
    grouped_data['person'] = f'{person}'
    plot_data.append(grouped_data)


plot_data.append(data_filtered_global)
plot_df = pd.concat(plot_data)

plot_df["Tema"] = "Global"  # Valor padrão

for tema, intervalo in topics.items():
    if intervalo:  # Verifica se o valor não é None
        start_time, end_time = intervalo
        mask = (plot_df["datetime"].dt.strftime("%H:%M") >= start_time) & \
               (plot_df["datetime"].dt.strftime("%H:%M") <= end_time)
        plot_df.loc[mask, "Tema"] = tema  # Atribui o tema correto


fig = px.line(
    plot_df, 
    x="datetime", 
    y="engagement", 
    color="person",
    title="Engagement ao Longo do Tempo",
    labels={"datetime": "Tempo", "engagement": "Engagement (%)", "person": "Participantes"},
    template="plotly_white",
    line_dash="person",
    line_group="person",
    line_dash_map={"Média Global": "dash", "André Neiva": "solid", "Daniel Furtado": "solid", "Francisco Falcão": "solid", "Rita": "solid"},
    hover_data=["Tema"],
    range_y=[0, 1]
)

st.plotly_chart(fig, use_container_width=True)

st.write("")

st.write("##### Momentos Relevantes")

col1, col2, col3, col4, b,c,d,e = st.columns(8)

# Inicializar estados para cada imagem
if "show_image_1623" not in st.session_state:
    st.session_state.show_image_1623 = False
if "show_image_1625" not in st.session_state:
    st.session_state.show_image_1625 = False


with col1:
    if st.button("11:49"):
        st.session_state.show_image_1623 = not st.session_state.show_image_1623

with col2:
    if st.button("12:34"):
        st.session_state.show_image_1625 = not st.session_state.show_image_1625



if st.session_state.show_image_1623:
    st.image(Image.open("pages/Reuniao_13_02_2025/Images/11_49.png"), caption="Momento Baixo Engagement", width=650)

if st.session_state.show_image_1625:
    st.image(Image.open("pages/Reuniao_13_02_2025/Images/12_34.png"), caption="Momento Alto Engagement", width=650)

st.write("")
st.write("")
st.write("")


st.header("📈 Participação", divider="gray")
st.write("")

st.write("##### 🗣️ Participação Ativa:")
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; •  André Neiva: <span style='font-weight:normal;'>00:27:13 (29.58%)</span>", unsafe_allow_html=True )
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; •  Daniel Furtado: <span style='font-weight:normal;'>00:06:26 (06.99%)</span>", unsafe_allow_html=True )
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; •  Rita: <span style='font-weight:normal;'>00:34:28 (37.46%)</span>", unsafe_allow_html=True )
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; •  Francisco Falcão: <span style='font-weight:normal;'>00:21:52 (23.77%)</span>", unsafe_allow_html=True )




df_resampled = pd.read_csv("pages/Reuniao_13_02_2025/Files/interventions.csv", index_col=0, parse_dates=True)
df_resampled["Média Global"] = df_resampled[["André Neiva", "Daniel Furtado", "Rita Batista", "Francisco Falcão"]].mean(axis=1)
df_resampled = df_resampled.rename(columns={"Rita Batista": "Rita"})




participants = df_resampled.columns.tolist()




df_filtered = df_resampled[participants].reset_index()
df_melted = df_filtered.melt(id_vars=["time"], var_name="Participant", value_name="Interventions")

selected_topic = st.selectbox("🔍 Filtrar por Tema:", list(topics.keys(),), key="participation")
if selected_topic != "Global":
    start_time, end_time = topics[selected_topic]
    mask_time = (df_melted['time'].dt.strftime("%H:%M") >= start_time) & (df_melted['time'].dt.strftime("%H:%M") <= end_time)
    data_filtered = df_melted[mask_time]
else:
    data_filtered = df_melted


data_filtered["Tema"] = "Global"  # Valor padrão

for tema, intervalo in topics.items():
    if intervalo:  # Verifica se o valor não é None
        start_time, end_time = intervalo
        mask = (data_filtered["time"].dt.strftime("%H:%M") >= start_time) & \
               (data_filtered["time"].dt.strftime("%H:%M") <= end_time)
        data_filtered.loc[mask, "Tema"] = tema  # Atribui o tema correto





fig = px.line(data_filtered, x="time", y="Interventions", color="Participant",
            labels={"time": "Horário", "Interventions": "Número de Intervenções"},
            line_dash="Participant",
            line_dash_map={"Média Global": "dash", "André Neiva": "solid", "Daniel Furtado": "solid", "Francisco Falcão": "solid", "Rita": "solid"},
            title="Participação ao Longo do Tempo",
            hover_data=["Tema"]
            )



fig.update_xaxes(title="Tempo")
fig.update_yaxes(title="Nº ntervenções")
fig.update_layout(legend_title="Participantes")

st.plotly_chart(fig, use_container_width=True)



st.write("")
st.write("")
st.write("")


st.header("🎭 Expressão Facial", divider="gray")

time_adjust = '1 min'



people_list = data['person'].unique()
people_list = ["Global"] + list(people_list)

selected_topic = st.selectbox("🔍 Filtrar por Tema:", list(topics.keys()), key="facial_expression")
selected_person = st.selectbox("👤 Filtrar por Pessoa:", people_list)

if selected_topic != "Global":
    start_time, end_time = topics[selected_topic]
    mask_time = (data['datetime'].dt.strftime("%H:%M") >= start_time) & (data['datetime'].dt.strftime("%H:%M") <= end_time)
    data_filtered = data[mask_time]
else:
    data_filtered = data

if selected_person != "Global":
    data_filtered = data_filtered[data_filtered['person'] == selected_person]

expression_counts = data_filtered.groupby(
    [pd.Grouper(key='datetime', freq=time_adjust), 'facial_expression']
).size().unstack(fill_value=0)

expression_normalized = expression_counts.div(expression_counts.sum(axis=1), axis=0).fillna(0)

expression_smoothed = expression_normalized.rolling(window=5, min_periods=1).mean()

plot_data = expression_smoothed.reset_index().melt(id_vars="datetime", var_name="Expression", value_name="Frequency")

plot_data["Tema"] = "Global"  # Valor padrão

for tema, intervalo in topics.items():
    if intervalo:  # Verifica se o valor não é None
        start_time, end_time = intervalo
        mask = (plot_data["datetime"].dt.strftime("%H:%M") >= start_time) & \
               (plot_data["datetime"].dt.strftime("%H:%M") <= end_time)
        plot_data.loc[mask, "Tema"] = tema  # Atribui o tema correto



# Criar o gráfico interativo com Plotly Express
fig = px.line(
    plot_data, 
    x="datetime", 
    y="Frequency", 
    color="Expression", 
    title=f"Variação da Expressão Facial - {selected_topic} ({selected_person})",
    labels={"datetime": "Tempo", "Frequency": "Expressão Facial (%)", "Expression": "Expressão Facial"},
    hover_data=["Tema"],
    template="plotly_white",
    range_y=[0, 1]

)
st.plotly_chart(fig, use_container_width=True)



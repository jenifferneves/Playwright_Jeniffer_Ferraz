Test_Sprint7_ServeRest

Test_Sprint7_ServeRest

Bem-vindo(a) ao repositório Test_Sprint7_ServeRest! Este projeto documenta a execução da Sprint 7, com foco em testes funcionais, automatizados e de performance na API ServeRest.

O objetivo foi aplicar boas práticas de planejamento, automação de testes e análise de desempenho, utilizando ferramentas modernas do mercado.

🤖 Testes e Planejamento de Testes
🎯 Objetivo do Repositório

O objetivo deste repositório é documentar a execução completa da Sprint 7, contemplando:

• Testes manuais exploratórios
• Testes automatizados de API com Playwright (Python)
• Testes de carga com JMeter
• Planejamento estruturado (Plano de Teste)
• Análise de critérios de aceite e riscos

A proposta foi validar funcionalidade, autenticação, controle de permissões e estabilidade da API.

📂 Estrutura do Repositório

O repositório está organizado para refletir as etapas da Sprint:

• Plano_de_Teste: Documento completo com escopo, estratégia, riscos e critérios de aceite.

• Testes_Automatizados_Playwright: Scripts automatizados para validação das rotas:

/usuarios

/login

/produtos

/carrinhos

• Testes_JMeter: Arquivos .jmx e relatórios de testes de carga executados.

• Evidencias: Prints e registros dos resultados obtidos.

• .gitignore: Configurado para ignorar arquivos temporários como a pasta .vs.

🌿 Ramos

• main: Versão estável com todos os testes consolidados.

• develop: Branch utilizada para desenvolvimento incremental da Sprint.

💻 Ferramentas Utilizadas

• Linguagem: Python

• Automação de Testes: Playwright

• Testes de Performance: Apache JMeter

• Testes Manuais: Postman

• Controle de Versão: Git & GitHub

• Editor: Visual Studio Code

• Planejamento: Jira

• Apoio: ChatGPT

🚀 Progresso e Métodos Aplicados
🔎 Testes Exploratórios

Foram analisados os seguintes endpoints da API:

• Rota /usuarios
Validação de cadastro, busca, edição e exclusão.

• Rota /login
Validação de autenticação e geração de token JWT.

• Rota /produtos
Testes de CRUD, controle de acesso por administrador e validação de exclusão.

• Rota /carrinhos
Criação de carrinho, adição de produtos, conclusão e cancelamento de compra.

🤖 Testes Automatizados (Playwright – Python)

Foram automatizados fluxos completos simulando cenários reais de uso:

• Cadastro de usuário administrador
• Login com geração de token JWT
• Cadastro de usuário comum
• Criação de produto (admin)
• Criação e conclusão de carrinho
• CRUD completo de produtos
• CRUD completo de usuários

Validações realizadas:

• Status codes (200, 201, 400)
• Mensagens de sucesso e erro
• Permissões de acesso
• Exclusão e validação pós-delete

Os testes foram estruturados para servir como base de regressão.

🚀 Testes de Performance (JMeter)

Foram executados testes básicos de carga na rota:

• GET /produtos

Cenários aplicados:

• 10 usuários simultâneos
• 20 usuários simultâneos
• 30 usuários simultâneos

Métricas analisadas:

• Tempo médio de resposta
• Throughput
• Percentual de sucesso
• Taxa de erro
• Estabilidade sob carga

📌 Observação:
A API manteve estabilidade até 30 usuários simultâneos. Acima disso, o ambiente local apresentou instabilidade.

📄 Planejamento de Testes

O plano de testes incluiu:

• Definição de escopo
• Estratégia funcional e de performance
• Critérios de aceite
• Priorização
• Riscos do ambiente

✔ Definition of Ready (DoR)

A Sprint foi considerada pronta para execução quando:

• Rotas estavam documentadas
• Requisitos de autenticação estavam definidos
• Ambiente estava acessível

✔ Definition of Done (DoD)

A Sprint foi considerada concluída quando:

• 100% dos testes automatizados passaram
• Testes de carga foram executados
• Relatório final foi documentado
• Evidências foram anexadas

🛠 Instalação de Ferramentas

Python

Instalar dependências:
pip install playwright
playwright install

Executar testes:
pytest

JMeter

Instalar o Apache JMeter e abrir o arquivo .jmx presente na pasta do projeto para execução dos testes de carga.

Para executar os testes de carga:

• Abrir JMeter
• Importar o arquivo .jmx
• Executar o plano de teste

🤝 Contribuição

Este projeto foi desenvolvido como prática de aprendizado e consolidação de conhecimentos em testes de API e performance. Sugestões e feedbacks são sempre bem-vindos.

📧 Contato

• E-mail: jenifferferrasz03@gmail.com

• LinkedIn: http://linkedin.com/in/jeniffer-ferraz-42166a254
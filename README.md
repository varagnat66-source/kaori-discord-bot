# Kaori — Discord Bot

Bot de Discord desenvolvido em Python como projeto de estudo e portfólio, aplicando conceitos de consumo de APIs externas, automação assíncrona e boas práticas de organização de código.

O objetivo do projeto não é só "fazer funcionar", mas praticar decisões reais de arquitetura: separação em módulos (cogs), tratamento de erros centralizado, segurança de credenciais e tarefas automáticas em segundo plano.

## Funcionalidades

- **Boas-vindas e despedida**: mensagens automáticas em embed (com gif) quando alguém entra ou sai do servidor, incluindo atribuição automática de cargo (auto-role) para novos membros
- **Conversor de moedas**: converte valores entre qualquer par de moedas suportado (ex: JPY → BRL), usando a API Frankfurter
- **Promoções da Steam**:
  - Comando manual (`.promo`) que lista as promoções ativas no momento
  - Notificador automático, que verifica periodicamente novas promoções e avisa em um canal fixo — um embed por jogo, com capa, preço original, preço promocional e desconto — sem repetir avisos de promoções já vistas
- **Limpeza de mensagens** (`.purge`): apaga mensagens do canal, restrito a usuários com permissão de "Gerenciar Mensagens"
- **Tratamento de erros global**: mensagens claras para comando inexistente, parâmetro faltando, argumento inválido ou falta de permissão — válido automaticamente para todos os comandos do bot

## Tecnologias

- **Python 3.14**
- **[discord.py](https://discordpy.readthedocs.io/)** — biblioteca principal de integração com a API do Discord
- **[requests](https://docs.python-requests.org/)** — consumo de APIs externas
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — gerenciamento de variáveis de ambiente
- **APIs externas**: [Frankfurter](https://frankfurter.dev/) (câmbio) e [CheapShark](https://apidocs.cheapshark.com/) (promoções de jogos)

## Estrutura do projeto

```
botest/
├── main.py                # ponto de entrada, eventos globais e tratamento de erros
├── cogs/
│   ├── geral.py            # comandos gerais (ex: .ola)
│   ├── convert.py          # conversor de moedas
│   ├── promo.py            # promoções da Steam (manual + automático)
│   └── purge.py            # limpeza de mensagens
├── imagens/                 # gifs usados nos embeds
├── .env                     # variáveis de ambiente (não versionado)
└── .gitignore
```

## Como rodar localmente

1. Clone o repositório
   ```bash
   git clone https://github.com/seu-usuario/kaori-discord-bot.git
   cd kaori-discord-bot
   ```

2. Instale as dependências
   ```bash
   pip install discord.py requests python-dotenv
   ```

3. Crie uma pasta `imagens/` na raiz do projeto e adicione seus próprios gifs (`doce.gif`, `kaori_ola.gif`, `tchau.gif` — ou outros nomes, ajustando as referências no código). Essa pasta não é versionada no repositório por conter mídia de terceiros (trechos de animações); use gifs de sua própria autoria ou com licença de uso livre.

4. Crie um arquivo `.env` na raiz do projeto com suas próprias credenciais:
   ```
   DISCORD_TOKEN=seu_token_aqui
   CANAL_CHEGADA=id_do_canal
   ID_CARGO=id_do_cargo
   CANAL_SAIDA=id_do_canal
   CANAL_PROMO=id_do_canal
   CONTATO=seu_email@exemplo.com
   ```

5. Rode o bot
   ```bash
   python main.py
   ```

> O token do Discord pode ser gerado em [Discord Developer Portal](https://discord.com/developers/applications). Nunca compartilhe seu `.env` nem faça commit dele — o `.gitignore` já está configurado para ignorá-lo.

## Decisões técnicas

**Arquitetura em Cogs**: em vez de manter todos os comandos em um único arquivo, o bot é dividido em módulos independentes (cogs), carregados dinamicamente pelo `main.py`. Isso facilita manutenção e permite adicionar novas funcionalidades sem tocar no código existente.

**Tarefa automática com controle de estado**: o notificador de promoções usa `tasks.loop` para verificar a API periodicamente, comparando o resultado de cada verificação com o anterior (guardado em memória) para avisar apenas promoções *novas* — evitando spam de notificações repetidas a cada execução.

**Tratamento de erros centralizado**: em vez de tratar exceções comando por comando, um único handler (`on_command_error`) cobre todos os comandos do bot, atuais e futuros, com mensagens específicas para os erros mais comuns.

**Segurança de credenciais**: tokens, IDs de canal/cargo e dados de contato usados em APIs externas ficam isolados em variáveis de ambiente (`.env`), nunca hardcoded no código-fonte.

## Próximos passos

- [ ] Sistema de pontos com persistência em banco de dados (SQLite)
- [ ] Comando de lembretes
- [ ] Persistência do histórico de promoções em arquivo/banco (atualmente reinicia ao reiniciar o bot)
- [ ] Testes automatizados

---

Projeto em desenvolvimento contínuo, feito como parte dos meus estudos em Análise e Desenvolvimento de Sistemas.

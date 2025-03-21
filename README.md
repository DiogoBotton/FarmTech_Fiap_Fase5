# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto
Sistema para prever rendimentos baseado em culturas e variáveis climáticas.

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/bryanjfagundes/">Bryan Fagundes</a>
- <a href="https://br.linkedin.com/in/brenner-fagundes">Brenner Fagundes</a>
- <a href="https://www.linkedin.com/in/diogo-botton-46ba49197/">Diogo Botton</a> 
- <a href="https://www.linkedin.com/in/hyankacoelho/">Hyanka Coelho</a> 
- <a href="https://www.linkedin.com/in/julianahungaro/">Juliana Hungaro Fidelis</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi</a>

## 📜 Descrição

Este projeto tem como objetivo criar um modelo de machine learning de regressão para prever valores de rendimento baseado no tipo da cultura (4 tipos variados) e variáveis climáticas, como humidade, precipitação e temperatura. Assim como, realizar uma estimativa de custos para usar uma máquina da AWS, que hipoteticamente, será utilizada para hospedar uma API com o modelo de machine learning de regressão mencionado anteriormente.

Também foi realizado a atividade Ir Além com ESP32, onde é utilizado um Sensor DHT11 para capturar informações de temperatura e humidade e enviar para um Broker MQTT (RabbitMQ), onde a partir de uma API Python com WebSocket é possível o consumo dessas mensagens através um front em html.

**Dentro da pasta src há um readme para cada projeto com detalhes**.


## 💰 Análise Comparativa de Custos

#### Comparação EC2 por Região
| Região      | Custo Mensal | vCPUs | Memória | Rede      |
|:------------|-------------:|:------|:--------|:----------|
| us-east-1   | $13,38       | 2     | 1 GiB   | 5 Gigabit |
| sa-east-1   | $21,80       | 2     | 1 GiB   | 5 Gigabit |

#### Comparação por Tipo de Instância (sa-east-1)
| Tipo        | vCPUs | Memória | Custo Mensal | Uso Recomendado |
|:------------|------:|--------:|-------------:|:----------------|
| t3.micro    | 2     | 1 GiB   | $21,80       | Desenvolvimento |
| t3.small    | 2     | 2 GiB   | $43,60       | Teste          |
| t3.medium   | 2     | 4 GiB   | $87,20       | Produção       |

#### Custos de Infraestrutura Completa
| Componente  | Custo (USD) | Especificação |
|:------------|------------:|:--------------|
| IoT Core    | $50         | 10K conexões  |
| Lambda      | $20         | 2M execuções  |
| S3          | $30         | 500GB        |
| ECS         | $150        | 2 instâncias |
| Glue        | $80         | 40 DPUs/mês  |
| Redshift    | $250        | 2 nós dc2.large |
| QuickSight  | $24         | 2 usuários    |
| **Total**   | **$604**    | **mensal**    |

#### Projeção de Crescimento
| Período     | Requisições/dia | Custo Mensal | Crescimento |
|:------------|---------------:|-------------:|------------:|
| Atual       | 1K             | $50          | -           |
| 6 meses     | 10K            | $160         | 220%        |
| 1 ano       | 100K           | $470         | 840%        |
| 2 anos      | 500K           | $900         | 1700%       |

#### Otimizações de Custo Disponíveis
| Estratégia          | Economia Potencial | Complexidade |
|:-------------------|------------------:|:-------------|
| Savings Plans      | Até 72%           | Baixa        |
| Reserved Instances | Até 75%           | Média        |
| Spot Instances     | Até 90%           | Alta         |

#### Comparativo de Custos por Ambiente
| Ambiente     | Custo Base | Com Otimização | Economia |
|:-------------|------------:|---------------:|---------:|
| Dev/Test     | $300        | $90            | 70%      |
| Staging      | $450        | $180           | 60%      |
| Production   | $604        | $302           | 50%      |

## 💰 Análise de Custos e Arquitetura Cloud

### Links das Calculadoras AWS
- [Calculadora 1](https://calculator.aws/#/estimate?id=fd3a9a6e6007c2826b98a0f455ae6ac1414c8312)
- [Calculadora 2](https://calculator.aws/#/estimate?id=2d55afdcbf9edbe54be830246c2daf0505828871)

### Comparação de Custos AWS por Região

#### Configuração Analisada
- 2 CPUs
- 1 GiB memória
- Até 5 Gigabit de rede
- 50 GB armazenamento (HD)

#### Custos Mensais (On-Demand 100%)
- **Região Norte da Virgínia (us-east-1)**: USD 13,38
- **Região São Paulo (sa-east-1)**: USD 21,80

### Otimizações de Custos Propostas

#### 1. Planos de Economia
- Savings Plans
- Instâncias Reservadas
- Spot Instances para workloads não críticos

#### 2. Arquitetura Proposta


[Sensores] -> [IoT Core] -> [Lambda] -> [ECS] -> [ML Processing]


#### Componentes da Arquitetura

##### Recepção de Dados
- **AWS IoT Core**
- Gerenciamento de sensores
- Protocolo MQTT
- Regras de roteamento

##### Processamento
- **AWS Lambda**
  - Free tier: 1 milhão execuções/mês
  - Tempo máximo: 15 minutos
  - Processamento assíncrono

- **Amazon ECS**
  - Containers para ML
  - Auto-scaling
  - Custo-benefício otimizado

##### Armazenamento
- **Amazon S3**
  - Dados brutos
  - Backups
  - Custo efetivo

#### Recomendação Final
Apesar do custo 63% maior, a região de São Paulo (sa-east-1) é recomendada:
- Conformidade legal
- Menor latência
- Performance local otimizada

### 🚀 Arquitetura Futura e Análise de Custos

### Diagrama de Arquitetura
<p align="center">
<img src="assets/iot.drawio.png" alt="Diagrama de Arquitetura IoT" width="100%">
</p>

### Fluxo Detalhado
1. **Ingestão de Dados**:
   - Sensores enviam dados brutos
   - IoT Core gerencia conexões MQTT
   - Lambda processa e valida dados

2. **Processamento e Armazenamento**:
   - S3 armazena dados validados
   - ECS executa modelos ML
   - Predições são persistidas

3. **Análise e Visualização**:
   - Glue cataloga dados
   - Redshift permite análises complexas
   - QuickSight gera dashboards

### 📊 Análise de Custos Projetados

#### Custos por Componente (Estimativa Mensal)

### Custos por Componente (Estimativa Mensal)

| Componente  | Custo (USD) | Especificação |
|:------------|------------:|:--------------|
| IoT Core    | $50         | 10K conexões  |
| Lambda      | $20         | 2M execuções  |
| S3          | $30         | 500GB        |
| ECS         | $150        | 2 instâncias |
| Glue        | $80         | 40 DPUs/mês  |
| Redshift    | $250        | 2 nós dc2.large |
| QuickSight  | $24         | 2 usuários    |
| **Total**   | **$604**    | **mensal**    |


#### Otimizações Propostas

1. **Curto Prazo**:
   - Savings Plans para ECS
   - S3 Intelligent-Tiering
   - Redshift Reserved Instances

2. **Médio Prazo**:
   - Implementar cache em memória
   - Otimizar queries Redshift
   - Ajustar TTL dos dados

3. **Longo Prazo**:
   - Migrar para arquitetura serverless
   - Implementar data lifecycle
   - Automatizar scaling

### 📈 Projeção de Crescimento

#### Cenários de Escala

| Período     | Requisições/dia | Custo Mensal |
|:------------|---------------:|-------------:|
| Atual       | 1K             | $50          |
| 6 meses     | 10K            | $160         |
| 1 ano       | 100K           | $470         |
| 2 anos      | 500K           | $900         |

### 🔄 Ciclo de Dados
1. **Coleta**: Sensores -> IoT Core
2. **Validação**: Lambda
3. **Processamento**: ECS/ML
4. **Armazenamento**: S3/Redshift
5. **Análise**: QuickSight

### 🎯 Benefícios Esperados

#### Performance
- Latência < 100ms
- Disponibilidade 99.9%
- Processamento near real-time

#### Escalabilidade
- Auto-scaling em todas camadas
- Elastic Load Balancing
- Multi-AZ deployment

#### Segurança
- Encryption em repouso
- VPC endpoints
- IAM roles granulares

### 💡 Recomendações Técnicas

1. **Ingestão**:
   - Implementar retry policy
   - Buffer para picos
   - Validação em tempo real

2. **Processamento**:
   - Containers otimizados
   - Cache distribuído
   - Batch processing

3. **Análise**:
   - Materialized views
   - Query optimization
   - Data partitioning

## 💰 Análise Comparativa de Custos

### Visualizações dos Custos

#### Comparação por Região
<p align="center">
<img src="assets/regiao.png" alt="Comparação de Custos por Região AWS" width="100%">
</p>

#### Distribuição de Custos por Serviço
<p align="center">
<img src="assets/distribuicao.png" alt="Distribuição de Custos por Serviço AWS" width="100%">
</p>

#### Projeção de Crescimento
<p align="center">
<img src="assets/projecao.png" alt="Projeção de Crescimento de Custos AWS" width="100%">
</p>


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: Aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>scripts</b>: Aqui está um arquivo de implementação (deploy), no caso, o docker-compose.yml que realiza o deploy da API juntamente com o modelo.

- <b>src</b>: Todo o código fonte criado, com o notebook de análise exploratória, treinamento do modelo e a API, assim como, a atividade Ir Além com ESP32.

## 🔧 Como executar o código

Para executar o código de **análise exploratória** (*01_exploratory_analysis.ipynb*) e **treinamento do modelo** (*02_regression_model.ipynb*), é necessário ter o **Visual Studio Code** e o **Jupyter Notebook** instalado em sua máquina. Para executar o código inteiro, basta acessar algum destes dois arquivos e executar o código clicando no botão **Run All**.

Para executar a API com o modelo gerado atráves do notebook *01_exploratory_analysis.ipynb*, é necessário ter o Docker instalado em sua máquina. Com ele instalado, basta com alguma CLI (por exemplo, o prompt do windows) navegar até a pasta *scripts* e digitar:

```bash
    docker-compose up -d --build
```

Ao rodar o comando, a API estará disponível com a documentação do Swagger e pronta para ser acessada através da url: *http://localhost/docs*

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

Co-pilot Médico

O primeiro passo de um projeto de banco de dados relacional é a criacao de um mini-mundo no qual possamos nos basear e
definir quais entidades, como elas se relacionam e possiveis dependencias.

Cenário Miniworld Dra. Alice, uma cardiologista, usa um sistema alimentado por IA para auxiliar no diagnóstico de Fulano,
um paciente que reclama de dor no peito. Dra. Alice registra o histórico médico e os sintomas de Fulano no sistema
(anamnese), consulta a IA para diagnósticos potenciais e toma uma decisão final sobre o tratamento de Fulano. O sistema
rastreia essas interações, armazenando os dados médicos de Fulano, a entrada da Dra. Alice e as respostas da IA ​​para
referência futura.


Resumo dos relacionamentos:
Relacionamento 1-N entre pacientes e histórico médico (um paciente, vários registros de histórico médico).
Relacionamento 1-N entre médicos e histórico médico (um médico, vários registros de histórico médico).
Relacionamento 1-N entre histórico médico e diagnósticos (um histórico médico, um ou mais diagnósticos).
Relacionamento 1-N entre pacientes/médicos e consultas (várias consultas para cada paciente e médico).
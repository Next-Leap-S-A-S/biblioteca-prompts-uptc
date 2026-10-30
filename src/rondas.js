const RONDAS=[
 {n:"Litigio civil", f:[
  {k:"rol",x:"Eres un abogado litigante con 15 años de práctica en procesos declarativos ante juzgados civiles del circuito."},
  {k:"rol",x:"Eres un abogado procesalista que revisa memoriales antes de radicarlos y detecta causales de rechazo."},
  {k:"ctx",x:"La sentencia de primera instancia se notificó por estado el [fecha] y negó todas las pretensiones."},
  {k:"ctx",x:"El demandado propuso la excepción de prescripción y el dictamen pericial no fue controvertido."},
  {k:"ins",x:"Redacta los reparos concretos de la apelación en una lista numerada de máximo 400 palabras."},
  {k:"ins",x:"Separa en dos columnas los hechos probados y los hechos que solo afirma el cliente."}]},
 {n:"Contratos y laboral", f:[
  {k:"rol",x:"Eres un abogado comercial que negocia contratos de suministro para empresas manufactureras."},
  {k:"rol",x:"Eres un abogado laboralista que representa trabajadores en procesos ordinarios de primera instancia."},
  {k:"ctx",x:"El proveedor incumplió tres entregas y el contrato tiene una cláusula penal equivalente al 20% del valor."},
  {k:"ctx",x:"El trabajador prestó servicios durante cuatro años con contratos de prestación de servicios sucesivos."},
  {k:"ins",x:"Devuelve una tabla con cada cláusula, el riesgo que genera y una redacción alternativa."},
  {k:"ins",x:"Calcula las prestaciones en una tabla que yo pueda revisar fila por fila, con la fórmula de cada concepto."}]},
 {n:"Penal y administrativo", f:[
  {k:"rol",x:"Eres un defensor penal con experiencia en audiencias preliminares del sistema acusatorio."},
  {k:"rol",x:"Eres un abogado de contratación estatal que asesora oferentes en licitaciones públicas."},
  {k:"ctx",x:"La audiencia de solicitud de medida de aseguramiento está fijada para el próximo lunes a las 8:00 a. m."},
  {k:"ctx",x:"El pliego exige una experiencia que solo cumplen dos oferentes del mercado y el término de observaciones vence mañana."},
  {k:"ins",x:"Prepara un guion de intervención de máximo diez minutos con los argumentos ordenados por fuerza."},
  {k:"ins",x:"Redacta las observaciones al pliego como un escrito numerado dirigido a la entidad."}]},
 {n:"Constitucional", f:[
  {k:"rol",x:"Eres un abogado constitucionalista que redacta tutelas en salud para pacientes con enfermedades graves."},
  {k:"rol",x:"Eres un abogado que escribe para un cliente sin formación jurídica y le explica sus opciones con claridad."},
  {k:"ctx",x:"La EPS negó el medicamento hace tres semanas y el médico tratante lo ordenó con carácter urgente."},
  {k:"ctx",x:"El derecho de petición se radicó el [fecha de radicación] y la entidad no ha respondido."},
  {k:"ins",x:"Analiza primero la procedencia de la tutela: subsidiariedad, inmediatez y legitimación."},
  {k:"ins",x:"No cites sentencias que no puedas identificar con certeza. Marca cada cita con [verificar]."}]},
 {n:"Las que engañan", f:[
  {k:"rol",x:"Actúa como un juez de segunda instancia que lee mi recurso buscando sus debilidades."},
  {k:"rol",x:"Eres un abogado prudente al estimar la probabilidad de éxito y nunca la presentas como certeza."},
  {k:"ctx",x:"Ya intentamos conciliar y la contraparte no asistió a la audiencia."},
  {k:"ctx",x:"Toda la información que pego está anonimizada y los nombres fueron reemplazados por marcadores."},
  {k:"ins",x:"Separa lo que es un hecho probado de lo que es una inferencia."},
  {k:"ins",x:"Antes de entregar, verifica que cada pretensión tenga al menos una prueba que la soporte."}]}
];

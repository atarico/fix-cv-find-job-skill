# fix-cv-find-job-skill

[English](README.md) · **Español**

**Arregla tu CV y te encuentra trabajo.** Una skill de Claude que audita tu
currículum como lo haría un reclutador, lo reescribe como plantilla maestra
adaptable a cualquier vacante, busca vacantes en los portales que usás, postula
por vos, alinea tu LinkedIn y clasifica tu correo buscando respuestas.

Sirve para **cualquier rubro**. Deduce tu campo a partir de tu propio CV en
lugar de asumir que trabajás en tecnología.

## Por qué existe

Me cansé de hacer esto a mano.

Cansado de abrir el mismo CV por vigésima vez para mover tres viñetas porque
esta vacante pedía algo apenas distinto de la anterior. Cansado de mantener una
planilla de dónde había postulado para no postular dos veces a la misma empresa.
Cansado de revolver una bandeja de entrada llena de acuses automáticos para
encontrar el único mensaje que era una respuesta real. Cansado de leer un aviso,
leer mi CV y hacer el cruce de palabras clave en la cabeza, otra vez.

Nada de eso es trabajo difícil. Es trabajo repetitivo, y es el tipo de trabajo
repetitivo que se come en silencio las horas que deberías estar dedicando a las
postulaciones que sí importan. Hacerlo mal te cuesta entrevistas. Hacerlo bien
te cuesta la semana.

Así que escribí todas las reglas que había aprendido de la manera cara — las que
vinieron de rechazos, de postulaciones que se esfumaron, de un aviso que leí
mal — y las convertí en una skill. Ahora la parte repetitiva corre sola y yo
pongo la atención donde hace falta una persona.

La construí para mi propia búsqueda. La publico porque nadie debería tener que
reaprender estas reglas de a una postulación perdida por vez.

## Qué hace

| Fase | Qué obtenés | Necesita navegador |
|---|---|---|
| 1. Auditoría del CV | Los 20 puestos para los que sos mejor candidato, las palabras clave ATS que deberías incluir, qué se ve en 10 segundos y un puntaje del 1 al 10 con el camino para subirlo | no |
| 2. CV maestro | Tu CV reconstruido con la fórmula XYZ, listo para ATS, dos páginas, con variantes de resumen intercambiables — entregado en `.docx` y `.pdf` | no |
| 3. Búsqueda | Todas las vacantes que encajan en tus plataformas, rankeadas, con puntaje de compatibilidad y las palabras clave que pide cada una | sí |
| 4. Postulación | CV y carta a medida por vacante, formularios completados, postulaciones registradas, reporte final | sí |
| 5. LinkedIn | Tu perfil alineado con el CV reescrito | sí |
| 6. Correo | Respuestas, vacantes nuevas y acuses automáticos clasificados — se dispara cuando quieras con "revisá mi mail" | sí |

Cada fase termina con un reporte y una pregunta. Nada corre de punta a punta por
su cuenta, y nada se envía sin que lo veas antes.

## Requisitos

Las fases 1 y 2 corren en cualquier lugar donde corran las skills de Claude.

Las fases 3 a 6 manejan un navegador real usando tus sesiones ya iniciadas, así
que necesitan alguna de estas:

- **Claude en Chrome** (panel lateral) — plan pago, solo Chrome o Edge de escritorio
- **Claude Cowork** en la aplicación de escritorio
- **Claude Code** iniciado con `claude --chrome`

Si no tenés ninguna, la skill se detiene después de la fase 2 y te entrega los
archivos con instrucciones para postular a mano. Eso es un resultado completo,
no una falla.

## Instalación

### Desde la interfaz — sin descargar nada, sin terminal

El camino más fácil, y el que corresponde para la mayoría.

1. En Claude, abrí **Personalizar → Plugins**
2. Tocá **+** → **Agregar marketplace** → **Agregar desde un repositorio**
3. Pegá `atarico/fix-cv-find-job-skill` y confirmá
4. Instalá el plugin

Eso es todo. Instalar el plugin activa la skill, y funciona igual que una
subida a mano.

Los plugins se habilitan por cuenta, así que hacer esto una vez desde claude.ai
también cubre el panel lateral de Claude en Chrome y Claude Cowork en
escritorio — no hay que configurar cada uno por separado.

### Subir el zip

Los plugins corren en Cowork, en el panel lateral de Chrome y en Claude Code,
pero **no en el chat común de claude.ai**. Si ahí es donde trabajás, instalala
como habilidad:

1. Descargá `fix-cv-find-job-skill.zip` desde
   [Releases](https://github.com/atarico/fix-cv-find-job-skill/releases), o
   generalo vos mismo con `./scripts/package.sh`
2. Andá a **Configuración → Habilidades → Subir habilidad**
3. Seleccioná el zip. Se ejecuta un análisis de seguridad al guardar.

### Desde la terminal

```
/plugin marketplace add atarico/fix-cv-find-job-skill
/plugin install fix-cv-find-job-skill@fix-cv-find-job
```

O en Claude Code, directo desde un clon:

```bash
git clone https://github.com/atarico/fix-cv-find-job-skill.git
ln -s "$PWD/fix-cv-find-job-skill/skills/fix-cv-find-job-skill" ~/.claude/skills/
```

## Cómo usarla

### Antes de empezar

- Tu CV en cualquier formato — PDF, Word o pegado como texto. Si no tenés uno,
  un enlace a tu perfil profesional sirve para arrancar.
- Para las fases de búsqueda: tené la **sesión iniciada** en los portales de
  empleo donde quieras buscar, en el mismo navegador. Esta skill nunca crea
  cuentas ni ingresa contraseñas.

### Cómo se arranca

No hay ningún comando que recordar. Adjuntá tu CV y escribí lo que querés:

> revisá mi CV · buscame trabajo · revisá mi mail

Te responde en el idioma en el que le escribas.

### Qué pasa, paso a paso

**1. Te pide lo que necesita.** Tu CV, y en qué superficie de Claude estás — la
respuesta define si las fases con navegador están disponibles.

**2. Recibís la auditoría.** Veinte puestos para los que sos mejor candidato,
divididos en directos, adyacentes y de salto; las palabras clave ATS que
deberías incluir, marcadas como presentes, débiles o faltantes; qué ve un
reclutador en los primeros diez segundos; y un puntaje del 1 al 10 con su
desglose y el camino para subirlo.

Ahí se detiene y te pregunta si reescribe.

**3. Recibís el CV maestro.** Cada viñeta reconstruida con la fórmula XYZ —
resultado, número, método — sin lenguaje vago ni pasivo, con las palabras clave
incorporadas, dos páginas, y varias variantes de resumen intercambiables para
reorientarlo según la vacante. Entregado en `.docx` y `.pdf`.

Si no tenés navegador disponible, acá termina, y te entrega los archivos más las
instrucciones para postular a mano. Eso es un resultado completo.

**4. Releva el mercado.** Te pregunta qué plataformas usás, tus pretensiones
salariales, a qué seniority apuntás y tus descalificadores duros — los
requisitos que realmente no podés cumplir. Después busca, puntúa cada vacante y
te da una tabla ordenada de mejor a peor, más la lista de lo que descartó y por
qué.

Ahí se detiene y te pregunta si postula.

**5. Postula.** CV y carta a medida por vacante, formularios completados, todo
registrado. Primero te pregunta si querés aprobar los envíos todos juntos al
final o de a uno.

**6. LinkedIn y correo, si los querés.** Perfil alineado con el CV nuevo;
bandeja de entrada clasificada en respuestas reales, vacantes nuevas y acuses
automáticos.

### Respondé con honestidad cuando pregunte

La auditoría y los puntajes de compatibilidad valen lo que vale lo que le
cuentes. Si exagerás tu seniority o escondés un descalificador, te va a mandar a
entrevistas que no podés pasar. Nunca inventa nada que no le hayas dado — lo que
también significa que no puede arreglar lo que vos informes mal.

### Disparar la revisión de correo por separado

No hace falta correr todo el flujo. En cualquier momento, en cualquier
conversación:

> revisá mi mail

Clasifica respuestas, vacantes nuevas y acuses, y te pasa el reporte.

### Mantener la campaña entre sesiones

El panel lateral de Chrome no tiene disco persistente, así que nada se conserva
por su cuenta. Al final de cada sesión la skill genera un **brief de campaña** —
descargalo y adjuntalo la próxima vez. Restaura tu perfil, tus objetivos, todo a
lo que postulaste y todo lo que quedó trabado.

También evita la falla más común de una búsqueda larga: postular dos veces al
mismo puesto.

## Lo que no va a hacer

Estos límites están incorporados y no son configurables.

- Crear cuentas, ingresar contraseñas o autenticarse con SSO
- Resolver CAPTCHAs
- Inventar datos personales, fechas, credenciales o experiencia
- Declarar habilidades o títulos que no estén en tu CV
- Enviar correos en tu nombre — los redacta, vos los mandás
- Aceptar una oferta, acordar condiciones o negociar
- Borrar correo de forma definitiva — los acuses van a Papelera, recuperables
- Abrir tu correo personal

También respeta los avisos que prohíben postulaciones asistidas por IA: los
marca y te los deja a vos.

### Dos cosas para saber

**Cada envío de formulario se detiene a pedir tu aprobación.** Claude siempre
pregunta antes de enviar un formulario o compartir datos personales. Es una
regla de la plataforma y no se puede desactivar. La skill te pregunta al
principio si querés aprobar todo junto al final o de a uno — pero una corrida
completamente desatendida no es posible, y cualquier herramienta que te prometa
lo contrario te está engañando.

**La revisión de correo es una primera pasada.** La skill decide qué abrir según
el remitente y el asunto, así que se le van a escapar mensajes redactados de
forma inusual. Revisá tu bandeja igual.

## Contribuir

Las reglas que están en `references/` son la sustancia de esta skill — la
mayoría se pagaron con postulaciones perdidas. Si tu rubro funciona distinto, o
aprendiste algo de la manera cara, abrí un issue o un PR.

Especialmente bienvenidos: convenciones de selección propias de cada rubro,
normas regionales de CV, particularidades de cada plataforma, y reglas que te
salvaron de un error.

## Licencia

Apache-2.0

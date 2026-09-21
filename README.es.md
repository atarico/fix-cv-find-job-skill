> 🇬🇧 **[Documentation in English](README.md)**

<div align="center">

# fix-cv-find-job-skill

**Arregla tu CV y te encuentra trabajo.**

[![Licencia](https://img.shields.io/badge/licencia-Apache--2.0-blue.svg)](LICENSE)
[![Versión](https://img.shields.io/badge/versi%C3%B3n-0.3.2-blue.svg)](.claude-plugin/plugin.json)
[![Fases](https://img.shields.io/badge/fases-6-blue.svg)](#seis-fases-ninguna-corre-sola)
[![Rubro](https://img.shields.io/badge/rubro-cualquiera-blue.svg)](skills/fix-cv-find-job-skill/SKILL.md)
[![Sin navegador](https://img.shields.io/badge/fases%20sin%20navegador-2%2F6-blue.svg)](#requisitos)

</div>

---

Una **skill de Claude** que audita tu CV como lo haría un reclutador, lo
reescribe como **plantilla maestra**, busca vacantes en los portales que usás,
postula por vos, alinea tu **LinkedIn** y clasifica tu correo buscando
respuestas. Sirve para **cualquier rubro** — deduce tu campo a partir de tu
propio CV en lugar de asumir que trabajás en tecnología.

Redacta, busca y postula por vos. Nunca envía, acepta ni decide nada sin que
lo veas antes.

Una corrida de la fase 1 se ve así (recortada a la forma, no a la lista
completa de 20 puestos):

```
Reading this as: mid-level logistics coordinator, targeting supply chain roles.
Correct me if that's the wrong market.

ROLES (20, ranked)
  DIRECT    Supply Chain Coordinator
  ADJACENT  Procurement Analyst
  STRETCH   Logistics Operations Manager

ATS KEYWORDS
  present   WMS (Warehouse Management System)
  weak      vendor negotiation — implied, never stated
  missing   Six Sigma — experience is there, the CV never names it

SCREENER (10-second read)
  "results-oriented professional" opens the summary — a phrase 40% of this
  pile also uses. It buys you nothing and costs you your best line.

SCORE   6/10 — ATS compatibility and quantification are dragging the average
  down. Ceiling without a certification you don't have yet: 8/10.
```

## Índice

- [Por qué existe](#por-qué-existe)
- [Seis fases, ninguna corre sola](#seis-fases-ninguna-corre-sola)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
  - [Desde la interfaz — sin descargar nada, sin terminal](#desde-la-interfaz--sin-descargar-nada-sin-terminal)
  - [Subir el zip](#subir-el-zip)
  - [Desde la terminal](#desde-la-terminal)
- [Cómo se usa realmente](#cómo-se-usa-realmente)
  - [Antes de empezar](#antes-de-empezar)
  - [Cómo se arranca](#cómo-se-arranca)
  - [Qué pasa, paso a paso](#qué-pasa-paso-a-paso)
  - [Respondé con honestidad cuando pregunte](#respondé-con-honestidad-cuando-pregunte)
  - [Disparar la revisión de correo por separado](#disparar-la-revisión-de-correo-por-separado)
  - [Mantener la campaña entre sesiones](#mantener-la-campaña-entre-sesiones)
- [Lo que no va a hacer](#lo-que-no-va-a-hacer)
  - [Dos cosas para saber](#dos-cosas-para-saber)
- [Ajustá tus expectativas](#ajustá-tus-expectativas)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

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

## Seis fases, ninguna corre sola

| Fase | Qué obtenés | Necesita navegador |
|---|---|---|
| 1. Auditoría del CV | Los 20 puestos para los que sos mejor candidato, las palabras clave ATS que deberías incluir, qué se ve en 10 segundos y un puntaje del 1 al 10 con el camino para subirlo | no |
| 2. CV maestro | Tu CV reconstruido con la fórmula XYZ, listo para ATS, dos páginas, con variantes de resumen intercambiables — entregado en `.docx`, `.pdf` y Markdown | no |
| 3. Búsqueda | Todas las vacantes que encajan en tus plataformas, rankeadas, con puntaje de compatibilidad y las palabras clave que pide cada una | sí |
| 4. Postulación | CV y carta a medida por vacante, formularios completados, postulaciones registradas, reporte final | sí |
| 5. LinkedIn | Tu perfil alineado con el CV reescrito | sí |
| 6. Correo | Respuestas, vacantes nuevas y acuses automáticos clasificados — se dispara cuando quieras con "revisá mi mail" | sí |

Cada fase termina con un reporte y una pregunta. Nada corre de punta a punta por
su cuenta, y nada se envía sin que lo veas antes.

## Requisitos

Dos cosas independientes deciden qué podés correr: tu **plan** y la
**superficie** en la que estás.

**Plan.** Las fases 1 y 2 — la auditoría del CV y la reescritura del CV
maestro — corren con el plan gratuito, en el chat común, actives o no
**Code execution and file creation** en **Configuración → Capacidades**: si
la activás, obtenés el `.docx`, el `.pdf` y el Markdown terminados; si la
dejás apagada, obtenés el CV reescrito como texto en el chat. Las fases 3 a 6
necesitan una superficie con navegador, y cada una de esas superficies
necesita un plan pago.

**Superficie**, para las fases 3 a 6, necesita alguna de estas:

- **Claude en Chrome** (panel lateral) — cualquier plan pago, solo Chrome de
  escritorio
- **Claude Cowork** en la aplicación de escritorio
- **Claude Code** iniciado con `claude --chrome`

Si no tenés ninguna — incluido si estás en el plan gratuito — la skill se
detiene después de la fase 2 y te entrega los archivos con instrucciones para
postular a mano. **Eso es un resultado completo, no una falla.**

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
2. Andá a **Personalizar → Habilidades** (*Customize → Skills*), tocá **+** y
   después **Crear habilidad → Subir una habilidad**. La ruta es la misma en
   todos los planes, incluido el gratuito.
3. Seleccioná el zip. Se ejecuta un análisis de seguridad al guardar.

### Desde la terminal

```
/plugin marketplace add atarico/fix-cv-find-job-skill   # registra este repo como fuente de plugins
/plugin install fix-cv-find-job-skill@fix-cv-find-job   # instala la skill desde ahí
```

O en Claude Code, directo desde un clon:

```bash
git clone https://github.com/atarico/fix-cv-find-job-skill.git
ln -s "$PWD/fix-cv-find-job-skill/skills/fix-cv-find-job-skill" ~/.claude/skills/   # symlink para que ~/.claude/skills la detecte
```

## Cómo se usa realmente

### Antes de empezar

- Tu CV en cualquier formato — PDF, Word o pegado como texto. Si no tenés uno,
  un enlace a tu perfil profesional sirve para arrancar.
- **Un navegador que Claude pueda manejar**, para las fases 3 a 6. El camino
  habitual es la [extensión de Claude para Chrome](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn) — instalala e iniciá
  sesión antes de arrancar. Claude Cowork y `claude --chrome` hacen lo mismo;
  mirá [Requisitos](#requisitos) para las tres y para qué pasa si no tenés
  ninguna.
- Para las fases de búsqueda: tené la **sesión iniciada** en los portales de
  empleo donde quieras buscar, en el mismo navegador. Esta skill nunca crea
  cuentas ni ingresa contraseñas.

### Cómo se arranca

No hay ningún comando que recordar. Adjuntá tu CV y escribí lo que querés:

> revisá mi CV · buscame trabajo · revisá mi mail

Te responde en el idioma en el que le escribas.

### Qué pasa, paso a paso

**1. Te pide lo que necesita.** Tu CV, un brief de campaña si tenés uno de una
sesión anterior, y en qué superficie de Claude estás — la respuesta define si
las fases con navegador están disponibles. Si adjuntás un brief, retoma
exactamente donde quedó esa sesión, sin repetir la auditoría ni la reescritura;
si adjuntás un brief junto con un CV nuevo, te pregunta una sola vez si querés
correr la auditoría y la reescritura sobre el nuevo.

**2. Recibís la auditoría.** Veinte puestos para los que sos mejor candidato,
divididos en directos, adyacentes y de salto; las palabras clave ATS que
deberías incluir, marcadas como presentes, débiles o faltantes; qué ve un
reclutador en los primeros diez segundos; y un puntaje del 1 al 10 con su
desglose y el camino para subirlo.

Ahí se detiene y te pregunta si reescribe.

**3. Recibís el CV maestro.** Cada viñeta reconstruida con la fórmula XYZ —
resultado, número, método — sin lenguaje vago ni pasivo, con las palabras clave
incorporadas, dos páginas, y varias variantes de resumen con nombre propio —
una por especialización de la auditoría — para reorientarlo según la vacante
eligiendo por nombre. Se construye en cada idioma en el que trabajás; el CV en
sí nunca sigue el idioma de una vacante puntual, eso solo pasa con las copias a
medida del paso 5. Entregado en `.docx`, `.pdf` y Markdown, un conjunto por
idioma.

Si no tenés navegador disponible, acá termina, y te entrega los archivos más las
instrucciones para postular a mano. Eso es un resultado completo.

**4. Releva el mercado.** Te pregunta qué plataformas usás, tus pretensiones
salariales como una tabla por seniority y mercado (si no tenés un número,
busca un rango y lo confirma con vos), a qué seniority apuntás — y que no vas a
postular por debajo de eso — y tus descalificadores duros, los requisitos que
realmente no podés cumplir. Después busca, puntúa cada vacante y te da una
tabla ordenada de mejor a peor, más la lista de lo que descartó y por qué, con
la frase textual de cada aviso como evidencia de cada descalificador que se
activó.

Ahí se detiene y te pregunta si postula.

**5. Postula.** CV y carta a medida por vacante, en el idioma de cada aviso,
formularios completados, todo registrado — incluido el puntaje de
compatibilidad. Los duplicados se chequean con el método propio de cada
plataforma antes de completar nada. Primero te pregunta si querés aprobar los
envíos todos juntos al final o de a uno.

**6. LinkedIn y correo, si los querés.** Perfil alineado con el CV nuevo;
bandeja de entrada clasificada en respuestas reales, vacantes nuevas y acuses
automáticos.

### Respondé con honestidad cuando pregunte

**La auditoría es un espejo, no un oráculo.** La auditoría y los puntajes de
compatibilidad valen lo que vale lo que le cuentes. Si exagerás tu seniority o
escondés un descalificador, te va a mandar a entrevistas que no podés pasar.
No puede inventar un título, un puesto, una fecha, una herramienta, una
métrica ni un empleador que no le hayas dado — lo que también significa que no
puede arreglar lo que vos informes mal.

### Disparar la revisión de correo por separado

No hace falta correr todo el flujo. En cualquier momento, en cualquier
conversación:

> revisá mi mail

Clasifica respuestas, vacantes nuevas y acuses, y te pasa el reporte.

### Mantener la campaña entre sesiones

El panel lateral de Chrome no tiene disco persistente, así que nada se conserva
por su cuenta. Al final de cada sesión la skill genera un **brief de campaña** —
descargalo y adjuntalo la próxima vez. Restaura tu perfil, tus objetivos, todo a
lo que postulaste y todo lo que quedó trabado — y retoma exactamente donde el
brief dice que quedó la última sesión, así que la auditoría del CV y la
reescritura del CV maestro nunca vuelven a correr una vez que el brief las
marca como hechas.

Si adjuntás un CV nuevo junto con un brief existente, te pregunta una sola vez
si querés volver a correr la auditoría y la reescritura sobre ese CV; si le
decís que no, conserva el CV maestro que ya tenías y va directo a buscar o
postular.

También evita la falla más común de una búsqueda larga: postular dos veces al
mismo puesto.

## Lo que no va a hacer

Estos límites están incorporados y no son configurables.

- Crear cuentas, ingresar contraseñas o autenticarse con SSO
- Resolver CAPTCHAs
- Inventar datos personales, fechas, credenciales o experiencia
- Inventar una cifra de salario — solo usa lo que confirmaste vos o un rango de
  mercado que aceptaste
- Declarar habilidades o títulos que no estén en tu CV
- Postular por debajo del piso de seniority que fijaste, aunque el aviso
  puntúe bien por lo demás
- Enviar correos en tu nombre — los redacta, vos los mandás
- Aceptar una oferta, acordar condiciones o negociar
- Borrar correo de forma definitiva — los acuses van a Papelera, recuperables
- Abrir tu correo personal

También respeta los avisos que prohíben postulaciones asistidas por IA: los
marca y te los deja a vos.

### Dos cosas para saber

**¿Te preguntás si una corrida puede ir completamente desatendida? No puede, y
acá está el porqué.** Claude siempre pregunta antes de enviar un formulario o
compartir datos personales. Es una regla de la plataforma y no se puede
desactivar. La skill te pregunta al principio si querés aprobar todo junto al
final o de a uno — pero una corrida completamente desatendida no es posible, y
cualquier herramienta que te prometa lo contrario te está engañando.

**La revisión de correo es una primera pasada.** La skill decide qué abrir según
el remitente y el asunto, así que se le van a escapar mensajes redactados de
forma inusual. Revisá tu bandeja igual.

## Ajustá tus expectativas

Esta skill te ayuda a pasar filtros y a poner tu atención donde importa. No te
garantiza un trabajo, y no puede garantizarte que sea pronto. No es infalible
y no te va a dar cien entrevistas en dos semanas — ninguna herramienta hace
eso, y cualquiera que lo prometa no te está diciendo la verdad.

Está pensada para correrse de manera repetida, no una sola vez: los puntos de
entrada independientes para el correo y para la búsqueda existen porque las
vacantes y las respuestas cambian todo el tiempo, y la detección de
duplicados existe justamente porque se espera que vuelvas a correrla, no
porque sea una excepción. Corré esta skill al menos una vez por día si querés
que cubra lo que cambió desde ayer.

Y respaldá lo que escribe. Las reglas de esta skill prohíben agregar un
título, un puesto, una fecha, una herramienta, una métrica o un empleador que
vos no hayas dado — cada afirmación del CV maestro sale de algo que dijiste.
Eso no la hace infalible: puede igual reformular o poner el énfasis donde no
corresponde, y el nombre que va en la hoja es el tuyo. Leé el CV maestro antes
de que salga a cualquier lado y confirmá que refleja tu situación real. Si una
línea no aguanta una entrevista, sacala antes de que un reclutador se dé
cuenta por vos.

## Contribuir

Las reglas que están en `references/` son la sustancia de esta skill — la
mayoría se pagaron con postulaciones perdidas. Si tu rubro funciona distinto, o
aprendiste algo de la manera cara, abrí un issue o un PR.

> **Una regla nueva necesita un costo real detrás — un rechazo, una
> postulación perdida, un aviso mal leído — no una suposición sobre lo que
> podría funcionar.**

Especialmente bienvenidos: convenciones de selección propias de cada rubro,
normas regionales de CV, particularidades de cada plataforma, y reglas que te
salvaron de un error.

## Licencia

Apache-2.0. Ver [`LICENSE`](LICENSE).

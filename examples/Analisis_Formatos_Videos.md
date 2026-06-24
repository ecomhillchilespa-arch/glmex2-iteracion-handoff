# Análisis de Formatos de Video — Biblioteca de Referencia para Ads
> 39 ads de respuesta directa (ecom/suplementos) analizados con ffmpeg + visión frame-a-frame. Para cada video: formato/género, hook, estructura, ritmo de edición (cortes/plano medio), recursos visuales, estilo de subtítulos, audio, CTA y nivel de recreabilidad. Pensado para pasarse a Claude (web) como swipe-file y guía de producción.

---

## 1. SÍNTESIS — patrones transversales

**Specs comunes:** casi todos **9:16 vertical, 720x1280, 30 fps, H.264 + AAC**. Excepciones: algunos 4:5 (720x900/892/960) y 1:1 (720x720); dos en baja resolución 360p (UGC nativo de móvil); 3 a 24–25 fps. **Audio wall-to-wall** (VO o música sin pausas) en la gran mayoría — el silencio largo casi no existe en DR.

**Los 4 arquetipos de formato que se repiten:**

1. **UGC / talking-head con cara real** — testimonio, founder-led, o "experto". Cámara selfie/trípode, jump-cuts, subtítulos karaoke. *Lo más barato y escalable.* (ej. 10038 enfermera, c51 grüns, e26 founder creatina, ac4 podcast testo, 495 próstata, 10f vet perros, d2b7 Moonbrew).
2. **CGI / IA animado (claymation–Pixar / villano-héroe / mascota de órgano)** — 100% generado, sin rodaje. Kinetic text de una palabra, VO IA, personajes que personifican el problema o el producto. *El más caro/técnico pero infinitamente escalable.* (ej. 262 magnesio, 92e7 tiroides, 412 VisionPure villano-jeringa, eb8b shampoo-villano DHT, 4eb8 linfático, e14f circulación, 264c claymation tiroides).
3. **VSL larga (3–6 min) problema→mecanismo→autoridad→prueba social→CTA** — story-driven o insider-médico, mucho b-roll/CGI intercalado o un plano casi fijo. (ej. 0ca4 cataratas-arrepentimiento, 12a fungus NASA, f4d9 articular portugués, a2615 esqueleto).
4. **Híbrido / formatos especiales** — split-screen reacción de médico (70b3, c50f derma), fake news + avatar IA (4f32), lead-magnet PDF gratis (d5a Tai Chi), demo física de producto (9ff8 filtro ducha), before/after slideshow (e15b nutravia).

**Hooks que más se repiten (tácticas):**
- "Secreto que te ocultan" / anti-establishment ("Urologists don't want you to know", "PRE DIABETES escúchame").
- Personificar al enemigo (jeringa villana, DHT villano, hormona).
- Invalidar lo que ya usas ("toothpaste/vinegar you're making it worse", "water/lozenges slide right past").
- Confesión negativa / arrepentimiento ("My biggest regret is agreeing to cataract surgery").
- Pregunta de curiosidad + condición específica ("Watch this if you have Melasma", "What's happening inside your anxious dog's brain?").
- Cifra-shock en formato podcast ("300 to 900 testosterone jump").
- Pattern-interrupt absurdo/humor (esqueleto comiendo plátano, "your kidneys left a voicemail 📞").

**Subtítulos:** dominan dos estilos — (a) **karaoke caption** mayúsculas con palabra clave resaltada en amarillo/azul (DR clásico), y (b) **una palabra por corte** centrada (CGI/TikTok). El texto SIEMPRE quemado en edición.

**Cierres/CTA:** los largos usan CTA duro ("CLICK BELOW", "TAP THE SCREEN", "HAZ CLIC ABAJO"); los cortos cierran por **garantía/risk-reversal** ("90 day money back", "risk free") o prueba social. Lead-magnets cierran con "FREE PDF".

**Ritmo (cortes/plano medio):** rango enorme. Desde **~0.7–1.2 s/plano** (demos y CGI hipercortados: 9ff8 filtro 0.68s, e26 founder 0.85s, bf1a 1.2s, 12a 1.5s) hasta **VSL de plano casi único** (0ca4 con 2 cortes en 6min, f4d9 4 cortes en 3.5min, 10f 2 cortes, ac4 2 cortes). Regla observada: **CGI y demos cortan rapidísimo; talking-head testimonial deja planos largos.**

**Idiomas:** inglés (mayoría), español neutro/LatAm (9ff8 ducha, f204 berberina, e15b nutravia), español MX, francés (54b perros), portugués BR (f4d9 articular). Mismo formato, distinto idioma = patrón de localización.

**Nichos detectados:** salud ocular/cataratas (muchísimos), suplementos (tiroides, riñón, magnesio, creatina, berberina, próstata, articular, linfático), skincare (melasma, ojeras, antiedad), salud de mascotas (dental perros, ansiedad perros), pérdida de peso, crecimiento capilar, fitness senior.

---

## 2. TAXONOMÍA — formatos y subformatos

> Los 39 ads clasificados en 4 familias de formato y sus subformatos. Cada video aparece una vez en su categoría principal (varios son híbridos; se nota cuando aplica). El prefijo del nombre de archivo refleja esta taxonomía.

### A. UGC / TALKING-HEAD CON CARA REAL — *(persona real, lo más barato y escalable)*
- **A1. Testimonial selfie** (auto/casa, recomendación personal): `UGC-testimonial_gruns-gummies_c51a` · `UGC_Moonbrew-sueno-magnesio_d2b7` · `UGC-testimonial_prostata-secreto_495f`
- **A2. Founder-led** (el fundador muestra fábrica/proceso): `UGC-founder_creatina-fabrica_e269`
- **A3. Experto/autoridad cara-a-cámara** (bata, diplomas de fondo): `UGC-experto_dental-perros_10f1`
- **A4. Demo física de producto** (antes/después tangible, aplicación): `UGC-ES_demo-ducha-filtrante_9ff8` · `UGC_corrector-ojeras-EyeCorrect_c5ac`
- **A5. Sketch cómico** (pattern-interrupt con humor + props): `UGC-sketch_astaxantina-rinon_fa90`
- **A6. Before/after slideshow móvil** (fotos reales encadenadas): `UGC-ES_antesdespues-nutravia_e15b`
- **A7. Listicle UGC corto** (lista de beneficios numerada): `UGC_creatina-listicle-10s_343c`
- **A8. UGC + CGI científico** (cara real intercalada con animación de mecanismo): `UGC-CGI_skincare-seabuckthorn_518f` · `UGC-CGI_spray-ocular-luteina_d4fc`

### B. CGI / IA ANIMADO — *(100% generado, sin rodaje; caro/técnico pero infinitamente escalable)*
- **B1. Villano-héroe** (personifica al enemigo vs. al producto): `CGI-villano_jeringa-VisionPure-ojos_412f` · `CGI-villano_DHT-shampoo-Spartan_eb8b`
- **B2. Mascota de órgano/producto** (claymation–Pixar, personaje tierno): `CGI-mascota_tiroides-ACTORA_92e7` · `CGI-claymation_tiroides_264c` · `CGI-claymation_mascota-creatina_7f41` · `CGI-claymation_circulacion-pies_e14f`
- **B3. Mecanismo "how it works"** (cuerpo por dentro, partículas, glow): `CGI_mecanismo-magnesio_262b` · `CGI_drenaje-linfatico-LYMPHORIA_4eb8` · `CGI-VSL_metabolismo-perdida-peso_7b4f`
- **B4. Lyric-video / kinetic text** (mascots + jingle cantado, letra = copy): `CGI-mascots_skincare-creatina-lyric_6604`
- **B5. Surrealista / metáfora visual** (concepto absurdo como hook): `CGI-surrealista_esqueleto-huesos_a261`
- **B6. Avatar IA fotorrealista** (fake news / news anchor + lip-sync): `FakeNews-avatarIA_vision-sanadora_4f32`

### C. VSL LARGA (1.5–6 min) — *(estructura problema→mecanismo→autoridad→prueba social→CTA)*
- **C1. Story-driven testimonial** (plano casi fijo, todo lo carga el guion): `VSL_cataratas-arrepentimiento_0ca4`
- **C2. Insider / "doctor revela secreto"** (mucho b-roll, conspirativo): `VSL_hongo-unas-NASA_12a7`
- **C3. Mecanismo educativo** (ingredientes uno a uno + b-roll científico): `VSL_mecanismo-garganta-EsoRepair_1b75`
- **C4. Podcast / talking-head largo** (una sola toma, retención por curiosidad): `VSL-PT_dolor-articular-podcast_f4d9`
- **C5. Testimonial-autoridad UGC** (enfermera/paciente en selfie, VSL): `VSL_enfermera-astaxantina-rinon_1003`
- **C6. Médico-autoridad escenificado** (set de farmacia/herbolario): `Medico-herbolario-ES_berberina_f204`
- **C7. VSL/PAS con b-roll demostrativo** (talking-head + intercut rápido): `VSL-FR_dental-perros-spray_54b3`
- **C8. Híbrido dramatizado** (story con actor IA + coach real): `VSL_fitness-calistenia-actorIA_7c78`

### D. HÍBRIDOS / FORMATOS ESPECIALES
- **D1. Split-screen reacción** (médico reacciona a un clip, estilo duet/stitch): `SplitScreen-medico_cataratas_70b3`
- **D2. Clip de podcast** (split-screen entrevista, cifra-shock): `Podcast_testosterona-MarsMen_ac4f`
- **D3. Advertorial** (warning card + animación médica + escena de consulta): `Advertorial_spray-cataratas-luteina_bf1a`
- **D4. Lead-magnet** (regala un PDF/recurso gratis, captación): `LeadMagnet_PDF-ChairTaiChi_d5af`
- **D5. Listicle de autoridad** (experto rankea/aprueba N opciones): `Listicle_dermatologo-6-ojeras_c50f`
- **D6. Autoridad + prueba social masiva** (experta + carrusel de testimonios + diagramas): `Skincare_melasma-experta_63ee`
- **D7. Mecanismo educativo con prueba científica** (estudio citado + b-roll): `Mecanismo_ansiedad-perros-JAVMA_a177`

**Conteo:** A=12 · B=12 · C=8 · D=7 → 39 videos.

---

## 3. TABLA TÉCNICA (ffprobe)

| Archivo | Dur | Resolución | Aspect | FPS | Bitrate | Formato (resumen) |
|---|---|---|---|---|---|---|
| VSL_cataratas-arrepentimiento_0ca4.mp4 | 6:17 | 720x1280 | 9:16 | 30 | 1461k | VSL cataratas-arrepentimiento (plano fijo) |
| VSL_enfermera-astaxantina-rinon_1003.mp4 | 5:21 | 720x1280 | 9:16 | 30 | 809k | VSL enfermera astaxantina (autoridad) |
| UGC-experto_dental-perros_10f1.mp4 | 2:23 | 720x892 | ~4:5 | 30 | 585k | UGC vet dental perros (plano único) |
| VSL_hongo-unas-NASA_12a7.mp4 | 4:08 | 720x900 | 4:5 | 30 | 976k | VSL hongo uñas "ex-NASA/Book of John" |
| VSL_mecanismo-garganta-EsoRepair_1b75.mp4 | 1:50 | 720x900 | 4:5 | 30 | 1218k | VSL mecanismo garganta/esófago EsoRepair |
| CGI_mecanismo-magnesio_262b.mp4 | 0:17 | 720x1280 | 9:16 | 30 | 1866k | CGI mecanismo magnesio (corto) |
| CGI-claymation_tiroides_264c.mp4 | 1:31 | 720x1280 | 9:16 | 30 | 879k | CGI claymation tiroides/Hashimoto |
| UGC_creatina-listicle-10s_343c.mp4 | 0:10 | 720x1280 | 9:16 | 30 | 925k | UGC creatina (listicle 10s) |
| CGI-villano_jeringa-VisionPure-ojos_412f.mp4 | 0:47 | 480x854 | 9:16 | 30 | 1050k | CGI villano-jeringa VisionPure (luteína ojos) |
| UGC-testimonial_prostata-secreto_495f.mp4 | 0:42 | 720x720 | 1:1 | 30 | 1149k | UGC próstata "urologists don't want you" |
| CGI_drenaje-linfatico-LYMPHORIA_4eb8.mp4 | 2:54 | 720x1280 | 9:16 | 30 | 1643k | CGI drenaje linfático LYMPHORIA |
| FakeNews-avatarIA_vision-sanadora_4f32.mp4 | 2:59 | 720x1276 | 9:16 | 30 | 1098k | Fake news + avatar IA sanadora (visión) |
| UGC-CGI_skincare-seabuckthorn_518f.mp4 | 0:46 | 720x1280 | 9:16 | 30 | 2053k | UGC+CGI skincare sea buckthorn |
| VSL-FR_dental-perros-spray_54b3.mp4 | 2:19 | 360x450 | ~4:5 | 30 | 339k | VSL francés spray dental perros |
| Skincare_melasma-experta_63ee.mp4 | 3:02 | 720x1280 | 9:16 | 30 | 1069k | Skincare melasma experta+testimonios |
| CGI-mascots_skincare-creatina-lyric_6604.mp4 | 1:04 | 720x1280 | 9:16 | 24 | 1593k | CGI mascots skincare/creatina (lyric-video) |
| SplitScreen-medico_cataratas_70b3.mp4 | 2:14 | 720x1280 | 9:16 | 30 | 1057k | Split-screen médico reacciona (cataratas) |
| CGI-VSL_metabolismo-perdida-peso_7b4f.mp4 | 2:01 | 720x1280 | 9:16 | 30 | 1114k | CGI VSL metabolismo/pérdida de peso |
| VSL_fitness-calistenia-actorIA_7c78.mp4 | 2:12 | 720x1280 | 9:16 | 25 | 1126k | VSL fitness calistenia (actor IA + coach) |
| CGI-claymation_mascota-creatina_7f41.mp4 | 1:39 | 720x960 | ~4:5 | 30 | 775k | CGI claymation mascota-creatina |
| CGI-mascota_tiroides-ACTORA_92e7.mp4 | 0:44 | 720x1280 | 9:16 | 30 | 925k | CGI mascota tiroides ACTORA |
| UGC-ES_demo-ducha-filtrante_9ff8.mp4 | 1:13 | 720x1280 | 9:16 | 30 | 1463k | UGC demo cabezal ducha filtrante (ES) |
| Mecanismo_ansiedad-perros-JAVMA_a177.mp4 | 1:55 | 720x1280 | 9:16 | 30 | 1390k | Mecanismo ansiedad perros (JAVMA 89%) |
| CGI-surrealista_esqueleto-huesos_a261.mp4 | 3:58 | 720x1280 | 9:16 | 30 | 1442k | CGI surrealista esqueleto (huesos/IA) |
| Podcast_testosterona-MarsMen_ac4f.mp4 | 1:04 | 720x1280 | 9:16 | 25 | 590k | Clip podcast testosterona Mars Men |
| Advertorial_spray-cataratas-luteina_bf1a.mp4 | 1:57 | 720x1280 | 9:16 | 30 | 1230k | Advertorial spray cataratas-luteína |
| Listicle_dermatologo-6-ojeras_c50f.mp4 | 0:54 | 720x1280 | 9:16 | 30 | 593k | Listicle dermatólogo 6 tratamientos ojeras |
| UGC-testimonial_gruns-gummies_c51a.mp4 | 0:54 | 720x1280 | 9:16 | 30 | 1530k | UGC testimonial grüns gummies |
| UGC_corrector-ojeras-EyeCorrect_c5ac.mp4 | 0:49 | 720x1280 | 9:16 | 30 | 1756k | UGC corrector ojeras EyeCorrect |
| UGC_Moonbrew-sueno-magnesio_d2b7.mp4 | 1:49 | 720x1280 | 9:16 | 30 | 1563k | UGC Moonbrew (sueño/magnesio, hook 2D) |
| UGC-CGI_spray-ocular-luteina_d4fc.mp4 | 1:08 | 720x1280 | 9:16 | 30 | 1232k | UGC+CGI spray ocular luteína (supercut) |
| LeadMagnet_PDF-ChairTaiChi_d5af.mp4 | 0:44 | 720x1280 | 9:16 | 25 | 1054k | Lead-magnet PDF Chair Tai Chi (senior) |
| CGI-claymation_circulacion-pies_e14f.mp4 | 0:56 | 720x1280 | 9:16 | 30 | 1379k | CGI claymation circulación pies/piernas |
| UGC-ES_antesdespues-nutravia_e15b.mp4 | 0:23 | 360x640 | 9:16 | 30 | 165k | UGC before/after nutravia (drenaje, ES) |
| UGC-founder_creatina-fabrica_e269.mp4 | 0:58 | 720x1280 | 9:16 | 30 | 1569k | UGC founder-led creatina (fábrica) |
| CGI-villano_DHT-shampoo-Spartan_eb8b.mp4 | 1:49 | 720x1280 | 9:16 | 30 | 1583k | CGI villano DHT shampoo Spartan |
| Medico-herbolario-ES_berberina_f204.mp4 | 2:17 | 720x1280 | 9:16 | 30 | 685k | "Médico" herbolario berberina (ES) |
| VSL-PT_dolor-articular-podcast_f4d9.mp4 | 3:33 | 720x1280 | 9:16 | 30 | 759k | VSL podcast dolor articular (PT-BR) |
| UGC-sketch_astaxantina-rinon_fa90.mp4 | 2:00 | 720x1280 | 9:16 | 30 | 1788k | UGC sketch cómico astaxantina/riñón |

---

## 4. FICHAS DETALLADAS POR VIDEO

### VSL_cataratas-arrepentimiento_0ca4.mp4
- **Specs:** ~6:17 (377.3 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** VSL narrativo de testimonio en off ("story-driven VSL") sobre salud ocular. Voz de una mujer ("Linda, 67") que cuenta su arrepentimiento tras una cirugía de cataratas y desemboca en un suplemento natural de luteína. Le habla a adultos mayores con problemas/miedo de visión que están considerando cirugía.
- **Hook (primeros 3s):** Texto en pantalla sobre b-roll de quirófano: *"My biggest regret in life is agreeing to cataract surgery... I'm just the 40% they never tell you about."* Táctica: confesión negativa + estadística contraintuitiva (el "40% oculto") + identificación con nombre y edad.
- **Estructura/beats:** Hook/confesión (0:00–0:20) → Credibilidad y contexto "cirugía rutinaria" (0:20–1:00) → Agitación del problema (visión nublada, ojos secos, gotas cada hora) (1:00–3:00) → Descubrimiento: una amiga le habla de la luteína y la absorción real de las cápsulas (~3:00) → Mecanismo / por qué funciona (3:00–5:00) → Cierre emocional + P.S. y CTA suave hacia "the natural option" (5:00–6:17).
- **Ritmo de edición:** Solo 2 cortes en 6+ min; plano medio ~3 min. Ritmo visual lentísimo: prácticamente un plano fijo de manos en cirugía en bucle; el "movimiento" lo dan los subtítulos.
- **Recursos de edición:** Un único b-roll de stock (manos operando en quirófano, tonos azul/quirúrgico) todo el video; cambio final a una persona con gorro quirúrgico. Sin zooms, sin gráficos, sin charts.
- **Texto en pantalla / subtítulos:** Bloque masivo de subtítulos blancos centrados ("wall of text" de VSL), frase a frase sincronizada con la VO. Frases: *"how much lutein actually reaches the eyes when taken orally"*, *"My sister cancelled her surgery. I can't cancel mine."*
- **Audio:** VO femenina en inglés, íntima/confesional/triste; sin silencios = VO continua con cama musical suave. Posible voz IA o actriz (cadencia uniforme).
- **CTA:** Tardío y suave (~6:00): *"Try the natural option first — because once you're on that table, the decision is permanent."* Sin botón; empuja a clic/seguir leyendo (advertorial/landing).
- **Recreabilidad:** Muy barato. 1 clip de stock de quirófano + guion largo en primera persona + VO (humana o IA) + subtítulos sincronizados. Sin actor en cámara, sin producto filmado.

### UGC_creatina-listicle-10s_343c.mp4
- **Specs:** 10.1 s, 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** UGC testimonial / demo de producto. Mujer (~40s, atlética) en la mesa de su casa probando un bote de creatina. Le habla a mujeres adultas activas (energía/recuperación).
- **Hook (primeros 3s):** A cámara, sostiene la bolsa "CREATINE MONOHYDRATE" + texto: *"I almost didn't buy this. I'm glad I did. Here's what happened..."* Táctica: objeción confesada + promesa de payoff inmediato.
- **Estructura/beats:** Hook + scoop de polvo (0–3s) → demo de mezclado/bebida (3–6s) → listicle de beneficios sobreimpreso (6–9s) → recap final con producto (9–10s).
- **Ritmo de edición:** ~4 cortes en 10 s → plano ~2.5 s. Jump-cuts sobre un solo setup.
- **Recursos de edición:** UGC handheld/trípode casero, luz natural. Jump-cuts. Card de producto en esquina inferior derecha persistente. Sin b-roll de stock ni motion graphics.
- **Texto en pantalla / subtítulos:** Titulares en caja blanca bold + listicle numerado con emojis. *"1. NO more 2pm nanna nap 😴", "2. Sharper mind", "3. Recovering faster", "4. Bloat-free", "5. I feel like myself again"*. Tono australiano coloquial.
- **Audio:** Cama musical/ambiente continuo. Probable VO de la propia creadora; tono casero.
- **CTA:** Sin CTA explícito; cierra mostrando el producto con el recap (CTA implícito).
- **Recreabilidad:** Trivial. Persona real, su cocina, el bote, un teléfono y overlays en CapCut. Ideal para batch de UGC.

### UGC-CGI_skincare-seabuckthorn_518f.mp4
- **Specs:** 46.0 s, 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad educativo de skincare ingrediente-céntrico (sea buckthorn/honey) mezclando UGC + CGI científico. Mujer madura aplicándose crema + animaciones de capas de piel + b-roll de bayas. Para mujeres maduras (hidratación/firmeza/antiedad).
- **Hook (primeros 3s):** Mujer mayor a cámara: *"You don't need JUST hydration... you also need..."* Táctica: corregir una creencia común → curiosity gap.
- **Estructura/beats:** Hook/objeción (0–4s) → ingrediente estrella "Sea buckthorn goes deeper" (4–10s) → mecanismo CGI (10–26s) → prueba/beneficios con checklist y b-roll de bayas (26–40s) → cierre + CTA (40–46s).
- **Ritmo de edición:** ~24 cortes en 46 s → plano ~1.9 s. Medio-rápido, mucha variedad de fuentes.
- **Recursos de edición:** Tres registros: UGC handheld, CGI de capas de piel/colágeno (dorado), b-roll cinemático de bayas/naranjas. Checklist con palomitas verdes.
- **Texto en pantalla / subtítulos:** Caja amarilla en el hook; luego titulares blancos bold; chips resaltados ("SOFTNESS / COMFORT / RESILIENCE").
- **Audio:** VO continua en inglés, cálida/educativa (actriz o IA) + cama musical.
- **CTA:** ~43s botón amarillo *"GET MORE INFO!"* bajo el bote. Clic-a-landing.
- **Recreabilidad:** Media. Actriz/creadora madura + packshot + b-roll de naturaleza (stock) + clips CGI de capas de piel (stock científico) que dan el aire "dermatológico".

### CGI-claymation_mascota-creatina_7f41.mp4
- **Specs:** ~1:39 (99.4 s), 720x960 retrato ~4:5, 30 fps.
- **Formato/género:** Ad animado claymation/stop-motion CGI (mascota de producto). Un bote de creatina antropomorfo (gafas, brazos musculosos) en una cocina con personajes de plastilina. Mashup demo+oferta con humor. Para público escéptico sobre creatina (mitos/efectos secundarios).
- **Hook (primeros 3s):** El personaje-bote "CREATINE" con gafas + claim **"STRONGER"** + "quick facts". Táctica: personaje llamativo + autoridad ("#1 most researched").
- **Estructura/beats:** Hook personaje (0–9s) → beneficios/servings "boost immunity" (9–20s) → objeciones "SIDE EFFECTS" + comparación con gummies (20–35s) → autoridad: doctor con bata + reseña/precio (35–50s) → más beneficios y escena social (50–75s) → b-roll dorado de ingrediente (75–88s) → cierre con badge de garantía (88–99s).
- **Ritmo de edición:** ~62 cortes en 99 s → plano ~1.6 s. Rápido, muy montado.
- **Recursos de edición:** Animación 3D/claymation (textura plastilina), sin metraje real. Cortes secos rápidos, escenas-viñeta. Overlays, badges, inserción de "producto real" (foto + captura tipo Amazon "$29"). Sello **"60 DAY MONEY BACK / 37,000+ REVIEWS"**.
- **Texto en pantalla / subtítulos:** Titulares grandes bold integrados (**"STRONGER"**, "SIDE EFFECTS") + subtítulos + badges.
- **Audio:** VO continua (narrador de beneficios) sobre música; enérgico/educativo. SFX de animación.
- **CTA:** Prueba social + garantía "60 DAY MONEY BACK / 37,000+ REVIEWS" (risk-reversal).
- **Recreabilidad:** Alta dificultad/coste. Producción de animación 3D claymation (personaje rigged, escenarios, varios personajes), guion beneficios+objeciones, VO profesional, badges. No batcheable con UGC.

### Listicle_dermatologo-6-ojeras_c50f.mp4
- **Specs:** 54.2 s, 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Listicle de reacción/review con figura de autoridad. Un dermatólogo (diplomas en la pared) valora 6 tratamientos para ojeras. Para quienes buscan soluciones de ojeras y dudan entre opciones (incl. cirugía).
- **Hook (primeros 3s):** A cámara: *"6 Undereye treatments and if they get my dermatologist approval 👍"*. Táctica: listicle numerado + autoridad médica que aprueba/reprueba.
- **Estructura/beats:** Hook/premisa (0–4s) → tratamiento 1 con PiP → tratamiento 2 → … veredictos rápidos incluyendo "eyelid surgery" → cierre con valoración final (~52s "It's pretty solid"). Cuenta atrás de 6 ítems.
- **Ritmo de edición:** ~22 cortes en 54 s → plano ~2.5 s. Medio.
- **Recursos de edición:** Talking-head estático + insertos picture-in-picture de cada tratamiento. Cortes secos. Autoridad visual = diplomas de fondo.
- **Texto en pantalla / subtítulos:** Titular del hook en caja semitransparente arriba; subtítulos blancos de veredictos cortos ("It's not awful", "It's pretty solid").
- **Audio:** Habla casi continua, voz del "dermatólogo" a cámara, casual de review; sin música prominente.
- **CTA:** Cierre suave con veredicto positivo sobre la opción ganadora; sin botón.
- **Recreabilidad:** Media-baja. Presentador creíble (aparente médico) en oficina con credenciales, guion de 6 ítems con veredictos, clips PiP (algunos stock). Muy batcheable como "experto rankea".

### VSL_enfermera-astaxantina-rinon_1003.mp4
- **Specs:** 5:21 (321.3 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** VSL testimonial de autoridad, talking-head UGC. Enfermera afroamericana con scrubs y estetoscopio, en su auto, narra en primera persona. Para personas con enfermedad renal crónica (stage 3) que temen la diálisis. Vende **astaxantina 12 mg**.
- **Hook (primeros 3s):** Plano cerrado en el auto + texto "Nurse with stage 3 kidney disease shares what she tried before dialysis" + "I'm a nurse with stage 3 kidney disease". Táctica: autoridad (soy enfermera) + paciente real + miedo a diálisis + curiosidad.
- **Estructura/beats:** Hook/credibilidad (0–20s) → agitación del problema con b-roll CGI de órganos (20s–1:30) → mecanismo y por qué fallan otros (tarjeta: "Synthetic not natural / Underdosed 4-6mg vs clinical 12mg / dry capsules your body can't absorb") (1:30–3:30) → producto en mano + beneficios (3:30–4:45) → cierre/urgencia "don't wait on it" (4:45–5:21).
- **Ritmo de edición:** ~28 cortes en 5:21 → plano ~11 s. Lento/conversacional; cortes para insertar b-roll y tarjetas.
- **Recursos de edición:** Selfie en auto (UGC estático), b-roll CGI biológico (células, intestino, riñón), tarjetas de bullets sobre fondo negro, shots de producto. Corte seco.
- **Texto en pantalla / subtítulos:** Captions blancos centrados-bajos (CapCut) + titular grande en el hook + tarjetas de bullets.
- **Audio:** VO/a cámara, mujer, inglés, cercano/confidencial; audio continuo. Sin SFX notorios.
- **CTA:** Cierre mostrando la caja + urgencia; CTA implícito de compra apoyado en escasez/insistencia.
- **Recreabilidad:** 1 actor con scrubs creíble + auto, guion VSL largo, packaging, b-roll CGI médico (stock o generado), subtítulos y tarjetas. Barato salvo el b-roll CGI.

### CGI_mecanismo-magnesio_262b.mp4
- **Specs:** 17.0 s, 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad 100% CGI/3D animado de mecanismo ("how it works"), estilo Pixar/mobile-game. Para hombres que entrenan y se sienten débiles; vende **magnesio**.
- **Hook (primeros 3s):** Personaje 3D musculoso esforzándose en gym + caption "Still feeling weak even when you train hard?". Táctica: identificación con el dolor + pregunta directa.
- **Estructura/beats:** Hook (0–3s) → problema interno "what's happening inside your muscles" + fibras CGI (3–6s) → agitación "signals firing chaotically… fatigue" (6–9s) → solución "Magnesium stabilizes those signals… stronger contractions" (9–13s) → beneficio + oferta "BUY 3 GET 3 FREE WHILE SUPPLIES LAST" (13–17s).
- **Ritmo de edición:** 16 cortes en 17s → ~1 s/plano. Muy rápido, casi un plano por frase.
- **Recursos de edición:** Render 3D completo (personaje cartoon + fibras/iones Mg con glow), flechas y etiquetas "Mg", overlays de oferta. Sin cámara real.
- **Texto en pantalla / subtítulos:** Captions grandes blancos sincronizados + overlay de oferta bold.
- **Audio:** VO probablemente IA, claro explicativo + música ligera; audio continuo.
- **CTA:** Oferta "Buy 3 Get 3 Free While Supplies Last" con escasez.
- **Recreabilidad:** Generación de personaje 3D + animación de mecanismo (Higgsfield/Runway/Blender), guion problema→mecanismo→solución→oferta, VO IA + captions. Sin actores; el costo es el CGI.

### VSL-FR_dental-perros-spray_54b3.mp4
- **Specs:** 2:19 (139 s), 360x450 (~4:5), 30 fps.
- **Formato/género:** VSL/PAS en **francés** sobre salud dental y mal aliento de perros. Talking-head UGC (mujer) + mucho b-roll demostrativo. Vende **spray dental natural para perros**.
- **Hook (primeros 3s):** Texto "CHIEN… VOTRE CHIEN A MAUVAISE HALEINE" + b-roll de boca de perro/sarro. Táctica: alarma + "mira esto en tu perro".
- **Estructura/beats:** Hook+problema (0–20s) → agitación (infecciones bajo encías, riesgo al corazón) (20s–1:00) → autoridad "Dr. Robert Peterson" (1:00–1:30) → solución/demo spray (1:30–2:00) → beneficios y cierre "pour en savoir plus" (2:00–2:19).
- **Ritmo de edición:** 104 cortes en 139s → plano ~1.3 s. Rápido, muy troceado (intercut talking-head ↔ b-roll).
- **Recursos de edición:** UGC en mano + b-roll abundante (perros, dientes/encías, instrumentos, producto), inserto de "experto", imágenes de bacterias.
- **Texto en pantalla / subtítulos:** Subtítulos en francés mayúsculas, blancos, centrados-bajos, karaoke ("QUELQUES PULVÉRISATIONS PAR JOUR", "UNE HALEINE PLUS FRAÎCHE").
- **Audio:** VO femenina en francés, informativa/preocupada (continua) + música suave.
- **CTA:** Cierre suave "pour en savoir plus" + perro sano. Hacia landing.
- **Recreabilidad:** 1 actor UGC + librería de b-roll de perros/dental (stock) + inserto de "veterinario" + guion PAS localizado + producto spray + edición rápida con subtítulos. La clave es el banco de b-roll y el guion.

### CGI-mascota_tiroides-ACTORA_92e7.mp4
- **Specs:** 43.6 s, 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad 3D animado con mascota (personaje "tiroides" peludo teal tipo Pixar). Advertorial animado de mecanismo + producto. Para fatiga/tiroides lenta; vende **ACTORA Thyroid Support** (dropper).
- **Hook (primeros 3s):** Mascota teal saliendo de una forma de tiroides, captions "HELLO" → "THYROID". Táctica: personaje tierno + curiosidad (personificar el órgano).
- **Estructura/beats:** Presentación mascota (0–6s) → problema (TIREDNESS/WEAK/CELLS/NUTRIENTS) (6–18s) → mecanismo (ENERGY, ✗/✓) (18–30s) → solución/producto: mascota con bata sostiene frasco ACTORA, "SUPPORT/70%" + botón CTA (30–43s).
- **Ritmo de edición:** 18 cortes en 43.6s → plano ~2.4 s. Medio-rápido, una idea por plano.
- **Recursos de edición:** Render 3D (mascota peluda + entorno intestino/células con glow), iconos ✗/✓, overlays de palabra clave, shot de producto, botón CTA inferior.
- **Texto en pantalla / subtítulos:** Captions de UNA palabra en mayúsculas, blancos, centrados-bajos.
- **Audio:** VO probablemente IA, amable/educativa + música suave; continuo.
- **CTA:** Mascota muestra el frasco + botón inferior (Shop/Learn more).
- **Recreabilidad:** Diseño y animación de mascota 3D del órgano, guion problema→mecanismo→producto, packaging, VO IA + captions de una palabra, botón CTA. Costo en el CGI; escalable a otros órganos/nichos.

### UGC-testimonial_gruns-gummies_c51a.mp4
- **Specs:** 54.2 s, 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Testimonial UGC talking-head (selfie en auto), mujer joven con gomita verde; lifestyle/recomendación. Marca **grüns (gruns.co)** — nutrición diaria en gummies. Para gente joven que odia pastillas/greens en polvo.
- **Hook (primeros 3s):** Mujer en top verde en el auto mostrando la gomita a cámara. Táctica: UGC auténtico + producto en mano + tono casual ("the vibe").
- **Estructura/beats:** Hook/contexto personal (0–10s) → beneficios y experiencia (sabor, conveniencia) (10–35s) → refuerzo (35–47s) → end-card de marca con packaging y CTA (47–54s).
- **Ritmo de edición:** 6 cortes en 54s → plano ~9 s; jump cuts de respiración. Lento, plano talking-head continuo.
- **Recursos de edición:** UGC en mano (selfie en auto), producto en mano, b-roll mínimo; end-card gráfica con gummies y pouch. Estilo "raw".
- **Texto en pantalla / subtítulos:** Captions blancos (CapCut). End-card con titular bold: **"DAILY NUTRITION THAT DOESN'T KILL THE VIBE"**, logo oso-gummy, botón "gruns.co".
- **Audio:** Voz a cámara, mujer, casual/entusiasta; silencios entre frases (jump cuts); música mínima.
- **CTA:** End-card de marca (~últimos 7s) con "gruns.co".
- **Recreabilidad:** 1 creator UGC + producto en mano + grabación selfie en auto + guion casual ("vibe"/conveniencia) + jump cuts + end-card prediseñado. Muy barato y rápido.

### VSL_hongo-unas-NASA_12a7.mp4
- **Specs:** ~4:08 (248.5 s), 720x900 (~4:5), 30 fps.
- **Formato/género:** VSL larga estilo "doctor/insider revela secreto" para hongo de uñas de pie (onicomicosis). Para adultos/mayores con hongo crónico que ya probaron todo. Autoridad médica + relato cuasi-religioso (Book of John, ex-NASA "Dr. Sam Walters").
- **Hook (primeros 3s):** Texto a pantalla completa "WATCH WHAT TOOTHPASTE DOES TO YOUR TOENAILS" + "APPLE CIDER VINEGAR, YOU'RE MAKING IT WORSE" + "IT'S AN IMMUNE SYSTEM PROBLEM!". Táctica: destruir remedios caseros que el espectador ya usa + reframe del problema.
- **Estructura/beats:** Hook destructivo de mitos (0–8s) → credenciales + caso de paciente (8–40s) → mecanismo "es inmune, esporas se comunican" + CGI microbios (40–90s) → autoridad: ex-NASA, "FOX/ABC/NBC", Book of John (90–130s) → prueba/escasez + miedo (uña removida quirúrgicamente) (130–180s) → CTA repetido a "free presentation / video de Dr. Sam" (180–248s).
- **Ritmo de edición:** 162 cortes en 248s → plano ~1.5 s. Rápido para VSL; talking-head intercalado con b-roll/CGI.
- **Recursos de edición:** UGC talking-head (hombre en coche, scrubs) + mucho b-roll de stock (uñas macro, pierna iluminada, CGI microbios, órganos), screenshot "exploded in popularity", clip de noticiero, billetes cayendo, flechas rojas animadas, pergamino. "Documental conspirativo".
- **Texto en pantalla / subtítulos:** Subtítulos karaoke con keyword en amarillo/azul + titulares de hook mayúsculas. ("free presentation", "Over 37,000 people", "simple fungus-clearing ritual / for the rest of your life").
- **Audio:** VO masculina, confidencial-urgente de "te cuento un secreto", probable actor real. Música continua tensa/inspiracional. Sin silencios.
- **CTA:** Soft-CTA repetido desde ~130s hacia un "free presentation / video de Dr. Sam" (lleva a otro advertorial/VSL externo).
- **Recreabilidad:** Locutor que actúe de insider médico (grabable en coche), banco de b-roll médico + CGI, clips de noticieros, animación de flechas, guion VSL largo con mecanismo único + autoridad inventada. Costo medio-alto.

### CGI-claymation_tiroides_264c.mp4
- **Specs:** ~1:31 (91.6 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad 100% IA estilo claymation/Pixar 3D. Suplemento tiroides/Hashimoto ("NETURES", Ashwagandha + Selenium). Para mujeres con Hashimoto/hipotiroidismo frustradas con levotiroxina.
- **Hook (primeros 3s):** Personaje femenino de plastilina frustrada al espejo + "Why levothyroxine doesn't work with hashimoto's"; palabras LEVOTHYROXINE/HASHIMOTO'S/EXHAUSTION. Táctica: callout de diagnóstico específico + agitar que el medicamento estándar no funciona.
- **Estructura/beats:** Problema (0–15s) → educación con diagrama anatómico (15–40s) → solución/ingredientes (frasco NETURES, Selenium, Ashwagandha) (40–60s) → transformación (energía, báscula, espejo feliz) + recomendación (60–91s).
- **Ritmo de edición:** 48 cortes en 91.6s → plano ~1.9 s. Cada plano = nueva pose sincronizada a una palabra.
- **Recursos de edición:** Claymation IA de principio a fin, diagramas anatómicos 3D, render de producto, glow dorado, cortes secos. Sin metraje real.
- **Texto en pantalla / subtítulos:** Caption de UNA palabra mayúsculas (one-word-per-cut TikTok). Marca "NETURES" en el frasco.
- **Audio:** VO femenina probablemente IA TTS + música suave; continuo.
- **CTA:** Implícito/suave (transformación + producto); sin botón "buy now". CTA débil, más educativo dentro del funnel.
- **Recreabilidad:** Generador de video IA claymation + TTS femenino + render de producto + guion one-word captions. Sin rodaje; el reto es la consistencia del personaje.

### Skincare_melasma-experta_63ee.mp4
- **Specs:** ~3:02 (182.3 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad largo de skincare para melasma. Híbrido: experta/"Doctor" talking-head + carrusel de testimonios UGC con before/after + diagramas de capas de piel. Para mujeres con melasma (embarazo/anticonceptivos) que probaron sunscreen/peels/cremas caras sin éxito.
- **Hook (primeros 3s):** Mujer-experta con banner verde "Watch this video if you have Melasma" + "these are dark / sun spots / just dark spots". Táctica: callout por condición + reframe (lo estás tratando mal).
- **Estructura/beats:** Hook + por qué fallan tratamientos comunes (0–20s) → causa (embarazo/anticonceptivos, CGI melanina) (20–50s) → mecanismo de 3 capas de piel (50–90s) → producto "Melasma Corrector / all three layers / tyrosinase inhibitors" + validación "Doctor" + ingredientes (90–120s) → catarata de testimonios UGC con before/after (120–175s) → CTA (175–182s).
- **Ritmo de edición:** 114 cortes en 182s → plano ~1.6 s. Rápido, rotación constante de caras/diagramas.
- **Recursos de edición:** Talking-head experta + múltiples testimonios UGC, diagramas de capas/melanina (CGI), tarjetas de ingredientes amarillas, render de producto, clip de "Doctor", before/after lado a lado. Autoridad + prueba social masiva.
- **Texto en pantalla / subtítulos:** Subtítulos en cajas negras texto blanco (CapCut) + banner verde fijo en el hook. ("kojic acid niacinamide", "Treat Melasma Now 🔔", "day money back").
- **Audio:** VO femenina (locutora/experta) educativa-empática + voces de testimonios + música continua.
- **CTA:** Explícito ~175s: "Treat Melasma Now" 🔔 + urgencia/escasez + garantía. A página de producto.
- **Recreabilidad:** Locutora/experta + banco de testimonios UGC con before/after (lo más difícil) + diagramas de piel (CGI/stock) + tarjetas de ingredientes + clip de "doctor" + guion de 3 capas. Costo medio-alto.

### UGC-ES_demo-ducha-filtrante_9ff8.mp4
- **Specs:** ~1:13 (73.2 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** UGC en **español** para un cabezal de ducha filtrante/alta presión. Para mujeres preocupadas por agua dura, residuos en cabello/piel, caída de pelo, presión baja.
- **Hook (primeros 3s):** Mujer de espaldas enjuagándose el cabello con espuma + "Te doy tres razones". Táctica: promesa de lista + situación cotidiana relacionable.
- **Estructura/beats:** Hook "tres razones" + dolor "aclarar el champú me llevaba una eternidad" (0–10s) → demo del problema: desmonta cabezal viejo, filtro con sedimento marrón, agua sucia en vaso, contraste con skincare (CeraVe) (10–35s) → consecuencias en piel/cabello + plano emocional (35–55s) → solución: instala cabezal nuevo, demuestra chorro potente, mujeres satisfechas (55–73s).
- **Ritmo de edición:** 108 cortes en 73s → plano ~0.68 s. Muy rápido, TikTok demostrativo con micro-cortes.
- **Recursos de edición:** UGC casero a mano en baños reales (varias escenas), b-roll macro (filtro sucio, sedimento, agua turbia, manguera), productos skincare como contraste, unboxing/instalación. Sin gráficos ni CGI; "antes/después" físico.
- **Texto en pantalla / subtítulos:** Subtítulos en español, blancos con borde/sombra, centrados, sin caja (auto-captions). ("Te doy tres razones", "Sin que te dieras cuenta").
- **Audio:** VO femenina en español, cercana de recomendación + música ligera; continua.
- **CTA:** Cierre suave demostrando el producto en uso; CTA principalmente en copy/landing.
- **Recreabilidad:** 1-2 creadoras UGC + un baño real + el producto + un cabezal viejo "sucio" para el demo de sedimento + props (vaso turbio). Muy barato; el activo clave es la demo del filtro sucio.

### UGC_corrector-ojeras-EyeCorrect_c5ac.mp4
- **Specs:** 49.0 s, 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** UGC en inglés para un corrector/iluminador de ojeras ("EyeCorrect Undereye Brightener"). Para mujeres maduras (40+) cansadas que quieren disimular ojeras sin maquillaje pesado.
- **Hook (primeros 3s):** Mujer 40+ señalándose las ojeras al espejo + "you look exhausted… really… that's exactly what". Táctica: espejo del problema en primera persona + ojera real sin filtro.
- **Estructura/beats:** Hook del problema (0–8s) → mecanismo/ingredientes aplicando producto ("brightening treatment", "caffeine to depuff", "niacinamide", "peptides") (8–22s) → beneficios de rutina ("every morning", "no heavy coverage", "after eight hours of sleep") (22–40s) → prueba social + oferta (★★★★★, "Buy 2 and Save 32%", "LIMITED STOCK") (40–49s).
- **Ritmo de edición:** 20 cortes en 49s → plano ~2.45 s. Medio-lento; planos sostenidos de aplicación.
- **Recursos de edición:** UGC selfie a mano + b-roll macro de textura/aplicación + pantalla final de producto con rating y badge de oferta. Limpio, luz natural, sin CGI.
- **Texto en pantalla / subtítulos:** Subtítulos blancos con resaltado en caja (rosa/morado para producto e ingredientes).
- **Audio:** VO femenina, tono de amiga entusiasta + música suave; continua.
- **CTA:** Explícito ~45s: pantalla de producto + estrellas + "Buy 2 and Save 32%" + "LIMITED STOCK".
- **Recreabilidad:** Creadora UGC 40+ + buena luz + producto + planos macro + pantalla final con rating y descuento. Muy barato; clave una talent creíble en el rango de edad.

### CGI_drenaje-linfatico-LYMPHORIA_4eb8.mp4
- **Specs:** 2:54 (174.5 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad DR 100% CGI/3D animado para suplemento de "drenaje linfático" (**LYMPHORIA**, gotas herbales). Para adultos preocupados por hinchazón/toxinas/retención, framing pseudo-médico.
- **Hook (primeros 3s):** Figura 3D anatómica (cuerpo desollado con gorrito a rayas estilo "Wally") + mascot de doctor de dibujo + overlay "layer of alcohol" señalando grasa amarilla. Táctica: shock visual anatómico + metáfora de "capa de toxinas". Curiosidad grotesca.
- **Estructura/beats:** Figura anatómica + problema visual (0–10s) → escenas cotidianas con el muñeco-esqueleto (bar, calle, coche) demostrando síntomas (10–60s) → mecanismo: b-roll 3D de vasos linfáticos, órganos, ingredientes (60–150s) → reveal del frasco LYMPHORIA + doctor mascot + CTA (150–174s).
- **Ritmo de edición:** 142 cortes en 174.5s → plano ~1.2 s. Rápido.
- **Recursos de edición:** Render 3D integral, mascot de doctor recurrente como "presentador", b-roll anatómico, ingredientes flotando, zoom-ins. Sin metraje real.
- **Texto en pantalla / subtítulos:** Subtítulos cortos blancos centrados con caja/etiqueta tipo botón ("layer of alcohol").
- **Audio:** VO continua masculina explicativa (tipo IA), educativo-alarmante + música ligera. SFX puntuales.
- **CTA:** Frasco LYMPHORIA + "button is still…" (apunta a Shop Now) en los últimos ~5s.
- **Recreabilidad:** Pipeline de animación 3D/CGI, modelo anatómico riggeado + mascot de doctor, guion pseudo-científico, voz IA, render de producto. Alta dificultad/costo.

### VSL_mecanismo-garganta-EsoRepair_1b75.mp4
- **Specs:** 1:50 (110.5 s), 720x900 (4:5 feed), 30 fps.
- **Formato/género:** VSL/ad de mecanismo para **EsoRepair (NanoTrition)**, líquido para garganta/esófago (reflujo, irritación, dificultad al tragar). Para personas con molestias de garganta/acidez/globus que ya probaron pastillas y sprays.
- **Hook (primeros 3s):** Primer plano de hombre con dolor agarrándose la garganta + overlay anatómico de esófago en rojo + **"WATER, LOZENGES, SPRAYS THEY SLIDE RIGHT PAST THE REAL PROBLEM."** Táctica: invalidar soluciones conocidas + "causa real" oculta.
- **Estructura/beats:** Problema + fallo de soluciones (0–15s) → "the actual cause not the perceived mucus" (15–30s) → ingredientes uno a uno (Marshmallow Root, Slippery Elm, DGL, Zinc-L-Carnosine, Sodium Alginate, L-Glutamine) con b-roll científico (30–60s) → beneficios (60–95s) → producto + "third-party lab tested USA" + garantía 90 días (95–110s).
- **Ritmo de edición:** 26 cortes en 110.5s → plano ~4.2 s. Medio-lento (educativo/VSL).
- **Recursos de edición:** Stock UGC (personas tomando el líquido, gestos de dolor) + b-roll 3D anatómico (esófago, mucosa) + renders de ingredientes cayendo + gráficos de capa protectora. Producto real en mano al final.
- **Texto en pantalla / subtítulos:** Subtítulo bold MAYÚSCULAS blanco con sombra, banda inferior ("THE ACTUAL CAUSE NOT THE PERCEIVED MUCUS", "90-DAY MONEY-BACK GUARANTEE").
- **Audio:** VO continua en inglés, educativo-confiable (probable IA o locutor) + música suave. Sin silencios.
- **CTA:** Frasco EsoRepair + "90-DAY MONEY-BACK GUARANTEE" (risk-reversal). Últimos ~10s.
- **Recreabilidad:** UGC/stock de personas + librería de b-roll anatómico 3D y renders de ingredientes (stock médico o IA) + guion "causa real vs solución falsa" + voz IA + plano de producto. Dificultad media.

### CGI-mascots_skincare-creatina-lyric_6604.mp4
- **Specs:** 1:04 (64 s), 720x1280 vertical 9:16, 24 fps.
- **Formato/género:** Ad CGI con mascots ("ingredientes con cara y piernas") para skincare/belleza (tub rosa "CREATINE") — comparativa de ingredientes dentro de la piel. Para público skincare/anti-edad (firmeza/colágeno).
- **Hook (primeros 3s):** Personaje 3D (jeringa de filler con cara y brazos) dentro de la dermis, overlay **"HI"**. Táctica: personaje carismático + pattern interrupt.
- **Estructura/beats:** Estructura "rap/karaoke" de palabras que arman la frase: FILLER (jeringa) → SITS/SETTLES (jade roller) → MYO-INOSITOL/SKIN (tub de creatina) → cierre FREE. Cada mascot = un ingrediente/método y "dónde se asienta".
- **Ritmo de edición:** 16 cortes en 64s → plano ~4 s, pero mucho movimiento interno + palabra-por-palabra (sensación musical/rápida).
- **Recursos de edición:** CGI 3D integral, mascots antropomórficos (jeringa, jade roller, tubo metálico, bote de creatina) en entorno "dermis" naranja con colágeno. Cámara virtual con dolly/zoom. Sin metraje real.
- **Texto en pantalla / subtítulos:** Una palabra grande por plano, blanca bold con sombra, centro-inferior, sincronizada al beat (lyric-video).
- **Audio:** Jingle cantado pegadizo (rap-pop), la letra ES el copy. Voz musical (probable IA).
- **CTA:** Bote "CREATINE" animado + overlay **"FREE"** (oferta) en los últimos ~5s.
- **Recreabilidad:** Pipeline CGI 3D con rigging de mascots + entorno dermis + canción/jingle generada con la letra como copy. Producción especializada (animación + música), dificultad alta.

### Mecanismo_ansiedad-perros-JAVMA_a177.mp4
- **Specs:** 1:55 (114.8 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad mecanismo/educativo para suplemento calmante de **ansiedad en perros** ("T-Sound Calming Routine"). Para dueños de perros ansiosos/reactivos.
- **Hook (primeros 3s):** Metraje real de un pastor alemán destrozando un cojín + **"What's really happening inside your anxious dog's brain?"**. Táctica: pregunta de curiosidad + problema visual relatable.
- **Estructura/beats:** Problema (perro destruyendo) + pregunta (0–10s) → ciencia "endocannabinoid system" + diagrama (10–25s) → descarte de soluciones fallidas con X roja (training/crate/mask it) (25–45s) → mecanismo "Cortisol – The Panic Hormone" + cerebro 3D (45–70s) → autoridad "JAVMA Published Study, 89% success rate" + experta (70–95s) → perros calmados + CTA al video (95–115s).
- **Ritmo de edición:** 76 cortes en 114.8s → plano ~1.5 s. Rápido para educativo.
- **Recursos de edición:** Stock UGC (perros, dueños, veterinarios) + b-roll científico (cerebro de perro con neuronas) + screenshots de estudio (JAVMA) + gráficos con **X rojas** + talking-head de experta. Cortes secos.
- **Texto en pantalla / subtítulos:** Subtítulos blancos en fuente **serif elegante** (poco común — aire documental/credible), centrados. ("89% Success Rate JAVMA Published Study", "Watch the Free Video").
- **Audio:** VO femenina continua, empática-experta (locutora/IA) + música emotiva. Talking-head sincronizado.
- **CTA:** Suave (lead-gen) "Watch the Free Video – The T-Sound Calming Routine". A un VSL, no compra directa.
- **Recreabilidad:** Stock/UGC de perros + b-roll de cerebro 3D + capturas de estudio (reales o simuladas) + talking-head de experta + overlays de X + voz IA/locutora + guion de mecanismo con prueba científica. Dificultad media.

### UGC_Moonbrew-sueno-magnesio_d2b7.mp4
- **Specs:** 1:49 (108.9 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad UGC/testimonial para **Moonbrew** (gummies "Sleep + Magnesium + Vitamin"). Para adultos 50+ con problemas de sueño, energía y digestión.
- **Hook (primeros 3s):** Arranca con **hook animado prestado** — cartoon de torso femenino en bikini rosa + **"5 MISSING NUTRIENTS FOR MEN AND WOMEN 50+"**, luego corta a UGC de creador masculino joven. Táctica: hook gráfico de "nutrientes faltantes 50+" + pivote a testimonio personal.
- **Estructura/beats:** Hook animado + síntomas (b-roll de venas, mujer cansada "wake up feeling groggy") (0–8s) → creador UGC presenta problema e ingredientes ("magnesium foundational") (8–55s) → demostración y beneficios + b-roll ejercicio/dormir (55–95s) → reveal del producto Moonbrew + "bloating and brain fog" + CTA (95–109s).
- **Ritmo de edición:** 98 cortes en 108.9s → plano ~1.1 s. Rápido, UGC moderno con jump-cuts.
- **Recursos de edición:** UGC talking-head (creador con lavalier, casa real) + jump-cuts + b-roll de stock (sangre/venas CGI, persona en cama, bici) + hook animado 2D al inicio + producto en mano (sobres Moonbrew).
- **Texto en pantalla / subtítulos:** Auto-caption TikTok, blanco bold, palabra/frase resaltada, centro-bajo. Hook inicial con caja sobre cartoon.
- **Audio:** Voz directa del creador UGC (inglés, casual/confiable, persona real, no IA) con lavalier + música mínima.
- **CTA:** Cierre mostrando los sobres + beneficios; CTA de compra implícito. Últimos ~12s.
- **Recreabilidad:** Lo más fácil: un creador UGC con guion (problema 50+ → ingredientes → producto) + hook animado 2D simple + algo de b-roll de stock + producto físico. Bajo costo, alta escalabilidad.

### FakeNews-avatarIA_vision-sanadora_4f32.mp4
- **Specs:** 2:59 (179 s), 720x1276 vertical 9:16, 30 fps.
- **Formato/género:** "Fake news + testimonio de curandero" 100% IA. Suplemento de visión (luteína / extracto de caléndula) para adultos mayores con problemas de vista/cataratas. Voceras: presentadora de noticias IA + anciana asiática "sanadora japonesa".
- **Hook (primeros 3s):** Set de noticiero falso, banner rojo "BREAKING NEWS — JAPANESE HEALER'S VISION..." + anciana en inserto. Táctica: autoridad/noticia falsa + curiosidad (se hizo viral).
- **Estructura/beats:** Noticiero falso (0–8s) → presentación de la sanadora y promesa (8–40s) → mecanismo con b-roll CGI (estómago/digestión "no se absorbe", ojo) (40–80s) → testimonio + ingrediente (caléndula/luteína, frasco) (80–150s) → prueba social + garantía + CTA (150–179s).
- **Ritmo de edición:** 72 cortes en 179s → plano ~2.5 s. Medio-rápido.
- **Recursos de edición:** Avatar IA (lip-sync) + b-roll CGI médico (estómago con manchas, ojo, vasos) + inserto de noticiero + frasco compuesto + campos de caléndula + sello dorado "MONEY BACK GUARANTEE".
- **Texto en pantalla / subtítulos:** Caption centrado/bajo, mayúsculas, keyword en amarillo ("BREAKING NEWS", "DOESN'T GET DIGESTED", "IN THE COMMENTS").
- **Audio:** VO IA en inglés, cálido/confidencial + música suave; narración casi continua.
- **CTA:** Cierre en veranda japonesa, "...IN THE COMMENTS" (link en comentarios) + garantía. Últimos ~20s.
- **Recreabilidad:** Media-alta. Generador de avatar IA (HeyGen/Higgsfield) + b-roll CGI médico + plantilla de noticiero falso + script de testimonio + voz IA + subtitulado.

### UGC-experto_dental-perros_10f1.mp4
- **Specs:** 2:23 (143 s), 720x892 (~4:5), 30 fps.
- **Formato/género:** UGC talking-head de autoridad — hombre barbudo frente a diplomas (posiciona como veterinario). Producto dental para perros (limpiador de placa sin cepillado). Para dueños de perros.
- **Hook (primeros 3s):** Plano fijo hablando a cámara + "...THEY SMELL / IT KIND OF" + inserto de foto de perro. Táctica: problema relatable (mal aliento) en boca de un "experto".
- **Estructura/beats:** Problema (aliento/placa) (0–15s) → educación (bacteria endurecida en encía) (15–60s) → solución/diferenciador ("unlike anything else", "protective barrier", "visibly cleaner teeth") (60–120s) → recomendación personal + CTA económico (120–143s).
- **Ritmo de edición:** Solo 2 cortes en 143s → plano único estático (~70 s). Muy lento; dinamismo por habla + subtítulos.
- **Recursos de edición:** Cámara fija selfie/trípode, sin transiciones; b-roll mínimo = 2 insertos de foto de perro en recuadro rojo. Sin gráficos/CGI. Crudo y auténtico a propósito.
- **Texto en pantalla / subtítulos:** Subtítulos en caja blanca texto negro, centrados a media altura (CapCut clásico), 2-4 palabras. ("PROTECTIVE BARRIER", "VISIBLY CLEANER TEETH", "WITHOUT BREAKING THE BANK").
- **Audio:** Voz humana real (no IA), cercano/coloquial de experto; sin música o muy baja; continua.
- **CTA:** Soft-CTA al final (recomendación + insinúa precio accesible). Verbal, no overlay.
- **Recreabilidad:** Muy alta. Presentador creíble (bata/credenciales detrás) + celular en trípode + guion + subtitulado. Costo mínimo.

### SplitScreen-medico_cataratas_70b3.mp4
- **Specs:** 2:14 (134.5 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Reacción/"stitch" de autoridad — médico con bata en consultorio reacciona a un video de un creador. Salud ocular / alternativa a cirugía de cataratas. Para adultos con problemas de visión que temen operarse.
- **Hook (primeros 3s):** Pantalla dividida: arriba banner "CATARACT SURGERY"; izq. creador joven + b-roll de ojo, der. el doctor con "Wait for my take...". Táctica: formato duet/reacción + autoridad médica + intriga.
- **Estructura/beats:** Setup de reacción (0–12s) → "el problema con la cirugía" + b-roll de ojo/cirugía/glare (12–50s) → mecanismo y solución natural (frasco, ingredientes) (50–95s) → testimonios/comparación + CTA "natural alternative" (95–134s).
- **Ritmo de edición:** 92 cortes en 134.5s → plano ~1.5 s. Rápido (saltos al b-roll y de vuelta).
- **Recursos de edición:** Split-screen de reacción + jump-cuts sobre el doctor + b-roll de ojo/cataratas/cirugía + carretera nocturna (deslumbramiento) + frasco + headlines + PiP del doctor sobre b-roll.
- **Texto en pantalla / subtítulos:** Subtítulos mayúsculas con keyword en amarillo, media-baja ("Wait for my take...", "CRUMBLING BEHIND THEM", "NATURAL ALTERNATIVE").
- **Audio:** VO masculina (probable IA/locutor) seria-autoritaria + música tensa; narración densa continua.
- **CTA:** El doctor a cámara "NATURAL ALTERNATIVE" (empuja a la alternativa/link). Últimos ~10s.
- **Recreabilidad:** Media. Talento con bata creíble + set clínico + clip "original" para el split-screen + b-roll oftalmológico + frasco + edición rápida con subtítulos.

### CGI-surrealista_esqueleto-huesos_a261.mp4
- **Specs:** 3:58 (238 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad de personaje CGI surrealista (IA). Un esqueleto animado con ojos y cabello humanos vive una vida normal (come, se mira al espejo, abraza a su pareja). Metáfora de pérdida ósea/energía; suplemento (probable calcio/colágeno/salud ósea). Para adultos preocupados por huesos/envejecimiento. El más largo y experimental.
- **Hook (primeros 3s):** Esqueleto humanizado en una recámara cálida sosteniendo un plátano + "something". Táctica: pattern-interrupt visual extremo (curiosidad por lo absurdo).
- **Estructura/beats:** Presentación del personaje + vida cotidiana (relatable + bizarro) (0–40s) → problema interno con b-roll CGI médico (40–120s) → desarrollo/empeoramiento + emociones (120–200s) → resolución (vuelve a verse sano) (200–238s).
- **Ritmo de edición:** 166 cortes en 238s → plano ~1.4 s. Rápido pese a la duración.
- **Recursos de edición:** Generación IA total (personaje 3D consistente en múltiples escenas) + mucho b-roll CGI médico (sangre, vasos, articulaciones, hueso poroso) + partner humano IA + cortes duros.
- **Texto en pantalla / subtítulos:** Subtítulos blancos bold 1-2 palabras, parte baja-centro (narrativa fragmentada palabra-por-palabra).
- **Audio:** VO narrativa/emocional (probable IA) + música ambiental; continua.
- **CTA:** Suave; el personaje "se recupera" frente al espejo (resolución de la metáfora más que botón duro; CTA fuerte en copy/link). Últimos ~30s.
- **Recreabilidad:** Baja-media en casero; pipeline de video IA con personaje consistente (Higgsfield/Kling/Sora + character ref) + b-roll CGI médico + guion metafórico. Concepto fácil de copiar, ejecución exigente.

### UGC-CGI_spray-ocular-luteina_d4fc.mp4
- **Specs:** 1:08 (68 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Mezcla UGC + CGI anatómico. Suplemento/spray ocular como alternativa a cirugía de cataratas. Mujer mayor protagonista; para adultos mayores con vista deteriorada.
- **Hook (primeros 3s):** Mujer canosa aplicándose spray cerca de los ojos con overlay CGI esqueleto/anatomía + "...TO YOUR CATARACTS". Táctica: pattern-interrupt visual (cuerpo transparente) + mención del padecimiento.
- **Estructura/beats:** Hook visual + problema (cataratas, "foggy film") (0–8s) → analogía/mecanismo (libro borroso, luces de coche de noche) (8–25s) → ingrediente/solución (estómago CGI, "LUTEIN", ojo) (25–45s) → prueba/contraste (lee sin lentes, sale a caminar, clínica) (45–60s) → contraste con quirófano + CTA (60–68s).
- **Ritmo de edición:** 62 cortes en 68s → plano ~1.1 s. Muy rápido (supercut DR).
- **Recursos de edición:** Overlay CGI de esqueleto/anatomía sobre actor + b-roll mixto (libro, conducción nocturna, ojo CGI, estómago CGI, exteriores, clínica) + inserto de cirugía real ("BEFORE GOING UNDER") + montaje "antes/después".
- **Texto en pantalla / subtítulos:** Subtítulos mayúsculas con keyword en amarillo/naranja, media-baja ("AFTER SPRAYING LUTEIN", "BEFORE GOING UNDER", "A NATURAL CHANCE").
- **Audio:** VO femenina (inglés, confidencial/esperanzador, posible IA) + música suave; continua.
- **CTA:** Close-up extremo del ojo "A NATURAL CHANCE" tras mostrar quirófano (miedo→solución). Últimos ~5-8s.
- **Recreabilidad:** Media. Clip UGC de actor mayor aplicando spray + overlay CGI de anatomía + b-roll de ojo/estómago + footage de quirófano (stock) + edición ultra-rápida + subtitulado.

### CGI-villano_jeringa-VisionPure-ojos_412f.mp4
- **Specs:** 47.0 s, 480x854 (9:16), 30 fps.
- **Formato/género:** Ad 100% CGI animado (render 3D/Pixar "personajes que hablan") para **VisionPure** (luteína para AMD/degeneración macular). Para mayores con problemas de mácula que temen o reciben inyecciones oculares. **(Nuestro producto Eye.)**
- **Hook (primeros 3s):** Villano antropomórfico — una **jeringa con ojos malvados y rayos rojos** — dice *"I'm your AMD eye injection"* / *"but I don't treat the underlying problem"*. Táctica: personificar al enemigo (la inyección cara/dolorosa) + miedo a perder visión.
- **Estructura/beats:** Villano-inyección plantea el problema "you owe me every month" (0–8s) → personaje "ojo" triste + héroe de luz "I'm lutein… I rebuild your macular pigment from the inside" (8–20s) → mecanismo "shield your retinal cells from oxidative damage", "buy back the vision you thought was gone" + reveal del frasco VisionPure "unlike most capsules that dissolve in your gut… directly to your eyelids" (20–33s) → prueba + cierre (abuelita feliz, "90 day money back guarantee", "stock runs out fast don't wait") (33–47s).
- **Ritmo de edición:** 10 cortes en 47s → plano ~4.3 s. Medio, dictado por diálogos de cada personaje.
- **Recursos de edición:** Todo CGI/animación 3D (sin cámara real), cortes duros entre personajes, reveal de producto renderizado, mecanismo ilustrado (rayos/escudos), close-ups del frasco.
- **Texto en pantalla / subtítulos:** Caption blanco con caja semitransparente, centrado abajo, una línea por beat.
- **Audio:** Diálogos (inglés) muy probablemente IA/TTS por personaje, dramático-caricaturesco + música tensa; continuo.
- **CTA:** Garantía 90 días + escasez ("stock runs out fast") en los últimos ~8s. CTA implícito de compra.
- **Recreabilidad:** Generación de personajes CGI consistentes (imagen→video animado) + guion villano-vs-héroe + voces IA + render del frasco. Media-alta complejidad, sin rodaje. **NOTA: este es el formato del C-villano que ya trabajamos para VisionPure.**

### CGI-VSL_metabolismo-perdida-peso_7b4f.mp4
- **Specs:** 2:01 (121 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** VSL larga CGI/animada estilo Pixar para producto de pérdida de peso/metabolismo en gotas (tincture). Personaje "semilla/frijol" parlante + mujer estresada→feliz. Para mujeres con sobrepeso, cansancio y metabolismo lento.
- **Hook (primeros 3s):** Personaje semilla CGI + mujer agarrándose la cabeza con overlays gigantes **"LAZY" / "THINK" / "YOU"**. Táctica: callout acusatorio ("no eres tú, es tu metabolismo") con palabras-impacto.
- **Estructura/beats:** Hook + agitación (0–12s) → problema fisiológico animado "METABOLISM/EXHAUSTION" + mujer agotada (12–30s) → introducción de la solución (escena de "médico", semilla bebe algo verde) (30–55s) → mecanismo simple + producto (frasco gotero verde) (55–90s) → transformación (mujer feliz saltando) + reveal final (90–121s).
- **Ritmo de edición:** 48 cortes en 121s → plano ~2.5 s. Rápido y constante para formato largo.
- **Recursos de edición:** 100% CGI/animación 3D; cortes duros, zooms, transiciones de "energía/luz", reveal repetido del frasco. Grandes overlays de una palabra como hilo conductor.
- **Texto en pantalla / subtítulos:** Palabra única en mayúsculas, blanca, centrada-inferior, sincronizada (kinetic text): LAZY, THINK, YOU, METABOLISM, EXHAUSTION, etc.
- **Audio:** VO continua (inglés, cálido-persuasivo, probable IA) + música emotiva; ininterrumpida los 2 min.
- **CTA:** Transformación feliz + reveal del frasco en los últimos ~10s (el render final lleva botón/landing).
- **Recreabilidad:** Alta producción: personajes CGI coherentes 2 min + guion VSL de metabolismo + VO IA + kinetic captions + render del gotero. La más laboriosa.

### Podcast_testosterona-MarsMen_ac4f.mp4
- **Specs:** 1:04 (64.2 s), 720x1280 vertical 9:16, 25 fps.
- **Formato/género:** Ad estilo **clip de podcast / testimonio UGC** para suplemento de testosterona ("Mars Men"). Para hombres preocupados por testosterona baja, energía y rendimiento.
- **Hook (primeros 3s):** **Split-screen tipo podcast**: arriba "CEO - Mars Men / Benjamin Smith", abajo un invitado; caption **"Insane 300 to 900 testosterone jump 👆"**. Táctica: cifra impactante + formato conversacional creíble ("escuchado en un podcast").
- **Estructura/beats:** Hook con la cifra (0–10s) → desarrollo del problema/historia ("a month on supplements", "zinc") (10–30s) → testimonio y mecanismo (segundo hablante, "Anxiety") (30–45s) → beneficios y cierre conversacional ("stronger", "being more clear") (45–64s).
- **Ritmo de edición:** Solo 2 cortes en 64s → prácticamente una toma continua (~32 s). Lento/orgánico, no editado a saltos.
- **Recursos de edición:** Talking-head / cámara fija de webcam o podcast, sin b-roll, sin gráficos. Único recurso: layout split-screen + etiqueta de nombre/rol. Estética "raw" para máxima credibilidad.
- **Texto en pantalla / subtítulos:** Etiqueta persistente arriba-izq (rol+nombre) + caption-hook en burbuja blanca redondeada + subtítulos cortos abajo.
- **Audio:** Voz humana real (inglés, casual-conversacional, dos hablantes) — entrevista grabada. Sin música prominente; habla casi continua.
- **CTA:** No hay CTA duro en el corte (la conversión iría en copy/landing). "Demostración social" más que "pitch".
- **Recreabilidad:** Muy fácil/barata: grabar un clip de conversación (o usar uno real) + etiqueta de nombre split-screen + subtítulos auto. Apuesta por autenticidad.

### LeadMagnet_PDF-ChairTaiChi_d5af.mp4
- **Specs:** 44.0 s, 720x1280 vertical 9:16, 25 fps.
- **Formato/género:** Ad de **lead-magnet (PDF gratis)** para un programa de fitness "Chair Tai Chi Challenge". Para mujeres mayores / +60 / +180 lbs que quieren bajar de peso suave.
- **Hook (primeros 3s):** UGC de señora mayor en cocina mostrando su cuerpo + overlay **"Mom… how did you lose 30 lbs at 60?"**. Táctica: pregunta-curiosidad de un familiar + prueba viva + segmentación por edad.
- **Estructura/beats:** Hook + segmentación ("printable Chair Tai Chi plan!", "if you're a woman over 180 lbs") (0–11s) → reveal del producto = slideshow del PDF imprimible ("DAY 1 Full Body 7 min") (11–22s) → desglose por días con ilustraciones ("Just 7 minutes a day", "After one week you'll feel the difference") (22–33s) → tracker de peso + cierre con flechas a **"FREE PDF"** (33–44s).
- **Ritmo de edición:** 8 cortes en 44s → plano ~5.5 s. Medio; alterna UGC y láminas estáticas del PDF.
- **Recursos de edición:** UGC vertical (señora real) + slideshow de gráficos del producto (mockups del PDF, ilustraciones de ejercicios en silla, tracker) + flechas chevron animadas a "FREE PDF". Aviso pequeño "AI-generated imagery".
- **Texto en pantalla / subtítulos:** Captions grandes blancos con borde/sombra centrados (CapCut). ("Just 7 minutes a day", "All your friends will be asking", **"FREE PDF"**).
- **Audio:** VO femenina (inglés) explicando el plan, cercano/motivacional, posible IA + música ligera; con pausas naturales entre láminas.
- **CTA:** Explícito y fuerte: flechas animadas + **"FREE PDF"** (captación de lead, no venta directa).
- **Recreabilidad:** Fácil-media: clip UGC de mujer mayor (o imagen IA) + mockups del PDF + ilustraciones + captions + flechas + VO. Modelo de embudo por lead-magnet.

### UGC-founder_creatina-fabrica_e269.mp4
- **Specs:** 57.8 s, 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad **UGC de fundador "founder-led"** muy editado para creatina monohidratada (marca tipo "Tropeaka"), ángulo de calidad de fabricación. Para fitness/wellness que dudan de la pureza.
- **Hook (primeros 3s):** Fundador en bata, gorro y guantes de fábrica + overlays gigantes **"CAUSE" → "TURN" → "THIS AMAZING SUPPLEMENT"** + etiqueta "CALEB MARSHALL — Founder & CEO". Táctica: autoridad/transparencia ("te muestro la fábrica") + intriga con palabras sueltas.
- **Estructura/beats:** Hook fundador en planta (0–8s) → prueba de pureza/proceso ("ULTRA CLEAN", b-roll de mezclar polvo) (8–20s) → beneficios cognitivos/físicos ("BRAIN GAINS") (20–35s) → prueba social = screenshot "20,000 reviews" + packaging (35–48s) → cierre ("WE'RE SO CONFIDENT", "RISK FREE") (48–58s).
- **Ritmo de edición:** 68 cortes en 57.8s → plano ~0.85 s. **Muy rápido**, jump-cut/vlog acelerado.
- **Recursos de edición:** UGC mano-alzada + mucho b-roll (fábrica, mezcla de polvo, beber greens) + screenshot de reviews (20,000) + packaging + lavalier visible. Cortes duros constantes. Sin CGI; "real backstage".
- **Texto en pantalla / subtítulos:** Una/dos palabras mayúsculas, blanco brillante (a veces verde), centradas-inferior, sincronizadas con cada jump-cut.
- **Audio:** Voz humana real del fundador (inglés, enérgico/entusiasta) + música dinámica; sin pausas.
- **CTA:** Por garantía/risk-reversal ("WE'RE SO CONFIDENT", "RISK FREE") en los últimos ~10s.
- **Recreabilidad:** Media: acceso a entorno de fábrica/lab (o simularlo) + fundador carismático + mucho b-roll + screenshots de reviews + edición jump-cut intensa con captions de una palabra.

### UGC-testimonial_prostata-secreto_495f.mp4
- **Specs:** 41.5 s, 720x720 (cuadrado 1:1), 30 fps.
- **Formato/género:** Testimonial/founder-style talking-head para suplemento de próstata/salud urinaria masculina (kit caja verde marca "ESTELO"/similar). Para hombres 50+ con micciones nocturnas y urgencia.
- **Hook (primeros 3s):** Plano cerrado de hombre canoso de barba + caja blanca **"UROLOGISTS DON'T WANT YOU TO KNOW THIS"**. Táctica: secreto prohibido + anti-establishment.
- **Estructura/beats:** Hook (0–3s) → problema "BATHROOM TRIPS" (3–10s) → objeción/escepticismo "SIDE EFFECTS… SKEPTICAL" + reveal del producto (~15–17s) (10–17s) → resultado "I WAS SHOCKED… LESS URGENCY… FIVE TIMES A night" (17–27s) → oferta/garantía "MONEY BACK… RISK FREE… FREE TRAVEL VIAL" (27–38s) → card final con producto + iconos "Relief in 30 days or your money back" (38–41s).
- **Ritmo de edición:** 18 cortes en 41.5s → plano ~2.3 s. Medio; jump-cuts sobre la misma persona.
- **Recursos de edición:** UGC/talking-head a una sola toma con jump-cuts; cortes secos + destello rosa en el hook. B-roll mínimo: insert del producto en caja + card final con iconos (gota, vejiga, hojas, próstata). Sin flechas/charts.
- **Texto en pantalla / subtítulos:** Mayúsculas estilo karaoke, dos estilos: caja blanca con borde negro (hook) y fuente naranja/dorada bold (resto). Card final: "Bathroom Trips? Enough of That."
- **Audio:** VO masculina, confidencial/testimonial (actor real o IA muy natural); wall-to-wall + música suave.
- **CTA:** Suave por oferta — garantía 30 días + "FREE TRAVEL VIAL" + card de producto; CTA implícito.
- **Recreabilidad:** Alta. Actor maduro de barba canosa + móvil/buena luz + producto en caja + guion problema-escepticismo-resultado-garantía + subtítulos. Sin VFX.

### CGI-claymation_circulacion-pies_e14f.mp4
- **Specs:** 56.3 s, 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad animado 3D/CGI claymation-Pixar educativo-mecanístico para producto de circulación/salud de pies y piernas (crema, parche o suplemento). Para mayores con hinchazón de tobillos/pies y mala circulación.
- **Hook (primeros 3s):** Pierna/pie gris con punto rojo de dolor + rótulo **"your ankles look like"**; transición a anciano CGI sentado. Táctica: dramatización visual del síntoma + identificación.
- **Estructura/beats:** Síntoma ("your ankles are puffier / just what happens now") (0–10s) → agravamiento (10–17s) → mecanismo/causa CGI: válvulas venosas "tiny one-way valves / it pools" (17–30s) → solución "you press every evening / gentle targeted pressure" (30–43s) → resultado "do their job again" (pie iluminado) (43–50s) → cierre con personas mayores reales sonriendo + "Over a hundred…" (prueba social) (50–56s).
- **Ritmo de edición:** Solo 10 cortes duros en 56s (~5.6s/plano), pero mucho movimiento de cámara CGI intra-plano. Contemplativo-educativo.
- **Recursos de edición:** 100% CGI/animación 3D (no UGC). B-roll generado: anatomía de venas/válvulas con luz dorada (healing glow) + flechas rojas + zooms al interior. Cierre con clips de "personas reales" (también IA) como prueba social.
- **Texto en pantalla / subtítulos:** Subtítulos en minúsculas, caja semitransparente lila/gris, centrados, sans simple ("tiny one-way valves", "But gentle, targeted pressure").
- **Audio:** VO (inglés, cálido empático, probable IA/locutor suave) + música ambiental; continuo. SFX sutiles en el "glow".
- **CTA:** Por prueba social ("Over a hundred [reviews/customers]") con producto en mano; suave, sin botón explícito en el tramo muestreado.
- **Recreabilidad:** Media-alta si tienes pipeline IA/CGI (clay + animación anatómica con glow y flechas). Sin actores; requiere generación 3D consistente + locución.

### VSL_fitness-calistenia-actorIA_7c78.mp4
- **Specs:** 2:12 (132.3 s), 720x1280 vertical 9:16, 25 fps.
- **Formato/género:** VSL/advertorial de fitness — "transformation story" + demo de programa de calistenia/bodyweight en casa (app o programa para hombres). Narrativa "loser-to-winner" + talking-head de coach con chaleco táctico.
- **Hook (primeros 3s):** Estacionamiento de súper: hombre con sobrepeso cargando bolsas mientras su pareja mira a un hombre musculoso; rótulos "Your husband…/No gym…/Calisthenics works". Disclaimer: "AI-generated actor. Story is for entertainment purposes only". Táctica: drama de estatus/celos + envidia social.
- **Estructura/beats:** Story dramatizada (humillación pareja/rival) (0–20s) → giro a entrenamiento (calistenia exteriores) (20–35s) → aparece el coach (chaleco táctico) "BY THE END / BUT WHAT IF I LITERALLY" (35–50s) → argumentación/objeciones "ZERO CURRENT… GUYS IN THE GYM" (50–95s) → mecanismo y objeciones "DO I NEED ANY EQUIPMENT… DANGEROUS" (95–125s) → cierre/CTA "TAP THE SCREEN" (125–132s).
- **Ritmo de edición:** 54 cortes en 132s → plano ~2.4 s. Medio-rápido; escena dramatizada (más cortes) + talking-head sostenido del coach (jump-cuts/reframes).
- **Recursos de edición:** Híbrido. Acto 1: escena dramatizada con actores IA (etiquetada). Acto 2: UGC/talking-head real del coach (cámara fija con zoom-ins) + b-roll de calistenia en parque/playa. Muchos subtítulos animados y reencuadres.
- **Texto en pantalla / subtítulos:** Subtítulos karaoke mayúsculas blancas/amarillas, palabra-por-palabra resaltada + disclaimer legal en el hook ("No gym", "DO I NEED ANY EQUIPMENT", "TAP THE SCREEN").
- **Audio:** Voz/diálogo en inglés; coach enérgico-persuasivo (talking-head real) + acto 1 dramatizado + música motivacional; wall-to-wall.
- **CTA:** Directo **"TAP THE SCREEN"** (DR para abrir landing/app).
- **Recreabilidad:** Media. (1) generación IA para la escena-historia, (2) coach real grabado talking-head, (3) b-roll de calistenia, (4) edición con subtítulos karaoke. Guion VSL de 2 min con manejo de objeciones.

### Advertorial_spray-cataratas-luteina_bf1a.mp4
- **Specs:** 1:57 (117.1 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Advertorial médico-mecanístico para spray/gotas oculares que "evitan la cirugía de cataratas" (luteína). Para mayores con visión nublada/cataratas que temen la cirugía. Animación médica + b-roll lifestyle + escena de consulta.
- **Hook (primeros 3s):** Card roja **"THIS SPRAY AVOIDED MY CATARACT SURGERY"** + "Listen carefully 👂" sobre animación 3D de cirugía ocular (lente amarillo extraído del ojo). Táctica: claim impactante + "presta atención" + miedo a la cirugía.
- **Estructura/beats:** Hook + qué hace la cirugía (animación de extracción del cristalino) (0–10s) → problema/mecanismo "this is what's happening" + b-roll naturaleza (10–30s) → ingrediente/solución **"LUTEIN"** con flores de caléndula y verduras (30–55s) → demostración en la vida ("no longer driving / can't see your daughter's / driving at night") (55–80s) → validación clínica/consulta (mujer mayor con médico revisando escáner) (80–110s) → cierre con rostro de mujer mayor (testimonio/CTA) (110–117s).
- **Ritmo de edición:** 100 cortes en 117s → plano ~1.2 s. Rápido.
- **Recursos de edición:** Multi-fuente: animación médica 3D del ojo/cirugía + b-roll de stock (atardecer, flores, carretera nocturna, conducción) + escena dramatizada de consulta (actores) + close-ups de ojos + overlays "LUTEIN". Cards de advertencia.
- **Texto en pantalla / subtítulos:** Card superior "warning" (texto negro, keyword en rojo/amarillo, p.ej. "AVOIDED") + subtítulos blancos centrados-abajo en minúsculas ("THIS SPRAY AVOIDED MY CATARACT SURGERY", "Listen carefully", "LUTEIN").
- **Audio:** VO femenina/testimonio (inglés, confidencial-preocupado, storytelling personal, probable IA/locutor) + música tensa-suave; continua.
- **CTA:** Cierre por testimonio personal con rostro de la mujer; suave hacia advertorial/landing ("learn more"/seguir leyendo).
- **Recreabilidad:** Media. Animación médica del ojo (CGI/stock médico) + b-roll de stock lifestyle + escena dramatizada de consulta + gráfico de ingrediente + locución de testimonio. Mucho corte rápido.

### CGI-villano_DHT-shampoo-Spartan_eb8b.mp4
- **Specs:** 1:49 (108.9 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad narrativo 100% CGI/IA estilo "Pixar villano" — fábula metafórica para shampoo anticaída ("Spartan Root Activator Shampoo"). Para hombres con caída de pelo/entradas (y post-injerto). Villano (DHT) vs. héroe (raíces).
- **Hook (primeros 3s):** Villano gigante azul/morado CGI en oficina: **"I gave you your drive… BUT TOOK YOUR HAIRLINE"**. Táctica: personificación del enemigo (DHT como villano) + intriga narrativa.
- **Estructura/beats:** Villano (DHT) presume haber robado el cabello (0–20s) → explica el mecanismo "I shut down the enzyme that builds DHT / 5-alpha reductase" (20–35s) → héroes raíces en batalla "they stop dying / fertile ground" (35–60s) → resolución "One scalp" + aparece hombre real (60–80s) → producto "Spartan Root Activator Shampoo / By month six" (80–100s) → cierre con hombre satisfecho + **"CLICK BELOW"** + "Your follicles have been waiting" (100–109s).
- **Ritmo de edición:** 92 cortes en 109s → plano ~1.2 s. Rápido.
- **Recursos de edición:** 100% IA/CGI (personajes 3D, batalla de raíces, villano) + insert de producto (botella SPARTAN) + imagen de "estudio científico" (retrato B/N de "investigador") + efectos de partículas/energía. Falsa autoridad científica.
- **Texto en pantalla / subtítulos:** Bocadillos/cajas de diálogo blancas (estilo cómic) para los personajes + subtítulos sans bold negro sobre caja blanca ("5-alpha reductase", "By month six", "CLICK BELOW").
- **Audio:** VO/diálogo del villano (inglés, teatral-siniestro, IA TTS o locutor con efecto) + música épica/tensa; continua. SFX de combate.
- **CTA:** Directo **"CLICK BELOW"** + "Your follicles have been waiting" + producto. DR explícito.
- **Recreabilidad:** Media-baja sin pipeline IA maduro. Generación consistente de personajes CGI (villano + raíces) + batalla + locución teatral + imagen de producto y "estudio" falso + edición rápida con bocadillos. Guion de fábula de ~2 min.

### Medico-herbolario-ES_berberina_f204.mp4
- **Specs:** 2:17 (137.2 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad DR de berberina ("Glucor Berberine", gotas sublinguales, etiqueta con bandera de EEUU) para azúcar en sangre/pre-diabetes. "Médico-autoridad / medicina tradicional": señor mayor asiático con bata blanca (herbolario/TCM) en una farmacia llena de frascos. En **español** para adultos mayores hispanos con prediabetes/hormigueo.
- **Hook (primeros 3s):** El "doctor" examina cuello y vientre de un paciente + subtítulo gigante **"PRE DIABETES"** (PRE en azul). Táctica: diagnóstico alarmante + autoridad médica ("escúchame con atención") = miedo + credibilidad.
- **Estructura/beats:** Hook diagnóstico "pre diabetes / escúchame con atención" (0–8s) → síntomas y miedo "ese hormigueo no es deshidratación / un incendio en el páncreas", culpa al sistema "ellos no te quieren / las pastillas" (8–40s) → presentación del producto y promesa (40–110s) → demo: gotas bajo la "LENGUA" para "máxima absorción", "solo dos gotas", "haz clic abajo" (110–137s).
- **Ritmo de edición:** 14 cortes en 137s → plano ~9-10 s. Lento/medio; planos sostenidos del presentador + inserts puntuales.
- **Recursos de edición:** Cámara trípode/UGC fijo + b-roll de exploración corporal (cuello, vientre) + inserts del bote en mano. Sin memes/charts; el recurso fuerte son los subtítulos-titular.
- **Texto en pantalla / subtítulos:** Caption central karaoke, mayúsculas, bold sans, keyword en azul/amarillo ("PRE DIABETES", "UN INCENDIO… EN EL PÁNCREAS", "SOLO DOS GOTAS / LENGUA", "HAZ CLIC ABAJO").
- **Audio:** VO masculina en español (continua, autoritaria/urgente; VO sincronizada o IA sobre el actor) + música tenue. Sin pausas.
- **CTA:** Directo en los últimos ~15s: demo de las 2 gotas bajo la lengua + "HAZ CLIC ABAJO". Compra dura.
- **Recreabilidad:** Actor/avatar de "médico" mayor + set de farmacia/herbolario + paciente para el b-roll + bote de gotas + guion miedo→mecanismo→solución + locución en español + subtitulado karaoke.

### VSL-PT_dolor-articular-podcast_f4d9.mp4
- **Specs:** 3:33 (213.5 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** VSL/testimonial largo en **portugués brasileño** para remedio de dolores articulares (hombros/brazos). "Podcast / talking-head": hombre calvo con gafas frente a un micrófono de podcast en sala. Para adultos mayores con dolor articular crónico.
- **Hook (primeros 3s):** Caja de producto a cámara + "Se você sente dores nos ombros, nos braços… **VEJA ESSE VÍDEO ATÉ O FINAL!!**" + b-roll de líquido oscuro en bol y bote "ARGO CORN STARCH". Táctica: callout de síntoma + orden de retención + promesa de "truco casero".
- **Estructura/beats:** Hook + callout de dolor + b-roll de "receta casera" (0–10s) → desarrollo educativo/testimonial largo (mecanismo del dolor, por qué fallan los métodos, historia personal) (10–120s) → solución/producto y cierre (120–213s). VSL: retención por curiosidad antes de revelar.
- **Ritmo de edición:** Solo 4 cortes en 213s → plano ~53 s. MUY lento, una sola toma sostenida (VSL/podcast de bajo corte para maximizar visionado).
- **Recursos de edición:** Cámara fija trípode (set de podcast con micrófono). B-roll puntual: bol con líquido oscuro, bote de maicena ARGO. Sin transiciones; minimalista para parecer orgánico/informativo.
- **Texto en pantalla / subtítulos:** Subtítulos en bloque central, mayúsculas, sans bold blanco con realce amarillo, sobre franja translúcida.
- **Audio:** VO/a cámara masculina en portugués, cercana y conversacional (confidencia); continua. Música mínima o nula.
- **CTA:** Tardío (último tercio); la oferta se revela tras el bloque largo de retención.
- **Recreabilidad:** Presentador creíble (señor mayor) en set de podcast + guion VSL largo en portugués con gancho de retención + b-roll de "remedio casero" (bol + ingrediente común) + subtitulado con keyword. Barato: una sola toma fija.

### UGC-sketch_astaxantina-rinon_fa90.mp4
- **Specs:** 2:00 (120.4 s), 720x1280 vertical 9:16, 30 fps.
- **Formato/género:** Ad DR en **inglés** para antioxidante de salud renal/celular "ASTAXANTHIN 12mg" (con CoQ10/Purity como prop comparativo). UGC con **sketch cómico**: hombre de mediana edad en hotel/baño habla a cámara con humor. Para adultos preocupados por riñones/energía/envejecimiento.
- **Hook (primeros 3s):** El hombre se lleva un auricular de teléfono antiguo a la oreja + caption **"Your kidneys left a voicemail 📞 / You're not gonna like what they said"**. Táctica: pattern-interrupt humorístico + personificación del órgano.
- **Estructura/beats:** Sketch del "buzón de voz de los riñones" (0–8s) → problema/educación con b-roll (pulpo/mariscos como fuente de astaxantina, ingredientes, pastillas en mano, bote de CoQ10) (8–60s) → presentación del producto (60–100s) → producto en mano + cierre (sostiene varios paquetes) (100–120s).
- **Ritmo de edición:** 32 cortes en 120s → plano ~3.75 s. Rápido/dinámico: talking-head + muchos inserts de b-roll.
- **Recursos de edición:** UGC a mano + b-roll abundante (pulpo/mariscos crudos, ingredientes, pastillas en palma, botes) + props cómicos (teléfono antiguo). Cortes secos. Mucho intercut producto↔presentador.
- **Texto en pantalla / subtítulos:** Doble capa: titular tipo meme arriba ("Your kidneys left a voicemail") + subtítulo karaoke abajo mayúsculas con keyword resaltada (verde/blanco con borde).
- **Audio:** VO masculina (inglés, cómico/coloquial); actuación de sketch + música ligera. Casi continuo. SFX/beats de comedia en los cortes.
- **CTA:** Suave en los últimos ~15-20s sosteniendo los paquetes a cámara (branding ASTAXANTHIN). Implícito.
- **Recreabilidad:** Creador UGC carismático + props (teléfono antiguo) + b-roll de mariscos/ingredientes y producto + paquetes + edición rápida con cortes secos + doble capa de texto (meme-headline + subtítulos karaoke) + guion humor→educación→producto.

### UGC-ES_antesdespues-nutravia_e15b.mp4
- **Specs:** 23.2 s, 360x640 (9:16, baja resolución UGC nativo de móvil), 30 fps.
- **Formato/género:** Anuncio UGC de transformación corporal en **español** para gotas herbales de drenaje linfático / pérdida de peso, marca "**nutravia**". Testimonio antes/después de mujer joven. Para mujeres que quieren adelgazar/desinflamar.
- **Hook (primeros 3s):** Foto de la chica "antes" (más llenita, en un evento) + caption **"Un día me descuidé tanto 😅😬"**. Táctica: confesión vulnerable + auto-deprecación + promesa implícita de transformación.
- **Estructura/beats:** Hook "antes" + confesión (0–3s) → más fotos del "antes" + problema (3–10s) → solución "decidí probar el drenaje linfático del que todo el mundo hablaba, con las gotas herbales de nutravia" (10–16s) → resultado/cierre: selfies en espejo del "después" "Y amé el resultado 🥰" + "Si yo pude… tú también podías ❤️" (16–23s).
- **Ritmo de edición:** 16 cortes en 23s → plano ~1.4 s. Rápido, montaje de fotos/clips (slideshow de móvil).
- **Recursos de edición:** 100% UGC de móvil: selfies de espejo, fotos de eventos, exteriores. Sin b-roll de producto explícito (solo se nombra). Cortes directos; baja resolución refuerza autenticidad.
- **Texto en pantalla / subtítulos:** Captions sobreimpresos manualmente en español, blanco con sombra, centrados, con emojis ("Un día me descuidé tanto 😅😬", "Si yo pude… tú también podías ❤️").
- **Audio:** Sin VO detectable; probablemente música trending y storytelling solo por texto en pantalla.
- **CTA:** Emocional/aspiracional ("Si yo pude, tú también") más que CTA duro — invita a probar las gotas nutravia.
- **Recreabilidad:** Muy fácil/barato: fotos reales antes/después (o UGC) + selfies de espejo + captions de storytelling en primera persona con emojis + música trending + mención de marca. Sin actores, set ni locución.

---

*Generado con análisis ffmpeg (ffprobe + scene-detect umbral 0.3 + silencedetect) y lectura de frames con visión. 39 videos · biblioteca de formatos para iteración de ads. Carpeta fuente: `videos formatos/`.*

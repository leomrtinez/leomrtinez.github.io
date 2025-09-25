---
layout: archive
title: "PhD Defense Announcement"
permalink: /PhD_defense/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

I am pleased to announce the public defense of my doctoral thesis, conducted under the supervision of **Pr. Frédéric Schmidt** and **Dr. François Andrieu** at **GEOPS (Université Paris-Saclay)**.

---

### Date & Time:
6 October 2025, 2:00 PM (Paris time, UTC+2)  

### Location:  
[Blandin Amphitheater](https://maps.app.goo.gl/AgZ5aw3tUPTGKppXA)   
Laboratoire de Physique des Solides   
1 rue Nicolas Appert, Bâtiment 510  
91405 Orsay Cedex – France  

<div style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; border-radius:12px; box-shadow:0 2px 6px rgba(0,0,0,0.2);">
  <iframe 
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2638.3001922710157!2d2.182097676968759!3d48.69912297131009!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e67701b2af65b3%3A0x7bfe8e7d7f2571bb!2sLaboratoire%20de%20Physique%20des%20Solides%2C%201%20Rue%20Nicolas%20Appert%2C%2091405%20Orsay%2C%20France!5e0!3m2!1sfr!2sfr!4v1727277312345!5m2!1sfr!2sfr" 
    width="100%" 
    height="100%" 
    style="position:absolute; top:0; left:0; border:0;" 
    allowfullscreen="" 
    loading="lazy" 
    referrerpolicy="no-referrer-when-downgrade">
  </iframe>
</div>
---

The defense is open to all, and everyone is warmly welcome to attend either in person or online.  

### Public Zoom link:
[Join the defense here](https://universite-paris-saclay-fr.zoom.us/j/93874359215pwd=8HtlagOW527a09Ha36V3OxPGl9F8BY.1)

---
### Jury Members: 

➲ **[Frédéric SCHMIDT](https://fredericschmidt.github.io)**, Directreur de thèse  
➲ **[François ANDRIEU](https://www.idref.fr/19359854X)**, Co-directreur de thèse  
➲ **[Marc HUERTAS-COMPANY](https://mhuertascompany.github.io)**, Rapporteur   
➲ **[Stéphane LE MOUELIC](https://lpg-umr6112.fr/member/le-mouelic-stephane/)**, Rapporteur   
➲ **[Sylvain BOULEY](https://www.iufrance.fr/les-membres-de-liuf/membre/2071.html)**, Examinateur     
➲ **[Myriam LEMELIN](https://www.usherbrooke.ca/geomatique/departement/personnel/personnel-enseignant/myriam-lemelin)**, Examinatrice  
➲ **[Cathy QUANTIN-NATAF](https://eplanets.univ-lyon1.fr/equipe/permanents/cathy-quantin/)**, Examinatrice   

---



## 📖 Résumé (Français)

Titre: **ACDC : Détection et Charactérisation automatique de Cratères**

Mots clés: Planétologie ; Cratère d'impact ; Intelligence Artificielle ; Géomorphologie ; Géochronologie ; Télédétection.

Résumé : 
L’étude des cratères d’impact à la surface des corps telluriques constitue un outil central pour dater les terrains et reconstruire l’histoire géologique des planètes. Cette méthode repose toutefois sur une connaissance fine de la morphologie des cratères, car certaines morphologies, comme les cratères secondaires ou fortement dégradés, doivent être exclus des comptages sous peine de biaiser les résultats. Pendant cette thèse, nous avons développé de nouvelles méthodes de traitement en combinant à la fois des techniques d’apprentissage à base de réseaux de neurone artificiels et des méthodes de traitement d’images et d’analyse géomorphologique avancée. Grâce à cela nous sommes capables de détecter automatiquement les cratères présents dans les images à haute résolution, de corriger leur géométrie, puis de les classifier selon leur morphologie. 
Nous nous appuyons sur les mosaïques globales de Mars acquises par la caméra CTX et sur une base de données de cratères classifiés, que nous avons améliorées par une méthode de détection de cercles fondée sur la transformée de Hough. Cette étape améliore la précision géométrique des annotations, en recentrant automatiquement les cratères et en ajustant leur rayon au plus proche de la structure visible sur l'image. Nous avons ensuite conçu une méthode de détection multi-échelle permettant d’identifier tous les cratères, quelles que soient leur taille, géométrie, éclairement ou position en latitude / longitude. Chaque image est analysée à différentes résolutions, et les résultats sont fusionnés pour éviter les redondances. Nous avons entraîné un modèle de classification profond (YOLOv11) capable d’attribuer à chaque cratère l’une des quatre classes gémorphologiques : ordinaire, secondaire, fantôme ou à rempart fluidisé. 
La dernière partie porte sur la détermination de l'ordre de superposition des cratères, lorsqu'ils se recouvrent. L’ensemble constitue une suite d'outils robuste pour automatiser la cartographie géomorphologique planétaire, améliorer la fiabilité des datations et, à terme, faciliter l’analyse d’autres corps. Tous ces outils ont été évalués et validés sur des données totalement indépendantes de l'entrainement pour une utilisation scientifique avec des incertitudes maitrisées. En perspective, cette suite d'outils permettra de mieux appréhender les larges volumes de données de l’imagerie astronomique, car les objets d’intérêts sont souvent présents à plusieurs échelles. En particulier, nous proposons d’étudier la détection et la caractérisation de cratères à la surface des planètes et autres corps du système solaire.

---

## 📖 Summary (English)


Title: **ACDC: Automatic Crater Detection and Characterization**

Keywords: Planetary Sciences ; Impact craters, Artificial Intelligence ; Geomorphology ; Geochronology ; Remote-sensing.

 
Abstract:
The study of impact craters on the surface of terrestrial bodies is a central tool for dating geological units and reconstructing planetary histories. However, this method relies on a detailed understanding of crater morphology, as certain types — such as secondary or heavily degraded craters — must be excluded from crater counting to avoid significant biases. The objective of this thesis is to develop new methods that combine deep learning techniques based on artificial neural network architectures with advanced image processing and geomorphological analysis, in order to automatically detect craters in high-resolution imagery, refine their geometry, and classify them by morphology. We rely on global mosaics acquired by the CTX camera on Mars and on an existing classified crater database, which we refined using a circle detection method based on the Hough transform. This step improves the geometric accuracy of annotations by automatically recentering craters and adjusting their radii to best match the visible structures on the image. We then designed a multi-scale detection method capable of identifying all craters, regardless of their size, geometry, illumination conditions or position in latitude / longitude. Each image is analyzed at different resolutions, and results are merged to avoid redundancy. We trained a deep classification model (YOLOv11) capable of assigning each crater to one of four morphological classes: regular, secondary, ghost, or layered-rimmed. The last part consist in the determination of the superposition order, when the crater are overlapping each other. The resulting pipelines are a robust suite of tools for automating planetary geomorphological mapping, improving the reliability of surface dating, and ultimately supporting the analysis of other planetary bodies. All the tools have been evaluated and validated with data totally independent from the training dataset in order to have a scientific use with known uncertainties. In perspective, this suite of tools will help to better apprehend the large datasets of astronomical imaging, as objects of interest often appear at multiple spatial scales. In particular, we propose the detection and characterization of craters on planets and other planetary bodies of the Solar System.

 

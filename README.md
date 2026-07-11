# Linux Privileged Access Review 🔐

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux-FCC624?logo=linux&logoColor=black)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Security](https://img.shields.io/badge/Focus-IAM%20Audit-darkred)
![Made With](https://img.shields.io/badge/Made%20with-Python-blueviolet)

---

## 🚀 Sobre el proyecto

En sistemas Linux, los privilegios suelen concederse con frecuencia, pero no siempre se revisan con la misma regularidad.

Con el tiempo, cuentas de antiguos empleados, contratistas o usuarios temporales pueden conservar permisos elevados sin que exista una necesidad operativa clara.

**Linux Privileged Access Review** es un proyecto personal desarrollado en Python que ayuda a identificar cuentas privilegiadas que podrían requerir una revisión, combinando la pertenencia a grupos privilegiados con la actividad registrada de cada usuario.

El objetivo del proyecto es demostrar conocimientos de administración de sistemas Linux, automatización y análisis básico de riesgo mediante reglas sencillas.

---

# 🏗️ Problema y Solución

### Problema

Durante una revisión de accesos suele ser difícil responder preguntas como:

- ¿Qué usuarios mantienen privilegios elevados?
- ¿Han utilizado realmente esos privilegios recientemente?
- ¿Qué cuentas deberían revisarse?

Aunque existen soluciones completas de IAM y PAM, muchas organizaciones pequeñas o laboratorios necesitan una forma sencilla de identificar cuentas que merecen una revisión.

### Solución

El proyecto recopila información de usuarios, grupos privilegiados (primarios y secundarios) y actividad registrada mediante `lastlog` para calcular un puntaje de riesgo basado en reglas simples.

El resultado es un resumen que ayuda a priorizar qué cuentas deberían revisarse primero durante una auditoría de accesos.

---

# ✨ Características

Actualmente el proyecto permite:

- ✅ Identificar usuarios pertenecientes a grupos privilegiados (`sudo`, `docker`, `adm`, entre otros), incluyendo grupos primarios (GID) y secundarios.
- ✅ Analizar la actividad reciente utilizando `lastlog`.
- ✅ Calcular un puntaje de riesgo basado en privilegios e inactividad.
- ✅ Mostrar un reporte formateado en consola como tabla para facilitar la revisión.
- ✅ Exportar resultados a JSON para auditorías o ingestión en otros sistemas.

---

# ⚖️ Lógica de evaluación

El puntaje de riesgo se calcula combinando distintos factores, entre ellos:

- Pertenencia a uno o varios grupos privilegiados.
- Tiempo de inactividad de la cuenta.
- Reglas de evaluación definidas dentro del proyecto.

El objetivo del análisis es ayudar a priorizar revisiones de acceso; no determina automáticamente si una cuenta representa una amenaza.

---

# 📊 Ejemplo de salida

```text
--- LINUX PRIVILEGED ACCESS REVIEW ---

+-----------+---------+---------+-----------------------------------+
| Usuario   | Nivel   |   Score | Razones                           |
+===========+=========+=========+===================================+
| eduar     | MEDIUM  |      40 | Privileged groups: adm, sudo, lxd |
+-----------+---------+---------+-----------------------------------+

Total usuarios revisados: 1

[+] Reporte exportado a report.json
```





# 🛠️ Tecnologías utilizadas

    Python 3
    Linux
    Bash
    pwd
    grp
    subprocess
    datetime
    tabulate


📁 Estructura del Proyecto
Text

.
├── analyzer/
│   ├── users.py
│   ├── groups.py
│   ├── risk.py
│   └── report.py
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE


# ⚙️ Arquitectura
El proyecto sigue un flujo modular donde cada componente tiene una responsabilidad específica.

Usuarios Linux
        │
        ▼
Obtención de usuarios
        │
        ▼
Identificación de grupos privilegiados (GID primario + secundarios)
        │
        ▼
Consulta de actividad (lastlog)
        │
        ▼
Motor de evaluación de riesgo
        │
        ▼
Reporte en consola (tabla) + Exportación JSON


# ⚠️ Limitaciones
Este proyecto está orientado a ejercicios de auditoría y aprendizaje.

    No realiza monitoreo continuo.
    No modifica permisos del sistema.
    El puntaje de riesgo se basa en reglas definidas dentro del proyecto.
    Los resultados deben interpretarse como apoyo para una revisión manual.



# 🎯 Objetivo del Proyecto
Este repositorio fue desarrollado como proyecto de aprendizaje para practicar:

    Automatización con Python.
    Administración de sistemas Linux.
    Auditoría básica de accesos privilegiados.
    Análisis mediante reglas de riesgo.
    Organización y documentación de proyectos técnicos en GitHub.

El proyecto no pretende sustituir soluciones completas de gestión de identidades (IAM/PAM), sino demostrar una implementación propia para apoyar revisiones periódicas de cuentas privilegiadas.

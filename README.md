# Linux Privileged Access Review 🔐

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux-FCC624?logo=linux&logoColor=black)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Security](https://img.shields.io/badge/Focus-Access%20Review-darkred)
![Made With](https://img.shields.io/badge/Made%20with-Python-blueviolet)

---

## 🚀 Sobre el proyecto

En la administración de sistemas Linux, crear usuarios y asignar permisos suele ser una tarea habitual.

El verdadero desafío aparece cuando es necesario revisar si esos privilegios siguen siendo necesarios con el tiempo.

Es común encontrar situaciones como:

- Usuarios que continúan perteneciendo a grupos privilegiados.
- Cuentas con permisos administrativos que ya no tienen una necesidad operativa clara.
- Accesos elevados que nunca fueron revisados después de ser asignados.

**Linux Privileged Access Review** es un proyecto personal desarrollado en Python que analiza cuentas privilegiadas en sistemas Linux combinando información de grupos críticos y actividad registrada mediante `lastlog`.

El objetivo del proyecto es generar información que facilite una revisión manual de accesos, practicando conceptos de:

- Administración de usuarios y grupos en Linux.
- Automatización con Python.
- Auditoría básica de privilegios.
- Análisis de riesgo basado en reglas.

Este proyecto no busca reemplazar soluciones empresariales de IAM o PAM, sino servir como laboratorio práctico para comprender cómo automatizar revisiones de acceso en entornos Linux.

---

# 🏗️ Problema y Solución

## Problema

Durante una revisión de accesos pueden surgir preguntas como:

- ¿Qué usuarios mantienen privilegios elevados?
- ¿Qué cuentas pertenecen a grupos administrativos?
- ¿Existen usuarios con permisos que deberían ser revisados?
- ¿Qué cuentas tienen poca o ninguna actividad reciente?

Realizar estas comprobaciones manualmente puede resultar repetitivo cuando se administran varios sistemas Linux.

## Solución

El proyecto recopila información del sistema para identificar cuentas privilegiadas mediante:

- Membresía en grupos críticos como `sudo`, `docker`, `adm`, entre otros.
- Grupos primarios y secundarios asociados al usuario.
- Última actividad registrada mediante `lastlog`.

Con esta información genera un puntaje de riesgo basado en reglas simples, permitiendo priorizar qué cuentas podrían requerir una revisión.

---

# ✨ Características

Actualmente el proyecto permite:

- ✅ Identificar usuarios pertenecientes a grupos privilegiados (`sudo`, `docker`, `adm`, entre otros).
- ✅ Analizar grupos primarios (GID) y secundarios asociados a cada usuario.
- ✅ Consultar actividad reciente utilizando `lastlog`.
- ✅ Generar un puntaje de riesgo basado en privilegios e inactividad.
- ✅ Mostrar resultados en consola mediante una tabla.
- ✅ Exportar reportes en formato JSON.

---

# ⚖️ Lógica de evaluación del riesgo

El puntaje generado funciona como una referencia para priorizar revisiones.

La evaluación considera factores como:

- Pertenencia a uno o varios grupos privilegiados.
- Tiempo desde la última actividad registrada.
- Reglas definidas dentro del proyecto.

El resultado no determina automáticamente si una cuenta representa un riesgo; sirve como apoyo para una revisión manual más eficiente.

---

# 📊 Ejemplo de salida

```text
--- LINUX PRIVILEGED ACCESS REVIEW ---

+-----------+---------+---------+-----------------------------------+
| Usuario   | Nivel   | Score   | Razones                           |
+===========+=========+=========+===================================+
| eduar     | MEDIUM  | 40      | Privileged groups: adm,sudo,lxd  |
+-----------+---------+---------+-----------------------------------+

Total usuarios revisados: 1

[+] Reporte exportado a report.json
```

---

# 🛠️ Tecnologías utilizadas

- Python 3
- Linux
- Bash

Librerías utilizadas:

- pwd
- grp
- subprocess
- datetime
- tabulate

---

# 📁 Estructura del Proyecto

```
linux-privileged-access-review/

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
```

---

# ⚙️ Arquitectura

El proyecto utiliza una estructura modular donde cada componente tiene una responsabilidad específica.

```
Usuarios Linux
        │
        ▼
Obtención de información del sistema
        │
        ▼
Identificación de grupos privilegiados
(GID primario + grupos secundarios)
        │
        ▼
Consulta de actividad mediante lastlog
        │
        ▼
Motor de evaluación de riesgo
        │
        ▼
Reporte en consola + Exportación JSON
```

---

# ⚠️ Limitaciones

Este proyecto está orientado a aprendizaje y práctica de administración Linux.

Actualmente:

- No realiza monitoreo continuo.
- No modifica permisos del sistema.
- No reemplaza soluciones IAM/PAM empresariales.
- El puntaje depende de reglas definidas dentro del proyecto.
- Los resultados requieren validación manual antes de tomar decisiones.

---

# 🎯 Objetivo del Proyecto

Este repositorio fue desarrollado como proyecto práctico para reforzar conocimientos en:

- Automatización de tareas administrativas con Python.
- Administración de usuarios y grupos Linux.
- Auditoría básica de accesos privilegiados.
- Análisis mediante reglas de riesgo.
- Organización y documentación técnica en GitHub.

La finalidad del proyecto es demostrar cómo una tarea repetitiva de administración Linux puede automatizarse para apoyar revisiones periódicas de privilegios.

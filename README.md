# Linux Privileged Access Review 🔐

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux-FCC624?logo=linux&logoColor=black)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Security](https://img.shields.io/badge/Focus-Access%20Review-darkred)
![Made With](https://img.shields.io/badge/Made%20with-Python-blueviolet)

---

## 🚀 Sobre el proyecto

En Linux, asignar privilegios administrativos es una tarea común. El desafío aparece con el tiempo: saber si esos accesos siguen siendo necesarios.

Durante la administración de sistemas es frecuente encontrar situaciones como:

- Usuarios que continúan perteneciendo a grupos privilegiados sin una necesidad operativa clara.
- Cuentas de servicio con permisos elevados que nunca fueron revisados después de ser asignados.
- Accesos administrativos que persisten porque nadie se dio cuenta de que ya no se usan.

Cuando aumenta la cantidad de usuarios o sistemas administrados, realizar estas comprobaciones manualmente se vuelve repetitivo y propenso a pasar información por alto.

**Linux Privileged Access Review** es una herramienta personal desarrollada en Python que analiza cuentas privilegiadas combinando información de grupos críticos (`sudo`, `docker`, `adm`, entre otros) con actividad registrada mediante `lastlog`.

El proyecto genera un puntaje de riesgo basado en heurísticas definidas, permitiendo priorizar cuentas que podrían requerir una revisión manual.

No busca reemplazar soluciones empresariales IAM/PAM, sino demostrar cómo una tarea de administración Linux puede automatizarse utilizando información disponible directamente desde el sistema.

---

## 🏗️ Problema y Solución

### Problema

Durante una revisión de accesos surgen preguntas como:

- ¿Qué usuarios mantienen privilegios elevados?
- ¿Qué cuentas pertenecen a grupos administrativos?
- ¿Qué accesos deberían revisarse?
- ¿Qué usuarios presentan poca o ninguna actividad reciente?

Realizar este análisis manualmente puede ser lento y propenso a errores.

### Solución

El proyecto recopila información del sistema para identificar cuentas privilegiadas mediante:

- Membresía en grupos críticos como `sudo`, `docker` y `adm`.
- Grupos primarios (GID) y secundarios asociados al usuario.
- Última actividad registrada mediante `lastlog`.

Con esta información aplica reglas de evaluación para generar un puntaje que ayuda a ordenar las revisiones de acceso.

---

## ✨ Características

- Identificación de usuarios pertenecientes a grupos privilegiados.
- Análisis de grupos primarios y secundarios.
- Consulta de última actividad mediante `lastlog`.
- Evaluación de riesgo basada en privilegios e inactividad.
- Reporte visual en consola mediante tabla formateada.
- Exportación de resultados en formato JSON.

---

## ⚖️ Lógica de evaluación del riesgo

El puntaje generado funciona como referencia para priorizar revisiones.

Los factores considerados incluyen:

- Pertenencia a uno o varios grupos privilegiados.
- Tiempo desde la última actividad registrada.
- Heurísticas definidas dentro del proyecto.

El resultado no determina automáticamente si una cuenta es segura o insegura. Su función es proporcionar información adicional para una revisión manual.

---

## 📊 Ejemplo de salida

```text
--- LINUX PRIVILEGED ACCESS REVIEW ---

+-----------+---------+---------+------------------------------+
| Usuario   | Nivel   |   Score | Razones                      |
+===========+=========+=========+==============================+
| raude     | MEDIUM  |      40 | Privileged groups: adm, sudo |
+-----------+---------+---------+------------------------------+

Total usuarios revisados: 1

[+] Reporte exportado a report.json
```

# 🎮 Uso
El proyecto se ejecuta en un solo paso:
```
python3 main.py
```
El script analiza automáticamente todos los usuarios del sistema, evalúa sus privilegios y genera el reporte en consola junto con la exportación a report.json.

🛠️ Tecnologías utilizadas

    Python 3
    Linux
    Bash

Librerías utilizadas:

    pwd
    grp
    subprocess
    datetime
    tabulate

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

# ⚙️ Arquitectura

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

# ⚠️ Alcance

- Analiza usuarios y grupos locales del sistema.
- No integra actualmente con LDAP, Active Directory u otros proveedores externos de identidad.
- No modifica permisos ni realiza acciones automáticas sobre cuentas.
- Diseñado para revisiones puntuales, no monitoreo continuo.
- Los resultados requieren validación manual.

# 🚀 Instalación
```
git clone https://github.com/eduar-q/linux-privileged-access-review.git
cd linux-privileged-access-review
pip install -r requirements.txt
```

📝 Licencia
MIT License — ver LICENSE para detalles.

# Access Relevance Analyzer

Identifica cuentas privilegiadas en sistemas Linux que podrían no necesitar acceso actualmente.

## Why?
Las organizaciones otorgan accesos constantemente, pero rara vez los auditan. Con el tiempo, cuentas de contratistas, empleados que cambiaron de rol o pruebas temporales permanecen activas con privilegios elevados. 

**Access Relevance Analyzer** ayuda a los administradores a auditar permisos olvidados combinando la actividad real de las cuentas y la jerarquía de grupos para generar un puntaje de riesgo accionable.

## Features
- ✅ **Privileged account discovery:** Detecta automáticamente usuarios en grupos críticos como `sudo`, `docker`, `adm` y otros.
- ✅ **Inactivity analysis:** Analiza `lastlog` para identificar cuentas que no han tenido actividad reciente.
- ✅ **Risk Scoring:** Calcula un nivel de riesgo basado en la combinación de privilegios y tiempo de inactividad.
- ✅ **Executive Summary:** Genera reportes directos en consola para auditorías rápidas.

## Installation

```
git clone [https://github.com/eduar696/access-relevance-analyzer](https://github.com/TU_USUARIO_AQUI/access-relevance-analyzer)
cd access-relevance-analyzer
pip install -r requirements.txt
```

## Usage

Para ejecutar el escaneo, simplemente usa:

```
python3 main.py
```

## Example Output

Este es un ejemplo de lo que verás al ejecutar el script en un sistema con usuarios privilegiados:

```
--- ACCESS RELEVANCE ANALYZER ---

User: eduar
  Level: MEDIUM (Score: 40)
  Reasons: Privileged groups: adm, sudo, lxd
--------------------
```


## How it works

El proyecto utiliza una arquitectura modular diseñada para facilitar la auditoría y el mantenimiento:

    users.py: Recopila la información de identidad del sistema.

    groups.py: Identifica qué usuarios poseen privilegios elevados.

    risk.py: Aplica la lógica de evaluación para clasificar la amenaza.

    main.py: Orquesta el flujo de trabajo y presenta los resultados.

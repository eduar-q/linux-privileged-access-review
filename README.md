# Access Relevance Analyzer

Identifica cuentas privilegiadas en sistemas Linux que podrían no necesitar acceso actualmente.

## ¿Por qué?
Las organizaciones otorgan accesos constantemente, pero rara vez los auditan. Con el tiempo, cuentas de contratistas, empleados que cambiaron de rol o pruebas temporales permanecen activas con privilegios elevados. 

**Access Relevance Analyzer** ayuda a los administradores a auditar permisos olvidados combinando la actividad real de las cuentas y la jerarquía de grupos para generar un puntaje de riesgo accionable.

## Características
- ✅ **Descubrimiento de cuentas privilegiadas:** Detecta automáticamente usuarios en grupos críticos como `sudo`, `docker`, `adm` y otros.
- ✅ **Análisis de inactividad:** Analiza `lastlog` para identificar cuentas que no han tenido actividad reciente.
- ✅ **Puntuación de riesgo:** Calcula un nivel de riesgo basado en la combinación de privilegios y tiempo de inactividad.
- ✅ **Resumen ejecutivo:** Genera reportes directos en consola para auditorías rápidas.

## Instalación
```
git clone [https://github.com/eduar696/access-relevance-analyzer](https://github.com/eduar696/access-relevance-analyzer)
cd access-relevance-analyzer
pip install -r requirements.txt
```

## Uso

Para ejecutar el escaneo, simplemente usa:

```
python3 main.py
```
## Ejemplo de salida

Este es un ejemplo de lo que verás al ejecutar el script en un sistema con usuarios privilegiados:


```
--- ACCESS RELEVANCE ANALYZER ---

User: eduar
  Level: MEDIUM (Score: 40)
  Reasons: Privileged groups: adm, sudo, lxd
--------------------
```

¿Cómo funciona?

El proyecto utiliza una arquitectura modular diseñada para facilitar la auditoría y el mantenimiento:

- users.py: Recopila la información de identidad del sistema.

- groups.py: Identifica qué usuarios poseen privilegios elevados.

-risk.py: Aplica la lógica de evaluación para clasificar la amenaza.

- main.py: Orquesta el flujo de trabajo y presenta los resultados.

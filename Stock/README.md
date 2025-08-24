# Stock Alert: Apple (AAPL)

Script en Python que monitorea el precio diario de AAPL (Apple) usando Alpha Vantage. Si la variación diaria supera un umbral (ej. 1%), obtiene titulares recientes sobre la compañía desde NewsAPI y envía un SMS con Twilio.

- Estado: En desarrollo
- Tipo: Script CLI
- Lenguaje: Python 3.12.5

## Características

- Obtiene los precios diarios de AAPL desde Alpha Vantage (Time Series Daily).
- Calcula la variación porcentual entre dos cierres recientes.
- Si supera el umbral, consulta las últimas noticias de Apple en NewsAPI.
- Envía un resumen por SMS utilizando Twilio.

## Requisitos

- Python 3.12.5
- Cuenta y API Key de:
  - Alpha Vantage
  - NewsAPI
  - Twilio (con un número habilitado para enviar SMS)

## Variables de entorno

Configura las siguientes variables de entorno antes de ejecutar:

- ALPHAVANTAGE_API_KEY: API key de Alpha Vantage
- NEWS_API_KEY: API key de NewsAPI
- ACCOUNT_SID_TW: Twilio Account SID
- AUTH_TOKEN_TW: Twilio Auth Token
- NUMBERS_TW: Número de Twilio (formato E.164, por ejemplo +15551234567)
- MY_NUMBER_TW: Tu número de teléfono receptor (formato E.164, por ejemplo +15557654321)

## Instalación

Se recomienda usar un entorno virtual.

## Uso

Ejecuta el script desde la raíz del proyecto: 

`bash python main.py`

Notas:
- El script compara variación diaria y, si supera un umbral (p. ej., 1%), obtiene hasta 3 titulares y los envía por SMS.
- Asegúrate de tener saldo/creditos y un número verificado/activo en Twilio.
- Ten en cuenta los límites de uso (rate limits) de Alpha Vantage y NewsAPI.

## Configuración

Valores por defecto importantes:
- Símbolo (ticker): AAPL
- Nombre de la compañía: Apple
- Umbral de alerta: 1% (puedes ajustarlo en el código si lo deseas)

## Solución de problemas

- 401/403 al consultar APIs: verifica tus API keys.
- 429 (rate limit): espera unos minutos o utiliza planes con mayor cuota.
- Twilio no envía el SMS:
  - Revisa que el número de origen (NUMBERS_TW) esté habilitado.
  - En modo trial, Twilio solo envía a números verificados.
  - Verifica formato E.164 en los números.

## Seguridad

- No subas tus API keys al repositorio.
- Usa variables de entorno o un gestor de secretos.

## Licencia

Define la licencia que prefieras (MIT/Apache-2.0/GPL-3.0). Ejemplo:
Este proyecto se distribuye bajo la licencia MIT. Consulta LICENSE para más detalles.

## Autor

- Joaquin Albano (@dimyakk)
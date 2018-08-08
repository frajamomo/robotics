#! /bin/bash

URL="http://www.bde.es/bde/es/secciones/convocatorias/Trabajar_bde/Convocatorias/"

mv new.html old.html 2> /dev/null
curl $URL -L --compressed -s > new.html

TEXTO_OLD=`grep -A 20 "Auxiliar administrativo de oficina" old.html | sed -e 's/<[^>]*>//g' | grep Actualizado`
TEXTO_NEW=`grep -A 20 "Auxiliar administrativo de oficina" new.html | sed -e 's/<[^>]*>//g' | grep Actualizado`

if [ "$TEXTO_OLD" != "$TEXTO_NEW" ]; then
    echo "Sería buena idea chequear la pagina del banco.... $TEXTO_NEW $URL" | mail -s "Alfred" frajamomo@gmail.com -u pi
    logger "checked $URL Sending mail"
else
    logger "checked $URL Nothing to report"
fi


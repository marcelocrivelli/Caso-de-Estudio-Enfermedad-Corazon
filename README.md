# Caso de Estudio Enfermedad Corazón

El siguiente caso de estudio es sobre la predicción de enfermedades del corazón en distintos pacientes. Los datos para este problema provienen de 4 bases de datos:

<ul>
  <li>Cleveland Clinic Foundation</li>
  <li>Hungarian Institute of Cardiology, Budapest</li>
  <li>V.A. Medical Center, Long Beach, CA</li>
  <li>University Hospital, Zurich, Switzerland</li>
</ul>

Cada base de datos tiene el mismo formato de los ejemplos. Las bases tienen 76 atributos en total. De estos atributos, los más importantes son 14:

<ul>
  <li><b>age</b>: Edad en años (Integer)</li>
  <li><b>sex</b>: (1 = hombre; 0 = mujer) (Polynominal)</li>
  <li><b>cp</b>: Dolor torácico (1 = angina típica; 2 = angina atípica; 3 = dolor no anginal; 4 = asintomático) (Polynominal)</li>
  <li><b>trestbps</b>: presión arterial en reposo (en mm Hg en el ingreso al hospital) (Integer)</li>
  <li><b>chol</b>: colestoral sérico en mg/dl (Integer)</li>
  <li><b>fbs</b>: (nivel de azúcar en sangre en ayuno mayor a 120 mg/dl) (1 = verdadero; 0 = falso) (Polynominal)</li>
  <li><b>restecg</b>: resultados electrocardiográficos en reposo (0 = normal; 1 = con anormalidad de onda ST-T (inversiones de onda T y/o elevación ST o depresión de > 0,05 mV); 2 = mostrando una hipertrofia ventricular izquierda probable o definitiva según los criterios de Estes) (Polynominal)</li>
  <li><b>thalach</b>: frecuencia cardíaca máxima alcanzada (Integer)</li>
  <li><b>exang</b>: angina inducida por ejercicio (1 = sí; 0 = no) (Polynominal)</li>
  <li><b>oldpeak</b>: depresión ST inducida por el ejercicio en relación con el descanso (Real)</li>
  <li><b>slope</b>: la pendiente del eje de pico segmento ST (0 = pendiente ascendente; 1 = plana; 2 = pendinete descendente) (Polynominal)</li>
  <li><b>ca</b>: número de vasos principales (0-3) coloreados por flourosopy (Polynominal)</li>
  <li><b>thal</b>: (3 = normal; 6 = defecto fijo; 7 = defecto reversible) (Polynominal)</li>
  <li><b>num</b>: diagnóstico de cardiopatía (estado de la enfermedad angiográfica) (0: estrechamiento de < 50% de diámetro; 1,2,3,4 : estrechamiento > 50% de diámetro (en cualquier vaso importante del corazón) (Polynominal) </li>
</ul>

La variable objetivo para este caso de estudio es num, que indica la presencia (valor 0) o no de la enfermedad del corazón en el paciente (valor 1,2,3,4). Se generó un modelo en RapidMiner para realizar la predicción.

Los datos se encuentran con una extensión ".data". Cada 10 líneas de cualquiera de los archivos se tiene los 76 atributos de un paciente. Para lograr importar estos datasets a RapidMiner se precisa de tener todos los atributos de cada paciente en una línea separados. Por lo que fue necesario desarrollar un script en python (orderdata.py) para colocar los datos de cada paciente en una línea separados por un espacio. Este script fue aplicado a las 4 base de datos.

Los valores faltantes para los atributos están representados con "-9". Se detectaron muchos valores faltantes para los atributos importantes:

<ul>
  <li>trestbps: 59</li>
  <li>chol: 30</li>
  <li>fbs: 90</li>
  <li>restecg: 2</li>
  <li>thalach: 55</li>
  <li>exang: 55</li>
  <li>oldpeak: 62</li>
  <li>slope: 308</li>
  <li>ca: 608</li>
  <li>thal: 477</li>
</ul>

Una vez obtenidos los datasets finales, se importaron en RapidMiner. Se generó un proceso colocando los 4 datasets y uniéndolos con el operador Append. Como se tenían los datos con todos los atributos (76) se colocó un operador para seleccionar los 14 más importantes detallados anteriormente. Los valores faltantes fueron identificados con el operador Declare Missing Values para los que tienen valor -9. Luego se colocó el operador Replace Missing Values para probar diferentes formas de tratar los valores faltantes(promedio de atributos, valor máximo, valor mínimo, vacío). Para identificar el atributo objetivo se usó el operador Set Role en la columna num. Cross Validation fue utilizado para estimar el performance estadistico del modelo.
El modelo utilizado fue Random Forest, con una profundidad máxima de 15 de los 100 árboles. El criterio por los que los atributos son seleccionados para el splitting es gain_ratio.


Los resultados no fueron muy alentadores, se obtuvó un porcentaje de predicción de 52.83% +/- 3.38%. El recall para la clase 0 (estrechamienteo menor a 50% de diámetro de los vasos) fue muy bueno 89.6% pero el de las otras clases no (1 = 41.36%; 2 = 10%; 3 = 15.91%; 4 = 0%). La precisión para la clase 0 fue buena 69.48% como se vió en el recall, pero las otras fueron bastante bajas. Se cree que estos valores no tan buenos se deben a la gran cantidad de datos faltantes para los valores de los atributos.

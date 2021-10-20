# Análisis de datos empresa bellabeat

## Información básica:
Esta es la documentación del análisis de datos de la empresa bellabeat, una empresa que desarrolla computadoras portátiles enfocadas en la salud para mujeres. 
Bellabeat es una pequeña empresa exitosa, pero quieren convertirse en uno de los grandes competidores de dispositivos inteligentes en el mercado.
Como analista me han pedido que analizara uno de sus productos con el fin de conocer como los consumidores están usando sus productos.

Los principales productos de la empresa son los siguientes:
•	App de Bellabeat: Una aplicación que provee a los usuarios información relacionada con su sueño, estrés, actividad, ciclo menstrual etc. Con esta información el usuario logra hacer decisiones mas saludables. La app se conecta con su línea de productos inteligentes.
•	Leaf: Un brazalete, collar o clip inteligente que se conecta con la App Bellabeat para obtener la información del usuario.
•	Reloj: Un reloj inteligente que también se conecta con al App Bellabeat para dar información acerca del usuario
•	Spring: Una botella de agua inteligente que mide los litros de agua que has consumidos, se conecta a la App Bellabeat para medir y rastrear tus niveles de hidratación.
•	Membresía Bellabeat:  Un programa de membresías que guía al usuario en materia de nutrición, sueno, salud y belleza basados en sus objetivos y estilo de vida.

El departamento de marketing nos ha pedido analizar productos inteligentes de otra empresa para luego aplicar ese conocimiento aprendido en uno de los productos de bellabeat.
Para esto marketing necesita saber la respuesta a 3 preguntas claves:
1.	¿Cuáles son las tendencias en el uso de estos dispositivos inteligentes?
2.	¿Como estas tendencias pueden aplicarse a productos de bellabeat?
3.	¿Como puede estas tendencias influenciar la estrategia de marketing de bellabeat?
Para resolver estas preguntas se me recomienda usar los siguientes datos públicos de la empresa FitBit.
https://www.kaggle.com/arashnic/fitbit
Pero podríamos considerar agregar otra fuente de datos.

## La fuente de datos:
Para este análisis se nos recomendó usar un dataset en la página kaggle.com el cual proviene de unas encuestas hechas por Amazon Mechanical Turk entre 03.12.2016 y 05.12.2016, 30 usuarios dieron su consentimiento a dar los datos de su FitBit.
El dataset en kaggle dice que saco la data del siguiente lugar https://zenodo.org/record/53894#.YMoUpnVKiP9
Esta no es una fuente de datos apropiada para realizar el análisis debido a que proviene de una tercera parte no del todo confiable y la muestra solo es de 30 personas lo cual es muy pequeño para representar a toda la población de usuarios de productos inteligentes además de ser data del 2016 la cual puede no representar la realidad de la actualidad.
Por esto este análisis de tratar con cautela y no se deben tomar los resultados de este análisis como resultado cierto.

## Manipulación de datos:
Tomando en cuenta de que alguna de los archivos del dataset tiene millones de filas o registros podríamos usar varias herramientas como Excel con Power Pivot y Acess, SQL y una base de datos, Python o R.
Para este caso vamos a usar el lenguaje de programación Python tanto para manipular como para graficar los datos.
Si quieres saber cómo manipule los datos te recomiendo ir al archivo main.py
https://github.com/drincon02/analisis-bellabeat-python/blob/main/main.py

## Análisis Final:
El objetivo principal de este análisis es obtener información, tendencias acerca del uso que se les da a los productos de FitBit y como ese conocimiento puede ser aplicado a Bellabeat.
Para empezar este análisis lo primero que quiero conocer es quienes son los usuarios de FitBit por lo que vamos a ver cuál es su estado físico.

![image](https://user-images.githubusercontent.com/87548196/138177535-24d41eef-1541-413b-9968-4ffbc9c519a3.png)

Con este grafico puedo ver que la mayoría de los usuarios tienen sobrepeso o tienen peso normal mientras que muy pocos usuarios son obesos. Un factor importante que podría llegar a influir en el estado físico de un usuario es el sueño o mejor dicho la cantidad de horas que duerme al día.
El siguiente grafico va a ilustrar en rangos la cantidad de usuarios que duermen determinadas horas al día.

![image](https://user-images.githubusercontent.com/87548196/138177614-a27f8344-0722-4e75-86f7-4c6be8f570ee.png)

Con esto veo que la mayoría de los usuarios duerme de 5 a 8 horas al día mientras que muy pocos duermen más de 8 horas al día.
Sabiendo esto quiero saber que variables influyen en la cantidad de horas dormidas y en el estado físico para esto hare un gráfico de correlación pearson.

![image](https://user-images.githubusercontent.com/87548196/138177647-9e2bea31-bdfa-4276-a3a7-3d7628a02696.png)

Hay muchas cosas interesantes que podemos sacar de este grafico como que mientras más veces duermes al día peor estado de salud tiene la persona ya que tiene una correlación positiva de 0.93 entre Normal_Count y TotalSleepRecords y de 0.66 entre BMI y TotalSleepRecords pero en cuanto a la cantidad de minutos u horas dormidas no hay ninguna correlación visible.
También puedo observar que hay una relación positiva entre calorías quemadas y minutos muy activos de 0.63.
Mientras que para el BMI o Normal Count hay una relación negativa con todas las variables de distancia y tiempo de entrenamiento mientras que hay una positiva con minutos sedentario.

Ahora que conocemos la relación entre las variables y queremos saber qué diferencia existe entre cada grupo de usuarios.

![image](https://user-images.githubusercontent.com/87548196/138177736-1613b549-a9e7-456f-b619-c8a18640fb54.png)

Los usuarios que tienen peso normal y sobre pesor comparten similaridades en algunos hábitos y diferencias en otros, pero existe una gran diferencia entre hábitos con los usuarios obesos.

Ahora quiero conocer mas a fondo los hábitos de los usuarios por lo que voy a revisar en que día de la semana los usuarios están mas activos o entrenan mas
El siguiente cuadro compara las calorías quemadas con cada día de la semana
 
![image](https://user-images.githubusercontent.com/87548196/138177767-8c0762d5-aea6-4f4a-b91a-5d247688f550.png)
 
Como vemos en promedio no hay ningún día que resalte más que otro en cuanto a calorías quemadas. Así que vamos a ver si hay alguna diferencia en las horas de entrenamiento.

![image](https://user-images.githubusercontent.com/87548196/138177782-a434a5a0-b953-43e9-9177-20d76eb71dab.png)

Aquí si podemos ver que la mayoría de la mayor cantidad de calorías quemadas existe entre las 17 y 19 horas.

## Conclusiones y recomendaciones:
Con base al análisis hecho previamente no se pueden hacer conclusiones ni recomendaciones fuertes debido a la procedencia de los datos, pero si se puede aprender varios puntos importantes:
-	La mayoría de los usuarios de FitBit tienen sobrepeso o peso normal por lo que son personas que le prestan la suficiente atención a su cuerpo para cuidarlo y no entrar en la obesidad. Con esto (tomando en cuenta la procedencia de la data) la empresa BellaBeat podría dirigir su marketing a personas que toman tiempo y esfuerzo en cuidar su cuerpo al menos para evitar la obesidad y dormir de 5 a 8 horas una cantidad aceptable para un adulto.

-	También podemos ver que la mayoría de los usuarios hace ejercicio en la tarde con lo que ir a gimnasios a hacer marketing de este producto en la tarde podría ser una idea interesante o en cuyo caso de ser marketing digital antes de las 17 horas y después de las 19 horas .


-	Para recolección de datos podría ser una opción que el dispositivo guarde datos automáticamente en vez de ser introducidos manualmente como FitBit

-	A pesar a que la mayoría de los usuarios son saludables aún existe una gran diferencia entre usuario y usuario por lo que ofrecer opciones de customización para los diferentes objetivos que puede tener el usuario podría ser una buena opción especialmente si se quiere captar la atención de usuarios con obesidad.

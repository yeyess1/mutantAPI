# mutantAPI
Primero es necesario habilitar el uso de scripts, en caso de ya ternerlos permitidos saltar al paso 1:
	Damos click derecho sobre el icono de windows, y seleccionamos Windows powershell(Admin)

![image](https://user-images.githubusercontent.com/92695542/172235184-3912560c-2f2a-4f26-b280-708d1c7021b8.png)

	Una vez ahi colocamos :
		Set-EtwTraceProvider
	Verificamos que queden activos con el comando:
		Get-ExecutionPolicy -list

![image](https://user-images.githubusercontent.com/92695542/172235261-26aedef2-6a4b-4caf-9d7d-98795472591d.png)

Ya podemos cerrar esta pestaña. Presionamos Windows + R y accedemos a: gpedit.msc

Una vez aqui seleccionamos: plantillas administrativas

![image](https://user-images.githubusercontent.com/92695542/172235487-56e8cfa4-92a7-4a0f-9018-39d2abfd1bf0.png)

Una vez aqui buscamos Windows PowerShelly abrimos la carpeta
	Damos eclick en la opcion Activar la ejecucion de scripts
	Seleccionamos Habilitada y en la barra de Directiva de ejecucion seleccionamos 
	Permitir todos los scripts, damos Aplicar y Aceptar.

![image](https://user-images.githubusercontent.com/92695542/172235691-0a11c190-4bf0-4109-987b-0f7bb85028b7.png)



1. Acceder al terminal (preferiblemente desde el terminal de VC) e ingresar a la carpeta raiz:
	cd mutant_API

2. Crear el entorno virtual:
	pip install virtualenv
	Luego:
	virtualenv -p python env

 	Una vez ejecutada esta linea deberia verse un folder llamado env, comprobado esto procedemos
	a activar el entorno virtual:
	
![image](https://user-images.githubusercontent.com/92695542/172211747-7ef96f39-69b7-436b-8015-8a936f4608d8.png)

	.\env\Scripts\activate 

3. Comprobar (env) en la consola de comandos, con el entorno ya activo instalamos django: 

![image](https://user-images.githubusercontent.com/92695542/172210867-f5589a22-80c0-4221-9ce7-37242a7a77eb.png)


	pip install Django==3.2.4 

4.Instalar rest Framework: 
	
	pip install djangorestframework

5. Instalar manejadores sql: 
	
	pip install mysqlclient pymysql

6. Dentro de VC pesionar Ctrl+ Shift + P, una vez ahi pondremos :
	
	Python: Select Interpreter;

	En este punto daremos click derecho sobre la carpeta env, en el explorador de archivos
	de VC y seleccionaremos copy path, pegaremos esta ubicacion en la paleta de comandos abierta
	
![image](https://user-images.githubusercontent.com/92695542/172210564-6983c795-5369-469a-ba3b-2c22793ba370.png)

Deberia verse algo asi:

![image](https://user-images.githubusercontent.com/92695542/172212449-7e1f3fd2-1fea-40c7-a55b-753d80e7bd0e.png)


	 

7. En este punto ya deberia ser posible Arrancar el servicio:
	
	Desde el terminal de comandos de VC. Nos aseguramos de estar en el env, debe salir (env) antes de la ubicacion actual:
	
![image](https://user-images.githubusercontent.com/92695542/172210867-f5589a22-80c0-4221-9ce7-37242a7a77eb.png)
	
	De no ser asi repetir los comandos:
		cd mutant_API
		.\env\Scripts\activate 
	Deberia aparecer ahora el (env)
	
	Una vez en el entorno virtual y con todos los pasos previos:
		python manage.py runserver

8. Desplegar base de datos: 
	Dentro del archivo zip que conforma el proyecto se encuentra el script de la 
	base de datos (mutantDB), abrir el script en un gestor de base de datos. Para la
	creacion del script se uso Mysql. Una vez abierto el script en el entorno local del
	gestor de bases y creada la base de datos estamos listos para utilizar el servicio:

URL BASE: http://localhost:8000/mutant:
	
	Casos de prueba:
	Para validar una cadena de Adn en busca de ADN mutante:

	POST → /mutant/ : http://localhost:8000/mutant/mutant/
	{ 
		"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"] 
	} 
	
	Se recibe un 200.

	ADN humano: 
	POST → /mutant/
	{
		"dna":["ATGCGA","CAGTAC","AGTAGG","CCGCTA","TCACTG"]
	}
	
	Se espera un 403.
	
Despues de realizar una serie de consultas es posible validar la proporcion de
ADN mutantes y humanos: 

	GET → /stats/:  http://localhost:8000/mutant/stats/
	


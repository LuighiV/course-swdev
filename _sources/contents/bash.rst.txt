Scripting en Linux: Bash
========================

.. toctree::



Una de las herramientas más interesantes que tiene GNU/Linux es el uso de su
terminal, la cual permite entre otras cosas ejecutar todas las instrucciones
dentro del sistema operativo y, en consecuencia, automatizar las tareas que se
requieran para una aplicación determinada.

GNU/Linux es uno de los sistemas operativos con mayor presencia en servidores,
por lo cual saber utilizar su terminal es una herramienta muy útil para poder
desplegar servicios. Para ello se requiere conocer el intérprete de esta
consola (shell), siendo el más conocido y, en la mayoría de los casos, por
defecto, Bash.

Fundamentos de shell
--------------------

Intérpretes de shell
~~~~~~~~~~~~~~~~~~~~

Existen varios intérpretes para comunicarse con la terminal de Linux, entre los
principales se encuentran:

- **sh (Bourne Shell)** Es el shell original utilizado en UNIX.

- **bash (Bourne Again Shell)** Es el estándar para GNU/Linux es más intuitivo
  y confiable que sh.

- **csh (C shell)** Con una sintaxis parecida al lenguaje de programación C.

- **tcsh (TENEX C shell)** Es un superconjunto de csh, más amigable con el
  usuario y más rápido.

Para conocer los shells instalados en su sistema puede ejecutar lo siguiente en
la terminal:

.. code-block:: console

   $ cat /etc/shells

Por otra parte, el shell por defecto por usuario se puede encontrar en el
archivo :code:`/etc/passwd`.

A lo largo de esta revisión, se empleará :code:`bash` para todos los ejemplos.

Tipos de Shell
~~~~~~~~~~~~~~

Puede ser interactivo o no interactivo, que se refiere a la ineracción entre el
usuario y la shell y de login o no login, que se refiere al tipo de shell
empleado para acceder a un sistema computacional.

Para invocar a un shell interactivo non-login con bash, basta con ejecutar:

.. code-block:: console

   $ bash

Al ejecutarlo lo que se va a cargar al inicio es un archivo ubicado en
:code:`~/.bashrc`. 

En el caso de un sell interactivo login con bash, es ligeramente diferente:

.. code-block:: console

   $ bash --login

o mediante

.. code-block:: console

   $ bash -l

Este shell autentica primero al usuario cargando los archivos del perfil de
usuario ubicado en :code:`/etc/profile`, luego :code:`~/.profile` antes de cargar `~/.bashrc`.


Ejecutando comandos
~~~~~~~~~~~~~~~~~~~

Bash soporta tres tipos de comandos:

- **Comandos incluidos en Bourne**: :code:`:, ., break, cd, continue, eval, exec, exit, export, getopts, hash, pwd, readonly, return, set, shift, test, [, times, trap, umask, unset`.

- **Comandos incluidos en Bash**: :code:`alias, bind, builtin, command, declare, echo, enable, help, let, local, logout, printf, read, shopt, type, typeset, ulimit, unalias`.

- **Comandos especiales**: cuando se ejecuta en modo POSIX, estos son :code:`:, ., break, continue, eval, exec, exit, export, readonly, return, set, shift, trap, unset`.


Componentes de shell
~~~~~~~~~~~~~~~~~~~~

Sintaxis de shell
"""""""""""""""""

Si la entrada no está comentada, el shell la lee y la separa en palabras y
operadores utilizando las reglas de separación de bloques para definir el
significado de cada uno. El proceso se puede distinguir en los siguientes
pasos:

- El shell lee desde un archivo, desde una cadena de texto o desde la entrada
  del usuario.

- Divide la entrada en palabras y operadores.

- Analiza y sustituye las partes en comandos simples y compuestos.

- Bash realiza las expansiones necesarias.

- Se realiza las redirecciones necesarias.

- Se ejecutan los comandos.

- Opcionalmente espera que termine de ejecutarse y retorna el estado de
  finalización.

Comandos de shell
"""""""""""""""""

Un comando de shell normalmente tiene la siguiente estructura:

.. code-block:: console

   $ comando argumento_1 argumento_2 argumento_3

Donde la primera palabra consituye el nombre del comando y las siguientes
separadas por espacios son los argumentos para el comando, los cuales pueden
ser en una cantidad variable.


Funciones de shell
""""""""""""""""""

Las funciones son básicamente una agrupación de varios comandos. Estas
funciones pueden aceptar también una serie de argumentos variable como los
comandos que ejecuta en su declaración.


Parámetros de shell
"""""""""""""""""""

Un parámetro es una entidad que almacena información, que puede ser un nombre,
un número o un valor especial. En el caso del shell, una variable es un parámetro que almacena una nombre.

Scripts de shell
""""""""""""""""

Son ficheros que tienen una serie de comandos. Cuando se invocan con bash, lo
primero que hace es buscarlo en el directorio actual, y en caso de no
encontrarlo allí, en las ubicaciones declaradas en el `PATH` del sistema.


Scripts en Bash
---------------

Un script es un fichero que contiene un conjunto de instrucciones las cuales
serán interpretadas por el shell. Para ejecutar un script es necesario o bien
utilizar el intérprete como parte del comando de ejecución, o declarar el
intérprete dentro del fichero.

En el primer caso, se puede invocar de la siguiente manera:

.. code-block:: console

   $ /bin/bash script.sh

Usualmente los scripts para bash o cualquier intérprete en general tienen la
extensión :code:`.sh`. 

Por otra parte, en caso de requerir ejecutarlo directamente desde la terminal,
sin especificar el intérprete en el comando, primero, debe dar permisos de
ejecución al fichero mediante:

.. code-block:: console

   $ chmod +x script.sh

Luego, se debe especificar dentro del archivo, qué intérprete va a usarse en el
subshell. Para ello la primera línea del fichero, debe tener el *shebang* que
es :code:`#!`, de la siguiente manera:

.. code-block:: bash

   #! /bin/bash -e

Al final en realidad se puede colocar cuaqluier opción que acepte bash. En este
caso :code:`-e` significa `exit on error` lo cual quiere decir que en caso de
presentarse un error el script se va a interrumpir. Otra opción común es
:code:`-x` el cual sirve para fines de debug, imprimiendo las líneas mientras
se va ejecutando.

Se pueden agregar comentarios dentro de un script mediante el símbolo de
numeral :code:`#`. Los comentarios son útiles para fines de docuemntación con
la finalidad de dar instrucciones acerca de lo que hace el fichero o
indicaciones para quien lo ejecute acerca de sus opciones.

Un ejemplo de script en bash puede ser el siguiente:

.. code-block:: bash
   :caption: Script de ejemplo :code:`script_user.sh`

   #! /bin/bash
   # Este es un fichero de ejemplo que imprime el usuario y directorio actual

   echo "Script de inicio"
   echo "Bienvenido $USER!"
   echo "Nos encontramos en $PWD"

Para ejecutar este fichero se debe realizar lo siguiente:

.. code-block:: console

   $ chmod +x script_user.sh
   $ ./script-user.sh


Material para revisar
---------------------

- Videos: 

   - *Bash in 100 Seconds* [EN] https://www.youtube.com/watch?v=I4EWvMFj37g
     Es una introducción corta pero bastante rápida a lo que es bash.

   - *TODOS deberían aprender BASH - Pelado Nerd* [ES] https://www.youtube.com/watch?v=4_ub6614dwY
     Es una introducción a Bash que explora diferentes comandos y estructuras
     de bash con ejemplos. Esta es una primera parte, pueden revisar más videos
     en su canal.
   
   - *Shell Scripting Tutorial for Beginners* [EN] https://www.youtube.com/watch?v=cQepf9fY6cE&list=PLS1QulWo1RIYmaxcEqw5JhK3b-6rgdWO_&index=1
     Este curso es bastante completo. Pueden revisar desde el video 1 al 28. Es
     El curso lo lleva relativamente lento. Si lo ven necesario pueden
     incrementar la velocidad de reproducción.

- Lecturas:

   - *Bash Guide for Beginners - Machtelt Garrels* [EN] https://tldp.org/LDP/Bash-Beginners-Guide/html/
     Es una guía bastante completa acerca del uso de bash y la elaboración de
     scripts con este lenguaje. Buena parte del material y conceptos colocados
     en esta sección, vienen de esa guía.

Referencias
-----------

- https://tldp.org/LDP/Bash-Beginners-Guide/html/

- https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html

- https://tldp.org/LDP/abs/html/


Actividades
-----------

Preparando entorno de ejecución
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Antes de comenzar a programar en bash es necesario contar con una terminal que
cuente con este intérprete de shell y con un editor para escribir los scripts.

Obtener Linux
"""""""""""""

Como se mencionó en el texto anterior, Bash ya viene por defecto en los
sistemas Linux al ser su intérprete por defecto. No obstante, también es
posible hallarlo en sistemas MacOS. 

Respecto a la distribución de Linux para emplear, en realidad no hay mucha
diferencia en cuanto se va a trabajar con bash. No obstante, por mayor
practicidad se puede optar por Ubuntu_ 20.04 o 22.04. En caso de preferir
explorar otras opciones, recomendaría emplear alguna con una buena cantidad de
usuarios (soporte de la comunidad) y con una buena documentación. Por ejemplo,
se puede utilizar Fedora_, ArchLinux_, Manjaro_, OpenSuse_, entre otros. 

.. _Ubuntu:  https://ubuntu.com/
.. _Fedora:  https://getfedora.org/
.. _ArchLinux:  https://archlinux.org/
.. _Manjaro:  https://manjaro.org/
.. _OpenSuse:  https://www.opensuse.org/

En caso de Windows, se tiene algunas opciones, puede escoger la que se ajuste
más a sus necesidades.

#. **Utilizar el Windows Subsystem Linux (WSL)**. A partir de Windows 10
   versión 2004, se puede instalar un subsistema de Linux en Windows, el cual
   provee entre otras cosas, un entorno con bash. En algunos sistemas puede ya
   encontarse instalado por defecto, de no ser así se puede instalar siguiendo
   los pasos de esta guía de Windows: https://learn.microsoft.com/es-es/windows/wsl/install
   
   .. warning::

      Advertencia: Si bien el WSL puede funcionar relaivamente bien, es posible
      que no se tenga todas las características de Linux, por lo que de ser
      posible explorar las otras alternativas.

#. **Instalar en una máquina virtual**. Esta es una alternativa
   para contar con un sistema de Linux en Windows con completa funcionalidad,
   pero con un impacto relativo en el rendimiento. Requiere de un
   software para virtualización. Recomendaría emplear VirtualBox, dado que es
   sencillo para instalar y existen bastantes guías para crear una máquina
   virtual con él. Respecto a la distribución, se puede emplear alguna de las
   citadas anteriormente, con preferencia en Ubuntu_. En Internet se pueden
   encontrar varias referencias de cómo instalarlo, una de ellas es esta: 
   `Install Ubuntu on Oracle VirtualBox`_


#. **Instalar en otra partición del disco duro (Dual Boot)**. Es la mejor
   alternativa para desarrollar en Linux. Si se cuenta con la paciencia y el
   tiempo disponible recomiendo esta opción, dado que tendrá Linux de forma
   nativa y se evitará varios de los inconvenientes ya sea por temas de
   compatibilidad con el WSL o por temas de rendimiento de una máquina
   virtual. No obstante, el proceso implica un riesgo de eliminación de
   información si no se hace de forma adecuada, por lo que si no se tiene 
   mucha experiencia con ello es mejor primero hacer un backup de lo archivos
   de Windows antes de aventurarse con los demás pasos requeridos para contar
   con una instalación Dual Boot. Una guía para realizar este procedimiento es
   esta: `How to Dual Boot Windows 10 and Ubuntu`_


#. **Utilizar un servidor remoto**. Tambien se cuenta con un Linux nativo, no
   obstante, se prescinde de la interfaz gráfica, la cual puede ser de ayuda si
   no se está muy familiarizado con la consola. Otra desventaja es que los
   servicios en la nube usualmente implican un costo mensual, que, si no van a
   emplear para el despliegue de un servicio para que esté disponible en
   Internet, posiblemente no se la mejor alternativa. Existen varios
   proveedores de infraestructura en la nube, de los cuales el que he
   encontrado más accesible en cuanto a relación al precio es Linode_. Para
   acceder a este servicio basta con crear una cuenta y desplegar una máquina
   virtual mínima, donde se instale Linux. Finalmente, una vez desplegado se
   puede conectar a esta instancia mediante SSH. Aquí hay una vídeo con una
   guía completa de introducción al ecosistema de Linode: `Linode Getting Started Guide`_

   .. note::

      Si se va a utilizar un editor con interfaz gráfica, es preferible emplear
      alguna de las otras opciones mostradas anteriormente.

.. _`Install Ubuntu on Oracle VirtualBox`: https://brb.nci.nih.gov/seqtools/installUbuntu.html
.. _`How to Dual Boot Windows 10 and Ubuntu`: https://www.freecodecamp.org/news/how-to-dual-boot-windows-10-and-ubuntu-linux-dual-booting-tutorial/
.. _Linode: https://www.linode.com/.
.. _`Linode Getting Started Guide`:
   https://www.youtube.com/watch?v=KEK-ZxrGxMA

 

Instalar editor para bash
"""""""""""""""""""""""""

Para editar scripts de bash básicamente se puede emplear cualquier editor de
texto. Existe una amplia lista de editores para Linux, tal como se muestra en
esta entrada: `Text editors`_

.. _`Text editors`: https://wiki.archlinux.org/title/List_of_applications/Documents#Text_editors

En general, se pueden distiguir dos tipos de editores: los que pueden
utilizarse desde la consola, y los que requiren de una interfaz gráfica.

- **Editores de consola**. Algunos de los más conocidos son:
  
    - *Nano* Uno de los más simples que se encuentra por defecto en la mayoría
      de instalaciones. Tiene algunos atajos de teclado, pero su función es
      limitada a simplemente editar texto.

    - *Vim/NeoVim* Es una versión mejorada del editor vi heredado de los
      sistemas UNIX. Es un editor modal, lo cual quiere decir que tiene modos
      de uso (normal, insertar, visual). Es bastante configurable, en especial
      NeoVim, el cual puede completarse con diferentes plugins para crear toda
      una IDE (Entorno de Desarrollo Integrado).

    - *Emacs* Es un editor modal también creado por el proyecto GNU/Linux.
      También es bastante configurable y ampliable en su funcionalidad con una
      serie de extensions. 

    De escoger alguno de los editores de console, recomendaría emplear NeoVim.
    Si bien es cierto tiene una curva de aprendizaje un poco alta, una vez
    familiarizado con el entorno, es bastante útil para programar. En Udemy hay
    un curso muy interesante sobre Vim: `Vim, aumenta tu velocidad de
    desarrollo`_. Este es mi editor por defecto, por lo que, de estar
    interesado, puede emplear mi archivo de configuración en
    `LuighiV/nvim-config`_.

.. _`Vim, aumenta tu velocidad de desarrollo`: https://www.udemy.com/course/vim-aumenta-tu-velocidad-de-desarrollo/

.. _`LuighiV/nvim-config`: https://github.com/LuighiV/nvim-config


- **Editores con interfaz gráfica** Entre los más conocidos y usados se
  encuentra:

   - **Visual Studio Code** Es un editor bastante completo y versatil, con el
     cual se puede desarrollar prácticamente en cualquier lenguage de
     programación, y para un gran variedad de plataformas. Es un editor que
     multiplataforma, por lo que funciona en los tres sistemas operativos más
     usados (Windows, MacOs y Linux). Para instalarlo puede referirse a esta
     guía: `Setting up Visual Studio Code`_

.. _`Setting up Visual Studio Code`: https://code.visualstudio.com/docs/setup/setup-overview


Ejercicios
~~~~~~~~~~

A continuación se presentan una serie de ejercicios para practicar el scripting
para bash. No existe manera única de desarrollarlo. El objetivo es poder
aplicar algunos de los comandos y conceptos revisados en la teoría y en el
material de ayuda.

#. Crear un fichero de bash que imprima la información del sistema operativo,
   la ubicación actual del fichero y el usuario que lo ejecuta.

#. Escribir un script que lea las variables de entorno :code:`DB_PASS` y
   :code:`DB_USER` y las escriba en un fichero :code:`.env` ubicado en la misma
   carpeta desde donde se ejecuta el archivo.

#. Escribir un fichero que procese un arreglo de strings y por cada string,
   imprima su valor y lo concatene en un único string separado por comas.



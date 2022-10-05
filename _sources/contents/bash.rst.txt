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


Intérpretes de shell
--------------------

Existen varios intérpretes para comunicarse con la terminal de Linux, entre los
principales se encuentran:

- **sh (Bourne Shell)** Es el shell original utilizado en UNIX.

- **bash (Bourne Again Shell)** Es el estándar para GNU/Linux es más intuitivo
  y confiable que sh.

- **csh (C shell)** Con una sintaxis parecida al lenguage de programación C.

- **tcsh (TENEX C shell)** Es un superconjunto de csh, más amigable con el
  usuario y más rápido.

Para conocer los shells instalados en su sistema puede ejecutar lo siguiente en
la terminal:

.. code-block:: bash

   user@hostname-> cat /etc/shells

Por otra parte, el shell por defecto por usuario se puede encontrar en el
archivo :code:`/etc/passwd`.

A lo largo de esta revisión, se empleará :code:`bash` para todos los ejemplos.

Tipos de Shell
--------------

Puede ser interactivo o no interactivo, que se refiere a la ineracción entre el
usuario y la shell y de login o no login, que se refiere al tipo de shell
empleado para acceder a un sistema computacional.

Para invocar a un shell interactivo non-login con bash, basta con ejecutar:

.. code-block:: bash

   user@hostname-> bash

Al ejecutarlo lo que se va a cargar al inicio es un archivo ubicado en
:code:`~/.bashrc`. 

En el caso de un sell interactivo login con bash, es ligeramente diferente:

.. code-block:: bash

   user@hostname-> bash --login

o mediante

.. code-block:: bash

   user@hostname-> bash -l

Este shell autentica primero al usuario cargando los archivos del perfil de
usuario ubicado en :code:`/etc/profile`, luego :code:`~/.profile` antes de cargar `~/.bashrc`.


Ejecutando comandos
-------------------

Bash soporta tres tipos de comandos:

- **Comandos incluidos en Bourne**: :code:`:, ., break, cd, continue, eval, exec, exit, export, getopts, hash, pwd, readonly, return, set, shift, test, [, times, trap, umask, unset`.

- **Comandos incluidos en Bash**: :code:`alias, bind, builtin, command, declare, echo, enable, help, let, local, logout, printf, read, shopt, type, typeset, ulimit, unalias`.

- **Comandos especiales**: cuando se ejecuta en modo POSIX, estos son :code:`:, ., break, continue, eval, exec, exit, export, readonly, return, set, shift, trap, unset`.


Componentes de shell
--------------------

Sintaxis de shell
~~~~~~~~~~~~~~~~~

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





Referencias
-----------

- https://tldp.org/LDP/Bash-Beginners-Guide/html/

- https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html

- https://tldp.org/LDP/abs/html/

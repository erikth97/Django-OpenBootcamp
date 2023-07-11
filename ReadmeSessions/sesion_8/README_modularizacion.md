¿Qué es la programación modular?
La programación modular es una forma o técnica de programar que consiste sencillamente en realizar divisiones de un programa grande en diversos módulos o subprogramas.

¿Qué aporta la programación modular?
La programación modular aporta un mayor manejo del código y lo hace más fácil de leer. ¿Te imaginas todo el código de Python y sus módulos integrados en un solo archivo? Traería muchos problemas y sería poco eficiente. Por no decir del tema del espacio de nombres o namespace del cual hablaré en este capítulo.

Los módulos de un programa complejo, podrán ser probados de manera individual. Si ocurre un fallo en uno de ellos, solo tendremos que solucionarlo y no tiene por qué dejar de funcionar todo el programa, solo esa parte.

Dependencia entre módulos - Programación modular
La idea de esta técnica de programación, es crear programas con poca o ninguna dependencia entre sus módulos. Por lo tanto, siempre que sea posible, intenta crear módulos que, si fallan, no afecten al resto.

¿Cómo se crea un módulo Python?
A todo esto, ¿cómo se crea un módulo en Python?

Crear un módulo en Python es tan fácil como hacer un archivo nuevo. No hay que establecer una sintaxis especial ni nada.
Atributos del tercero
=====================

Permite añadir un grupo de atributos a los terceros. En cada grupo de atributos
se deben definir los atributos del mismo.

Cuando se asigne un grupo de atributos a un tercero, podrá añadir los atributos
relacionados con dicho grupo al tercero. Por ejemplo:

* Grupo: Personas físicas
* Atributos: Peso, Altura, Número de afiliación a la Seguridad Social, etc.

.. inheritref:: party_attribute/party_attribute:section:atributos

Atributos
---------

Abra el menú |menu_attribute| y cree un nuevo atributo o campo. Para crear un
nuevo campo deberá rellenar:

* Nombre: Nombre interno del campo
* Etiqueta: El nombre que aparecerá en tryton
* Tipo:

  * Boleano
  * Entero
  * Fecha
  * Fecha/Hora
  * Numérico
  * Número coma flotante
  * Selección
  * Texto

Una vez creados los campos que desee que esten disponibles en los terceros,
abra el menú |menu_attribute_set| para añadir a cada grupo los campos
relacionados con el mismo.

.. inheritref:: party_attribute/party_attribute:section:tercero

Tercero
--------

Abra el menú |menu_party| y cree un nuevo tercero. Seleccione el grupo de
atributos que desee para el tercero. Una vez seleccionado, podrá añadir los
atributos del tercero relacionado con el grupo de atributos.

.. |menu_attribute| tryref:: party_attribute.menu_attribute/complete_name
.. |menu_attribute_set| tryref:: party_attribute.menu_attribute_set/complete_name
.. |menu_template| tryref:: party.menu_party/complete_name

from dominio import Dominio
from typing import List


class DominioTSP(Dominio):
    """
    Esta clase modela el dominio del problema del Vendedor Viajero para su resolución
    con algoritmos probabilísticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar() -> List[int]
        Construye aleatoriamente una estructura de datos que representa una posible 
        solución al problema.

    fcosto(sol: List[int]) -> float
        Calcula el costo asociado con una solución dada.

    vecino(sol: List[int]) -> List[int]
        Calcula una solución vecina a partir de una solución dada.

    validar(sol: List[int]) -> bool
        Valida que la solución dada cumple con los requisitos del problema.

    texto(sol: List[int]) -> str
        Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

    generar_n(n: int) -> List[T]
        Construye aleatoriamente una lista de estructuras de datos que representa n 
        posibles soluciones al problema.

    cruzar(sol_a: List[int], sol_b: List[int]) -> List[int]
        Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

    mutar(sol: List[int]) -> List[int]
        Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.
    """

    def __init__(self, ciudades_rutacsv: str, ciudad_inicio: str) -> None:
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioTSP correctamente inicializada.
        """

        # Pendiente: implementar este constructor
        raise NotImplementedError()

    def validar(self, sol: List[int]) -> bool:
        """Valida que la solución dada cumple con los requisitos del problema.

        Si n es el número de ciudades en el grafo, la solución debe:
        - Tener tamaño (n-1)
        - Contener sólo números enteros menores que n (las ciudades se numeran de 0 a (n-1))
        - No contener elementos repetidos
        - No contener la ciudad de inicio/fin del circuito

        Entradas:
        sol (List[int])
            La solución a validar.

        Salidas:
        (bool) True si la solución es válida, False en cualquier otro caso
        """

        # Pendiente: implementar este método
        raise NotImplementedError()

    def texto(self, sol: List[int]) -> str:
        """Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

        La hilera cumple con el siguiente formato:
        Nombre ciudad inicio -> Nombre ciudad 1 -> ... -> Nombre ciudad n -> Nombre ciudad inicio

        Entradas:
        sol (List[int])
            Solución a representar como texto legible

        Salidas:
        (str) Hilera en el formato mencionado anteriormente.
        """

        # Pendiente: implementar este método
        raise NotImplementedError()

    def generar(self) -> List[int]:
        """Construye aleatoriamente una lista que representa una posible solución al problema.

        Entradas:
        ninguna

        Salidas:
        (List[int]) Una lista que representa una solución válida para esta instancia del vendedor viajero
        """

        # Pendiente: implementar este método
        raise NotImplementedError()

    def fcosto(self, sol: List[int]) -> float:
        """Calcula el costo asociado con una solución dada.

        Entradas:
        sol (List[int])
            Solución cuyo costo se debe calcular

        Salidas:
        (float) valor del costo asociado con la solución
        """

        # Pendiente: implementar este método
        raise NotImplementedError()

    def vecino(self, sol: List[int]) -> List[int]:
        """Calcula una solución vecina a partir de una solución dada.

        Una solución vecina comparte la mayor parte de su estructura con 
        la solución que la origina, aunque no son exactamente iguales. El 
        método transforma aleatoriamente algún aspecto de la solución
        original.

        Entradas:
        sol (List[int])
            Solución a partir de la cual se originará una nueva solución vecina

        Salidas:
        (List[int]) Solución vecina
        """

        # Pendiente: implementar este método
        raise NotImplementedError()

    def generar_n(self, n: int) -> List[List[int]]:
        """Construye aleatoriamente una lista de estructuras de datos que representa n 
        posibles soluciones al problema.

        Entradas:
        n (int)
            Número de soluciones aleatorias a generar.

        Salidas:
        (List[int]) Lista que contiene n estructuras de datos, cada una representando
        una posible solución al problema modelado por el objeto de dominio.
        """

        # Pendiente: implementar este método
        raise NotImplementedError()

    def cruzar(self, sol_a: List[int], sol_b: List[int]) -> List[int]:
        """Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

        Entradas:
        sol_a (List[int])
            Estructura de datos que modela la solución antecesora A que será cruzada con la B

        sol_b (List[int])
            Estructura de datos que modela la solución antecesora B que será cruzada con la A

        Salidas:
        (List[int]) Una nueva solución producto del cruzamiento entre las soluciones A y B
        """

        # Pendiente: implementar este método
        raise NotImplementedError()

    def mutar(self, sol: List[int]) -> List[int]:
        """Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.

        Entradas:
        sol (List[int])
            La solución a mutar.

        Salidas:
        (List[int]) Una nueva solución que refleja un ligero cambio con respecto 
        a la solución dada por parámetro
        """

        # Pendiente: implementar este método
        raise NotImplementedError()
